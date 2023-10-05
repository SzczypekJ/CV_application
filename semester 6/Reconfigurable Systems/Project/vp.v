`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03.04.2023 21:05:50
// Design Name: 
// Module Name: vp
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module vp#(
//    parameter IMG_H = 720,
//    parameter IMG_W = 1280
    parameter IMG_H = 64,
    parameter IMG_W = 64
    )
    (
    input [2:0] sw,
    input clk,     
    input de_in, 
    input h_sync_in, 
    input v_sync_in,
    input [23:0] pixel_in,
    output de_out, 
    output h_sync_out, 
    output v_sync_out,
    output [23:0] pixel_out
    );
    
    
//    reg r_de = 0;
//    reg r_hsync = 0;
//    reg r_vsync = 0;
//    wire [23:0]temp_pixel;
    
    
    
//    always @(posedge clk)
//    begin
//        r_de <= de_in;
//        r_hsync <= h_sync_in;
//        r_vsync <= v_sync_in;
//    end
    
//    assign de_out = r_de;
//    assign h_sync_out = r_hsync;
//    assign v_sync_out = r_vsync;



// coe z UPeL

//    LUT lut_r(
//        .clk(clk),
//        .a(pixel_in[23:16]),
//        .qspo(pixel_out[23:16])
//    );
    
//    LUT lut_g(
//        .clk(clk),
//        .a(pixel_in[15:8]),
//        .qspo(pixel_out[15:8])
//    );
    
//    LUT lut_b(
//        .clk(clk),
//        .a(pixel_in[7:0]),
//        .qspo(pixel_out[7:0])
//    );

// ceo BIN

//    LUT_1 lut_r(
//        .clk(clk),
//        .a(pixel_in[23:16]),
//        .qspo(temp_pixel[23:16])
//    );
    
//    LUT_1 lut_g(
//        .clk(clk),
//        .a(pixel_in[15:8]),
//        .qspo(temp_pixel[15:8])
//    );
    
//    LUT_1 lut_b(
//        .clk(clk),
//        .a(pixel_in[7:0]),
//        .qspo(temp_pixel[7:0])
//    );


//      assign pixel_out[23:0] = (temp_pixel[16]&temp_pixel[8]&temp_pixel[0]) ? 24'b111111111111111111111111 : 0;
    
    wire [23:0]rgb_mux[7:0];
    wire de_mux[7:0];
    wire hsync_mux[7:0];
    wire vsync_mux[7:0];
    
    assign de_mux[0] = de_in;
    assign hsync_mux[0] = h_sync_in;
    assign vsync_mux[0] = v_sync_in;
    assign rgb_mux[0] = pixel_in;
    
    // rgb2ycbcr

    rgb2ycbcr_0 nowy(
        .CLK(clk),
        .de_in(de_mux[0]),
        .h_sync_in(hsync_mux[0]),
        .v_sync_in(vsync_mux[0]),
        .pixel_in(rgb_mux[0]),
        .de_out(de_mux[1]),
        .h_sync_out(hsync_mux[1]),
        .v_sync_out(vsync_mux[1]),
        .pixel_out(rgb_mux[1])
    );
    
    // progowanie
    
    tresholding tsh(
        .CLK(clk),
        .de_in(de_mux[1]),
        .h_sync_in(hsync_mux[1]),
        .v_sync_in(vsync_mux[1]),
        .pixel_in(rgb_mux[1]),
        .de_out(de_mux[2]),
        .h_sync_out(hsync_mux[2]),
        .v_sync_out(vsync_mux[2]),
        .pixel_out(rgb_mux[2])
    );
    
    // srodek ciezkosci
    
    wire [11:0]x;
    wire [11:0]y;
    
    centroid #(.IMG_H(IMG_H), .IMG_W(IMG_W)) cen (
        .clk(clk),
        .ce(1'b1),
        .rst(1'b0),
        .de(de_mux[2]),
        .hsync(hsync_mux[2]),
        .vsync(vsync_mux[2]),
        .mask(rgb_mux[2]),
        .x(x),
        .y(y)
    );
    
    vis_centroid #(.IMG_H(IMG_H), .IMG_W(IMG_W)) vis_cen(
        .x(x),
        .y(y),
        .clk(clk),
        .de_in(de_mux[2]),
        .h_sync_in(hsync_mux[2]),
        .v_sync_in(vsync_mux[2]),
        .pixel_in(rgb_mux[2]),
        .de_out(de_mux[3]),
        .h_sync_out(hsync_mux[3]),
        .v_sync_out(vsync_mux[3]),
        .pixel_out(rgb_mux[3])
    );
    
    median5x5 mediana(
    .clk(clk),
    .de_in(de_mux[2]),
    .h_sync_in(hsync_mux[2]),
    .v_sync_in(vsync_mux[2]),
    .mask(rgb_mux[2]),
    .de_out(de_mux[4]),
    .v_sync_out(vsync_mux[4]),
    .h_sync_out(hsync_mux[4]),
    .pixel_out(rgb_mux[4])
);
    

    
    assign de_out = de_mux[sw];
    assign h_sync_out = hsync_mux[sw];
    assign v_sync_out = vsync_mux[sw];
    assign pixel_out = rgb_mux[sw];  
endmodule