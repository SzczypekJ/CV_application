// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Sun Mar 26 16:05:50 2023
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
AzA4YQyZAzRi1/2G+WPpWDWZ75tGml5TPRsyGZ1r4McgMk0rLTOTKhY0QlLYqWc8aFNv8YLQLtJx
Wrmho+PKEJWIhqlFAFJjlXc3Cllfi9eT54GV4TbaMBBefO1RzgyL0o2HJi2NFo6fwMT4dHBP/WCr
YI9MPlwrqCCfwVEE2KY2upPjMbBfphIc6+AmUbp4DCmFv2F1wjK+EiLXK71ieK2EnLOnRqOvlGXs
U+G6LGIq+DPWACvK73G8NA2r664+EnP5NMUL+groqVDE4L94+62wzGE8S8LhTLKydEl+GVt0IbiI
+o93n5YGa7z6wc7tD3UFx1tQ9n+8th9I161lIQ==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
nQJ6pTGdmUpeNDckfp3hzzAVyV5aAGZ+lOC4ISW4aMCedIKXvOn1GTSz7wjsEGI2/43UQAnXQ8SS
sFTo7F2vwQkGRxQYwD8FReB3N0hWd1H/Th5RYTXnmMAiYo9BMRPnVEYsDifzO85EPyZuprMw69AK
OWYUdiMp37BhfOMLNoq5GzZIzYAr3idcCIEIOofC5JLHp13TcraMjIE88LMXZpAbAX7I5DamLZib
b+nz9UjKeqwdvusA9FV3mu3dbbdB5V5APeERLrUi3wbNdUxtAq164ApUOhRszrQn3skU80QhoF5t
XQhFLsROB4wQEidyCv7fnPAvM8DK8ZJ5Rp4mWg==

`pragma protect data_method = "AES128-CBC"
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 11216)
`pragma protect data_block
E7xj2Vdhq5zqFmsLYvjhy8u9L+RYc+GrzmqtufIhv/IMk+oPsBhuBr0uY/Px6GeDWEU47pSfnC5F
dA3gQyejC2dULGH3OTpimL6tj+4DEzQOqMjXMcim/NKSznnf7ANd4vMuOAaabsY66cDTBT7DkykL
4cj9vrdcTiyuS+RX/weyaeSHObeel6/BMsAvo47Udlv/aUNqJEdDkzyeETPzu+hMi6sENhLeFmbd
b5RuAgUijAStLjUPUKsbIzs9benV48kZ10eeSenR3AjIqh6ZoH/IKt/lYAp0wIMZT1F+gXZlBFyi
+2OWbahl+M0ywWWhn1l4vRH9iy+ZLa6Nv5N0gZPpPtQ5iRPHVF+ktPJMiEetpMkrJphxHLtQywiz
HB2dC3oS/krfQ2Oz5v/OYMPfmyz/FZ6E6onO1ENp8FB83jAw0d/MrXn6r4eqYd8vq0T7vhlERmT9
cv45hgX9c5uLepcnMH/olCRf8EpwhnxENmL42LoiYUwU9f/qQ2RRxP/hemI2rSCZ0MODf+bBixOA
g1JfARNrudu53zOocffUJ/aooZgXC0yU8yDc8Iku9T1Cbtuyfga8YO36tV9xPNIid04onp44cKq/
8Q/VEsfLCsmEh387Jl41QGSBNbzDfr1y22yy/TqawsIKamJ9CoDqG9ZElfVQa8CTmE6MQW479Vdp
8LJyCet5XTlnjw+8PLN47YNWesjLIFBjW5AC40YksGc6/Bve9fDkb3RiuTF6OPbIKLsA9VJUwIhj
7OipiHscI29VDXAYec+i5DvRMLVnV32LzthCaXE7T1KAj15CnObaRBFUanwSpc8i7v3WYCex/xrm
GLyjrYyv7qdKZtLKYONLN6v/ZgHwd2azDsnvTb1xT8+wttH+UgYo0lAWnIJosxRK7kUxEW0rrNo5
KfNN3t0ZwjNbq511G9DaJvCY9nzBCCqKCT0+x88PJpPxEyWAFCKo9QvvMHXH/Cbkn4tOATEBnhtC
zrkwVr4H7j690XX91tXr0QaHQyViQXaLXjO7kKTuN881wS8Z2T1LKVRK3riIk1xA/+BY+2J4P9HV
KXHWAl20GVpABlD6DthAVme7vSfF5VYNTaoSxJzcFt0xwe0PurlDreFb1B5DhLYHl/WyUQmFEh/m
gLYRFzFybUrxkL8DpWOMGp+0+ZFAl/2m4fWR5jBhdFIjCrQywothXToMN29bvPnDEkjcLlVx7sOw
MwCQjcPEXgdHrT8qbY5c8+9CDCUkm45EAGdxod1evtMBYHaT3kJuiFRozpGzGqmBkgeMIJW+mz4T
PPASyJmn5MNdmjMedjmqQKJOOiYP9isqPefjCsVUXFQDMwW73u/EEUdRqItryyK7xAYgBCESWy78
Z2MH9Uv58JMUpzcw3xJwZRyUCr/SVVKgHPcTqDwtA75Xtx4tdcXXJ4rAl/GH2KTZWatjD1z0zSlP
BSmL0R/6KjTuaVXmGrjJxuaH8mrnRaxUIjsFSz6l3poLL59iEH45XNr5wjF6SNtp2L+nfY0EKF06
xxm7ClB9yODKGtAT62yWswX4II7MAdsOrcdx0ty20PorufJQcVXkdPju//8dTSBhfKS4e1k0Ig18
dw4Nd/hkFRWB75ztRl5BJOrg70r2rUsRV0XNILRnIS5gi2lEgdYmc3+NWDSgx+oaXrhRK7vuFm2i
Nxk0K3WyuxKhU5IC5KTs+WFpSN9zrkdHXP2uUjKdYeODeqPiagN/rVc0ZTBpH37pNRKPFxceL3lu
SiVoq0yVp8dbbTql0xo4XooRC4cP1KXGNpUQexLzIoGR5Dlbx/jvAcNY1WQLz8W24kdQn5nA1iwV
YE3N4QCouBxds3udMHj989Wv+FcKO4ZCM5Rv4pTriOX8Z8jBk1buBkQ0/8t29Uu2Zo1SQPPtRFlK
bTUAqN3m1FhwlaM53APj1jiZWJCQVJTcie0g5lZ97b0c7YDvALaWWUP5b55x73bjnTx90Wf3RJ4j
656Ni5FrY1xdtiX4zs5KslMgnaVT5adnuuA+wXCTpc4zMICId9jHmtczPDz7VZTnYV5pTmW3EHGL
nUG3PSIa5TpHclD2R3aZpealJlT1vDoQq667z6nsZtRfdX2y06hj/QwTrq1a+oOobJKwVR4zRYMy
eyT+SHT3BS3u/C82RXzVV7gNUcl8s9jQ8dsOrhXfxpcIkfEJxaMOqK/ICR5aiP2N6t695kJIhRRw
dGIlypSS/hRVm6b3q+MRMdn+gLYuHPjLEqXAT5JTjNOT2qLuV2dXoRAu2+EMS4+ndTMo58srWRW0
GjZaMaxU3GXHCgGHUtW5xoJml6SDNfIGhu49S15eH1DzlnGvLqRYyLwOmwCoVpVSA67yc7Si+l3w
ddqloYzd/2zQt3yxFGMiemTd2MxfNOgMqd8TWgj+SlrZQHCMhfxgtDCClFoKyegkhiiLf7Cav4TH
V9CFwQqeQkfo/77L5zusFGiXl53nfcizJU5FSm2411+xA8MCXqAJLm6nOdN47J4FI3PMKan5QtBi
jzafRXwBI55Uaf3gwEVFWtPvFI1OTd4fYKYe9cVgzSrH1Wem5vZqw+RKCGJlG/SNvn+g1KBz6qd6
yj2oKGpnxN3zZraz8Ch3iG9ZmoABnMyL+l4OtMfLkKdSxtzKHEj/Aa32hen78f6q4emCDmR1/W/3
Vib9hnCZtynY6oJgKO5gEgJNtKnr4hxKgolrePhMX/f7hBcPLRbvJ3KnZSb3Cbkkigd5CaJLnCvJ
D7g1SlYi9utV70SWuXxDqBtb/uVDxjmFe3mh0ceUDaampZC88t+SiPksT/3qp6TO8PkTLnTwaeci
PQJnntMuAdDAkuFJUGA/6JrVFA6zVKI48U0UqAZPbvuzwkCOYC9mzbD+X08ZB2VA3/ON4YtHFsuk
GIt7NrjYiKxUx3A8STTBhiLw34pu8fQOEX1Ksjp/KmZxJ0GLoSazvmFwmCxnLIbErn1TcYBmBpAO
irL4t2VHTm3oZtk0BWrkOnjqeNLZSiNRGCLuHmtfm+2SvyOui1PEiQth1jNAijq3mt2Vzcr/fFT0
8c89kqpARlHPF1hXdbPqxUfquXZxHzhjMr8fSi3/Y2eA/yl78fFpVv9I6Bz+HOZX1CH5Z7WEnwdf
4HTkQHmUzTLMrd2Za3A6ZQWkG5Nciza2QNbcUVOwlsjMxykm2jWeMLpgUBkAH1/cRc2nEU+YYpY2
8QuRCTdouhzap/CrSPjvslzX7p+Auv39VpqjbKW7oPxEmjXTpkIv6W4JBd5Je9rrcm7teIgEGtlW
cA/pDiX6ty9Rld5vprLkhiXqU6gTVjDb5MlK8M2rJNuHKc1HlXQoKCiICQpqVa30GFP38VpzeHny
aoxNV+ktVSi6KFsfwsVmFZFQZkKuHbevs+G6gXPvg4+Hfiasgs8fH1eHZyJVd7L7nQ7wWuS1wrvF
pRmcoVclsBsM15xr/b9x95vfLIIgbIdqglE5Dm28P2EKgxMCxsDFVTYYalEomlUMr3gxIt7giO0F
qw7U3dH/hcP6DD42EXmd6PcqJ0bKmVW/ayQJ8Rf1h2KZt4XTXmpLQtaQKNuc3D4zS7vFPb7sJnly
kee/SH5HVE2mRBk6kg6Z56uVBXeFnljXduibDLy+2vTHg5+4swkIpkK9fEWMD16buFJrXd8kQDNj
8PHj9mtx2HpaKIfBNLdmjIoy+/fCQ1YIM9f/V2Ea8s3u83nt0rS6O+hK/R1BiLDyg+ASi2+h7AIi
ZnezCBdm8I3URrMXozCFYiaMwHjlJ5KmA7f20uAyh9CC8cbzZgylMTExHvOANyOyATfcT6GPBsHZ
Y1rnC8X4JjG3fGi6Pn3pUgz9QumWIef2VViyFdqO0SGY3MGy+Aii+AI4H/zK0DFHmc8r8ccYLI0c
PohzG5pm32vDQQB15ElWiSiGgavLG0YAUXDXv7yK9vE8ID/Wfbqt8OpBT4LCOps5XNnPlnZxGPa6
3EEWA86KbBIofk1KNDRcM0DW8w2Qwpb56I4YeOvnXoKhWPbFDLKd0QxmY8dxThl0Kcs8STUX5nul
10mMFBJgeNf4iWhlWIakkw7t4lFmrBO5Rjv/8w+iTns01MzKmIPthwOAUbH39H0Z6qpNiwq4u39W
9M17Yg0PaMQLMC2aAoeqtIXNsXiw7BT/0v+NyzDkuG0oF2WLlspZhJEE0oo6dPGbr6i5oEf58IzN
hERaxTBz1lhjavQzguwlNwIbLZIywDak2m9AmoH8X6pVr3oWpecQLcdu8zeofFaboW5dE2HQ+3Rb
/VHFg15ZReDpmCUmJVh200B27Dmn9y3flgdRyeUcqqjz1712v1y3V2ApFHBBgUpvjA1K6WZfzTfE
7bV3xyQoyYGXm+DIUzPv9z8QEMa9SVyWAfdV1vtDTIUiXJ7YJ/sFChUpU/axPfcNZzXEzgmcRcKN
szgfX+hfZL6b3Dmc2vZEFwgikeipjglEVxgoV8Z/DSyNjUpDbf+DKKoSCSscn3msit7Dg/BjGsMC
RU81CPc2KDekmQAtTE4kXiMWB4wWLI81zy2Amk217X8ku3bbJh03QnauFbd2Cl7rme8S/aB5uqfU
zZaWq5vSOADoShxwOdmQUjs3P3pCAgNAEWjGebKtq31iEcuZXsYCM/+gb3AkCQmBJQfQuO3OFT5A
vAaZxu8vxvRVq5gxvl3ThfyGNfa02s7c/dgR7SQcJXieHWHekDQLy6uMQlLYBTqCNMrVd/JEaI2S
LxqUO/UgLYzZZ7fRrVTDOOoBqs9htun0ZmeA2/FxC0Z0fG5KZLTf8bEVP1otX0ZiHDz3nHYN8T94
YjcvGWO8oqSn7Bt9p+Za6HqZ5LlXmxDO1fQng6yemZJySmVHTQj8DmYtAo5QlkcgSP78t1T4vgzW
1VjmzXVtj+tNaEV9m2e4S4qa66S750nSUxUrBS3mzq/SPOl3TtCX/vlK2YKsnBSaalSWKAF5IAEj
Ma0afTX9EPO3+Mo5tQD06w5hEM95QlL4xWWQk2augZlSFCkLYRvRR1s0V4Db0FGZxz1dgSYCOZMf
hgGkkO+dnJBBo5s/p8FaO5nxUOOP3CtPjR6RlglW6UoLkAI81ax29i0sUQ/TbHDvGgC9Mg/QuisV
K97NnfVGRe3aa/2Ls5kw/B2XqgQ/LuSOKA9qu/WQhvXICYPpkqbtRt10LYSgCA6QNN/8ZqYy3GAl
6M6AN92eyagxIzOAdBWIw6Z2h2UCewcdT1Qk0wFFuhlfy3xurUBTDXlfIv3H2K3+tADdo7Ui/+Ku
3MHqxP3zgft9H6ZnWQHogNQCmnc8o4hbIq0PAgpZOKN30Ht6VeiGgt3cusSgRYF3fjsKdYr8EGtB
+sd92kCkwA8aDmTZl0OU7agrlPX4VuYxQtkosQyIGHk8WYA9JkQDZFUSYEke2rdtZxXv+lZ3pCcG
Pp7JT/sI8mdfZVYXy8APEVVkVSIbE5w6IC7lUdSWIe85DRSAsRNIEQUVa0HjUl1VLUWa0ejivRZp
FrbUtkkKIfFmWixbqfcmXYo4kuyTZ5VNXGsIZG2UzLWaK2LNbnSo+t8K2v1RId5O41yq2mnlK4co
GQMd7ICuaMAktVmhQq7q9A5BOg7fRMYw6HeqOLHyDHAqBqqoIW3kkGElDl0nV4hmTJtyo4HBWNi3
/Q/xliPUtHKWgcG3GrhiLJPESILVDJinhBORdobc9r+6fVYkfoWshQx2uMUwldys40gEEMYIT72M
rx4YV7lDr2qJUeEiHNrbKiPMDhh1+aG7k9F7486/9FJC4datf9yiH0UpzFB97DON34hGBJZdnlRP
0CmJBCSsK33rKvLI4bU10jtxDzXEy/hF1AzU/F3SOW8BEGsaJQsQyzpzwkwoZFSs6kXb77Lemnml
jzITNee/17rAyG7s9pCbaz7BdpxnEqgqLyDN3jGcdDlq45zBXqr7S8J1OvTZ2kXPkvrF1ON9GtTa
inX/wWMvk6Z6+kVPIy16yG8GCzIQRZULapauk+FBVK+IrcyzeRQjMqUX5Eixcjs18nAVarAyU+ZD
b31cc45YFNY82p2s4LjHP9ApDZN5oaULl811PjXC22EvyB1KsL7oMAzbPj2Tx4fwbOtkghj7ln3+
EApB6P7hg0URnMekdKRJHD1E1VWqv4xaKJ9cUVAzzeWZjuDnz6qEvEDEVoMJXjn0LZ0hn2c+C6oE
gKTUO/cpF2D+PUQmxgg6yghX3UwwD/g7p5Ux1Rk8wT8zUxWLgEKBPUrTIplD0duvh0TTKF8aUcSl
e84tVgH5wMRjfFw71KWxwp+agW//ASyLk9oA2hN7B9TDIe4Tp70EzkmRJSKQK0KwUXhg4zCqYiif
VjCoyA3TAILE4cw/2FRn7ZsxmxN2y1Q+oMtvfLwU3DJ1r0fAEGKE8jpbEugFDX82n1/82fs4gEWm
/LjgQJgCRI94p9/1SzVG6Akz/N0Axvn4jXfz8ximxQitNSnYEl+Zl4hadsn/lgMCWt7PS+xsQOW5
cmk2axtpHuTlGxPUCg0P6gDrP8LYB+Do7stnHzhQW70awi9tgm9MntnzApXgyE2p+XXIhycDZprU
e4zppcHr4RqOd1V7aIMB+MzJyZtO/QYqCiRJuQVgoQvjlBONsGbBmKKm9BtHpGXepPS6pHawiJgF
tMT1PmKWDcUrowIl1G7Rq2H/p2uwd2UpYNfpUJe5JI9ztItxR49cVkO5Dm27MBHmIf/dPXjJM4KH
P7R4NnQyVtEpJVxBE6ZqQ8R9NfpKFovLNaY8wkO5XnOKr2zmU+D2AEGWEvL7pgYgflpKlUZ/eYpD
V7355peqhcRKybkZu0ws4stnJHger2yyDJ9Z6W9MIcTfwuK2bWpeTtE1mo8zYzirk0QiWDWH1RbV
bzC2Y0Not3wEZAcdtRhkc+xV67bQHlFDjZlfI9t7qsA/J7uompqLR+VbP+Y1cFd9Oop6qaOMZDT9
wR3WU+cp1i4anCA0blsdxblDQI0nwg5FGNQGjKbptQfugF0G05O6StRIw8aTpjNJjA29rZI+oupP
yb34DRtyCg8PSQuw7ttedTW96LKm1O5Airp+bFVQB/Cj80+1VGPtGcvAchu+oFARbA9DA/IAnAxn
UlQI115MP/NKpU3OtJsVHwz8rTZcmeSmZ3jnIgKYGDA4cuEiROtLOAqXRx6WVDTkmJAQk8edAaVZ
GG6M/8u035GySs81+io/idjaOlrYiQ9p1rdvfMi1/KJRCd9AdcVhCqXPfiddBlSAiQF8BLgCLFmQ
UH0LdsAtZvFsG5/2KTOUAsbEljbqxM1Ir21fFoY/kN7M8uAeX9KrnqBQKklyt9LDH61qnIdeZR2b
h+pV3I0+uMafgAhn3aaPmgK9U3ImyRmH3/6vWROyOI6QHlPPEJoD5yj31FkDJUH35wEl89/43/DY
tyEZOED+j4MgeI3kokquEV3E1KIW0Y+8Mr2kveq3Qo8tPuwGJCYWoY0S5IOeY1p665Yx9+Cqe8NH
pQ2+zzF4D+wbL9CjKGoqNja9PeDhc9SnleG9qwVsJ0fkjn7QHZLAgSI4pwE+Qbsrjk4iFFlA+Nf6
C3jmtEVZhFxp6N1Iad0T5NS8N1NrtJ1G8E4GPc3Xf7FQulCw/0b24cud6GlzYmHsy5GCuc40/uXX
nYYxwwonJQeLUv5qqlJNAxZAxsequ4BtqrolZduCTbIIMkNNJXBkPyDrw6KBSgdolMxLMy08Di7n
pYMx8SVqBZIi1H3xBJIWH/jwV2kUKqQV02nvyi4xhz0pTVHn0j9DSxE0P9DRnWmJ0a1IN2Fbi6vG
9D52pWsZpP9zm5frEPPC327xMbCze0IfjryFIogDCbKRk4YrzbUe/xCccMt0GqoGRcSNuPzG0Hv3
KggjgPjRNuAH94XoHnk0XnJxXFC+Mz4/eYZ+dA3KAFPO1+d5juWqrjeByurCLGb7KO9847sZVM4l
5juqdOkEjK5lCp2cbSaxgslr/yi2EGv51dhUjILuozF50pmV/AiLij2GqBhJDkmUfX6aRZxnzyt/
btx/5Y/PjuNEhBKX3icCRFRNrXBoJ3uQ9tRQxVeRTNIAOq83QbbraIq3Z/KSdwui+cD6faDROIMj
OzoZetnEo6ui8RzjyG6AIkaCD22k7lQjHgmncohc5ZZici6sw2dmS9SSGSyRchJgU6KweYq196wi
iEf2a4zwq1p/jOz3i0jHBnVX66gMmNK7aZelU9joNikwX5sW0NqhixtZ6gYkieayatipNn55UNZD
rYSf9vOBjlMqmF78vLbnemlb/Gc2TKL6ltdF3gyUifWu+oKwKSwCZupitkW6GrPWLdTeCkHv7a8l
Vc6wZnur29FXqIdkAAJ0CJ59XWsvya8oV1chPCiZaphEvUDAJ5jd1E3nWnQwtxe3WcIBeikKF2+x
ZbQDx5lWnxhpqdgD09FRwneOmh9VYJMVCS9pkOLbajmyESEG5iTiECqAB/gSgt+q3fcLKxczxBPe
bhCyj4+uuFqpEB1rxNqujG9qi85Jg4AyAtKrpelP4T7xS/zUGcCokyd1Kz8DuRBIkC3MiFc6oKrw
SX6t942G7m7wT5+icogMmV20sSH4LXq3i2DtqyuIulGu/bFFI8Rqgop/9cpzXzzTADJ1HMmawf5h
UQGRXm04iEC839JRVy26LJILP4k6KnRGYuWXfB98377L1zf8ae28ZD/ykOFwW4j/vgEaeWJ9kjII
p1SDUuuj/9sTtOIk3GtbZ/b8UmqFw/zujOpcf4orfGoZ/s//rJS1oVHgQknYy3gbL7NskmUbfovy
OMUBGgCnslVgPaqmmauqyqn7dn64xm0JVnsTC/AD6FwAem9bAyXAg/1KeYDdkapJcKpNv74ndHdM
/eMrrCLmCvDEmT+1sPkEhQwF/q1GJJqwmz75NMwWJrYwuD0nXKRm9ShDeoUvwhDz9hduObJCr31H
O7+JTraU8VFWHF0MJNij+GMI+H4/FQQP1n7Xpxo2QMQGDyWAeC+TU+qJCCqWpAirvum7cwIfZPK4
0jrJkDHQoYV604UhezwN1Aw9umznJIxTBQn6pN/gb57A89bxC8NfsiEgxCPVL/PL11FZPPl0KKCS
G48DKeOwbdIIRFbc8FMYddgjMR9uxLOgp/r1K7qXe8XXhaUU3hePp+ge3yyCJrxbCGkkPZmo25hf
y400xZjXU7HVgHhOphJ4xjSLnkYS1K8B+jWTku2bdOwhpuoOiQhu/jzCQGw6NjlxWA3DJnGOF2FO
jra1YyysRYiV8PWeLmE/uVGrz4d78mRgAE6h1w35kWl/MbBYBm/wKd7iJfsUXct4BkooLygLVZQd
WU6G5A/j35z7b6XAv5Is+8/M+rCxZAl5w+EmflHJjjm3CXSNEn0JJIQv8EI6QHSFNi27vkfn0KE0
wabpNgQr6m+/NVxG5cl/waAp0XMHMCTZNF6jNM1GndxWFpex+rrCfjdLDoS3nvhWfCxx8ZepPCla
gRLhh+P+IKkgA9WQr8CCYY3/awFmtPXEGTGwAEVy9kD9h/ck2ooX7rozJReZ7BS4GUdpBqRm0Kjx
vekTXWARuFGjDKXaW5SfELfr4tbTexSq6yAbJecgKi6UfyGFEdSxWPq1a57cYMWtIXx0UuXwVEzw
30xuzcLiSk6BKAF9uS7BpMLoSA8dipcUXqyeWxiUbXAMXAieKdXI840G1NPk98qkWkZRMVb8EL1U
q4IZbld/sz7t2dJnAnHO8dLB7K2TzWg/w5rKvP+cuGS3wGNE20vL3b2RwWCPgThwXuK/fCDWT1VU
gOhEN1c8A3qifgjkoZ9NCjFGYKXZad2k7fb0sr9S/LszAx77bcIA8h+8+MIl0Ztsn9aCEn8HkqDo
k9scFBH/zgnpnT9f6S1578rspKEHPgpyLJQB81jkwUx38wUGOjblHD9P8/7honZH3jE6ZSNN/0uj
5g8wOkwKJFWyHSAM6Jghh8SgfpK+SsHf5yAGM4YLoJ+PvtkiAEevLoNQcSaLcSFHo9duwjBaybn1
qYLGXLp28G6QTquK6V0jqs3rSALNdWQ5EOIVb39DsbzaP/MRMCjwxDAcC/+h5kpTYUHfH8rJXgyu
6Mr9de8U8MdxFjdtKXkpRFXyNFSt9a2vKS0C+R+28AbNeMXA/oHZNrW4wJxneFFwGy+hvO9cMXxp
IYvuL/wAdGqnvRbUb0DBvWjbalyeqGNJibDGyOME7lCv0Yqq2NSogINiihKj2r3bEvDkolvl3UJw
hXyEQURpOvlBK2iZCC2g+kPw7mnGFNpkGiFRSPyP9DZRhip/U0CAN+DmD0xRg3mClCrcwTSUYe4t
uRHN/DEjc8mZoCnvXpntTu4lX+U/TdiiQjrtgFKtaCoba6k6ZdWpx33G2YCR5GUxKMZepyuzbFN4
0E2HX6rKUxEr+t00glCaCZ/2ZJV9s47Utcf03+9Qrjn3ty78tz/NUcObC82pL6lIvAGpW6ozXhuf
vd8GjsM/ikQV9qNpl0mNNconf4Z9LN2hqNXiklEqDLJw+swPsXA2qTl0hj55VFoVhRpyPHrdk1hp
cFoZr1hA8zq8rdbFk/2/1xdO2JzgpU0JpPcRXtizeTHwhhPIdIvLb2KVULYg3hXZ0caJfGMuvvIs
IpVaqDg3RmsyjXMZnL9gqdo8NdmmdCNPbaeRDer8BcjpnS8LrvI45/qDAe0KzmlVwgDMVvkc5fu7
gRM12qX6nrznqj7L+JUg0Q+RlvBjAtCXjmWnjpHvD3tjRuGcPIRVTb4bB1zoc+rH0xcP/C3oqcY8
cxy9CkLpi/VyW0sCDP5cKC/VRj2iVZhmSjEnkXGys9QNdDxnw8HsSW9k/ZdBtC9knIpl1O3LZc76
zwzCSxmzLe1Md21+5TvUPVyTklKt/xDQ08EzGXhkWrXYgRLIVsXi+b/FkNNlIDQAwLWz03flqvEy
3bmxJNf1LtrQ0e/qeWKmYMQd4+DRS87fxEoteerbtoR+LIJtT6ouhwyoYTjV1rGHkuljGYtQ1QXx
3F/MrPKmABv70LQXjavQB3cpMl9Y9H/yXf/qM/ZXxlB7mnQfaEv9d4pP1T0kYjXjfg+9v8CuQ6F+
8AeXxeNknqHbdGXV5hTbAt8V95XJJUeHzbu5ehbuVaNgKYG3FXTFuQA+R0m58nFBCmzEDr62jvTD
F5AHjihH9BhXm63I+vHk6hot84HYuNwCA1t5h9pkO5Dq8zo4cPvdCviv+uENAemzt3CmUz5I06CS
iH0tPzwoVyCjrfdXYfx5nWXEYEN2nTUSLFVEnlsCuoJiaO6gKDJiM/uC387/ijpVK2p5eFBeTBHW
eKCrvoSo4Ht+o+Z4SuHg2navwhJm/Ge6MEAUvxqRqrm99sFgdYXHF2r0fD7I1OpEWCpMSniNMYbU
gh5HNSnsXj4R4gebrwDg5C1207KOz07tj80y/+TjK6Nqf5gJHGZvDWhLRoZH2+HjzOiR0R2s83to
eSfrUBPX3CU82IHHYU3RRWKuQ3ETbGnsgPK4HzkwqYOLJEr4FGD6Ex5WcYeGbUywrytYfQ2sDPBo
xLR0cw4K7wf7AQKv07xpYbHH0vo9afirh7hb8YD/7iYRVTI8W9MeUGuJUcJElY3w12bciscQ1z2P
YZ2x6axzqvKttzYYvgqLky6mXkb9vrVaJ0SyhSkPiGEiItUnx6wBu/CS5NHpRCdiBp+daK3HjKQw
1oxDNn2vwVJuodiCTYs+OPb4xgEQECAxb2Q3qbV88IvXsv6OzP4YgAspPhtkNVOEVmKaudMm8jyg
poFSi5Lljj8xyQfaDUwg+zM/vd4X9soQoBLwXLzThmEzzuGNUqneePkc2wqY8cohzlRdcZP41kQ8
mLtCv3YOBK3WD8UA7OdHh9pBU80O8sDLMlPf114ljZ+ipFOC042rPxnW5Boh0MGAgJxnpqihObrc
NUlrV0w/Y0ax4+l49DsAOjbBLJo1FKeG0FZRt+znH1kW3QBiNRFRwhgDTzU6acpdIvS0T6ljdcyT
E/jXOHchblxRgLLBiuSBdGDicoF7karow0uPOpLHtH1NnVqvkEk9MiDJv/Zw0j1HbmRcKEhr4MJK
v2TVjrDRagd9y8wIaj06FlPY0qIFIp/WGyhHd08iLfOPhdYmCStlcboAbVAEjGlSGJswE1rdTbbc
DhL7BZE2fSv12+iCZcDc7G34JvLeBwYaU2mdD7LeZugR+UBeOqsmR8HBEAuuQaGjBw94PGIaNFJO
NTeo8HyolcT1JjLUBL+vaNUV4B8centHgYRpA1k5BNeuwhRQ8Vyk5feVxhq3Ljts5naiF0UW6qFu
3uTk/Nt6Y7kuh5NgOUCmGic4lL+umb3SYk9Sue/xPnfq1zrlZyvwcnzc1LmZACbhQxMkSbEN6RLn
+iAdCQoY5U91UREsqkU+I9UaxK4NAACcm7Gg6UPiha3S767EpsAP5trmDSUECK4d9kxn3yUXSRvB
M7WhppPl4hYMyIDivipPoIuyn3PjqzCNVOKWU5GYz8LFjLntNZ2viKeLJ1ViDsI5JVyt2fthfTEB
3+9vnt4rM4Xf4fk3YX5j7VZ/0jmGFwOtsHl+bND8v6DODl3dv3MACH/GqrvxUytSZUU4yxipIVDb
iXaDA33RIGgraHAb8TkD4th0YRqR+HNTISuCF9+Fgmc/NvZ+BFr51FXPvvDwpo5V7CZvylEWHKrU
XJ71AhBsYpoEGyVFKKdgWj+I2t946H9bbvdrZmEc2KKE6qSAr90r8gFguVXiPlcOar7M22evMbu6
5Amyelqd3WtCD8aCMdDgqOz7k46q9PPvHao2NFNApoqX3GVSAiDCo7lmeMzQqCfKewjWl1eQEPQz
BjzbGvDM3j2K7pUr8Sxzc2/pT/MnVYmRYz9XAiL7PlgMyzLu7J4+qcHUG3zLTUWbloOw7lcycFTF
r1BV8X5QMVY7/EGnhy95JF1BfQIIkCdg+9J9eMvm81okk5ulH5ef3u38GTF4gx4BEdeOm6b1stTo
gi9HJAFpULeNtnJ/q3jjLchEYbQN1pXTVeXVMkx+75hZ4mNW8CFcaK7eyrCYN86hucaZ1rcNVvP9
zVNnrz62zrPjBMtGLgNdWbHV9w/E4HPouZRz7coCW853usXJ8t4T1TKGO0kyQYsIcrpUFli6ATAA
n1hjr3xPLG2Xe0qw6Hv8kBjOMv0UyXsPEDHheJkR+hkeFBxRNJXUtpr2pzHjCo4gNmEyXjslwuCI
PuHn2GBHsQ3CKGPolqtXykac8SXzI+oUFFhDEUyf6E21P4gebN63mA6Ug9gfi/1NMTovVQDUT4W7
K7RSFDzftcH8t95bGztYkgECLlVc3FVsBlVU2YaGBWfGjJRVf9A6Df9k+xdmI9lqpLgr9xapzpeV
/zK8IOGsz1TcyFM/v72X45SvtzO8bSsrzWoyxFrfHlajsMBgsWfv1QKkvwhotfAQUP31N/7NeMSm
5HcF6VN3dzFD0jM5ikyW2sRnJ0gv3pdcvS2xwuLQHOvc1MyBerSdXgLUcikeS1gncHhrx0rpA8mr
ngc6OLBazPOEXsel0iqev/p1+cZ8kAzd0/fAZvbdQBKkR+29D1+MMEtYIKpVLVO1OiW9kyyy+qZv
qzDjV0cZnIiRHjR5c8jm2j7qRxrIYy9qDLca42KcnOu4HMqo0ZL0JWIgGOdg8RFC10qObhP2K0FT
iNfW/fXpD7ScxJ+4V5OhnNiom9KVj19UH+LKOSDf96qpzPn10A6jOHN1t7tDMjzWycEqV2TYub2c
wQ6w49F9UTVlcgKbkK6KxaBY54SSnQ9W4UEIc2GdW+XvAEmc/Wj+V0ftF2hOa1d7u+kaoL7G1dbr
TBbjv4VzZOjLV+QxlqizQUGvijEDlp3W3QgQgIBbKxebeiLwylPgvRWDNbMNx7M3Of+4R4zv+E4n
+7XbmxLPCRRpqMu0AjNWQFCnsNUk1nbEz6rBw5Cu9vbCwzC127Rlzh8hMQ39kBl4xxlT1VJsw7lM
rDKBBW5gW+aD7vZx8Z8Zsday+imdNInhUPPTPY0ZNba/TD/csR/7+fH7IDLmCWAX0nMlxi9fxbcu
GEtE1QJMOq4KiGQjX86sMSD/vDPasJ3WeXuONGu6xadijMwpHnm9XzDDntRt94c9WezWe8QiLpTR
iu8jSHmi0b1XX98VePJ7EiB9f82dITxF1OGosYUFWNPIdVLWdkAl1d25TvzoE8V1LgTQBeWSOz0q
f4D2phJYXk2cTu1uDTb+A0mwWISshzmC9KqSqqYEBKx8GtNCfgnS01ZJDz0c2TXReGIlW/XfgcgZ
TkvgBu1xiL79zi6UtjfFtatjp2OcjWqkvESj1HgiTU/tPylzWRVJZXQ9x3E10LS0wD6RuHNgXmx1
9htxasoGZEM2XvIgjapl7DUcuAyutjaiP59pfZhsIm/uRQ4WVhMJnZL6BM0DAs4+TIIkxRcChKdf
DTDV1UH822GBQr6Ge3D6N74EuqgLGyTZQu8VPr0cMuk3Qz4MrgMkY8PCeSzwHV9fyTVkf4cXmC7w
LkFWj7H/aDBdjlzRS4qBB3zjkdFqhYimdNhmY0eTCO63tX8vvEi8AMBJYiLK0q7PnSJVsY7mr+wV
vPpsNJx7b3Eu81KEa5TRooEpxCtWx/6jQIi1fujiNn9Zzkmp2vyFLchF46yn2dT4aLnSalikvVwP
DJTH6Xo7GIsk+KwEr3HIBj3zcfipWtw3aH9UY6k7lEeiC71GJxIeJ9HTQY2mOD9u7MZUGSkd3zA5
ppT3le1h8MiMsu8nmUPOIxSauSafwZDlRDE7xTYUPqJIQ+YJ0VGwAJubLWClmD67x61zVe7Vh75L
3beMdDOK2beZmGT6GNyWKmwnRMh09Po3Q6EImG5gQuBvAvoeEnx6w4qWtqcw0Aig8O2t4ILDPt4Z
+q4DWZHtHNzJ7muijJs1ZTeCYse7CTRFYFf4WeRU2FlgvREVsvCvgm1Js5vIvSPKBQuQfLMTfxg/
h0g5JbWsIBXkaapVqJn+UxR9oVbJcaqBtQoezdUgFDVbjd1UKCAJZdQeidw=
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
