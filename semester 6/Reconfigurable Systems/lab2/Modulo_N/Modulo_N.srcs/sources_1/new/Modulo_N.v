`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.03.2023 17:35:40
// Design Name: 
// Module Name: Modulo_N
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


module Modulo_N #(
    parameter N = 12,
    parameter WIDTH = $clog2(N)
)
(
    input clk,
    input ce,
    input rst,
    output [WIDTH:0]y
);

reg [WIDTH:0]val = 0;

always@(posedge clk)
begin 
    if(rst)
        val <= 0;
    else if (ce)
        val <= (val + 1) % N;
    else
        val <= val;
end

assign y = val;

endmodule

