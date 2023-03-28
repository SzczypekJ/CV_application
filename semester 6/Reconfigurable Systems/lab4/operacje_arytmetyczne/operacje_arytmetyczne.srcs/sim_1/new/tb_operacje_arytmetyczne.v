`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 26.03.2023 16:11:19
// Design Name: 
// Module Name: tb_operacje_arytmetyczne
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


module tb_operacje_arytmetyczne(
);

reg clk = 1'b0;
reg ce = 1'b1;
reg signed[11:0] A = 12'b000101001011;
reg signed[11:0] B = 12'b110011011010;
reg signed[11:0] C = 12'b001001000011;
wire signed[24:0] Y;

initial
begin
    while(1)
    begin
        #1; clk = 1'b0;
        #1; clk = 1'b1;
    end
end

operacje_arytmetyczne module0 (
    .clk(clk),
    .ce(ce),
    .A(A),
    .B(B),
    .C(C),
    .Y(Y)
); 

endmodule
