`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 26.03.2023 14:19:34
// Design Name: 
// Module Name: linia_opozniajaca
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


module linia_opozniajaca #(
    parameter N = 8,
    parameter DELAY = 3
)
(
    input [N-1:0]idata,
    input clk,
    output [N-1:0]odata
);

wire [N-1:0] tdata [DELAY:0];
assign tdata [0] = idata;
genvar i;

generate
if (DELAY > 0)
begin
    for (i = 0; i < DELAY; i = i + 1)
    begin
        register #
        (
            .N(N)
        ) regi     
        (
            .clk(clk),
            .idata(tdata[i]),
            .odata(tdata[i+1])
        );
        end 
end else
begin
    assign odata = idata;
end
assign odata = tdata[DELAY];
  
endgenerate

endmodule
