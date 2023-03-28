`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 18.03.2023 14:05:03
// Design Name: 
// Module Name: tb_maszyna_stanowa
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


module tb_maszyna_stanowa(
    );

wire [7:0]input_maszyna_stanowa_data;
wire send_wire;
wire serial_data;
reg clk = 1'b0;

initial
begin
    while(1)
    begin
        #1; clk <= ~clk;
    end
end

read_data read_data_i (
    .data(input_maszyna_stanowa_data),
    .send(send_wire)
);

send_data send_data_i (
    .c(serial_data)
);

maszyna_stanowa maszyna_stanowa_i (
    .clk(clk),
    .rst(0),
    .send(send_wire),
    .data(input_maszyna_stanowa_data),
    .txd(serial_data)
);
endmodule
