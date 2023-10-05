`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 24.05.2023 19:28:29
// Design Name: 
// Module Name: tresholding
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


module tresholding(
    input CLK,
    input de_in, 
    input h_sync_in, 
    input v_sync_in,
    input [23:0] pixel_in,
    output de_out, 
    output h_sync_out, 
    output v_sync_out,
    output [23:0] pixel_out
    );
    wire [7:0]Y;
    wire [7:0]Cb;
    wire [7:0]Cr;
    wire [7:0]bin;
    localparam Ta = 110;
    localparam Tb = 190;
    localparam Tc = 100;
    localparam Td = 160;
    assign Y = pixel_in[23:16];
    assign Cb = pixel_in[15:8];
    assign Cr = pixel_in[7:0];
    assign bin = (Cb > Ta && Cb < Tb && Cr > Tc && Cr < Td) ? 0: 8'd255;
    
    assign pixel_out = {bin,bin,bin};
    assign h_sync_out = h_sync_in;
    assign v_sync_out = v_sync_in;
    assign de_out = de_in;

endmodule
