`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 15.05.2023 23:49:09
// Design Name: 
// Module Name: vis_centroid
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


module vis_centroid#(
//    parameter IMG_H = 720,
//    parameter IMG_W = 1280
    parameter IMG_H = 64,
    parameter IMG_W = 64
    )(
    input clk,
    input de_in,
    input h_sync_in,
    input v_sync_in,
    input [23:0] pixel_in,
    input [11:0] x,
    input [11:0] y,
    output de_out,
    output h_sync_out,
    output v_sync_out,
    output [23:0] pixel_out
    );  
    
    reg [11:0]x_pos = 0;
    reg [11:0]y_pos = 0;
    
    always @(posedge clk)
    begin
        if (v_sync_in == 1)
            begin
            x_pos <= 0;
            y_pos <= 0;
            end
        else if (de_in == 1)
            begin
            y_pos <= y_pos + 1;       
            if (y_pos == IMG_W - 1)
                begin
                y_pos <= 0;
                x_pos <= x_pos + 1;
                if (x_pos == IMG_H -1)
                    x_pos <= 0;
                end  
                
            end
        
    end
    
    assign pixel_out[23:16] =((x_pos==x || y_pos==y)?8'hff: pixel_in[23:16]);
    assign pixel_out[15:8] =((x_pos==x || y_pos==y)?8'h00: pixel_in[15:8]);
    assign pixel_out[7:0] =((x_pos==x || y_pos==y)?8'h00: pixel_in[7:0]);
    assign h_sync_out = h_sync_in;
    assign v_sync_out = v_sync_in;
    assign de_out = de_in;
    
    
endmodule
