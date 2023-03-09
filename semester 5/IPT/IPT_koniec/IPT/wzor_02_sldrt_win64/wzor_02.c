/*
 * wzor_02.c
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
#include "wzor_02_dt.h"

/* list of Simulink Desktop Real-Time timers */
const int RTWinTimerCount = 1;
const double RTWinTimers[2] = {
  0.01, 0.0,
};

/* Block signals (auto storage) */
B_wzor_02_T wzor_02_B;

/* Block states (auto storage) */
DW_wzor_02_T wzor_02_DW;

/* Real-time model */
RT_MODEL_wzor_02_T wzor_02_M_;
RT_MODEL_wzor_02_T *const wzor_02_M = &wzor_02_M_;

/* Model output function */
void wzor_02_output(void)
{
  /* Constant: '<Root>/Constant' */
  wzor_02_B.Pump = wzor_02_P.Constant_Value;

  /* Level2 S-Function Block: '<S3>/RT-DAC Safety Alert' (tank_safetyalert) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[0];
    sfcnOutputs(rts, 0);
  }

  /* Level2 S-Function Block: '<S2>/RT-DAC Frequencies' (tank_frequencies) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[1];
    sfcnOutputs(rts, 0);
  }

  /* Sum: '<S1>/Sum5' incorporates:
   *  Constant: '<S1>/b1'
   *  Gain: '<S1>/Tank 1 Scale'
   */
  wzor_02_B.Zbiornik_1 = wzor_02_P.a1 * wzor_02_B.RTDACFrequencies[0] +
    wzor_02_P.b1;

  /* Sum: '<S1>/Sum6' incorporates:
   *  Constant: '<S1>/b2'
   *  Gain: '<S1>/Tank 2 Scale'
   */
  wzor_02_B.Zbiornik_2 = wzor_02_P.a2 * wzor_02_B.RTDACFrequencies[1] +
    wzor_02_P.b2;

  /* Sum: '<S1>/Sum7' incorporates:
   *  Constant: '<S1>/b3'
   *  Gain: '<S1>/Tank 3 Scale'
   */
  wzor_02_B.Zbiornik_3 = wzor_02_P.a3 * wzor_02_B.RTDACFrequencies[2] +
    wzor_02_P.b3;

  /* Level2 S-Function Block: '<S4>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[2];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Pump' */
  if (wzor_02_B.Pump > wzor_02_P.SaturationControlPump_UpperSat) {
    wzor_02_B.SaturationControlPump = wzor_02_P.SaturationControlPump_UpperSat;
  } else if (wzor_02_B.Pump < wzor_02_P.SaturationControlPump_LowerSat) {
    wzor_02_B.SaturationControlPump = wzor_02_P.SaturationControlPump_LowerSat;
  } else {
    wzor_02_B.SaturationControlPump = wzor_02_B.Pump;
  }

  /* End of Saturate: '<S1>/Saturation Control Pump' */

  /* Level2 S-Function Block: '<S5>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[3];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Valve 1' incorporates:
   *  Constant: '<Root>/Valve 1'
   */
  if (wzor_02_P.Valve1_Value > wzor_02_P.SaturationControlValve1_UpperSat) {
    wzor_02_B.SaturationControlValve1 =
      wzor_02_P.SaturationControlValve1_UpperSat;
  } else if (wzor_02_P.Valve1_Value < wzor_02_P.SaturationControlValve1_LowerSat)
  {
    wzor_02_B.SaturationControlValve1 =
      wzor_02_P.SaturationControlValve1_LowerSat;
  } else {
    wzor_02_B.SaturationControlValve1 = wzor_02_P.Valve1_Value;
  }

  /* End of Saturate: '<S1>/Saturation Control Valve 1' */

  /* Level2 S-Function Block: '<S6>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[4];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Valve 2' incorporates:
   *  Constant: '<Root>/Valve 2'
   */
  if (wzor_02_P.Valve2_Value > wzor_02_P.SaturationControlValve2_UpperSat) {
    wzor_02_B.SaturationControlValve2 =
      wzor_02_P.SaturationControlValve2_UpperSat;
  } else if (wzor_02_P.Valve2_Value < wzor_02_P.SaturationControlValve2_LowerSat)
  {
    wzor_02_B.SaturationControlValve2 =
      wzor_02_P.SaturationControlValve2_LowerSat;
  } else {
    wzor_02_B.SaturationControlValve2 = wzor_02_P.Valve2_Value;
  }

  /* End of Saturate: '<S1>/Saturation Control Valve 2' */

  /* Level2 S-Function Block: '<S7>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[5];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Valve 3' incorporates:
   *  Constant: '<Root>/Valve 3'
   */
  if (wzor_02_P.Valve3_Value > wzor_02_P.SaturationControlValve3_UpperSat) {
    wzor_02_B.SaturationControlValve3 =
      wzor_02_P.SaturationControlValve3_UpperSat;
  } else if (wzor_02_P.Valve3_Value < wzor_02_P.SaturationControlValve3_LowerSat)
  {
    wzor_02_B.SaturationControlValve3 =
      wzor_02_P.SaturationControlValve3_LowerSat;
  } else {
    wzor_02_B.SaturationControlValve3 = wzor_02_P.Valve3_Value;
  }

  /* End of Saturate: '<S1>/Saturation Control Valve 3' */

  /* Level2 S-Function Block: '<S8>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[6];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Valve 4' incorporates:
   *  Constant: '<S1>/Valve 4'
   */
  if (wzor_02_P.Valve4_Value > wzor_02_P.SaturationControlValve4_UpperSat) {
    wzor_02_B.SaturationControlValve4 =
      wzor_02_P.SaturationControlValve4_UpperSat;
  } else if (wzor_02_P.Valve4_Value < wzor_02_P.SaturationControlValve4_LowerSat)
  {
    wzor_02_B.SaturationControlValve4 =
      wzor_02_P.SaturationControlValve4_LowerSat;
  } else {
    wzor_02_B.SaturationControlValve4 = wzor_02_P.Valve4_Value;
  }

  /* End of Saturate: '<S1>/Saturation Control Valve 4' */

  /* Level2 S-Function Block: '<S9>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[7];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Valve 5' incorporates:
   *  Constant: '<S1>/Valve 5'
   */
  if (wzor_02_P.Valve5_Value > wzor_02_P.SaturationControlValve5_UpperSat) {
    wzor_02_B.SaturationControlValve5 =
      wzor_02_P.SaturationControlValve5_UpperSat;
  } else if (wzor_02_P.Valve5_Value < wzor_02_P.SaturationControlValve5_LowerSat)
  {
    wzor_02_B.SaturationControlValve5 =
      wzor_02_P.SaturationControlValve5_LowerSat;
  } else {
    wzor_02_B.SaturationControlValve5 = wzor_02_P.Valve5_Value;
  }

  /* End of Saturate: '<S1>/Saturation Control Valve 5' */
}

/* Model update function */
void wzor_02_update(void)
{
  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++wzor_02_M->Timing.clockTick0)) {
    ++wzor_02_M->Timing.clockTickH0;
  }

  wzor_02_M->Timing.t[0] = wzor_02_M->Timing.clockTick0 *
    wzor_02_M->Timing.stepSize0 + wzor_02_M->Timing.clockTickH0 *
    wzor_02_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void wzor_02_initialize(void)
{
}

/* Model terminate function */
void wzor_02_terminate(void)
{
  /* Level2 S-Function Block: '<S3>/RT-DAC Safety Alert' (tank_safetyalert) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[0];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S2>/RT-DAC Frequencies' (tank_frequencies) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[1];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S4>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[2];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S5>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[3];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S6>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[4];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S7>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[5];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S8>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[6];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S9>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_02_M->childSfunctions[7];
    sfcnTerminate(rts);
  }
}

/*========================================================================*
 * Start of Classic call interface                                        *
 *========================================================================*/
void MdlOutputs(int_T tid)
{
  wzor_02_output();
  UNUSED_PARAMETER(tid);
}

void MdlUpdate(int_T tid)
{
  wzor_02_update();
  UNUSED_PARAMETER(tid);
}

void MdlInitializeSizes(void)
{
}

void MdlInitializeSampleTimes(void)
{
}

void MdlInitialize(void)
{
}

void MdlStart(void)
{
  wzor_02_initialize();
}

void MdlTerminate(void)
{
  wzor_02_terminate();
}

/* Registration function */
RT_MODEL_wzor_02_T *wzor_02(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)wzor_02_M, 0,
                sizeof(RT_MODEL_wzor_02_T));
  rtsiSetSolverName(&wzor_02_M->solverInfo,"FixedStepDiscrete");
  wzor_02_M->solverInfoPtr = (&wzor_02_M->solverInfo);

  /* Initialize timing info */
  {
    int_T *mdlTsMap = wzor_02_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    wzor_02_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    wzor_02_M->Timing.sampleTimes = (&wzor_02_M->Timing.sampleTimesArray[0]);
    wzor_02_M->Timing.offsetTimes = (&wzor_02_M->Timing.offsetTimesArray[0]);

    /* task periods */
    wzor_02_M->Timing.sampleTimes[0] = (0.01);

    /* task offsets */
    wzor_02_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(wzor_02_M, &wzor_02_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = wzor_02_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    wzor_02_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(wzor_02_M, 4.0);
  wzor_02_M->Timing.stepSize0 = 0.01;

  /* External mode info */
  wzor_02_M->Sizes.checksums[0] = (1373358906U);
  wzor_02_M->Sizes.checksums[1] = (2414038126U);
  wzor_02_M->Sizes.checksums[2] = (588024014U);
  wzor_02_M->Sizes.checksums[3] = (3607655209U);

  {
    static const sysRanDType rtAlwaysEnabled = SUBSYS_RAN_BC_ENABLE;
    static RTWExtModeInfo rt_ExtModeInfo;
    static const sysRanDType *systemRan[1];
    wzor_02_M->extModeInfo = (&rt_ExtModeInfo);
    rteiSetSubSystemActiveVectorAddresses(&rt_ExtModeInfo, systemRan);
    systemRan[0] = &rtAlwaysEnabled;
    rteiSetModelMappingInfoPtr(wzor_02_M->extModeInfo,
      &wzor_02_M->SpecialInfo.mappingInfo);
    rteiSetChecksumsPtr(wzor_02_M->extModeInfo, wzor_02_M->Sizes.checksums);
    rteiSetTPtr(wzor_02_M->extModeInfo, rtmGetTPtr(wzor_02_M));
  }

  wzor_02_M->solverInfoPtr = (&wzor_02_M->solverInfo);
  wzor_02_M->Timing.stepSize = (0.01);
  rtsiSetFixedStepSize(&wzor_02_M->solverInfo, 0.01);
  rtsiSetSolverMode(&wzor_02_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* block I/O */
  wzor_02_M->ModelData.blockIO = ((void *) &wzor_02_B);

  {
    int32_T i;
    for (i = 0; i < 5; i++) {
      wzor_02_B.RTDACFrequencies[i] = 0.0;
    }

    wzor_02_B.Pump = 0.0;
    wzor_02_B.RTDACSafetyAlert = 0.0;
    wzor_02_B.Zbiornik_1 = 0.0;
    wzor_02_B.Zbiornik_2 = 0.0;
    wzor_02_B.Zbiornik_3 = 0.0;
    wzor_02_B.SaturationControlPump = 0.0;
    wzor_02_B.SaturationControlValve1 = 0.0;
    wzor_02_B.SaturationControlValve2 = 0.0;
    wzor_02_B.SaturationControlValve3 = 0.0;
    wzor_02_B.SaturationControlValve4 = 0.0;
    wzor_02_B.SaturationControlValve5 = 0.0;
  }

  /* parameters */
  wzor_02_M->ModelData.defaultParam = ((real_T *)&wzor_02_P);

  /* states (dwork) */
  wzor_02_M->ModelData.dwork = ((void *) &wzor_02_DW);
  (void) memset((void *)&wzor_02_DW, 0,
                sizeof(DW_wzor_02_T));

  /* data type transition information */
  {
    static DataTypeTransInfo dtInfo;
    (void) memset((char_T *) &dtInfo, 0,
                  sizeof(dtInfo));
    wzor_02_M->SpecialInfo.mappingInfo = (&dtInfo);
    dtInfo.numDataTypes = 14;
    dtInfo.dataTypeSizes = &rtDataTypeSizes[0];
    dtInfo.dataTypeNames = &rtDataTypeNames[0];

    /* Block I/O transition table */
    dtInfo.B = &rtBTransTable;

    /* Parameters transition table */
    dtInfo.P = &rtPTransTable;
  }

  /* child S-Function registration */
  {
    RTWSfcnInfo *sfcnInfo = &wzor_02_M->NonInlinedSFcns.sfcnInfo;
    wzor_02_M->sfcnInfo = (sfcnInfo);
    rtssSetErrorStatusPtr(sfcnInfo, (&rtmGetErrorStatus(wzor_02_M)));
    rtssSetNumRootSampTimesPtr(sfcnInfo, &wzor_02_M->Sizes.numSampTimes);
    wzor_02_M->NonInlinedSFcns.taskTimePtrs[0] = &(rtmGetTPtr(wzor_02_M)[0]);
    rtssSetTPtrPtr(sfcnInfo,wzor_02_M->NonInlinedSFcns.taskTimePtrs);
    rtssSetTStartPtr(sfcnInfo, &rtmGetTStart(wzor_02_M));
    rtssSetTFinalPtr(sfcnInfo, &rtmGetTFinal(wzor_02_M));
    rtssSetTimeOfLastOutputPtr(sfcnInfo, &rtmGetTimeOfLastOutput(wzor_02_M));
    rtssSetStepSizePtr(sfcnInfo, &wzor_02_M->Timing.stepSize);
    rtssSetStopRequestedPtr(sfcnInfo, &rtmGetStopRequested(wzor_02_M));
    rtssSetDerivCacheNeedsResetPtr(sfcnInfo,
      &wzor_02_M->ModelData.derivCacheNeedsReset);
    rtssSetZCCacheNeedsResetPtr(sfcnInfo,
      &wzor_02_M->ModelData.zCCacheNeedsReset);
    rtssSetBlkStateChangePtr(sfcnInfo, &wzor_02_M->ModelData.blkStateChange);
    rtssSetSampleHitsPtr(sfcnInfo, &wzor_02_M->Timing.sampleHits);
    rtssSetPerTaskSampleHitsPtr(sfcnInfo, &wzor_02_M->Timing.perTaskSampleHits);
    rtssSetSimModePtr(sfcnInfo, &wzor_02_M->simMode);
    rtssSetSolverInfoPtr(sfcnInfo, &wzor_02_M->solverInfoPtr);
  }

  wzor_02_M->Sizes.numSFcns = (8);

  /* register each child */
  {
    (void) memset((void *)&wzor_02_M->NonInlinedSFcns.childSFunctions[0], 0,
                  8*sizeof(SimStruct));
    wzor_02_M->childSfunctions = (&wzor_02_M->
      NonInlinedSFcns.childSFunctionPtrs[0]);

    {
      int_T i;
      for (i = 0; i < 8; i++) {
        wzor_02_M->childSfunctions[i] =
          (&wzor_02_M->NonInlinedSFcns.childSFunctions[i]);
      }
    }

    /* Level2 S-Function Block: wzor_02/<S3>/RT-DAC Safety Alert (tank_safetyalert) */
    {
      SimStruct *rts = wzor_02_M->childSfunctions[0];

      /* timing info */
      time_T *sfcnPeriod = wzor_02_M->NonInlinedSFcns.Sfcn0.sfcnPeriod;
      time_T *sfcnOffset = wzor_02_M->NonInlinedSFcns.Sfcn0.sfcnOffset;
      int_T *sfcnTsMap = wzor_02_M->NonInlinedSFcns.Sfcn0.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_02_M->NonInlinedSFcns.blkInfo2[0]);
      }

      ssSetRTWSfcnInfo(rts, wzor_02_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_02_M->NonInlinedSFcns.methods2[0]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_02_M->NonInlinedSFcns.methods3[0]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_02_M->NonInlinedSFcns.statesInfo2[0]);
      }

      /* outputs */
      {
        ssSetPortInfoForOutputs(rts,
          &wzor_02_M->NonInlinedSFcns.Sfcn0.outputPortInfo[0]);
        _ssSetNumOutputPorts(rts, 1);

        /* port 0 */
        {
          _ssSetOutputPortNumDimensions(rts, 0, 1);
          ssSetOutputPortWidth(rts, 0, 1);
          ssSetOutputPortSignal(rts, 0, ((real_T *) &wzor_02_B.RTDACSafetyAlert));
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC\nSafety Alert");
      ssSetPath(rts, "wzor_02/Tank3/RT-DAC Safety Alert/RT-DAC Safety Alert");
      ssSetRTModel(rts,wzor_02_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_02_M->NonInlinedSFcns.Sfcn0.params;
        ssSetSFcnParamsCount(rts, 2);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_02_P.RTDACSafetyAlert_P1_Size);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_02_P.RTDACSafetyAlert_P2_Size);
      }

      /* registration */
      tank_safetyalert(rts);
      sfcnInitializeSizes(rts);
      sfcnInitializeSampleTimes(rts);

      /* adjust sample time */
      ssSetSampleTime(rts, 0, 0.01);
      ssSetOffsetTime(rts, 0, 0.0);
      sfcnTsMap[0] = 0;

      /* set compiled values of dynamic vector attributes */
      ssSetNumNonsampledZCs(rts, 0);

      /* Update connectivity flags for each port */
      _ssSetOutputPortConnected(rts, 0, 1);
      _ssSetOutputPortBeingMerged(rts, 0, 0);

      /* Update the BufferDstPort flags for each input port */
    }

    /* Level2 S-Function Block: wzor_02/<S2>/RT-DAC Frequencies (tank_frequencies) */
    {
      SimStruct *rts = wzor_02_M->childSfunctions[1];

      /* timing info */
      time_T *sfcnPeriod = wzor_02_M->NonInlinedSFcns.Sfcn1.sfcnPeriod;
      time_T *sfcnOffset = wzor_02_M->NonInlinedSFcns.Sfcn1.sfcnOffset;
      int_T *sfcnTsMap = wzor_02_M->NonInlinedSFcns.Sfcn1.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_02_M->NonInlinedSFcns.blkInfo2[1]);
      }

      ssSetRTWSfcnInfo(rts, wzor_02_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_02_M->NonInlinedSFcns.methods2[1]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_02_M->NonInlinedSFcns.methods3[1]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_02_M->NonInlinedSFcns.statesInfo2[1]);
      }

      /* outputs */
      {
        ssSetPortInfoForOutputs(rts,
          &wzor_02_M->NonInlinedSFcns.Sfcn1.outputPortInfo[0]);
        _ssSetNumOutputPorts(rts, 1);

        /* port 0 */
        {
          _ssSetOutputPortNumDimensions(rts, 0, 1);
          ssSetOutputPortWidth(rts, 0, 5);
          ssSetOutputPortSignal(rts, 0, ((real_T *) wzor_02_B.RTDACFrequencies));
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC\nFrequencies");
      ssSetPath(rts, "wzor_02/Tank3/RT-DAC Frequencies/RT-DAC Frequencies");
      ssSetRTModel(rts,wzor_02_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_02_M->NonInlinedSFcns.Sfcn1.params;
        ssSetSFcnParamsCount(rts, 2);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_02_P.RTDACFrequencies_P1_Size);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_02_P.RTDACFrequencies_P2_Size);
      }

      /* registration */
      tank_frequencies(rts);
      sfcnInitializeSizes(rts);
      sfcnInitializeSampleTimes(rts);

      /* adjust sample time */
      ssSetSampleTime(rts, 0, 0.01);
      ssSetOffsetTime(rts, 0, 0.0);
      sfcnTsMap[0] = 0;

      /* set compiled values of dynamic vector attributes */
      ssSetNumNonsampledZCs(rts, 0);

      /* Update connectivity flags for each port */
      _ssSetOutputPortConnected(rts, 0, 1);
      _ssSetOutputPortBeingMerged(rts, 0, 0);

      /* Update the BufferDstPort flags for each input port */
    }

    /* Level2 S-Function Block: wzor_02/<S4>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_02_M->childSfunctions[2];

      /* timing info */
      time_T *sfcnPeriod = wzor_02_M->NonInlinedSFcns.Sfcn2.sfcnPeriod;
      time_T *sfcnOffset = wzor_02_M->NonInlinedSFcns.Sfcn2.sfcnOffset;
      int_T *sfcnTsMap = wzor_02_M->NonInlinedSFcns.Sfcn2.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_02_M->NonInlinedSFcns.blkInfo2[2]);
      }

      ssSetRTWSfcnInfo(rts, wzor_02_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_02_M->NonInlinedSFcns.methods2[2]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_02_M->NonInlinedSFcns.methods3[2]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_02_M->NonInlinedSFcns.statesInfo2[2]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_02_M->NonInlinedSFcns.Sfcn2.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_02_M->NonInlinedSFcns.Sfcn2.UPtrs0;
          sfcnUPtrs[0] = &wzor_02_B.SaturationControlPump;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_02/Tank3/RT-DAC PCI PWM Pump/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_02_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_02_M->NonInlinedSFcns.Sfcn2.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_02_P.RTDACPCIPWM_P1_Size);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_02_P.RTDACPCIPWM_P2_Size);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_02_P.RTDACPCIPWM_P3_Size);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_02_P.RTDACPCIPWM_P4_Size);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_02_P.RTDACPCIPWM_P5_Size);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_02_P.RTDACPCIPWM_P6_Size);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_02_P.RTDACPCIPWM_P7_Size);
      }

      /* registration */
      tank_pwm(rts);
      sfcnInitializeSizes(rts);
      sfcnInitializeSampleTimes(rts);

      /* adjust sample time */
      ssSetSampleTime(rts, 0, 0.01);
      ssSetOffsetTime(rts, 0, 0.0);
      sfcnTsMap[0] = 0;

      /* set compiled values of dynamic vector attributes */
      ssSetNumNonsampledZCs(rts, 0);

      /* Update connectivity flags for each port */
      _ssSetInputPortConnected(rts, 0, 1);

      /* Update the BufferDstPort flags for each input port */
      ssSetInputPortBufferDstPort(rts, 0, -1);
    }

    /* Level2 S-Function Block: wzor_02/<S5>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_02_M->childSfunctions[3];

      /* timing info */
      time_T *sfcnPeriod = wzor_02_M->NonInlinedSFcns.Sfcn3.sfcnPeriod;
      time_T *sfcnOffset = wzor_02_M->NonInlinedSFcns.Sfcn3.sfcnOffset;
      int_T *sfcnTsMap = wzor_02_M->NonInlinedSFcns.Sfcn3.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_02_M->NonInlinedSFcns.blkInfo2[3]);
      }

      ssSetRTWSfcnInfo(rts, wzor_02_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_02_M->NonInlinedSFcns.methods2[3]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_02_M->NonInlinedSFcns.methods3[3]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_02_M->NonInlinedSFcns.statesInfo2[3]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_02_M->NonInlinedSFcns.Sfcn3.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_02_M->NonInlinedSFcns.Sfcn3.UPtrs0;
          sfcnUPtrs[0] = &wzor_02_B.SaturationControlValve1;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_02/Tank3/RT-DAC PCI PWM Valve 1/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_02_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_02_M->NonInlinedSFcns.Sfcn3.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_02_P.RTDACPCIPWM_P1_Size_a);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_02_P.RTDACPCIPWM_P2_Size_p);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_02_P.RTDACPCIPWM_P3_Size_h);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_02_P.RTDACPCIPWM_P4_Size_i);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_02_P.RTDACPCIPWM_P5_Size_m);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_02_P.RTDACPCIPWM_P6_Size_i);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_02_P.RTDACPCIPWM_P7_Size_p);
      }

      /* registration */
      tank_pwm(rts);
      sfcnInitializeSizes(rts);
      sfcnInitializeSampleTimes(rts);

      /* adjust sample time */
      ssSetSampleTime(rts, 0, 0.01);
      ssSetOffsetTime(rts, 0, 0.0);
      sfcnTsMap[0] = 0;

      /* set compiled values of dynamic vector attributes */
      ssSetNumNonsampledZCs(rts, 0);

      /* Update connectivity flags for each port */
      _ssSetInputPortConnected(rts, 0, 1);

      /* Update the BufferDstPort flags for each input port */
      ssSetInputPortBufferDstPort(rts, 0, -1);
    }

    /* Level2 S-Function Block: wzor_02/<S6>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_02_M->childSfunctions[4];

      /* timing info */
      time_T *sfcnPeriod = wzor_02_M->NonInlinedSFcns.Sfcn4.sfcnPeriod;
      time_T *sfcnOffset = wzor_02_M->NonInlinedSFcns.Sfcn4.sfcnOffset;
      int_T *sfcnTsMap = wzor_02_M->NonInlinedSFcns.Sfcn4.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_02_M->NonInlinedSFcns.blkInfo2[4]);
      }

      ssSetRTWSfcnInfo(rts, wzor_02_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_02_M->NonInlinedSFcns.methods2[4]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_02_M->NonInlinedSFcns.methods3[4]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_02_M->NonInlinedSFcns.statesInfo2[4]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_02_M->NonInlinedSFcns.Sfcn4.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_02_M->NonInlinedSFcns.Sfcn4.UPtrs0;
          sfcnUPtrs[0] = &wzor_02_B.SaturationControlValve2;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_02/Tank3/RT-DAC PCI PWM Valve 2/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_02_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_02_M->NonInlinedSFcns.Sfcn4.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_02_P.RTDACPCIPWM_P1_Size_p);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_02_P.RTDACPCIPWM_P2_Size_k);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_02_P.RTDACPCIPWM_P3_Size_a);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_02_P.RTDACPCIPWM_P4_Size_j);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_02_P.RTDACPCIPWM_P5_Size_h);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_02_P.RTDACPCIPWM_P6_Size_k);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_02_P.RTDACPCIPWM_P7_Size_i);
      }

      /* registration */
      tank_pwm(rts);
      sfcnInitializeSizes(rts);
      sfcnInitializeSampleTimes(rts);

      /* adjust sample time */
      ssSetSampleTime(rts, 0, 0.01);
      ssSetOffsetTime(rts, 0, 0.0);
      sfcnTsMap[0] = 0;

      /* set compiled values of dynamic vector attributes */
      ssSetNumNonsampledZCs(rts, 0);

      /* Update connectivity flags for each port */
      _ssSetInputPortConnected(rts, 0, 1);

      /* Update the BufferDstPort flags for each input port */
      ssSetInputPortBufferDstPort(rts, 0, -1);
    }

    /* Level2 S-Function Block: wzor_02/<S7>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_02_M->childSfunctions[5];

      /* timing info */
      time_T *sfcnPeriod = wzor_02_M->NonInlinedSFcns.Sfcn5.sfcnPeriod;
      time_T *sfcnOffset = wzor_02_M->NonInlinedSFcns.Sfcn5.sfcnOffset;
      int_T *sfcnTsMap = wzor_02_M->NonInlinedSFcns.Sfcn5.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_02_M->NonInlinedSFcns.blkInfo2[5]);
      }

      ssSetRTWSfcnInfo(rts, wzor_02_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_02_M->NonInlinedSFcns.methods2[5]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_02_M->NonInlinedSFcns.methods3[5]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_02_M->NonInlinedSFcns.statesInfo2[5]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_02_M->NonInlinedSFcns.Sfcn5.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_02_M->NonInlinedSFcns.Sfcn5.UPtrs0;
          sfcnUPtrs[0] = &wzor_02_B.SaturationControlValve3;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_02/Tank3/RT-DAC PCI PWM Valve 3/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_02_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_02_M->NonInlinedSFcns.Sfcn5.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_02_P.RTDACPCIPWM_P1_Size_g);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_02_P.RTDACPCIPWM_P2_Size_j);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_02_P.RTDACPCIPWM_P3_Size_o);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_02_P.RTDACPCIPWM_P4_Size_g);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_02_P.RTDACPCIPWM_P5_Size_j);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_02_P.RTDACPCIPWM_P6_Size_i4);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_02_P.RTDACPCIPWM_P7_Size_b);
      }

      /* registration */
      tank_pwm(rts);
      sfcnInitializeSizes(rts);
      sfcnInitializeSampleTimes(rts);

      /* adjust sample time */
      ssSetSampleTime(rts, 0, 0.01);
      ssSetOffsetTime(rts, 0, 0.0);
      sfcnTsMap[0] = 0;

      /* set compiled values of dynamic vector attributes */
      ssSetNumNonsampledZCs(rts, 0);

      /* Update connectivity flags for each port */
      _ssSetInputPortConnected(rts, 0, 1);

      /* Update the BufferDstPort flags for each input port */
      ssSetInputPortBufferDstPort(rts, 0, -1);
    }

    /* Level2 S-Function Block: wzor_02/<S8>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_02_M->childSfunctions[6];

      /* timing info */
      time_T *sfcnPeriod = wzor_02_M->NonInlinedSFcns.Sfcn6.sfcnPeriod;
      time_T *sfcnOffset = wzor_02_M->NonInlinedSFcns.Sfcn6.sfcnOffset;
      int_T *sfcnTsMap = wzor_02_M->NonInlinedSFcns.Sfcn6.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_02_M->NonInlinedSFcns.blkInfo2[6]);
      }

      ssSetRTWSfcnInfo(rts, wzor_02_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_02_M->NonInlinedSFcns.methods2[6]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_02_M->NonInlinedSFcns.methods3[6]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_02_M->NonInlinedSFcns.statesInfo2[6]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_02_M->NonInlinedSFcns.Sfcn6.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_02_M->NonInlinedSFcns.Sfcn6.UPtrs0;
          sfcnUPtrs[0] = &wzor_02_B.SaturationControlValve4;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_02/Tank3/RT-DAC PCI PWM Valve 4/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_02_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_02_M->NonInlinedSFcns.Sfcn6.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_02_P.RTDACPCIPWM_P1_Size_d);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_02_P.RTDACPCIPWM_P2_Size_g);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_02_P.RTDACPCIPWM_P3_Size_n);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_02_P.RTDACPCIPWM_P4_Size_g2);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_02_P.RTDACPCIPWM_P5_Size_g);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_02_P.RTDACPCIPWM_P6_Size_io);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_02_P.RTDACPCIPWM_P7_Size_a);
      }

      /* registration */
      tank_pwm(rts);
      sfcnInitializeSizes(rts);
      sfcnInitializeSampleTimes(rts);

      /* adjust sample time */
      ssSetSampleTime(rts, 0, 0.01);
      ssSetOffsetTime(rts, 0, 0.0);
      sfcnTsMap[0] = 0;

      /* set compiled values of dynamic vector attributes */
      ssSetNumNonsampledZCs(rts, 0);

      /* Update connectivity flags for each port */
      _ssSetInputPortConnected(rts, 0, 1);

      /* Update the BufferDstPort flags for each input port */
      ssSetInputPortBufferDstPort(rts, 0, -1);
    }

    /* Level2 S-Function Block: wzor_02/<S9>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_02_M->childSfunctions[7];

      /* timing info */
      time_T *sfcnPeriod = wzor_02_M->NonInlinedSFcns.Sfcn7.sfcnPeriod;
      time_T *sfcnOffset = wzor_02_M->NonInlinedSFcns.Sfcn7.sfcnOffset;
      int_T *sfcnTsMap = wzor_02_M->NonInlinedSFcns.Sfcn7.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_02_M->NonInlinedSFcns.blkInfo2[7]);
      }

      ssSetRTWSfcnInfo(rts, wzor_02_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_02_M->NonInlinedSFcns.methods2[7]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_02_M->NonInlinedSFcns.methods3[7]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_02_M->NonInlinedSFcns.statesInfo2[7]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_02_M->NonInlinedSFcns.Sfcn7.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_02_M->NonInlinedSFcns.Sfcn7.UPtrs0;
          sfcnUPtrs[0] = &wzor_02_B.SaturationControlValve5;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_02/Tank3/RT-DAC PCI PWM Valve 5/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_02_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_02_M->NonInlinedSFcns.Sfcn7.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_02_P.RTDACPCIPWM_P1_Size_i);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_02_P.RTDACPCIPWM_P2_Size_jl);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_02_P.RTDACPCIPWM_P3_Size_nz);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_02_P.RTDACPCIPWM_P4_Size_b);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_02_P.RTDACPCIPWM_P5_Size_d);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_02_P.RTDACPCIPWM_P6_Size_ig);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_02_P.RTDACPCIPWM_P7_Size_ac);
      }

      /* registration */
      tank_pwm(rts);
      sfcnInitializeSizes(rts);
      sfcnInitializeSampleTimes(rts);

      /* adjust sample time */
      ssSetSampleTime(rts, 0, 0.01);
      ssSetOffsetTime(rts, 0, 0.0);
      sfcnTsMap[0] = 0;

      /* set compiled values of dynamic vector attributes */
      ssSetNumNonsampledZCs(rts, 0);

      /* Update connectivity flags for each port */
      _ssSetInputPortConnected(rts, 0, 1);

      /* Update the BufferDstPort flags for each input port */
      ssSetInputPortBufferDstPort(rts, 0, -1);
    }
  }

  /* Initialize Sizes */
  wzor_02_M->Sizes.numContStates = (0);/* Number of continuous states */
  wzor_02_M->Sizes.numY = (0);         /* Number of model outputs */
  wzor_02_M->Sizes.numU = (0);         /* Number of model inputs */
  wzor_02_M->Sizes.sysDirFeedThru = (0);/* The model is not direct feedthrough */
  wzor_02_M->Sizes.numSampTimes = (1); /* Number of sample times */
  wzor_02_M->Sizes.numBlocks = (31);   /* Number of blocks */
  wzor_02_M->Sizes.numBlockIO = (12);  /* Number of block outputs */
  wzor_02_M->Sizes.numBlockPrms = (162);/* Sum of parameter "widths" */
  return wzor_02_M;
}

/*========================================================================*
 * End of Classic call interface                                          *
 *========================================================================*/
