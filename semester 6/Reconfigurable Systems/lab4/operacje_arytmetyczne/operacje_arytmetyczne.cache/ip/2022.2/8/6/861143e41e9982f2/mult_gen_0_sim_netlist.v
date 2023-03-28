// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Sun Mar 26 14:59:36 2023
// Host        : DESKTOP-92KUKD6 running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim -rename_top decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix -prefix
//               decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_ mult_gen_0_sim_netlist.v
// Design      : mult_gen_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7z010clg400-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "mult_gen_0,mult_gen_v12_0_18,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "mult_gen_v12_0_18,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix
   (CLK,
    A,
    B,
    CE,
    P);
  (* x_interface_info = "xilinx.com:signal:clock:1.0 clk_intf CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME clk_intf, ASSOCIATED_BUSIF p_intf:b_intf:a_intf, ASSOCIATED_RESET sclr, ASSOCIATED_CLKEN ce, FREQ_HZ 10000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, INSERT_VIP 0" *) input CLK;
  (* x_interface_info = "xilinx.com:signal:data:1.0 a_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME a_intf, LAYERED_METADATA undef" *) input [12:0]A;
  (* x_interface_info = "xilinx.com:signal:data:1.0 b_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME b_intf, LAYERED_METADATA undef" *) input [11:0]B;
  (* x_interface_info = "xilinx.com:signal:clockenable:1.0 ce_intf CE" *) (* x_interface_parameter = "XIL_INTERFACENAME ce_intf, POLARITY ACTIVE_HIGH" *) input CE;
  (* x_interface_info = "xilinx.com:signal:data:1.0 p_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME p_intf, LAYERED_METADATA undef" *) output [24:0]P;

  wire [12:0]A;
  wire [11:0]B;
  wire CE;
  wire CLK;
  wire [24:0]P;
  wire [47:0]NLW_U0_PCASC_UNCONNECTED;
  wire [1:0]NLW_U0_ZERO_DETECT_UNCONNECTED;

  (* C_A_TYPE = "0" *) 
  (* C_A_WIDTH = "13" *) 
  (* C_B_TYPE = "0" *) 
  (* C_B_VALUE = "10000001" *) 
  (* C_B_WIDTH = "12" *) 
  (* C_CCM_IMP = "0" *) 
  (* C_CE_OVERRIDES_SCLR = "0" *) 
  (* C_HAS_CE = "1" *) 
  (* C_HAS_SCLR = "0" *) 
  (* C_HAS_ZERO_DETECT = "0" *) 
  (* C_LATENCY = "1" *) 
  (* C_MODEL_TYPE = "0" *) 
  (* C_MULT_TYPE = "1" *) 
  (* C_OPTIMIZE_GOAL = "1" *) 
  (* C_OUT_HIGH = "24" *) 
  (* C_OUT_LOW = "0" *) 
  (* C_ROUND_OUTPUT = "0" *) 
  (* C_ROUND_PT = "0" *) 
  (* C_VERBOSITY = "0" *) 
  (* C_XDEVICEFAMILY = "zynq" *) 
  (* downgradeipidentifiedwarnings = "yes" *) 
  (* is_du_within_envelope = "true" *) 
  decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_mult_gen_v12_0_18 U0
       (.A(A),
        .B(B),
        .CE(CE),
        .CLK(CLK),
        .P(P),
        .PCASC(NLW_U0_PCASC_UNCONNECTED[47:0]),
        .SCLR(1'b0),
        .ZERO_DETECT(NLW_U0_ZERO_DETECT_UNCONNECTED[1:0]));
endmodule
`pragma protect begin_protected
`pragma protect version = 1
`pragma protect encrypt_agent = "XILINX"
`pragma protect encrypt_agent_info = "Xilinx Encryption Tool 2022.2"
`pragma protect key_keyowner="Synopsys", key_keyname="SNPS-VCS-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
C/5Mh/YfQK+xvzcE2CGtETuPBeLiyJko5tNa9mMrxf8GTM/0mqqMZ+vYDutRWwlkGLoBJ0ubJ2JM
hSYnF9uwe22zt9N5LFdSRZxMoN1o6c2PdIJyFX9QiG+G0k5olg9eEzsigfNpc9kE5brQ+zVlZ0BV
klXrD05hnhWq+ZJys/w=

`pragma protect key_keyowner="Aldec", key_keyname="ALDEC15_001", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
nhu9PWmxjSOqIMDTXJV+4qo0FPiBJCygcWuN/bfQzqY2oUKKM8378Fb2UT55vg8n4G10m17vIBgN
+Wy6buZC7GhxULhm+9qKdG61k/7yfhvEyQUBzudlOBUaIUk7ZAeE6SGH26C8h1WgBFSBJBshielG
kmSnefelvtJmMqQynpqanYQE+2/nM45zHVEXMtgEl8NM+ittmjnbmsjMG+VmkcpjTiitr8v+SSgM
RUwmbOuITmj1SaUWkm+IJTDW4bnipSqF0iXScNDVurlEpJm4oLvKdM1ottYIIcXR6+Fa5dGLRubI
LjYe8sQ49kCgXyYdFk4JbJANd3OdYx/U0839pw==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VELOCE-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
oLOGB6O+5m7WVYa3aB6L+szJIkfErI3K6c0Z4Xd6Cc9YLnPbUoTR/E3N7bfACANo1RtCR1KrgOT9
QRzSpMaWuUNpHkoBWkpOvvqpujGg7n+KNjtsXpeAJDMZq0hpkCFMyTIbglQJfVL4ds7LBIztVpT+
XPSPp0rHN6MvUs/o0sQ=

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VERIF-SIM-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
b3H7uIeGCIVDgn3FEC671rtMncRXCjR9RBfw6OuWzlyF5wFk4ElX2tB2gwrWUb2Com7mmOGUcT8m
dWBnb4fgFyaI4CcP0cDJZ1RBfKHzHsnVnUtydmh17jwFjOhuG4oqUfxDBVOziYixuf8xqsPD1kIx
AAGgp8eCh/3TTWsXe8MqUHFhWLAFBHiM+g9tiFtJxHBAyX5v+8avU7rSRQOteILiCl/aE/ZTg1U1
TZRYZm9xCtpTek8kcIXycf8cf1vmkeYfjYqsPcKnLXjswHKcSvCTgJBvdf6/NU1hADbYz5krZkN6
cP43YF8Es6pXZ5MZxRyvAulHMEmC1vBKEV4L2Q==

`pragma protect key_keyowner="Real Intent", key_keyname="RI-RSA-KEY-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
hNojWTRiv5xJXFjSuajQtOI6VJWjSVIasMceSy/iOADWwlykMyPQqJwBZv9vgyG2lsbPzupIZZOt
sY4+VQKC49eSzzBiqlXJuuRgTh4eG5Sj78MJPFi8Z4JHdANbBDjcsfEyFcFinPG8C+6ObqSWv3sT
fh66lPvK05YKvRong1DaI4yDI+LeF0XCXF9jXawejRWPqZyQQRofEUn3P6/HL3rOQ9WrwtOgLOh4
eld6oolD6hKjdN6z7BtfypoG1+c9GyXB8peQYSYy2mC/UhPM2He7IScIeEh8FKNZOETke8ShtPdd
8KijcT3YF0mZbR+JEAYmPRwljDtmkR1nmLPJ5g==

`pragma protect key_keyowner="Xilinx", key_keyname="xilinxt_2021_07", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
vNoNhNOiLgedrjzCipcIWa66MfCSJrQLJjludHrumavTx1oA+4ROcs5sx9EIY16AxVabVb6PSj/B
6g7QMmhWOHO5XWCGsLGngpWlMaz7FPJIrMDMH0FqHULVZgn+ytshKF3OiHU9DKUfGAkx2o6xKR8J
v2jv+NfcjYrjtp1y5L007VCIwcNtkKJJXaDQjJxbYYOB0uzxwQIXRo+SEib+esXDvZD6Ikc55nl4
wE0bh+voYoBpOgDoGMiOgpg8YJnYWFS+aCT4aHJqb0+12fK4HJHyN34p2V9mna/PBHxQttZEjbwL
t5GBDgl9IiQOzvoyMMwa3D9yJPGWNEJTOJaUbw==

`pragma protect key_keyowner="Metrics Technologies Inc.", key_keyname="DSim", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
UWO1yL0EL8CXhMsuZN3v7pq9vqI3Hx8I4AdpxQRWS35PlhqAcAjYeBVG9msiPa5PzWiULLQfpvtc
jErP46XJGtGsEiYBMIv0Sy4sw0m1buhgPQC3ebkJgAk3bspWMUEsvYaN1IfFXabxN+RYANz3tJ2Y
oHgpnvvpm8OrlQUsgkwwn7FgVUGvBHoaj3vopWTMROl61+OL1aj+VLKQvwlZuA30e5yG7JAT159Y
e+xbMUxDz+W4RK0kPzZxnlU6X2HGieEEqGVzuAHvbaqUsRHZF294LqHX4u2WuTM74rvH69Kh5wL6
jYEYgCU9ma4gBAA98slrAnjNqn4bY2f9DG+now==

`pragma protect key_keyowner="Atrenta", key_keyname="ATR-SG-RSA-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=384)
`pragma protect key_block
iXm1XonW4ervg3D4DUJphNzJ6vN12GMfC70OgzuNrZ2kX9fFpWbL5IBPnCTMNnNWQy0GGe6hvPmb
j7EpeR3MIhJR5BcSdHMR4BVvSo0AEM+UmieNsuTc7dTw++8EucnKuLvloLldJo1b29DO+LZfqkGP
M9z2zkXfSVOqQRNGzxLR5gGJLHNfjxGz8MOIJ3HaDDAbO1eEgkWN9ZeesYwJrgERNSubcEhjLzl8
dVi5A1iTEa6WcsQ7XpUZkZTrHlM+/ZUnuZelrt2eHwx7m5XAZzHXbVz6YPrxLVx80IcJzqkykiEp
dMotGjzHWB0+tNy/gRFTUB5rpFt3LtF2+O9mZEf4nNluB9zmYqmvU9T4zeiID3NuEe4WOZjruJ0Q
gBPt5imaHECnAFxZ7QWVRp1rGkX8eS8I5qjfVJm8+pKqvjc1MGkAv2Vh4RG+n36yShUI44QIDYIY
zqj5fbexc27+CEmjJEFy/Cwik0yDg15IXyQYIkVLbBBdXfuQsGR6lI0A

`pragma protect key_keyowner="Cadence Design Systems.", key_keyname="CDS_RSA_KEY_VER_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
e2TCE/IVroj0BoMutEWWgUoHdqmqHN4Vq1aGvl8tHLqPMgKPyusaF/EU/+MvsIWjDyZip1MmWOcx
jQu5Oy8IWt51LTRIQJ0x+kU2WDMNmZRHSdVAR8ORyzaV+63xJ+1FR21OuVBTsdN0zc5+xPOZn251
Ih7Dkw8u+guep7Yr4t3jgw+4crsiBVVM+5WJvUb5HgZZLCirWswHL2EOSwrlxmh1UfYzXoib6RPE
Ra/hqZSom0279kPBw6Fx+riPQZSw7jyFJal9sJMpp1RQHG0wo0DgA0V8Ot4NHxUc9Fwq4+hnCyfi
r2lvbn1yjpQbLFKBIZrlQAud1cQVbPc9abtdFA==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-PREC-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
QZSpoks56LVq89EnijQPQYocgcNh4lZ2r1xECa6mY+RA7kAajtzD9EIpORW3niAUU/jtsFf/n4Fe
kbKeaRWnwZBtKrgNE8cHMKLzmJdPV2YOiOqLmkrVu6vPTmY9Be5EiKJ0hTSRRir9iSsFjI1Lwnef
5BOG68oJ5I+GrOUQMmvWxmuJM5ek17AfIybvfcxD54DSrRIDhQxgj2VOkIuEhk6bgRgBIuzm1J3S
tvW9m98z5qKhRKzFP7vi/aaIbCQUAHXW5+JiyhEVhO8AxtUBHh4CR9FGfYmJAXcePJkNEB6+B5Vx
fA92jAVPPXh1QKBBmactJHT+xDOrLRUz1UUKQg==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
keMQRVm/s9vcdhW0r8p0dJTWavMlMpMbx4izb3+u4+LGcg8fJx2sk8Wfzpe7JLbFX0hvmk3+IRJz
9z+FwFVmyUWwEMNec9tqz75yZt6JUNGDV2FhpW7CFEj8tCOXrliLX1tGRG411mtobKq9pcFS3hYr
DU1/HKl/Cuo6OtblE/1vMD4uoQenEJT3zqot78oMEOOVo5LZeyq/D+duWQXDYRkc+Lf1ndgV8EEZ
jDw+pgAiIa8jVevZBkZPQa1HEXogd5ia/eTGGtFlxNuOj63UOsyWseSdlxYLxf4HG/0cRq4UrQoW
NXldpG7Bz1Zif8Eb4A2ddoGoz1HABtA48FOQ2A==

`pragma protect data_method = "AES128-CBC"
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 11264)
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
