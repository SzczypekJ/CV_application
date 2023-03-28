`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.03.2023 13:56:47
// Design Name: 
// Module Name: delay_line
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


module delay_line #
(
    parameter N = 4,
    parameter DELAY = 4
)
(
    input [N-1:0]idata,
    input clk,
    input ce,
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
            .ce(ce),
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
