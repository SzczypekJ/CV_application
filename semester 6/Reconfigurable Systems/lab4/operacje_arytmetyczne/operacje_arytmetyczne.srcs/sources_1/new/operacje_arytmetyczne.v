`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 26.03.2023 13:56:55
// Design Name: 
// Module Name: operacje_arytmetyczne
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


module operacje_arytmetyczne(
    input clk,
    input ce,
    input [11:0] A,
    input [11:0] B,
    input [11:0] C,
    output [24:0] Y
);
    
    
wire signed [12:0] sum;
wire signed [11:0] delay_out;

c_addsub_0 adder0(
    .A(A),
    .B(B),
    .CE(ce),
    .CLK(clk),
    .S(sum)
);

linia_opozniajaca #(
    .N(12),
    .DELAY(2)
) 

delay0(
    .idata(C),
    .odata(delay_out),
    .clk(clk)
);

mult_gen_0 multi0(
    .A(sum),
    .B(delay_out),
    .CE(ce),
    .CLK(clk),
    .P(Y)
);
endmodule
