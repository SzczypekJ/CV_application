// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Sun Mar 26 14:08:30 2023
// Host        : DESKTOP-92KUKD6 running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim
//               c:/Users/szczy/Desktop/STUDIA/SEM6/SR/lab4/operacje_arytmetyczne/operacje_arytmetyczne.gen/sources_1/ip/c_addsub_0/c_addsub_0_sim_netlist.v
// Design      : c_addsub_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7z010clg400-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "c_addsub_0,c_addsub_v12_0_14,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "c_addsub_v12_0_14,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module c_addsub_0
   (A,
    B,
    CLK,
    CE,
    S);
  (* x_interface_info = "xilinx.com:signal:data:1.0 a_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME a_intf, LAYERED_METADATA undef" *) input [11:0]A;
  (* x_interface_info = "xilinx.com:signal:data:1.0 b_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME b_intf, LAYERED_METADATA undef" *) input [11:0]B;
  (* x_interface_info = "xilinx.com:signal:clock:1.0 clk_intf CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME clk_intf, ASSOCIATED_BUSIF s_intf:c_out_intf:sinit_intf:sset_intf:bypass_intf:c_in_intf:add_intf:b_intf:a_intf, ASSOCIATED_RESET SCLR, ASSOCIATED_CLKEN CE, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, INSERT_VIP 0" *) input CLK;
  (* x_interface_info = "xilinx.com:signal:clockenable:1.0 ce_intf CE" *) (* x_interface_parameter = "XIL_INTERFACENAME ce_intf, POLARITY ACTIVE_HIGH" *) input CE;
  (* x_interface_info = "xilinx.com:signal:data:1.0 s_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME s_intf, LAYERED_METADATA undef" *) output [12:0]S;

  wire [11:0]A;
  wire [11:0]B;
  wire CE;
  wire CLK;
  wire [12:0]S;
  wire NLW_U0_C_OUT_UNCONNECTED;

  (* C_ADD_MODE = "0" *) 
  (* C_AINIT_VAL = "0" *) 
  (* C_A_TYPE = "0" *) 
  (* C_A_WIDTH = "12" *) 
  (* C_BORROW_LOW = "1" *) 
  (* C_BYPASS_LOW = "0" *) 
  (* C_B_CONSTANT = "0" *) 
  (* C_B_TYPE = "0" *) 
  (* C_B_VALUE = "000000000000" *) 
  (* C_B_WIDTH = "12" *) 
  (* C_CE_OVERRIDES_BYPASS = "1" *) 
  (* C_CE_OVERRIDES_SCLR = "0" *) 
  (* C_HAS_BYPASS = "0" *) 
  (* C_HAS_CE = "1" *) 
  (* C_HAS_C_IN = "0" *) 
  (* C_HAS_C_OUT = "0" *) 
  (* C_HAS_SCLR = "0" *) 
  (* C_HAS_SINIT = "0" *) 
  (* C_HAS_SSET = "0" *) 
  (* C_IMPLEMENTATION = "1" *) 
  (* C_LATENCY = "2" *) 
  (* C_OUT_WIDTH = "13" *) 
  (* C_SCLR_OVERRIDES_SSET = "1" *) 
  (* C_SINIT_VAL = "0" *) 
  (* C_VERBOSITY = "0" *) 
  (* C_XDEVICEFAMILY = "zynq" *) 
  (* downgradeipidentifiedwarnings = "yes" *) 
  (* is_du_within_envelope = "true" *) 
  c_addsub_0_c_addsub_v12_0_14 U0
       (.A(A),
        .ADD(1'b1),
        .B(B),
        .BYPASS(1'b0),
        .CE(CE),
        .CLK(CLK),
        .C_IN(1'b0),
        .C_OUT(NLW_U0_C_OUT_UNCONNECTED),
        .S(S),
        .SCLR(1'b0),
        .SINIT(1'b0),
        .SSET(1'b0));
endmodule
`pragma protect begin_protected
`pragma protect version = 1
`pragma protect encrypt_agent = "XILINX"
`pragma protect encrypt_agent_info = "Xilinx Encryption Tool 2022.2"
`pragma protect key_keyowner="Synopsys", key_keyname="SNPS-VCS-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
KdkdvVsuosc8qR9X5PxQ/ghTeTrEz4qKVuenhDR9wRSL/BO/mhSwQtiFj74UO0sGv0zvjAntaq/3
l2/v8gOiVKmM666gbk/2UCISA4OFA3FDR9jYmiXdNXb2qHeS1ywQz5n/sTR5iu4KFEfwrl3IXtQw
aEiGegL+CQMaovJsto4=

`pragma protect key_keyowner="Aldec", key_keyname="ALDEC15_001", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
pZCj3qT3VD1SCS5RiZExsqqu16KpMtHXilQL9p5/eBl7qrfQjT1VhFtVbYUusepbChjsCCmCn7hr
72SuHmOmDWG78UARN7MLdO/+sePuyS06ak4nAw5xwjT0g+9970uMWYKvTeeYqoz2i+k+zX60Cuvu
iwBfxWM22DqukHlYzbEFWhNyXIkgJe71p67vGdXBmqu4/2wmlwGApqBxlwR+alwZ9UGHlxNQS4N5
z1wHu3Cp8LwGRjlaXjElcY8RDpvyz5l59ey8ar5HXR9Zqf6e1unE2NdhzHhEGRerRFXoKZppk1HB
6kIEY4EHAWz+HvPcqoP9eoYKDazoAGkJRVP6YA==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VELOCE-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
gLgm7VvY3cNcNvdXvikCQd2nRniE4ae4hePOcAUlPDMoHDzQAD7Ngo12MGFns9JNPcCaUXfAmxL2
JNGojjrDRUWrv8FPV6FOEbDHs96fef8+gqLF4OqLck4kWpKhnJwaJjjzQirvXEzZxP+GsBKnkSp8
ceVlZJwP0F6XRv+RpQA=

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VERIF-SIM-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
GeZP242oKQSNuofqDs4oIIXZEufPhRVrlFFeRSLY4VCxhMEMwfPrNXe33xO0zIEBoPW2X9mvUoTY
izdWQEtWImFzjzPCjkSLhEdIMmUBH02Y+Tw3eW5x23T0cK96pmoV2MH8kl99I27MN6stVd977fuB
Mjao5MnSXIGZ/uXGtgfUO9Zjs4/2wGmsI2/lANN2WOL9Sz4xeA8k40c2dNYgxgHoCwx8Ya/RYIZS
Cpuvzq4ZyFSNT/kMXnUmqj75/flpXT3mmyW+frexux3j9PxpKHmxAE9crvDx85rMamGiA4ftl+ac
H0FtL2cBqdlP60x+FjqleWCJoN6AYdxA0YZaeg==

`pragma protect key_keyowner="Real Intent", key_keyname="RI-RSA-KEY-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
URmEGftuxvv0+tViRUdsFNnPXucZlVDfUQpjjXkpOA38QUzsIL9j1pGGp9doC4jcg/9MD149BTSw
vAG8684a3k+Tx/8sFGl/viK1q8ty9nktEABSahv8Etm5ZJVAzQJT7EaOzrYqyywSwabogvGUmN/7
DE3eOn6+sMCiMl6BLUhYyK39ntTWNFYVPiheclbBb36V1vzMOQl0mvPuS4hDXqba/+qBZXhqeYWK
ceNfwci6SsRRef6hLF/1S+20r2uBxJeYJjyfWGGFEGfxlAOz1MiYUUR/bEHWnbjwIcJTBHQNRdq4
4Ryb+iPuKcsXU/8ApD14i6ScW+VBPWSqnH9w+A==

`pragma protect key_keyowner="Xilinx", key_keyname="xilinxt_2021_07", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
NtQgA3rUKfJt+21sTot44yr4gmte57FoFl8Q/327tsRJeEyNAiwWZaZN2mbo2NFcvyN2GhDw6avJ
NsF1Oxs36P8shoqOOiloWWrdTcyAdMhdk+UjeZgKcNSqd4Js87w/5LVQTwjB2mcBDfe1jrivv+IW
ZRBC8NvlW5z/1wF7+vzXRMziLQYeOkLB0OkpIY+eT5cZXDKuZ+4l0FMPjd+El96JGAEHG7Q0qS3F
OEApYEp8+nSZnragoytq4pkhVJEC22ye0hBhoBClJpszCcg0u+Ugf+mYZsj8BC2uqSY6Hh/gpjjw
enQ7aEYBaUR7GCwQN7fZmNhZYtBkyvNqydRQcA==

`pragma protect key_keyowner="Metrics Technologies Inc.", key_keyname="DSim", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
CpIFM8Y8dBmpjtOVnOKcfppEFV+c1cRgsQtewNUe+5apiLDoRCdMyTqoCay7nz+Xagc0OvfZDg/Y
jSTsDjKVcEIyxOfix7iwjKW8Rz+a5wBIatI8wfCo7uLtuucz9otOWWI7BFQ2gn4VdQ73HJJlZMMY
OyEOd33tGjNSjxz3W07knDr1FwTE3BOfhq+Qj2ErnuV1dQbrTb3MiQMTnHaTCwtz6ip0pD6b5G4K
kBRUYe+UNXCMvSfNIN9MPSmolO4MjNwM5gnZZqLcR1hGuzH/Yeb/jPnhsZ7jFvlTT3nsM9JzMRAE
QwlzVuulHKQDS2I96arFosYPYMsalmn6CQW0gg==

`pragma protect key_keyowner="Atrenta", key_keyname="ATR-SG-RSA-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=384)
`pragma protect key_block
qinIxHFISC9r9LS7OKOuYVGM5EBkuuQNV1nDRui+QVNLn2QFCrWPeEClQIlNViKOt8MX9urHvu4e
l2L+eZKw6+St9cW9yUsYu36yoB4LqwG+vKvfR9CW82LGPyMAxdgk/p3n+F0Xp9Y2HaERwWDL99tW
V7cDvLLhyIwz7w4rI0BWWV+KMjXP2F5MNgykzZn7tzV8oY6MxOykFqRdI8DLAdlYGAs90wjJ3x84
S3fHciSox97FYpDi64v31Vb4RmRrwueXcvCc3w8gzjuwg7qraWLMYyPB+mERB2v1htX80PsWWVHE
QXkWiHWYvvrXEykUS04MmLNHpV8ZgBXO/NBEGn7mrITDEswk3u1Yviqy7CW2wLPQBoo5xW+uiu2e
8YZV/E+bAt+P/EH5RsC9alBgtuVKU1s9DaiEH8eUPEgJQ/TXwQW01pg8ECTYgiBS+IQSbld23aq3
goVo0ZMzRu/SA00Jmwt7upvsMkh9Q+2732ahu1FmlSNmyNGB1+bYf782

`pragma protect key_keyowner="Cadence Design Systems.", key_keyname="CDS_RSA_KEY_VER_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
T1jqx5hmzZZMhPApzUC1oZLMAkHma8Ki4b2CvLNqxSn+MNWoTPomvQ775DMBEDai/gahYALsohdX
0f/e6LuPqt4zYtyAzmH+nRgOG/tilS1J674KsaHxudAfo4sM3awB/C4Q3VdYsO9FgvPQylnYKSGE
gJ46W+1Y789VQqPbt4dpnprhix6sLlwfww7We6cq2wu4PilFzovejouUBZqNMZHYi4suKcMcenp3
C7QRKloo8IF9yKrhGPcRJLQt2nus3bI0Q3ICxRk13Nrfhh/z4cdm0OGXz42q44snFEVy1lLxPOs7
W9tSe5ag3923oCT4NGGgK/gMTx5qXxFhV2MJUw==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-PREC-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
ID8HU711xFSfMpLf0Vb/8ZiKMx2kyfaOnWn9tpHaXY9mcP5kqPOUUvXwgRN4Z4HSAiQkDUFfcd8O
qKL+3vmKTtGaBYZf1Rjq0Mh66owcR9x89tljkam+8E0WMzieXGv4t/XxgR1Wo+8QzVb9mnJxpcCv
lPuKn2+sOpATCXOVamyr86Jxhz6YMI77OOOGTAvISYibzBkGB4IO5kTvr4YTJV9nZ+dHwrlfeyz+
sbpZSLiocLakCAR9ufd/C+Dw5YZrU8w/fa3i33Q64INpm4mdKjCA/NtmG70yecmTOkoFbgiVkmhk
seYSq5jk/KU+UWHdwQuwCV/4gkMGr+KXS5VpRA==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
z1+F9KTFy1KkYP7tAOhXtiPT5dTtsllcVg3ZwBaQXA7aBKIIiuDtoJ7V3xtg5eYjkmI+8gldEx34
GhrxFG2h/n+DR8JM7joqy1HDvIY7yfjJIPLIwx2ymnEb3Koqu3chmh0T3XCVuI0VzlSqsdPc5Hoq
6yTW9eDs9+icnm++N3SlvsbByQD9rSN+9G4oAQ1GVsqaCbVj4nQPqtjVzmFyI+qeY3pMqIhAjLEI
65jAfCQ1ZqG+AG4Pdkg0oUttHOybZJUkmYs0NoD2FsS7KPlv4lqMj9Eoz+kKeicsjbDLqnPIP4Si
5Y2flcWNQnq58ZGgA9NkGftbr8Axdd78WMK4gQ==

`pragma protect data_method = "AES128-CBC"
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 15872)
`pragma protect data_block
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
tuOU/GRPcWTO6MKILu8v7o4mB5uia8aQHQA=
`pragma protect end_protected
`ifndef GLBL
`define GLBL
`timescale  1 ps / 1 ps

module glbl ();

    parameter ROC_WIDTH = 100000;
    parameter TOC_WIDTH = 0;
    parameter GRES_WIDTH = 10000;
    parameter GRES_START = 10000;

//--------   STARTUP Globals --------------
    wire GSR;
    wire GTS;
    wire GWE;
    wire PRLD;
    wire GRESTORE;
    tri1 p_up_tmp;
    tri (weak1, strong0) PLL_LOCKG = p_up_tmp;

    wire PROGB_GLBL;
    wire CCLKO_GLBL;
    wire FCSBO_GLBL;
    wire [3:0] DO_GLBL;
    wire [3:0] DI_GLBL;
   
    reg GSR_int;
    reg GTS_int;
    reg PRLD_int;
    reg GRESTORE_int;

//--------   JTAG Globals --------------
    wire JTAG_TDO_GLBL;
    wire JTAG_TCK_GLBL;
    wire JTAG_TDI_GLBL;
    wire JTAG_TMS_GLBL;
    wire JTAG_TRST_GLBL;

    reg JTAG_CAPTURE_GLBL;
    reg JTAG_RESET_GLBL;
    reg JTAG_SHIFT_GLBL;
    reg JTAG_UPDATE_GLBL;
    reg JTAG_RUNTEST_GLBL;

    reg JTAG_SEL1_GLBL = 0;
    reg JTAG_SEL2_GLBL = 0 ;
    reg JTAG_SEL3_GLBL = 0;
    reg JTAG_SEL4_GLBL = 0;

    reg JTAG_USER_TDO1_GLBL = 1'bz;
    reg JTAG_USER_TDO2_GLBL = 1'bz;
    reg JTAG_USER_TDO3_GLBL = 1'bz;
    reg JTAG_USER_TDO4_GLBL = 1'bz;

    assign (strong1, weak0) GSR = GSR_int;
    assign (strong1, weak0) GTS = GTS_int;
    assign (weak1, weak0) PRLD = PRLD_int;
    assign (strong1, weak0) GRESTORE = GRESTORE_int;

    initial begin
	GSR_int = 1'b1;
	PRLD_int = 1'b1;
	#(ROC_WIDTH)
	GSR_int = 1'b0;
	PRLD_int = 1'b0;
    end

    initial begin
	GTS_int = 1'b1;
	#(TOC_WIDTH)
	GTS_int = 1'b0;
    end

    initial begin 
	GRESTORE_int = 1'b0;
	#(GRES_START);
	GRESTORE_int = 1'b1;
	#(GRES_WIDTH);
	GRESTORE_int = 1'b0;
    end

endmodule
`endif
