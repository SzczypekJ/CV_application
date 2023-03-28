`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.03.2023 14:43:47
// Design Name: 
// Module Name: tb_delay_line
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


module tb_delay_line();

localparam DELAY = 2;
localparam N = 3;

wire [N-1:0] out;
reg [N-1:0] in = 4'b0000;

reg clk = 1'b0;
reg ce = 1'b1;

initial 
begin
    while(1)
    begin
        #1; clk = 1'b0;
        #1; clk = 1'b1;
    end
end

always @(posedge clk)
    begin
        in <= in + 1;
    end

delay_line #(
    .DELAY(DELAY),
    .N(N)
)

dut
(
    .clk(clk),
    .ce(ce),
    .idata(in),
    .odata(out)
);
endmodule
