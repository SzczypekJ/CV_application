`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.03.2023 14:28:36
// Design Name: 
// Module Name: register
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


module register #(
    parameter N = 4
)
(
    input clk,
    input ce,
    input [N-1:0] idata,
    output [N-1:0] odata
);

reg [N-1:0] val = 4'b0000;

always @(posedge clk)
begin
    if(ce) val <= idata;
    else val<=val;
end

assign odata = val;
endmodule

