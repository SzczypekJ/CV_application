`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 18.03.2023 13:43:14
// Design Name: 
// Module Name: maszyna_stanowa
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


module maszyna_stanowa(
    input send,
    input clk,
    input rst,
    input [7:0]data,
    output txd
    );
    
localparam STATE0 = 2'd0;
localparam STATE1 = 2'd1;
localparam STATE2 = 2'd2;
localparam STATE3 = 2'd3;

integer counter = 7;
reg [7:0]bufor = 8'd0; 
reg [1:0]state = STATE0;
reg send_del = 1'b0;
reg txd_reg = 1'b0;

always @(posedge clk)
begin 
    if(rst)
    begin
        state <= STATE0;
    end
    else
    begin
        case(state)
        STATE0:
        begin
            if(send == 1 & send_del == 0)
            begin
            
            // AKCJA 0
            bufor <= data;
            state <= STATE1;
            send_del <= send;
            end
            send_del <= send;
        end
        
        STATE1:
        begin
            // AKCJA 1
            send_del <= send;
            txd_reg <= 1'b1;
            state <= STATE2;
        end 
        
        STATE2:
        begin
            // AKCJA 2
            send_del <= send;
            txd_reg <= bufor[counter];
            if(counter > 0) counter = counter - 1;
            else
            begin
                counter = 7;
                state <= STATE3;
            end
        end
        
        STATE3:
        begin
            // AKCJA 3
            txd_reg <= 1'b0;
            state <= STATE0;
            send_del <= send;
        end
        endcase
    end
end
assign txd = txd_reg;
endmodule
