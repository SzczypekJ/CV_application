`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 24.05.2023 16:43:46
// Design Name: 
// Module Name: median_delay_1
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


module median_delay_1 #(
    parameter N = 5
)(
    input clk,
    input ce,
    input [N-1:0] d,
    output [N-1:0] q
);
reg [N-1:0] val = 0;

always @ (posedge clk)
begin
    if(ce) 
        begin
        val = d;
        end
    else val <= val;
end

assign q = val;

endmodule
