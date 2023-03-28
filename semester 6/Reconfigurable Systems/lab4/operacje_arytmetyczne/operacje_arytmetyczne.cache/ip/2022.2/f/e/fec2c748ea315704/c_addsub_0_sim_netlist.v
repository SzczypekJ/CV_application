// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Sun Mar 26 14:08:28 2023
// Host        : DESKTOP-92KUKD6 running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim -rename_top decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix -prefix
//               decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_ c_addsub_0_sim_netlist.v
// Design      : c_addsub_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7z010clg400-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "c_addsub_0,c_addsub_v12_0_14,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "c_addsub_v12_0_14,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix
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
  decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_c_addsub_v12_0_14 U0
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
q+BtwAwM7WucT0pdt/ujXfA9AVcyNfRQC3d0laKddGB1rAzz28OixOqPTIDUsV4geeHIMG4Kla4Q
1YA5NKUndr3U4HAUmET6t7eJaSy5voADOJ3uNT24q1ubPB7PaOYJen2pYawkga3BS/33WMNDmlnC
H9lT9IzOruZnpk8wAvzSwI497qQxoMzqjvXCJxqkIQnbRtFy6pXKh+ZWnHYR4v3lRoSdyTqUrE95
YRO8g3hFS9vA9oSOg1ifhbs/4fHZAA0K3Fg8ALH5iaB/VSQGx8Ua/iih5tlM62IMIrozPYtqbL1G
UEBPfknw5FufexGs7rgQ43IWru89nrjGkl4htg==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
R82YjxRtxHvCkgAkik3fMSDDaMAgzphMZIZlO7vjkR0h+85OjN9yWqQ6PoGwYYhLKg1cNr50VhhN
AgtmTSZj+/DACA1YfUT2BuPN06/tMmLdO1MZ/TfUq8d7PmTb0J+sZPIhcUzHtkMOA4ka9DVon5vI
rrK2EcvfxlLCajpF5TApomJDHl09Suy2nzB1aHl0JaSBI0ls1sNh6/vb/iBkepGhlA0M5MipP/hB
mzvpHTOVEEpqnFkZ4hSyqX3xjSut/sy0Yp49U+5Kp7bD6iiRc2MC1Y3TMGSNyHsDpxy8TeTVQ8Lz
zIb9qlzQ8BGcsS6BlPjFAugx+aMDNjla6udQwg==

`pragma protect data_method = "AES128-CBC"
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 15936)
`pragma protect data_block
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
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
