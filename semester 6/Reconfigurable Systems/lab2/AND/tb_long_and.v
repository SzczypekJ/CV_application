`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/06/2023 01:53:36 PM
// Design Name: 
// Module Name: tb_long_and
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


module tb_long_and  #
(
    parameter LENGTH=8
);

reg clk=1'b0;
reg [LENGTH-1:0]cnt=8'b0;

initial
begin
while(1)
    begin
    #1; clk=1'b0;
    #1; clk=1'b1;
    end
end

always @(posedge clk)
begin
cnt<=cnt+1;
end

wire y;
long_and dut
(
    .x(cnt),
    .y(y)
);
endmodule