  function targMap = targDataMap(),

  ;%***********************
  ;% Create Parameter Map *
  ;%***********************
      
    nTotData      = 0; %add to this count as we go
    nTotSects     = 1;
    sectIdxOffset = 0;
    
    ;%
    ;% Define dummy sections & preallocate arrays
    ;%
    dumSection.nData = -1;  
    dumSection.data  = [];
    
    dumData.logicalSrcIdx = -1;
    dumData.dtTransOffset = -1;
    
    ;%
    ;% Init/prealloc paramMap
    ;%
    paramMap.nSections           = nTotSects;
    paramMap.sectIdxOffset       = sectIdxOffset;
      paramMap.sections(nTotSects) = dumSection; %prealloc
    paramMap.nTotData            = -1;
    
    ;%
    ;% Auto data (wzor_01_P)
    ;%
      section.nData     = 110;
      section.data(110)  = dumData; %prealloc
      
	  ;% wzor_01_P.Constant_Value
	  section.data(1).logicalSrcIdx = 0;
	  section.data(1).dtTransOffset = 0;
	
	  ;% wzor_01_P.RTDACSafetyAlert_P1_Size
	  section.data(2).logicalSrcIdx = 1;
	  section.data(2).dtTransOffset = 1;
	
	  ;% wzor_01_P.RTDACSafetyAlert_P1
	  section.data(3).logicalSrcIdx = 2;
	  section.data(3).dtTransOffset = 3;
	
	  ;% wzor_01_P.RTDACSafetyAlert_P2_Size
	  section.data(4).logicalSrcIdx = 3;
	  section.data(4).dtTransOffset = 4;
	
	  ;% wzor_01_P.RTDACSafetyAlert_P2
	  section.data(5).logicalSrcIdx = 4;
	  section.data(5).dtTransOffset = 6;
	
	  ;% wzor_01_P.RTDACFrequencies_P1_Size
	  section.data(6).logicalSrcIdx = 5;
	  section.data(6).dtTransOffset = 7;
	
	  ;% wzor_01_P.RTDACFrequencies_P1
	  section.data(7).logicalSrcIdx = 6;
	  section.data(7).dtTransOffset = 9;
	
	  ;% wzor_01_P.RTDACFrequencies_P2_Size
	  section.data(8).logicalSrcIdx = 7;
	  section.data(8).dtTransOffset = 10;
	
	  ;% wzor_01_P.RTDACFrequencies_P2
	  section.data(9).logicalSrcIdx = 8;
	  section.data(9).dtTransOffset = 12;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_Size
	  section.data(10).logicalSrcIdx = 9;
	  section.data(10).dtTransOffset = 13;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1
	  section.data(11).logicalSrcIdx = 10;
	  section.data(11).dtTransOffset = 15;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_Size
	  section.data(12).logicalSrcIdx = 11;
	  section.data(12).dtTransOffset = 16;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2
	  section.data(13).logicalSrcIdx = 12;
	  section.data(13).dtTransOffset = 18;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_Size
	  section.data(14).logicalSrcIdx = 13;
	  section.data(14).dtTransOffset = 19;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3
	  section.data(15).logicalSrcIdx = 14;
	  section.data(15).dtTransOffset = 21;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_Size
	  section.data(16).logicalSrcIdx = 15;
	  section.data(16).dtTransOffset = 22;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4
	  section.data(17).logicalSrcIdx = 16;
	  section.data(17).dtTransOffset = 24;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_Size
	  section.data(18).logicalSrcIdx = 17;
	  section.data(18).dtTransOffset = 25;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5
	  section.data(19).logicalSrcIdx = 18;
	  section.data(19).dtTransOffset = 27;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_Size
	  section.data(20).logicalSrcIdx = 19;
	  section.data(20).dtTransOffset = 28;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6
	  section.data(21).logicalSrcIdx = 20;
	  section.data(21).dtTransOffset = 30;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_Size
	  section.data(22).logicalSrcIdx = 21;
	  section.data(22).dtTransOffset = 31;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7
	  section.data(23).logicalSrcIdx = 22;
	  section.data(23).dtTransOffset = 33;
	
	  ;% wzor_01_P.SaturationControlPump_UpperSat
	  section.data(24).logicalSrcIdx = 23;
	  section.data(24).dtTransOffset = 34;
	
	  ;% wzor_01_P.SaturationControlPump_LowerSat
	  section.data(25).logicalSrcIdx = 24;
	  section.data(25).dtTransOffset = 35;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_Size_a
	  section.data(26).logicalSrcIdx = 25;
	  section.data(26).dtTransOffset = 36;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_c
	  section.data(27).logicalSrcIdx = 26;
	  section.data(27).dtTransOffset = 38;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_Size_p
	  section.data(28).logicalSrcIdx = 27;
	  section.data(28).dtTransOffset = 39;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_f
	  section.data(29).logicalSrcIdx = 28;
	  section.data(29).dtTransOffset = 41;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_Size_h
	  section.data(30).logicalSrcIdx = 29;
	  section.data(30).dtTransOffset = 42;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_d
	  section.data(31).logicalSrcIdx = 30;
	  section.data(31).dtTransOffset = 44;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_Size_i
	  section.data(32).logicalSrcIdx = 31;
	  section.data(32).dtTransOffset = 45;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_c
	  section.data(33).logicalSrcIdx = 32;
	  section.data(33).dtTransOffset = 47;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_Size_m
	  section.data(34).logicalSrcIdx = 33;
	  section.data(34).dtTransOffset = 48;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_b
	  section.data(35).logicalSrcIdx = 34;
	  section.data(35).dtTransOffset = 50;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_Size_i
	  section.data(36).logicalSrcIdx = 35;
	  section.data(36).dtTransOffset = 51;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_i
	  section.data(37).logicalSrcIdx = 36;
	  section.data(37).dtTransOffset = 53;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_Size_p
	  section.data(38).logicalSrcIdx = 37;
	  section.data(38).dtTransOffset = 54;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_m
	  section.data(39).logicalSrcIdx = 38;
	  section.data(39).dtTransOffset = 56;
	
	  ;% wzor_01_P.Valve1_Value
	  section.data(40).logicalSrcIdx = 39;
	  section.data(40).dtTransOffset = 57;
	
	  ;% wzor_01_P.SaturationControlValve1_UpperSat
	  section.data(41).logicalSrcIdx = 40;
	  section.data(41).dtTransOffset = 58;
	
	  ;% wzor_01_P.SaturationControlValve1_LowerSat
	  section.data(42).logicalSrcIdx = 41;
	  section.data(42).dtTransOffset = 59;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_Size_p
	  section.data(43).logicalSrcIdx = 42;
	  section.data(43).dtTransOffset = 60;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_f
	  section.data(44).logicalSrcIdx = 43;
	  section.data(44).dtTransOffset = 62;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_Size_k
	  section.data(45).logicalSrcIdx = 44;
	  section.data(45).dtTransOffset = 63;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_g
	  section.data(46).logicalSrcIdx = 45;
	  section.data(46).dtTransOffset = 65;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_Size_a
	  section.data(47).logicalSrcIdx = 46;
	  section.data(47).dtTransOffset = 66;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_i
	  section.data(48).logicalSrcIdx = 47;
	  section.data(48).dtTransOffset = 68;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_Size_j
	  section.data(49).logicalSrcIdx = 48;
	  section.data(49).dtTransOffset = 69;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_l
	  section.data(50).logicalSrcIdx = 49;
	  section.data(50).dtTransOffset = 71;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_Size_h
	  section.data(51).logicalSrcIdx = 50;
	  section.data(51).dtTransOffset = 72;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_c
	  section.data(52).logicalSrcIdx = 51;
	  section.data(52).dtTransOffset = 74;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_Size_k
	  section.data(53).logicalSrcIdx = 52;
	  section.data(53).dtTransOffset = 75;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_h
	  section.data(54).logicalSrcIdx = 53;
	  section.data(54).dtTransOffset = 77;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_Size_i
	  section.data(55).logicalSrcIdx = 54;
	  section.data(55).dtTransOffset = 78;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_k
	  section.data(56).logicalSrcIdx = 55;
	  section.data(56).dtTransOffset = 80;
	
	  ;% wzor_01_P.Valve2_Value
	  section.data(57).logicalSrcIdx = 56;
	  section.data(57).dtTransOffset = 81;
	
	  ;% wzor_01_P.SaturationControlValve2_UpperSat
	  section.data(58).logicalSrcIdx = 57;
	  section.data(58).dtTransOffset = 82;
	
	  ;% wzor_01_P.SaturationControlValve2_LowerSat
	  section.data(59).logicalSrcIdx = 58;
	  section.data(59).dtTransOffset = 83;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_Size_g
	  section.data(60).logicalSrcIdx = 59;
	  section.data(60).dtTransOffset = 84;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_d
	  section.data(61).logicalSrcIdx = 60;
	  section.data(61).dtTransOffset = 86;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_Size_j
	  section.data(62).logicalSrcIdx = 61;
	  section.data(62).dtTransOffset = 87;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_d
	  section.data(63).logicalSrcIdx = 62;
	  section.data(63).dtTransOffset = 89;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_Size_o
	  section.data(64).logicalSrcIdx = 63;
	  section.data(64).dtTransOffset = 90;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_g
	  section.data(65).logicalSrcIdx = 64;
	  section.data(65).dtTransOffset = 92;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_Size_g
	  section.data(66).logicalSrcIdx = 65;
	  section.data(66).dtTransOffset = 93;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_d
	  section.data(67).logicalSrcIdx = 66;
	  section.data(67).dtTransOffset = 95;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_Size_j
	  section.data(68).logicalSrcIdx = 67;
	  section.data(68).dtTransOffset = 96;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_d
	  section.data(69).logicalSrcIdx = 68;
	  section.data(69).dtTransOffset = 98;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_Size_i4
	  section.data(70).logicalSrcIdx = 69;
	  section.data(70).dtTransOffset = 99;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_m
	  section.data(71).logicalSrcIdx = 70;
	  section.data(71).dtTransOffset = 101;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_Size_b
	  section.data(72).logicalSrcIdx = 71;
	  section.data(72).dtTransOffset = 102;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_f
	  section.data(73).logicalSrcIdx = 72;
	  section.data(73).dtTransOffset = 104;
	
	  ;% wzor_01_P.Valve3_Value
	  section.data(74).logicalSrcIdx = 73;
	  section.data(74).dtTransOffset = 105;
	
	  ;% wzor_01_P.SaturationControlValve3_UpperSat
	  section.data(75).logicalSrcIdx = 74;
	  section.data(75).dtTransOffset = 106;
	
	  ;% wzor_01_P.SaturationControlValve3_LowerSat
	  section.data(76).logicalSrcIdx = 75;
	  section.data(76).dtTransOffset = 107;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_Size_d
	  section.data(77).logicalSrcIdx = 76;
	  section.data(77).dtTransOffset = 108;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_e
	  section.data(78).logicalSrcIdx = 77;
	  section.data(78).dtTransOffset = 110;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_Size_g
	  section.data(79).logicalSrcIdx = 78;
	  section.data(79).dtTransOffset = 111;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_l
	  section.data(80).logicalSrcIdx = 79;
	  section.data(80).dtTransOffset = 113;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_Size_n
	  section.data(81).logicalSrcIdx = 80;
	  section.data(81).dtTransOffset = 114;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_du
	  section.data(82).logicalSrcIdx = 81;
	  section.data(82).dtTransOffset = 116;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_Size_g2
	  section.data(83).logicalSrcIdx = 82;
	  section.data(83).dtTransOffset = 117;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_j
	  section.data(84).logicalSrcIdx = 83;
	  section.data(84).dtTransOffset = 119;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_Size_g
	  section.data(85).logicalSrcIdx = 84;
	  section.data(85).dtTransOffset = 120;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_k
	  section.data(86).logicalSrcIdx = 85;
	  section.data(86).dtTransOffset = 122;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_Size_io
	  section.data(87).logicalSrcIdx = 86;
	  section.data(87).dtTransOffset = 123;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_c
	  section.data(88).logicalSrcIdx = 87;
	  section.data(88).dtTransOffset = 125;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_Size_a
	  section.data(89).logicalSrcIdx = 88;
	  section.data(89).dtTransOffset = 126;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_a
	  section.data(90).logicalSrcIdx = 89;
	  section.data(90).dtTransOffset = 128;
	
	  ;% wzor_01_P.Valve4_Value
	  section.data(91).logicalSrcIdx = 90;
	  section.data(91).dtTransOffset = 129;
	
	  ;% wzor_01_P.SaturationControlValve4_UpperSat
	  section.data(92).logicalSrcIdx = 91;
	  section.data(92).dtTransOffset = 130;
	
	  ;% wzor_01_P.SaturationControlValve4_LowerSat
	  section.data(93).logicalSrcIdx = 92;
	  section.data(93).dtTransOffset = 131;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_Size_i
	  section.data(94).logicalSrcIdx = 93;
	  section.data(94).dtTransOffset = 132;
	
	  ;% wzor_01_P.RTDACPCIPWM_P1_g
	  section.data(95).logicalSrcIdx = 94;
	  section.data(95).dtTransOffset = 134;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_Size_jl
	  section.data(96).logicalSrcIdx = 95;
	  section.data(96).dtTransOffset = 135;
	
	  ;% wzor_01_P.RTDACPCIPWM_P2_n
	  section.data(97).logicalSrcIdx = 96;
	  section.data(97).dtTransOffset = 137;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_Size_nz
	  section.data(98).logicalSrcIdx = 97;
	  section.data(98).dtTransOffset = 138;
	
	  ;% wzor_01_P.RTDACPCIPWM_P3_b
	  section.data(99).logicalSrcIdx = 98;
	  section.data(99).dtTransOffset = 140;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_Size_b
	  section.data(100).logicalSrcIdx = 99;
	  section.data(100).dtTransOffset = 141;
	
	  ;% wzor_01_P.RTDACPCIPWM_P4_f
	  section.data(101).logicalSrcIdx = 100;
	  section.data(101).dtTransOffset = 143;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_Size_d
	  section.data(102).logicalSrcIdx = 101;
	  section.data(102).dtTransOffset = 144;
	
	  ;% wzor_01_P.RTDACPCIPWM_P5_e
	  section.data(103).logicalSrcIdx = 102;
	  section.data(103).dtTransOffset = 146;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_Size_ig
	  section.data(104).logicalSrcIdx = 103;
	  section.data(104).dtTransOffset = 147;
	
	  ;% wzor_01_P.RTDACPCIPWM_P6_n
	  section.data(105).logicalSrcIdx = 104;
	  section.data(105).dtTransOffset = 149;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_Size_ac
	  section.data(106).logicalSrcIdx = 105;
	  section.data(106).dtTransOffset = 150;
	
	  ;% wzor_01_P.RTDACPCIPWM_P7_h
	  section.data(107).logicalSrcIdx = 106;
	  section.data(107).dtTransOffset = 152;
	
	  ;% wzor_01_P.Valve5_Value
	  section.data(108).logicalSrcIdx = 107;
	  section.data(108).dtTransOffset = 153;
	
	  ;% wzor_01_P.SaturationControlValve5_UpperSat
	  section.data(109).logicalSrcIdx = 108;
	  section.data(109).dtTransOffset = 154;
	
	  ;% wzor_01_P.SaturationControlValve5_LowerSat
	  section.data(110).logicalSrcIdx = 109;
	  section.data(110).dtTransOffset = 155;
	
      nTotData = nTotData + section.nData;
      paramMap.sections(1) = section;
      clear section
      
    
      ;%
      ;% Non-auto Data (parameter)
      ;%
    

    ;%
    ;% Add final counts to struct.
    ;%
    paramMap.nTotData = nTotData;
    


  ;%**************************
  ;% Create Block Output Map *
  ;%**************************
      
    nTotData      = 0; %add to this count as we go
    nTotSects     = 1;
    sectIdxOffset = 0;
    
    ;%
    ;% Define dummy sections & preallocate arrays
    ;%
    dumSection.nData = -1;  
    dumSection.data  = [];
    
    dumData.logicalSrcIdx = -1;
    dumData.dtTransOffset = -1;
    
    ;%
    ;% Init/prealloc sigMap
    ;%
    sigMap.nSections           = nTotSects;
    sigMap.sectIdxOffset       = sectIdxOffset;
      sigMap.sections(nTotSects) = dumSection; %prealloc
    sigMap.nTotData            = -1;
    
    ;%
    ;% Auto data (wzor_01_B)
    ;%
      section.nData     = 12;
      section.data(12)  = dumData; %prealloc
      
	  ;% wzor_01_B.Pump
	  section.data(1).logicalSrcIdx = 0;
	  section.data(1).dtTransOffset = 0;
	
	  ;% wzor_01_B.RTDACSafetyAlert
	  section.data(2).logicalSrcIdx = 1;
	  section.data(2).dtTransOffset = 1;
	
	  ;% wzor_01_B.RTDACFrequencies
	  section.data(3).logicalSrcIdx = 2;
	  section.data(3).dtTransOffset = 2;
	
	  ;% wzor_01_B.Fcn
	  section.data(4).logicalSrcIdx = 3;
	  section.data(4).dtTransOffset = 7;
	
	  ;% wzor_01_B.Fcn1
	  section.data(5).logicalSrcIdx = 4;
	  section.data(5).dtTransOffset = 8;
	
	  ;% wzor_01_B.Fcn2
	  section.data(6).logicalSrcIdx = 5;
	  section.data(6).dtTransOffset = 9;
	
	  ;% wzor_01_B.SaturationControlPump
	  section.data(7).logicalSrcIdx = 6;
	  section.data(7).dtTransOffset = 10;
	
	  ;% wzor_01_B.SaturationControlValve1
	  section.data(8).logicalSrcIdx = 7;
	  section.data(8).dtTransOffset = 11;
	
	  ;% wzor_01_B.SaturationControlValve2
	  section.data(9).logicalSrcIdx = 8;
	  section.data(9).dtTransOffset = 12;
	
	  ;% wzor_01_B.SaturationControlValve3
	  section.data(10).logicalSrcIdx = 9;
	  section.data(10).dtTransOffset = 13;
	
	  ;% wzor_01_B.SaturationControlValve4
	  section.data(11).logicalSrcIdx = 10;
	  section.data(11).dtTransOffset = 14;
	
	  ;% wzor_01_B.SaturationControlValve5
	  section.data(12).logicalSrcIdx = 11;
	  section.data(12).dtTransOffset = 15;
	
      nTotData = nTotData + section.nData;
      sigMap.sections(1) = section;
      clear section
      
    
      ;%
      ;% Non-auto Data (signal)
      ;%
    

    ;%
    ;% Add final counts to struct.
    ;%
    sigMap.nTotData = nTotData;
    


  ;%*******************
  ;% Create DWork Map *
  ;%*******************
      
    nTotData      = 0; %add to this count as we go
    nTotSects     = 1;
    sectIdxOffset = 1;
    
    ;%
    ;% Define dummy sections & preallocate arrays
    ;%
    dumSection.nData = -1;  
    dumSection.data  = [];
    
    dumData.logicalSrcIdx = -1;
    dumData.dtTransOffset = -1;
    
    ;%
    ;% Init/prealloc dworkMap
    ;%
    dworkMap.nSections           = nTotSects;
    dworkMap.sectIdxOffset       = sectIdxOffset;
      dworkMap.sections(nTotSects) = dumSection; %prealloc
    dworkMap.nTotData            = -1;
    
    ;%
    ;% Auto data (wzor_01_DW)
    ;%
      section.nData     = 4;
      section.data(4)  = dumData; %prealloc
      
	  ;% wzor_01_DW.Tank_PWORK.LoggedData
	  section.data(1).logicalSrcIdx = 0;
	  section.data(1).dtTransOffset = 0;
	
	  ;% wzor_01_DW.Scope_PWORK.LoggedData
	  section.data(2).logicalSrcIdx = 1;
	  section.data(2).dtTransOffset = 1;
	
	  ;% wzor_01_DW.Scope1_PWORK.LoggedData
	  section.data(3).logicalSrcIdx = 2;
	  section.data(3).dtTransOffset = 2;
	
	  ;% wzor_01_DW.Scope2_PWORK.LoggedData
	  section.data(4).logicalSrcIdx = 3;
	  section.data(4).dtTransOffset = 3;
	
      nTotData = nTotData + section.nData;
      dworkMap.sections(1) = section;
      clear section
      
    
      ;%
      ;% Non-auto Data (dwork)
      ;%
    

    ;%
    ;% Add final counts to struct.
    ;%
    dworkMap.nTotData = nTotData;
    


  ;%
  ;% Add individual maps to base struct.
  ;%

  targMap.paramMap  = paramMap;    
  targMap.signalMap = sigMap;
  targMap.dworkMap  = dworkMap;
  
  ;%
  ;% Add checksums to base struct.
  ;%


  targMap.checksum0 = 659317551;
  targMap.checksum1 = 3560812498;
  targMap.checksum2 = 361668384;
  targMap.checksum3 = 2922332836;

