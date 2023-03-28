`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 18.03.2023 15:29:13
// Design Name: 
// Module Name: send_data
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


module send_data(
    input c
    );
    
integer file;
reg [7:0]i;
wire data;

assign data = {0, c};

initial
begin
    file=$fopen("C:/Users/szczy/Desktop/STUDIA/SEM6/SR/lab3/Maszyna_stanowa/sample_send.txt","wb");
    $fwrite(file, "To jest wynik:\n");
    for(i = 0; i  < 192; i = i + 1)
    begin
        #2;
        $fwrite(file,"%d",data);
    end
    $fclose(file);
end
endmodule
