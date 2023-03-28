`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.03.2023 17:37:19
// Design Name: 
// Module Name: tb_Modulo_N
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


module tb_Modulo_N #(
    parameter N = 12,
    parameter WIDTH = $clog2(N)
)
();

wire [WIDTH:0] chain;

reg clk = 1'b0;
reg ce = 1'b1;
reg rst = 1'b0;

Modulo_N #(
    .N(N)
)

dut(
    .clk(clk),
    .ce(ce),
    .rst(rst),
    .y(out)
);

integer i;
initial
begin
    for(i = 0; i < 50; i = i + 1)
    begin
        clk = 1'b0; #1;
        rst = (i == 18) ? 1'b1 : 1'b0;
        ce = (i > 34 && i < 40) ? 1'b0 : 1'b1;    
        clk = 1'b1; #1;
    end
end
    


endmodule
