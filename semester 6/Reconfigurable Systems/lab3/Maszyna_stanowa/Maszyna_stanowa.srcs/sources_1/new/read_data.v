`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 18.03.2023 15:28:49
// Design Name: 
// Module Name: read_data
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


module read_data(
    output [7:0]data,
    output send
    );
    
integer file;
reg [7:0]data_reg;
reg [7:0]i;
reg send_reg;

initial
begin
    file=$fopen("C:/Users/szczy/Desktop/STUDIA/SEM6/SR/lab3/Maszyna_stanowa/sample_read.txt","rb");
    for(i=0;i<16;i=i+1)
    begin
        data_reg = $fgetc(file);
        send_reg <= 1'b1;
        #2;
        send_reg <= 1'b0;
        #22;
    end
    $fclose(file);
end

assign data = data_reg;
assign send = send_reg;

endmodule

