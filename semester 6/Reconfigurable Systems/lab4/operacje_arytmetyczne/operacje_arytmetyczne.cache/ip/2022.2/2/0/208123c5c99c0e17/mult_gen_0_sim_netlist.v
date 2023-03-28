// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Sun Mar 26 16:42:00 2023
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
  (* C_LATENCY = "3" *) 
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
OtsTwXNiowLAt6/r+eHGv74ZrYhwthk9riv6enF7Ih/JCBibpdh6XQwHrfShvO3AhnZmm1UNTt6p
zLe+Lm5EQFfvZpVOzSulXgy2RKJHD8dlk49yaATFnTEA4b6WIc3/u8U/z9gODqZr3lJ1nVA/jPIH
55laFzfDnfzg/+hKIuwICIBF9CJF5DDhkar+ULxZVnCjn4GFy+NqCHkZgqRZ6ZGMkW70ZbOSclDi
vZii8AC5JrBoTjMpnms01ayJUft149nZZ+TYj+WI6JU+vnx51JI18h0eBCQZDnh06iOEwRA2n546
oqJze2hxmHvLZv/L9vhKEDNWBxAiw1c6Z7x8/w==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
0ZSF6tArNLnvYl9soD6bOSdoBkVctRJVRf9Aah2RaadQfI5eAPWcC3KwH5ihzNZe1bnI+DUvT7LA
shvKhYSw4lFe4C1V98ovJat6JqLuswRlBIE9KgCS7Cy2aDSU1tHPOAtM/BnhGeOdjFSuT0358ONU
yUCy8VtJYqRBY7hn5wPPQtf7WmHEFvy5Uk8AE1ZUWHKt5p0eg17nRP2h2Ef3M/R9jNPKAj6b2m3c
YsnycxWVrl0NvUMNSKeYO5ChoFj2UrFceJSxYJM3qSQ19TWsfNuQI8Ygct6BQrvj62nmmrELhNVG
UcFFrdHOwqIbRBtGSB4cuAWowVrYmPcJo8sd0w==

`pragma protect data_method = "AES128-CBC"
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 11216)
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
