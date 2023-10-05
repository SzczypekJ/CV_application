`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09.05.2023 10:01:17
// Design Name: 
// Module Name: centroid
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


module centroid #(
//    parameter IMG_H = 720,
//    parameter IMG_W = 1280,
    parameter IMG_H = 64,
    parameter IMG_W = 64,
    parameter PIX = 20,
    parameter M = 30
    )
    (
    input clk,
    input ce,
    input rst,
    input de, 
    input hsync,
    input vsync,
    input mask,
    output [11:0]x,
    output [11:0]y
    );
    
    reg [11:0]x_pos = 0;
    reg [11:0]y_pos = 0;
    reg eof = 0;
    reg [PIX-1:0]m00 = 0;
    wire [M-1:0]m10;
    wire [M-1:0]m01;
    
    wire qv_x;
    wire qv_y;
    wire [31:0]x_c1;
    wire [31:0]y_c1;
    reg [11:0]x_c2 = 0;
    reg [11:0]y_c2 = 0;
     
    
    
    always @(posedge clk)
    begin
        if (vsync == 1)
            begin
            x_pos <= 0;
            y_pos <= 0;
            end
        else if (de == 1)
            begin
            y_pos <= y_pos + 1;
            if (mask == 1)
                m00 <= m00 + 1;
            
            if (y_pos == IMG_W - 1)
                begin
                y_pos <= 0;
                x_pos <= x_pos + 1;
                if (x_pos == IMG_H -1)
                    x_pos <= 0;
                end  
                
            end
            
        if (y_pos == IMG_W - 1 & x_pos == IMG_H -1)
            eof <= 1;
        else
            eof <= 0;
            
            
            
        if (eof == 1)
            begin
            m00 <= 0;
            end
            
        if (qv_x == 1)
            x_c2 <= x_c1[11:0];
            
        if (qv_y == 1)
            y_c2 <= y_c1[11:0];
        
    end
    
    add_acc_0 c10(
        .data_in(x_pos),
        .rst(eof),
        .ce(mask & de),
        .clk(clk),
        .data_out(m10)
    );
    
    add_acc_0 c01(
        .data_in(y_pos),
        .rst(eof),
        .ce(mask & de),
        .clk(clk),
        .data_out(m01)
    );
    
    divider_32_20_0 d_x(
        .clk(clk),
        .start(eof),
        .dividend({2'b00, m10}),
        .divisor(m00),
        .quotient(x_c1),
        .qv(qv_x)
    );
    
    divider_32_20_0 d_y(
        .clk(clk),
        .start(eof),
        .dividend({2'b00, m01}),
        .divisor(m00),
        .quotient(y_c1),
        .qv(qv_y)
    );
    
    assign x = x_c2;
    assign y = y_c2;
    
    
    
endmodule
