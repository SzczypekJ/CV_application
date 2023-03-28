// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Sun Mar 26 16:42:02 2023
// Host        : DESKTOP-92KUKD6 running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim
//               c:/Users/szczy/Desktop/STUDIA/SEM6/SR/lab4/operacje_arytmetyczne/operacje_arytmetyczne.gen/sources_1/ip/mult_gen_0/mult_gen_0_sim_netlist.v
// Design      : mult_gen_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7z010clg400-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "mult_gen_0,mult_gen_v12_0_18,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "mult_gen_v12_0_18,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module mult_gen_0
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
  mult_gen_0_mult_gen_v12_0_18 U0
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
aiLq2/1Mi1GYVPslSC3cmet5rDEdc4uE+tSQkzdcZtTif2I65Y5raoZX8cag8L4f8n4NvEUs24Wc
R/2XARSn2GibnLG2SzT+t5pBsKDnTP9z6OMZfwp8NOlrSAWXgM+rFLy8QtVPf1eZcvwzak78gxSA
WyHDR+TWSsEzjtHRrgMjQ6s47Ea2BhYwOQoyDvMqCpDp2O8sf3y3tvCYiSgqjIWvRZ4A603BwAqN
ELZY0OtZrchdVcB2AB9RbLyeKPdw9Cg9ZPAy4pJr+1iLnMXJRvzQXsIKv766avdi6gHOhC+RWnAA
OV3CKhf771lvH+gFKh2+Mi53zBeSVGakxpR0jw==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
tVKF02hY7cxL1ZmZuenPnhTeTByfGDcGRDAwCsHxPYQJksXD3HoRhExsLRuIVamoMuJrS8bzdBAJ
XYTbQT2D46EbCj1j0Bn1MUvVlMtMZtvazrYmRbB4Qp7pXc9aobJiCcvHxP2UJEw/X+5WitArtzKt
fFd2Uzx5boZ/CLQH2v6w9YdtOdo/GxXHU1sy7jtJOnUX//lbJcRF3O67If/QCbU8YgX7pFI7K9gp
BLyDAkAnLXitaoubxt4Dvv4dw4bUAYRCX021L+KlEc7jLL01+fnQ9n4dvlBQV6zYC5vZySdpXzeq
nhe23fP72PyqMBkJGoljfM/QK2ywhPY/4o8m3A==

`pragma protect data_method = "AES128-CBC"
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 11184)
`pragma protect data_block
hhjYXjSkJNTojKapbRdsFMOgRlbqCwY+W73Btsh/8Kndl5g4+yk2mhK9mdnqXy9EpnlOVLN3hJ2w
y63Lj5XKzeDDX/HFlZvIlFVtcRKNAVsKKkjpl0inq7R6SByUcJV4uL/xc5tAjoDjinJY1ZojwUDZ
FR1ZqNChGMi7p3pk0nKwkvtBTx49f2uwWKWgWPKo6Y6NUOjfC0897G2KISKzJbD9QLzh8moXRvBb
Ja5ljpuMSiemxiOUmPHA30roHHObM/YsdWD2XyUCIOO96tlqxVJFGf97o+uWV4ur0AllrcENpDNH
3tH0v0AiWEAX+TBKRhGagpC+n39SpXrLccvx2ndB8pybKKMMXi6YRH+4olYv0lZa5bJvxkcoowpy
Ey2Y9FhPs4Fn8rvg5l9NCsALJ6oAYvI6D7935HCslRqrJ8hSjl95QEfauBiVW0yu2QdMVKJw4tgu
ggRAJXr7VTG6GnLPJwZ7ZBvLCLG8g2EeZNbNcw2wW9Rsod+dS/21Qy1ydOkJwUR3KXugVX6tu1Qv
Kmm9Iidl5lCkIh/nEE7fe0wVPOVNMg4vBVbt896TL6nMdPuWM/sytuUXdurhpLTAr2DOdJCD/S4q
zKdo8o5lZr8w07lJjZRf+xSusyXfwnjXS6I4PtYm09Xhu+vzM3Bw0Gf2S5mb0unrN2gUwJig2JPg
a1CcxyD7KMw5lKIRHo9UF4ESwta2UTxaaQ1eqP9MWvtrkxZGRaF0P+/ox66PKP0WKByBAAlgQd8s
1GE2RFvdgzCS0E2IaeGCMqYisZieauO4tPOz/uNG7rbHKNbVb0rElWNmlG6WSZv7Rdq4L8P9m6OJ
45vrbj9vk0ziLrt0d6ylI9lD4qzvvYu/wYnSl7yflC/yEyKDt39YBlaEuOvo4Xp/VkihDgBSNvEq
Fpxb3Q+ugirN0/BDmQ+cS43i1l4YW4tmQU/yc9MZ59WX0H6zFe506zYIFBHVOuiVLhM0mEoITtPC
nyTeckZOmN0zb4VFBdjFiGJXCai9efX8eB5v2f0c89ODm//+A6Z3WEjOUHLYTqVA81/zqJQrIe5m
nStNGH0gHv7NOB+//CoUdbPjvIVZXaQv64kzzgstIgGLLx1V2SEMP+qp2RFCQomRi4HfaNomibvM
x0cdhoOHbbHWk6bMpEhKU8Xr351h5cXcd0n3jiigJPsUyUVk5BxY+vOe2kCKa4PgDB0ITSmUfX7T
rC3DqY7ldFK+RFZ9ieFrDJnkMZQOkxC7RBLOGHcdTrbIzzMJdsFY2IucoUUDhmi+Pz+pdQ0nMz54
MBRWt0l/YWL5wWs40qzWmGUoUW9oE7wjHe3RIFqm6wuwfhnSesewoaQxUgnDfEwUVakT9i55Pf6y
Em1q/RrNNo78YND5NmDXD9xCThrPYK+2mKasKmoRPwZu7IZvp441LuXfse+ZFxc029Q7KwrjPYZ6
NWSC09paMmYw40WRYr9bnujhnWc7yZYpd+lcKN5Z8A8UV+D6M6YoVAf7/yl6amrtU8w6jTjUXEwC
KVQuVO2MhjvXRZnV66eZDhp5ULxtwvtGqaZfnc/6x1EWH7CfHIqund3RDG6xR+7eOUw5prNunn/r
xyjr8m4eGV/EJf+t5OFLoAcNaVS0LHkIu8/ySs3kSnwcmw/15QqqE8O85Tfnp7uF686jw4Vi2ZFl
VTVfK9dnX06I67KwSnKFlKLgXoXT12+l2KH5EmXcbhIXLa9TqLJrwReS0UlzaIP3ha2mYCNtjb9Y
CspKNxN0Lz0/qEzWo17zv3lOrGeJFD5ULSnqWPynNzIkmYsWMgrMlRZ1r947TiwAxG21tTKFBIAT
W+Rx0V95Ksd5sIf9KGzs92hCTATBk68iYNFqUIBv1eGSGN5lOqwBRUAqdod68rpjtn2yxMtebx41
49nuUnZgRzypMLfcSj9pz8j4CaC8cDI6Aw3LChiGL2WgEiVbm8Qot6e5cibAcMeTWs7Ma/3CKLh2
YU57g9OPyUn70ODbvRnpEgvZd+g8VzQ4Z/lzzjj9OBZofTiFdIVfibU0oFIjmFls7pnQXzmA9N53
2Co1YL57ahbEIdfnent7B2Tu8evvOMUrWOs/zd76/AppHpGoOCNoxVzMoj8biPJj+DqSzF0ACKI0
Zx/4xhSpAlzJ9QwDQeEQecuBMKNk+8Gly4wiW5F4/JL2QMmSX7wJxyO7ngl43v6IH4JSrJB2D6WP
RujkWGpK5DCkozkc7MaRXbFmUpTlGyOedXmlnG0G+FxA4erAb7VgOkIui9C1FjboI0IeoIrTBYNw
3vwi/BIc7r159A+3twUB1bM+3HciYHuDyvGIDxy04Gb5+BRGoYNCKhU7loq/O4Lt9NM98RTwVQQz
K90cUFnK3BhnFP0aDyJ5TVOoEaTa9drbSBgLS5HdAqj53HYupWlwfoD3I0jG50nmi/HAVzl5U61E
8dADFIr0TnaP0itwXURn1REQ3AZhDFs6cI/DUEtwDmg9ibAoBeKDl0C2IXfsMZ7WyQPHrEofUmyZ
VdeXe61hrvck5HNQdmF3t32YZIs92i4AuObrIvoGxXELsimKM5eW7BAaTv7xJ1FiuawWKqoFiPHp
6WI6wWJR0gSDH7fZjFWfd71lHrDtitCZYZAA9lDa1F2bbi+RpjS5MUGKTYDdRwheSwVBK/7dWj1D
eKOwpuPJicY2Ivi29sZmw/DFqbk/L09uCRKORqHK1mBcuwDsdxwfnMCM2Qe/OERcME24qf+v5Suq
XMrF2LWTc6pdhyyJofNasf3PznjRHJKM65QTDbxjI+rqeZ0WFiAZDRpdAzzTCwUV8jfat2nowe2w
4B5aV/w+nS4SgPgLJkGLx8EuBNFIREa0S82t5J9JnKzP9CXGakxZpFkHgF06pORmnUaTY0hz+vXD
Jj6t7wuav1xO7al2q/k6h21VYCtm2r9apRQZGUXnwe+2MkB04hNbkUqgEwDw0Cw7MuyEwt/TlnmU
fsB1iAOH0boiP83FHHcBhy0bv8OjB14+e1DBCAXy9OA439gtabdYgreXRnnqJB8B1NKzUzQ0kvBD
++hicYCxC/XnMKE5jFak4pb5LiIESPwvMrUdviSQBo9rZr82eSs3v5cCY/C6BkAtKSmJuKChzl2E
kgE+ES4CsF+6obYqj8ccvPQKhl76mOoRlbd/XGg+U2K/QJ+v1blqip7ji9EB7+IIKkT4NCrA/8Bn
PkJvpPywIA/sSa6qZjQY0rhMieuBLHV9U8WDm1ydRl/H57ms/BaLk8ZICLuBp56USVwOAoHFLtRn
IKEBNSTxVKVDAVE6PTTkbi1XXSEgDDjyGhZ27huc/h4BQUxgle/JTY044D7sUeAIUWot1aKUDmF1
EC7KZn/hKGUmzeST9P43brPSs4SwCycm4pkBZvrZnr/ZA9a148hF10R6o2tsnq/DfpYrJVNhv6E+
JWLgGdfkKCUzLGGMTVA1OYeLzYbztkQGOXUU0qhmNFFGMWOVFI5Q+TtUEvCSHbYCr0fwRxjwc6Qs
UPe/DfyR8b++YV/GusfUpJES5VfXw/mKC5OR0IxwAm9TLM3YvcrTtzBP3sUDbafJzEIE19rX7qHb
3QNoiMX6b/d3Umz5xaT4XO7L6VD705O3SPpO0gaKqM9e+Oqr/B8nPjUAtzeWuTvhXuyREsQaVwvs
7mFW9bQrdKwagqEDJOp1XRnqIvm8ENLa1OvcAVg/CxwLRjX+otfxC9gk1XsCK+E4lwYfReM6SkKt
caYVDhZT0oFCxRaHKUgIyHji+YepIYX26RUfYZFffXFI9hDqNFYRbc1vvNidFpv3bpg6Ut/xc87F
Nc4PROlcY32RXTePY+3EYCrBh9nBSylSamiM46xvqvsPP34xkb5RhMyrV7btA5ANI8oLYF7qpNCb
owDwZIVO2HdShm/rTRPHBq3+3LdIltVYBPpOKcTe8FqAivZFNnW6zHocdg1d/S0t+MGyvMPfvTxN
qPm8F3vISxZuGwuA04klgsUR4p6wawThY5AnCDWta/vtFwBvo1nOKhkCjvoyNAeZU53IN8jSQZ7T
9kG8dVkS3EB+hn/SlFrQ81HcJPMRRFwIhBCkNWimC0D222Azvr8u/gBho/JeUovV33AhD+PwQ6SG
p3Pwi2+78GJ0f2K47q5GuJsjzociYRPK/bWTXwI9UEHRWQGUHJnWYe6c5W09lSKfka4v7rVOFXlj
tFRpQjDjA5Vo7pwh7t1ZAB2pVphc9BN8HKaz+Ruhy/7Xzo+BA1ESNfD1r8ZmRTGNSvVpqq2QDlNO
DK1+8hIjQaFneVyjfwsayVIWGgs7lA6hI+92DZoniZL+e4WTDKYJ/+X51PQ+Eenr0Wx5vyjw++s7
LljPGtdBdxH7fM6SeNDW4VjMV+6qH4OdU6GT4EmKclXzWaehhdhl4smNIeTOJuj0Kti9CO1BzQWX
wkLog1PVAQ1zs3clPvxMP0rV36M0YULuToYM8lGEtiTK99cUfPtvBnx2eDrJggD7wGCoXZT1TV7N
9AU+FZ2bbRO3zlDhWGQYKXZrBt1IzWtKOQk224f5EHebGxCVNpdrVoWMrjseeH/MzxVWqS8YGGv/
VcXosvtUun8+Q9J/6x0EHQKP3rQLpfdpJc7to1hwMPr3r7SoBFMk8EsnnmsNTj0N12UGENY7r8aS
INmlnIvh+RWVYoItmww1o94U9ORI4evlmXvpRa00AP6VHE9L3gVl/PoQoR2cBt44nyGGUI4/RIkV
Sxd9XaQcNGMonCQii0MlGeJyi9J8P9N2qV0kc9+XptQdHTJx56Ec1DOCmV3LUAqw+4TXk56LCzIO
eDFu3aLBOTs+5HtlrTO1JReCYEQZRy6/+84Nns0DXQhoTIHu644Eofl6oPXhRpBmmsdYw3Ga/f93
gh24/wv76IJhHYe5nB8sabkAISURhzy5Y0ttGup8KDBFBFpbyoHCgQwCM/SGJbUmByZIlOtSTgXT
nCTFUXmVWIsLdAnmAqvYsiARGjR3AnXZWWmxhnLArutiQjyV+SK62nJHyay84YjDsnPxmr7FKnDK
pVXcIbQ2gjCSAA1TinMypO8gK18aRNEHhXPSqVaTrVZUNjNRLV6vF0lVZnlT8Cia3BNpyxB3VaKH
lwx43Hh+9927gvyze5RzWfU5Ur7uq2RM1KmPwXSJvcPoroDJTQHoFRf8RULZ4vePkuNFTYz8DE0M
GKmEeQvjLel0DJqztxTUxvHx2g9JpWou1hnHd/2Q3reElynfVw3fc4Y5wk/FSJp5/+ZCYOAMy7ca
sfHK4WvQfIB99sGuOytzsBhT9z6LwtuzTeaGomyT100u2Ro8m16808BnnhJxuBUwYwIUZkKvZWdr
p4nPUBX/vvBNZ9n+JaLgNU0NVq5Hfems6+BIYumbgjJSnl5QLHcrwrxJXmbsgXH0teUIQPvZsLNr
nkkLftRrZ+4g9NPWiy+UUQBkHSOnkkBQ9eEREacN3VWgLJ5qaRUiiEU/0YVZ2nKs9HIK8C/oGuE7
5lEY6ZuVaBAOzdls+DDrXV9E+h3Rmd2bRzg/iB4+pXEqwEOfquD6mIONDUSCSKL5GB1v+2ZjspkV
yJrusavCb0xy5WxHcdEHCeXn6viY1Ye6FiXQCsOaSC873JNwnDUPf4t8tMnbdXBN1PfbVuUv3KtD
f+mFdIxPuLFwHVOOYfP9XVxjP1AtqtlADlULRsJLKfFkUYph+5JjiWp+hvPGVdGuRskQ77jJJbw7
cV+s042dAwX10v5B4huloUX0t9qVCRvobPk3Nx05WJ+VNaquEKM168fbazKSQotI3q80t/3unk8q
MGvo4Q6aZzOEzznkknY25/ZG5Cfl0acsDVU3W4rD5FIS9aJ2QwZEQ7nk3/ndIM9BID9352rYR8SN
VPT6FTNMIgCm6LNFlUli/8f9qiVc+zyV+tDtlU+P9Z1gMxf/6hvlK2uMW1OXXcGmGA4TfJSmdnxV
22CSBZgtVI3OkHujWUBbg5ZjEogOPk6wjBeQSSDJD/Y4nQ8QTGzYqOoAG9z/jmo6U8wnprBc0jxQ
mtzWExvd+No8T/i1DNahJkJu9OotZ31oKXuxKc+6Fq5fJJgnuH/nTn6RYspf5CZ+ZOUE2xbrl5uz
oDmzS1c89Vp38XNL2MVDDnlJAUe5HCv0CKO4fxWAbpm3oy5LbT8CiBlBwauCZTUJvgbQOHxw79XF
i2C7B+mzC2zgEXxu0Vk8UWglQzOxbGCLVMTh45AdLFm9QHngK9wC9VCCtMtm0ogzBqb/TOLri3OK
tIMLJmGXMhTiVRPiPceL1uVl+wefH1nSc6oTsSEg40SE7ysOgxj14mS3t7Ab3G/gjgL7ujEv+sKx
V4V9pWK5z30fh14hmAlUGWBnrK16uaQWb66h8y/DgUK4WFTKZ/3DWSeqY1rV++A+0NsLiwtieWlq
jQlLnmJJL49xzeI0AdbnTwDf7mNmpLA1jSmucmwt856aRuotBq3BddHdJT6ZXCXyHPtnHvn7eror
bjUdBrtvuqds/WMsIjWsXs1cY3zwXVbtfG35qcb9RgJYgsc1BrlqIO/r0qehSQR5vo8uiYPByDjC
LGToFprjwxjX/bJAofL8SsKO9Za7SXiEtjB+lI7C5DUv2Z7nsazNLX+P7eWZHeV9vE3OOFpj+n14
mJEmwNLvmUb/MbTRn+EvyL3PENwOCoW5ecj86jKyfru9kmhzPjd0chAN8myFC/hA07kaq96AKkDH
09vEQJB67tpCqwbN+Ba17IUYl+kKNpi+glnVZu/xfICwV1WjQYxCmreQvj1om0lmbKoKjHUAau4z
9/R8hRryE7G9NO63tHRg1apDm0IJPOQm+T29h8Sr9geYNqd1eKgzEiuraBcxCmxXqEjWGWGhCgxP
GrmnjUnVsi5HdwrM/zkzMtfOJRo2/iX5rk/f1tr4cOv08XQcBoPbbKZOY+LuD9DhzhZ41PdREMvm
DQwUchGjOljQRqXRwAJXQBy6FgH88tW7Gnjs9IEBgbEzs3tUJfpf2q3cjomjhkHiA5kjSxtBXLhI
smSrGzhpeMY8a5V0Q2eGof9NrF0kFD2+c5hxGHfk6wzF1VY4S3vRQnt7SgjNhyoya9eJJOTClBAO
q833r+1GdvjMpCv1YAylvl9l0S6bUETgUhoB6FyVzV2BR369VMAJI6gFl5+8TTC3ugIL/hM9uBB0
Ey/J5nyRMb28LS2/CSSvm65yIZKT16k0UeETp4a3L+P12kXXIXKrO8liNO1uvlQGfdcqo4hoP98J
LKBF0VHEDgG3yXLzGCVKiS9vYpYHroMfsbXuV/d+4KttfNPF81ihgadi7zKcCfLGiev62L0B4ht4
skKMBMugiEtJNx40gVPICOB/PZ3hkoC/F02V70wS3rxcC6w1BmbTzzXw6FYFPIWEHYCeVWD687B1
H0u0FVLF4Av9oZyFW/MLtySgwoI3OsQkNjuux/3RkBxIglpDkt81sw3hk3rb6qzXhaen1ifQvMlD
kS2GOrX6d0t70RcEB5IhaQMZE5ydVRS4QSg/S9q458XqAjrsQd04Hkh1kL3XETQyFuaOLGkbAKGF
PAc+EM+DA7FhzlyVjbg67gAJa2nH8XiYyrxk4lBbY+jeDuVq8IpiWlmuFvTMh2SjUa45iJXyhp3B
toBCiqsKRCJByE4Di7LeB8npknUX7c8y+91lcb7XsmN9uVNYTtrH7XgNSb/2mYQPMwOuViT+Qbox
oNBsg54X32HccoDH8c1OqaP3gdgZcsQl5bP7rSShiF7cued+I/mUNtxr6HdNIyQ82Er8/PwH66oY
nq3PxjjSCbm+7F0Nh79cOqlL5iaZkknxxSXOO3MXPsA74XAqvXUQ4BrmDRvHjb8H82RaJ5+Vse9G
eS1f4CKAOGv7FaTqa5zUiceU7JTQXopCyVvvKGaA6Q1JFZNlJm3kNiq/qLiytm+JzRVACTr8npKC
3jfQjWdu2UlPL7tAJbJx06BFwU7zFx9zwMbxadjGckkJSRkE+ta1Jtqio8HA8YYNlQ+Vv+di7O9O
P3ayjtOm8MfhF/Qor+cYE8/teLaeLDo+SQ9dEmABguZK3S2rrbXlK51ah8ucuPNjILWz7rhqApP9
X1LnZXLa/PMVOlzgqMdbclgq9NupKlUiGpYl6EM4ZnFmr4untruaeVtQKOQ/qGbzgvpeMaDiqsoo
2PllixSSsTeuMuiKZTD26ag/ZA/WHfh/nJUyBY8ZEq1NnRDOGj7lUXzjl5tlqrevZ+r4ih8+wieX
eA65I/IVEIlworLcnLJPDqljJmDWnUYNriDcP5qANVUpdD+F9a+mnSAFLPxHltNYo+aYwRO+huqX
AMV7k3iuWC5s3rrRzjlWOOx3EFFPhUUz3Yda3mK5OirT1gCzZ4WFY8zSpPOnxtB3KO4lKOSgt3IO
ohaKfhAyRdilpofe/qszqqACqeubuEg9jSofYQUc+gvIAIKcUOmECULW0+a4G45HP/17ANXKYRiR
F6FdnSjexHtzmjBkJvgHPyVQY83YIPYJIEfFBDO0HvFFb6YS93lorVD8rXiKqg7BWUD1lC8cAC95
q48W9yWo0Quju7uyV0DC2E683D4NUdFQC7S9xmI3HS4ca+hpEpTtjpzeOKuNm23bYo/K+478qdpi
kZ72sAgXJN8p6bGyN7wr8scvW0F4RAIHd59Gwf6hJbZZdY21IY0Mr68Pgqk55Jf/f+AONXXF+N3a
dF3A/0g9K8ZoiFwfmnCyx/5GmLLVrn6fB5vmKiRv5+e8O07wwoYEWI92uDV1VU3I2cjffLjDITre
Dq7nPJajTme6MfGTzllSHkWHA/jFahAIIPY2oC17DbUOQGr6uZBM+caZX/haDBcaqgWzpPkxQrlO
VNhI2BhKyiUyHtBQgWUkxte3DIsRyGgngp5MbiKVRwPInBNInUiMJSnN4Z4YOYBZ8hg7s+eVtKzp
uMsQ8TTNdTtNOCHh/z0X75GFC8J26ENAGQj2XrPan7vIsBX03Gmg9NwaHLHF7FZatmNf9TXzwrAO
xYlB2YN6KJuw+iZoP/lRjnBV3foLbxj7U4vCy/svHGuIl9YjmRcZosIM/gn+CPy4atHi8zqSCEWs
pUJHgStT2naOUz0reM8eAdLjPYElhc7kljlBM51A6XdJl4ZuEnUh0IADlt2wQpixaJOU2z9GSs3h
X/unRuRyraZeBYhuwhk4Oa2AJIAgZmXQ/zXmQAETcah7Q5oCa5cO+zB07XNz50B15sl702KkJ7R1
AZufXjFWkteyXC1VOR0/9ndGocxxmdDHz53M5P+PhFBRSIxJwhtwsuSQ1g3d2cci7fwcJER2vvzI
wEFZcxY8tR7qBy5ywHaL+GYMzvQAuSJIIYQpj8i5z8Wkhr+n56f62yaCdZS1TJNuaTiXepTyDnOV
3kMmpRWTjT5c16qJ/BbSY/jrtUNYvb+d9SVK8GS7z2fYD5adXSlB41bh/93TSlNq6dWQ+V5SHMJ+
+hBtchggIYfR23FwpDzQOpYEqP8WJUGa0Jg6UDVRKiU8IUDeFFkBRZt426DLsxvGETZWezZZrisE
oDKwyZeHccOS4Eb8m2GNwruvg3DK64y4rHJW827UHQOe53Uso48R6Sx8E46h4tHN2Ba8h9KVn3/H
hMIwiO4qjnWjecp29Jc+NSEon51TDeuk5ZQk+YGQgF40huyXEW/Kg9EbgypDm8ndsjOVbHjitD7s
X2lpRgdOQ8HkT0rwFRvE3/m3aqCFtpEy2qremjq8UFIw84utmU+5rTKCWzBs5SgXVwhv6b8QMH/D
4TU0NAQnVqVZDHUdKwJhkNbly5pisL/49MqkiM4RGRlTA6QVd9C7E48qqy+IZS9xET6eCQo54Idr
48e8lM8feH/kR+uOiNG3hU7FH9FgnfUqdwy2XnCPkL00PXa0Auw5w4ia4aYooUwo7vm8XkBI7JxE
qlIYucsf2EGrKCzy49J8/3dQMC0e5UhZqek9iJ7PqwAq+ititHQruK1BYu08l2AzFeLEJjNA7ibt
FpwBlwg9KGt4HxZGw6xvHnWVBcD+ViFift3LLy1+yyLkvqoMVfrseLLzo/85VWjFxFrqh53NRMOh
JB80RZk/JZi4nIWfc6+Qn1ACrJR5P2bYbuNpZZu+uKFdH4btupzzUNJffgMGX+mHAQpTVp241UXG
JLqNmbVvv1e+3pia/Kh3BtSgJqfCu4tkRRcf/GsXkBbAZ+0D9Npbg31fZ0RyKtvoUfQuMzaWk8TR
lVqmJaaERTUlL53+u+DrvFPo10LlIwRs/pQkMJ2ZPN5A/ay4x+wnUYhzX8/163U9jTb7cS9IolfX
y278T6cyTJrKeazX89TILIg/MRwS8Tt/p8pp1WK6enzt1qWX8PBCsIBhfqBAUH/HzzVFJ3kbcrvy
rZhXFSvZu3CRkIJolRaeRm0w0ye8CiB9FH6MWR0e5Nt7RDuNEHlssCyObiihT+4T/g/ccsO9DivJ
ONv1pwiYmnvhI4tTWoYzYOAd7vz18AhxfLgYwmKfSAKIBuSbLLzBsPkZdYXvYlLGphPFX718Jv/B
vy8NK6wqzadN4zh3A9ziak3DnPrjsiPJHY+xcHbBcXU51UqDzf5MXZw1EDrhDZrNxPa2o5TXZ3Cp
+hu6Fmv1vCFgiHfkDWAb4cQYDgDWxxCr7FPKeSveYrnjEZoOCKVB2Mlqde0TB3snhvrjj3c+AfLP
E1NRULzOfnPULtqw4g99SXknVoVLV29JZGUF0Kcbm4ftBsPrbf7PRgW/u6gYQxNWOJ/xXxZy5CAc
R0dtA4m9gi5hOlbVnj7AU7C5XaZO8tl9zOv/4DNQOsV9FmMjs9FySMz1wrDiv+OVblhXvN6TKfir
a8sgZXEgxVzVUtsMVILGjyc7sE7hcfKaBOVXHfndlLjp9PovHzTsISdiKuJzTP6Fd/P1PnVqzb9k
eeRaALgrO9bYZ0ERod1Q/6vGvYzjG8YmlhvDPUF3ActF68ylLYT6poDm2JLvdEW5No2fISLTFtF+
Sp2S2hS1siTxfjHzuN947USTbYMNe8vEFk2zExyWB+3YC3O0I7816apmih0toCUNPoy6fgPI86ZV
i5vI1huInB1BxcmXYHBTPXlSTESieJ3yTRAwQa+p15U6aH1y44IgiryrADYCvpGnhRNU99sr9gsJ
1UuuodqjRfhIolqRiHILLtS/kaOg91arAqIA9+YMwzxxvqTwPq1aqbuxrPpg05oxSsO6Em3zzRwt
WbtsJaKcUSx66jLCi/18ww5VQXu6JdyVMxbDkTiBrKtnCxkXN+fQ/yv0KGWARZKQA4iSMmgcL+Pw
81Cyi04LkVUJScufhktim1kS6n279ykiPRss9a4ISPCbHLz2WqDNGLno0J/mXEtaa44JZnmLzae4
MiKPdLn6CRvJ0pL0bW8kQzOzVqrhppWPP9aQtMEJS3ykU9ibXXLcE1hvjKxzhl9PteJBqWYOG/RE
5GfHTjqyopDecsPCax1EuQXZMX6QycMZRSKuKlWImKCYD4+ncWMtcu15kQ5FdILL05Z9kCAJpL6J
CvSNP6A6eho7zsnApUNQdSkpvRuLulWFjtnZMaivYAXApXD4ZMfVSaoEIVvY5NTRZmUOPtOvdbQw
K32BsltKK7P/2Anu1qHZAxEwfp6ndd2U+o/9G8mT5q9b9Egqpo/i1Exm7a5rrlfM8pvoNApLuHTx
ROvvu277N+sOoxfv2XomO8J2UC8nUJPHXptmvaMoW9wSHktJKsLG3HB2XmeNqa2+urBQpYpsgQcF
inERlJtzyS6F/+zdHCK7PdsVyjk/2byU1BTZbXyhRC1mmZlVaxb643yH0lYyn4Wo+KWur81ZqrFy
Ect5O1uM3DNzATjXweN+v2YV7F2EA0E6LcaZGZ8tyVZCyg+Okte/w8sCO+YT4S+hUWlAnxNKIAhP
vm/lEP3weuN1j9lNKZvEDexbLWFt6IqGhcjComRqUsQXEi3Olrraq4Y1ilJZe87FdGUnFaUZ/OvE
+BSTFXOt/ddPQDFus7cSiGq7dWfXvu1Se15Yejr0JDq5PTOQIHJnslIjsJL3iTb/ux3Vmol5KG+d
UXFSUMXeS4frc/vTw97C8+0d6Ahh8dBsTNJ0koXP+GBq1AaXUd7pNIm8uVqFuE7Gvm6am5ylwtpA
0TjmzgGTqpDpB0pI67kN2ZnTFVbV93qbVvvVygRm3Vr21Sn0L7PQY3E6EJJdbRk7gXsGmMZShum1
TP6GMnMLfXwlSZh21/PnvwAPtFVGPXsBAgkbyhmPXSQaZoiIl4BztBNk2WUR2yLhnqKn2y65s/oj
4wqJoBp0pXCVtPmUEZ6Hsp2Rgj1VDuRJCfB5ggzTHq4NWS3wlM2+rGOBmGXUkEwVdg0+Wmvs9T21
WZY0x1s2aSHGnKkExzrJVrphkH/wvxIKbAZZGptNKbJ+EtjdYS2Oy/RvwkxPwp40He5K/oRtM6PG
l1qintQyRLEAmmNV1HJ2/VYqwAZQtYg7jTufkF4eQtX6zo+jkDw0KfoV2UzHG8fQJ60UHFcpev3j
gsxPEWWdL2wIbg+FEhsEi95+1ZcPNkWtMY1djHtUuJjbX9zuKYKvOwXQEguEkiikkiU0N6oPHr5G
qrz+YpAZh+Ma23Tns9YC5QK7VRcJCpzv69EdJ4fZhcXaA9p6dHiZr+8XTAppDUrtTv/RDptsiC5y
A47KmRzmogo8UZV6yhWUu+A9hvT/bkX9l3Gnq/+vtPi/78T4lxdummcJZWjjw1hbR2Gm9lrEchx2
vyPmdWskrBhnv/2QdGEvpN9aP7FNBlaPUD1WAIVo2B3cw2Lt2W+ayvQR31n4Jf0ON7Z57Gl/kjeb
HRFZgVFn8XuVUPoLZAj3TNi87eCekqCVZLo24upXyJTMz6Wl82S/88NI8X+BGYa9XbKK1pRT4f8k
qzIH5mWleDZzAeVT8ND3KvkNnGLaH7YEKdLFDQ+Qa7LFv0T+Aadu+Ys03pc5aZ3NUGvBhJ/hxSqQ
93L3fptdKQYHHvzOwKKBTL9KgjbwPjFsCzDFFUOSc8rLbPrgEF1x4UjGMfNuyB+ShpYQU5Fosry1
uwjUZaSskblEhbULcvm5mu9/UfI7d4F8UpfDnu3fpOIEM4sBLUIqNn30gkvTc5xMjOI4eR9m20fx
QchxOOzqpKZ1SLJB/HagyJHAuaQzyQ+/b8Kg+seD9ec4keV25Z+vE/b6GhaOVO7OFE61UqSuuSJn
xlgPce5lbAfeIy+v2TwgP78Ctnl1PegY2At7ofmFKNLi8oWHwL4v9U+yLcmBgAbc3KEzlNBrqr7o
AwsPWK8AK/jFLacnaQ635DO/ynmNvxbDDBRNvj+JVHNJo+uNHAOE2jM2dTxzNESPDEO9J36pvEhT
tGfSMJId9OtobJPVLW1wBtgvogLXZfapJSSD15WgARW27xnO6/1K54DSAnOfuAwYc98jpGBl+zDB
KJ+m+HaizUdKyHDOw/E/mZ1s7SYIdVnwwRifAthVKlNdHoZKSvUXjE7RuTbzobaVlEcKaEzl6IfN
qAHdng2WhqDUYe9G8wgnmyNRBkDjb0fEso784qMSeGntOogeRG4WlDZr95roNTqceQE6U43+ZU8E
xzupCL8oPw/T3rpR3d+i++ozj4ht3epj/BsczeeH8xXstQtepQyUevzh571K1+1VuC2MBKH7m1BB
TgWeknjHZzkswxvdINVTk67bOWVYCcRamX8SLtnIRlSkgM+SBJ1aNB/3w8Ky3t5dGSvSEKxLJEWn
tSaxYW489by2w/752QH/kIUpX5YbTk3wZm+mGbzh0+g2vr/ZvueFKFyuSmeOFvxFQiLlVZkml3dO
+WQHubtnHdwhnLH6iXiW+JzQgS/DbANcUyy3+RAiMijppb5NCjeXpddDLxSU79RbX82wt+eKwgnr
6vt+50oI3rxnXjptjhJvwBhnwDwEEHFIhDpvcCxqn7bUtQOM9aDo7DGuRvu6nJEBSmsGT8xKvRDB
qhEolH1FG7Hk0MZUHyjSJC4Yb4NXI7wKZomfcd0sYr/k3BJUy2fYDL6+pMZmXtjukXEYiFfa8Qg8
qRaPeKQZu66M4nLgcKyjR110jzfOaGqkwdJIJZNJvaTRytAri04S3EfGvFSMBPerXjK/frUhNUqc
sIilKlk1TteZkJaX6V0RESPCREMYSaFZtlLZx2CG29+Ui2wl2hoMF9OMn0tAmNGcQwGSJv9xyIfq
g5NoHvHSX4r3H/5oVsJjFX3kJWcVxUi01Q3fu0swCw5VKIrSSa92X2m1AzaYrL56M6eAhGlzyu82
dO688MbMV1a3vP4EJwofwRbG9O924nUFFvMaJh15GfKF5tQPH7MFqqHl9VClifLJzWMVcvxHVZCY
XgPD8hb+2koXQmdRUeGz0z1W05BTg+09K9Z4mtfL2rDZNPpOn7UFy/5419KEgc8s3rZB5GjHOmmB
T5aoCEni+LWgGgQI/Zoc5tTbzq9uDWnZd4gOqAqmAj3FIhbmr1Y49ud4PtSIWMz7MmvZIpQLmEyA
jgw1ZVbkVpbdgaHH7QRxb6AFpYjEkvypOHzWmWwAO2MSQNM3qCCu49aKvx8ezJJVRXR4oMfRxK/q
6JIb5MqWz/agesdXVTHnwj2U4HWN+MLE9yGMlbaFA4TD2BMcC35nkef4Oi1dseM4gx7FusAA61E1
2ugorjqoHMVrgEe7Zu1VT7hiK8AcE+T0GLdDEYfhKmlWMyd7hs3+vCrUuv58JLpEllkij7kvCiKg
8Q4OU10lHZj1WmuGL+O4SAdkceKr5G+3kKXUJvDq7qWtxxaBp4WgpxPoUdc6dQmlzMG6tqVYTicc
cHiN4d3WX4uzw/U2whRz70vdL0lAKLlxH3+2++J9T30EMpLEKEjenkFGHkuffMrPmtoYwax67wCM
CfYIzQ/0fAc0LSNkqJe3rnzYwlTh4iLM/Hr7GuB5ReO6VgDj4s+9cgE3IhyBj3CxK0ZYNff1b/zG
iP1F1Is8AxHBZtNy
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
