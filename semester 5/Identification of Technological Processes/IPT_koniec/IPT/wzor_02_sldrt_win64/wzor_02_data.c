/*
 * wzor_02_data.c
 *
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * Code generation for model "wzor_02".
 *
 * Model version              : 1.225
 * Simulink Coder version : 8.8.1 (R2015aSP1) 04-Sep-2015
 * C source code generated on : Wed Oct 26 12:19:15 2022
 *
 * Target selection: rtwin.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: Intel->x86-64
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "wzor_02.h"
#include "wzor_02_private.h"

/* Block parameters (auto storage) */
P_wzor_02_T wzor_02_P = {
  0.016849876427279038,                /* Variable: a1
                                        * Referenced by: '<S1>/Tank 1 Scale'
                                        */
  0.016390005764854922,                /* Variable: a2
                                        * Referenced by: '<S1>/Tank 2 Scale'
                                        */
  0.01643475487492543,                 /* Variable: a3
                                        * Referenced by: '<S1>/Tank 3 Scale'
                                        */
  -36.222019418852156,                 /* Variable: b1
                                        * Referenced by: '<S1>/b1'
                                        */
  -35.703674634436936,                 /* Variable: b2
                                        * Referenced by: '<S1>/b2'
                                        */
  -35.978001788402544,                 /* Variable: b3
                                        * Referenced by: '<S1>/b3'
                                        */
  1.0,                                 /* Expression: 1
                                        * Referenced by: '<Root>/Constant'
                                        */

  /*  Computed Parameter: RTDACSafetyAlert_P1_Size
   * Referenced by: '<S3>/RT-DAC Safety Alert'
   */
  { 1.0, 1.0 },
  53248.0,                             /* Expression: BaseAddress
                                        * Referenced by: '<S3>/RT-DAC Safety Alert'
                                        */

  /*  Computed Parameter: RTDACSafetyAlert_P2_Size
   * Referenced by: '<S3>/RT-DAC Safety Alert'
   */
  { 1.0, 1.0 },
  0.01,                                /* Expression: T0
                                        * Referenced by: '<S3>/RT-DAC Safety Alert'
                                        */

  /*  Computed Parameter: RTDACFrequencies_P1_Size
   * Referenced by: '<S2>/RT-DAC Frequencies'
   */
  { 1.0, 1.0 },
  53248.0,                             /* Expression: BaseAddress
                                        * Referenced by: '<S2>/RT-DAC Frequencies'
                                        */

  /*  Computed Parameter: RTDACFrequencies_P2_Size
   * Referenced by: '<S2>/RT-DAC Frequencies'
   */
  { 1.0, 1.0 },
  0.01,                                /* Expression: T0
                                        * Referenced by: '<S2>/RT-DAC Frequencies'
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P1_Size
   * Referenced by: '<S4>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  53248.0,                             /* Expression: BaseAddress
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P2_Size
   * Referenced by: '<S4>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  1.0,                                 /* Expression: ChanIdx
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P3_Size
   * Referenced by: '<S4>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  2.0,                                 /* Expression: ChanMode
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P4_Size
   * Referenced by: '<S4>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  1.0,                                 /* Expression: ChanPresc
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P5_Size
   * Referenced by: '<S4>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  1.0,                                 /* Expression: SetOutputsFlag
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P6_Size
   * Referenced by: '<S4>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.0,                                 /* Expression: SetOutputsValue
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P7_Size
   * Referenced by: '<S4>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.01,                                /* Expression: T0
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  1.0,                                 /* Expression: 1
                                        * Referenced by: '<S1>/Saturation Control Pump'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<S1>/Saturation Control Pump'
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P1_Size_a
   * Referenced by: '<S5>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  53248.0,                             /* Expression: BaseAddress
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P2_Size_p
   * Referenced by: '<S5>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  4.0,                                 /* Expression: ChanIdx
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P3_Size_h
   * Referenced by: '<S5>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  2.0,                                 /* Expression: ChanMode
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P4_Size_i
   * Referenced by: '<S5>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  31.0,                                /* Expression: ChanPresc
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P5_Size_m
   * Referenced by: '<S5>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  1.0,                                 /* Expression: SetOutputsFlag
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P6_Size_i
   * Referenced by: '<S5>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.0,                                 /* Expression: SetOutputsValue
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P7_Size_p
   * Referenced by: '<S5>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.01,                                /* Expression: T0
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<Root>/Valve 1'
                                        */
  1.0,                                 /* Expression: 1
                                        * Referenced by: '<S1>/Saturation Control Valve 1'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<S1>/Saturation Control Valve 1'
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P1_Size_p
   * Referenced by: '<S6>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  53248.0,                             /* Expression: BaseAddress
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P2_Size_k
   * Referenced by: '<S6>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  3.0,                                 /* Expression: ChanIdx
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P3_Size_a
   * Referenced by: '<S6>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  2.0,                                 /* Expression: ChanMode
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P4_Size_j
   * Referenced by: '<S6>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  31.0,                                /* Expression: ChanPresc
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P5_Size_h
   * Referenced by: '<S6>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  1.0,                                 /* Expression: SetOutputsFlag
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P6_Size_k
   * Referenced by: '<S6>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.0,                                 /* Expression: SetOutputsValue
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P7_Size_i
   * Referenced by: '<S6>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.01,                                /* Expression: T0
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<Root>/Valve 2'
                                        */
  1.0,                                 /* Expression: 1
                                        * Referenced by: '<S1>/Saturation Control Valve 2'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<S1>/Saturation Control Valve 2'
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P1_Size_g
   * Referenced by: '<S7>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  53248.0,                             /* Expression: BaseAddress
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P2_Size_j
   * Referenced by: '<S7>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  2.0,                                 /* Expression: ChanIdx
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P3_Size_o
   * Referenced by: '<S7>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  2.0,                                 /* Expression: ChanMode
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P4_Size_g
   * Referenced by: '<S7>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  31.0,                                /* Expression: ChanPresc
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P5_Size_j
   * Referenced by: '<S7>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  1.0,                                 /* Expression: SetOutputsFlag
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P6_Size_i4
   * Referenced by: '<S7>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.0,                                 /* Expression: SetOutputsValue
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P7_Size_b
   * Referenced by: '<S7>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.01,                                /* Expression: T0
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<Root>/Valve 3'
                                        */
  1.0,                                 /* Expression: 1
                                        * Referenced by: '<S1>/Saturation Control Valve 3'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<S1>/Saturation Control Valve 3'
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P1_Size_d
   * Referenced by: '<S8>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  53248.0,                             /* Expression: BaseAddress
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P2_Size_g
   * Referenced by: '<S8>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  6.0,                                 /* Expression: ChanIdx
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P3_Size_n
   * Referenced by: '<S8>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  2.0,                                 /* Expression: ChanMode
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P4_Size_g2
   * Referenced by: '<S8>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  31.0,                                /* Expression: ChanPresc
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P5_Size_g
   * Referenced by: '<S8>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  1.0,                                 /* Expression: SetOutputsFlag
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P6_Size_io
   * Referenced by: '<S8>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.0,                                 /* Expression: SetOutputsValue
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P7_Size_a
   * Referenced by: '<S8>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.01,                                /* Expression: T0
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<S1>/Valve 4'
                                        */
  1.0,                                 /* Expression: 1
                                        * Referenced by: '<S1>/Saturation Control Valve 4'
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<S1>/Saturation Control Valve 4'
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P1_Size_i
   * Referenced by: '<S9>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  53248.0,                             /* Expression: BaseAddress
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P2_Size_jl
   * Referenced by: '<S9>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  5.0,                                 /* Expression: ChanIdx
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P3_Size_nz
   * Referenced by: '<S9>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  2.0,                                 /* Expression: ChanMode
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P4_Size_b
   * Referenced by: '<S9>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  31.0,                                /* Expression: ChanPresc
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P5_Size_d
   * Referenced by: '<S9>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  1.0,                                 /* Expression: SetOutputsFlag
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P6_Size_ig
   * Referenced by: '<S9>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.0,                                 /* Expression: SetOutputsValue
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */

  /*  Computed Parameter: RTDACPCIPWM_P7_Size_ac
   * Referenced by: '<S9>/RT-DAC PCI PWM '
   */
  { 1.0, 1.0 },
  0.01,                                /* Expression: T0
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  0.0,                                 /* Expression: 0
                                        * Referenced by: '<S1>/Valve 5'
                                        */
  1.0,                                 /* Expression: 1
                                        * Referenced by: '<S1>/Saturation Control Valve 5'
                                        */
  0.0                                  /* Expression: 0
                                        * Referenced by: '<S1>/Saturation Control Valve 5'
                                        */
};
