/*
 * wzor_01.c
 *
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * Code generation for model "wzor_01".
 *
 * Model version              : 1.225
 * Simulink Coder version : 8.8.1 (R2015aSP1) 04-Sep-2015
 * C source code generated on : Wed Nov 16 13:11:12 2022
 *
 * Target selection: rtwin.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: Intel->x86-64
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "wzor_01.h"
#include "wzor_01_private.h"
#include "wzor_01_dt.h"

/* list of Simulink Desktop Real-Time timers */
const int RTWinTimerCount = 1;
const double RTWinTimers[2] = {
  0.01, 0.0,
};

/* Block signals (auto storage) */
B_wzor_01_T wzor_01_B;

/* Block states (auto storage) */
DW_wzor_01_T wzor_01_DW;

/* Real-time model */
RT_MODEL_wzor_01_T wzor_01_M_;
RT_MODEL_wzor_01_T *const wzor_01_M = &wzor_01_M_;

/* Model output function */
void wzor_01_output(void)
{
  /* Constant: '<Root>/Constant' */
  wzor_01_B.Pump = wzor_01_P.Constant_Value;

  /* Level2 S-Function Block: '<S3>/RT-DAC Safety Alert' (tank_safetyalert) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[0];
    sfcnOutputs(rts, 0);
  }

  /* Level2 S-Function Block: '<S2>/RT-DAC Frequencies' (tank_frequencies) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[1];
    sfcnOutputs(rts, 0);
  }

  /* Fcn: '<S1>/Fcn' */
  wzor_01_B.Fcn = 0.017 * wzor_01_B.RTDACFrequencies[0] - 36.5137;

  /* Fcn: '<S1>/Fcn1' */
  wzor_01_B.Fcn1 = 0.0164 * wzor_01_B.RTDACFrequencies[1] - 35.7037;

  /* Fcn: '<S1>/Fcn2' */
  wzor_01_B.Fcn2 = 0.0164 * wzor_01_B.RTDACFrequencies[2] - 35.978;

  /* Level2 S-Function Block: '<S4>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[2];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Pump' */
  if (wzor_01_B.Pump > wzor_01_P.SaturationControlPump_UpperSat) {
    wzor_01_B.SaturationControlPump = wzor_01_P.SaturationControlPump_UpperSat;
  } else if (wzor_01_B.Pump < wzor_01_P.SaturationControlPump_LowerSat) {
    wzor_01_B.SaturationControlPump = wzor_01_P.SaturationControlPump_LowerSat;
  } else {
    wzor_01_B.SaturationControlPump = wzor_01_B.Pump;
  }

  /* End of Saturate: '<S1>/Saturation Control Pump' */

  /* Level2 S-Function Block: '<S5>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[3];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Valve 1' incorporates:
   *  Constant: '<Root>/Valve 1'
   */
  if (wzor_01_P.Valve1_Value > wzor_01_P.SaturationControlValve1_UpperSat) {
    wzor_01_B.SaturationControlValve1 =
      wzor_01_P.SaturationControlValve1_UpperSat;
  } else if (wzor_01_P.Valve1_Value < wzor_01_P.SaturationControlValve1_LowerSat)
  {
    wzor_01_B.SaturationControlValve1 =
      wzor_01_P.SaturationControlValve1_LowerSat;
  } else {
    wzor_01_B.SaturationControlValve1 = wzor_01_P.Valve1_Value;
  }

  /* End of Saturate: '<S1>/Saturation Control Valve 1' */

  /* Level2 S-Function Block: '<S6>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[4];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Valve 2' incorporates:
   *  Constant: '<Root>/Valve 2'
   */
  if (wzor_01_P.Valve2_Value > wzor_01_P.SaturationControlValve2_UpperSat) {
    wzor_01_B.SaturationControlValve2 =
      wzor_01_P.SaturationControlValve2_UpperSat;
  } else if (wzor_01_P.Valve2_Value < wzor_01_P.SaturationControlValve2_LowerSat)
  {
    wzor_01_B.SaturationControlValve2 =
      wzor_01_P.SaturationControlValve2_LowerSat;
  } else {
    wzor_01_B.SaturationControlValve2 = wzor_01_P.Valve2_Value;
  }

  /* End of Saturate: '<S1>/Saturation Control Valve 2' */

  /* Level2 S-Function Block: '<S7>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[5];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Valve 3' incorporates:
   *  Constant: '<Root>/Valve 3'
   */
  if (wzor_01_P.Valve3_Value > wzor_01_P.SaturationControlValve3_UpperSat) {
    wzor_01_B.SaturationControlValve3 =
      wzor_01_P.SaturationControlValve3_UpperSat;
  } else if (wzor_01_P.Valve3_Value < wzor_01_P.SaturationControlValve3_LowerSat)
  {
    wzor_01_B.SaturationControlValve3 =
      wzor_01_P.SaturationControlValve3_LowerSat;
  } else {
    wzor_01_B.SaturationControlValve3 = wzor_01_P.Valve3_Value;
  }

  /* End of Saturate: '<S1>/Saturation Control Valve 3' */

  /* Level2 S-Function Block: '<S8>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[6];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Valve 4' incorporates:
   *  Constant: '<S1>/Valve 4'
   */
  if (wzor_01_P.Valve4_Value > wzor_01_P.SaturationControlValve4_UpperSat) {
    wzor_01_B.SaturationControlValve4 =
      wzor_01_P.SaturationControlValve4_UpperSat;
  } else if (wzor_01_P.Valve4_Value < wzor_01_P.SaturationControlValve4_LowerSat)
  {
    wzor_01_B.SaturationControlValve4 =
      wzor_01_P.SaturationControlValve4_LowerSat;
  } else {
    wzor_01_B.SaturationControlValve4 = wzor_01_P.Valve4_Value;
  }

  /* End of Saturate: '<S1>/Saturation Control Valve 4' */

  /* Level2 S-Function Block: '<S9>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[7];
    sfcnOutputs(rts, 0);
  }

  /* Saturate: '<S1>/Saturation Control Valve 5' incorporates:
   *  Constant: '<S1>/Valve 5'
   */
  if (wzor_01_P.Valve5_Value > wzor_01_P.SaturationControlValve5_UpperSat) {
    wzor_01_B.SaturationControlValve5 =
      wzor_01_P.SaturationControlValve5_UpperSat;
  } else if (wzor_01_P.Valve5_Value < wzor_01_P.SaturationControlValve5_LowerSat)
  {
    wzor_01_B.SaturationControlValve5 =
      wzor_01_P.SaturationControlValve5_LowerSat;
  } else {
    wzor_01_B.SaturationControlValve5 = wzor_01_P.Valve5_Value;
  }

  /* End of Saturate: '<S1>/Saturation Control Valve 5' */
}

/* Model update function */
void wzor_01_update(void)
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
  if (!(++wzor_01_M->Timing.clockTick0)) {
    ++wzor_01_M->Timing.clockTickH0;
  }

  wzor_01_M->Timing.t[0] = wzor_01_M->Timing.clockTick0 *
    wzor_01_M->Timing.stepSize0 + wzor_01_M->Timing.clockTickH0 *
    wzor_01_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void wzor_01_initialize(void)
{
}

/* Model terminate function */
void wzor_01_terminate(void)
{
  /* Level2 S-Function Block: '<S3>/RT-DAC Safety Alert' (tank_safetyalert) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[0];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S2>/RT-DAC Frequencies' (tank_frequencies) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[1];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S4>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[2];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S5>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[3];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S6>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[4];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S7>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[5];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S8>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[6];
    sfcnTerminate(rts);
  }

  /* Level2 S-Function Block: '<S9>/RT-DAC PCI PWM ' (tank_pwm) */
  {
    SimStruct *rts = wzor_01_M->childSfunctions[7];
    sfcnTerminate(rts);
  }
}

/*========================================================================*
 * Start of Classic call interface                                        *
 *========================================================================*/
void MdlOutputs(int_T tid)
{
  wzor_01_output();
  UNUSED_PARAMETER(tid);
}

void MdlUpdate(int_T tid)
{
  wzor_01_update();
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
  wzor_01_initialize();
}

void MdlTerminate(void)
{
  wzor_01_terminate();
}

/* Registration function */
RT_MODEL_wzor_01_T *wzor_01(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)wzor_01_M, 0,
                sizeof(RT_MODEL_wzor_01_T));
  rtsiSetSolverName(&wzor_01_M->solverInfo,"FixedStepDiscrete");
  wzor_01_M->solverInfoPtr = (&wzor_01_M->solverInfo);

  /* Initialize timing info */
  {
    int_T *mdlTsMap = wzor_01_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    wzor_01_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    wzor_01_M->Timing.sampleTimes = (&wzor_01_M->Timing.sampleTimesArray[0]);
    wzor_01_M->Timing.offsetTimes = (&wzor_01_M->Timing.offsetTimesArray[0]);

    /* task periods */
    wzor_01_M->Timing.sampleTimes[0] = (0.01);

    /* task offsets */
    wzor_01_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(wzor_01_M, &wzor_01_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = wzor_01_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    wzor_01_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(wzor_01_M, -1);
  wzor_01_M->Timing.stepSize0 = 0.01;

  /* External mode info */
  wzor_01_M->Sizes.checksums[0] = (659317551U);
  wzor_01_M->Sizes.checksums[1] = (3560812498U);
  wzor_01_M->Sizes.checksums[2] = (361668384U);
  wzor_01_M->Sizes.checksums[3] = (2922332836U);

  {
    static const sysRanDType rtAlwaysEnabled = SUBSYS_RAN_BC_ENABLE;
    static RTWExtModeInfo rt_ExtModeInfo;
    static const sysRanDType *systemRan[1];
    wzor_01_M->extModeInfo = (&rt_ExtModeInfo);
    rteiSetSubSystemActiveVectorAddresses(&rt_ExtModeInfo, systemRan);
    systemRan[0] = &rtAlwaysEnabled;
    rteiSetModelMappingInfoPtr(wzor_01_M->extModeInfo,
      &wzor_01_M->SpecialInfo.mappingInfo);
    rteiSetChecksumsPtr(wzor_01_M->extModeInfo, wzor_01_M->Sizes.checksums);
    rteiSetTPtr(wzor_01_M->extModeInfo, rtmGetTPtr(wzor_01_M));
  }

  wzor_01_M->solverInfoPtr = (&wzor_01_M->solverInfo);
  wzor_01_M->Timing.stepSize = (0.01);
  rtsiSetFixedStepSize(&wzor_01_M->solverInfo, 0.01);
  rtsiSetSolverMode(&wzor_01_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* block I/O */
  wzor_01_M->ModelData.blockIO = ((void *) &wzor_01_B);

  {
    int32_T i;
    for (i = 0; i < 5; i++) {
      wzor_01_B.RTDACFrequencies[i] = 0.0;
    }

    wzor_01_B.Pump = 0.0;
    wzor_01_B.RTDACSafetyAlert = 0.0;
    wzor_01_B.Fcn = 0.0;
    wzor_01_B.Fcn1 = 0.0;
    wzor_01_B.Fcn2 = 0.0;
    wzor_01_B.SaturationControlPump = 0.0;
    wzor_01_B.SaturationControlValve1 = 0.0;
    wzor_01_B.SaturationControlValve2 = 0.0;
    wzor_01_B.SaturationControlValve3 = 0.0;
    wzor_01_B.SaturationControlValve4 = 0.0;
    wzor_01_B.SaturationControlValve5 = 0.0;
  }

  /* parameters */
  wzor_01_M->ModelData.defaultParam = ((real_T *)&wzor_01_P);

  /* states (dwork) */
  wzor_01_M->ModelData.dwork = ((void *) &wzor_01_DW);
  (void) memset((void *)&wzor_01_DW, 0,
                sizeof(DW_wzor_01_T));

  /* data type transition information */
  {
    static DataTypeTransInfo dtInfo;
    (void) memset((char_T *) &dtInfo, 0,
                  sizeof(dtInfo));
    wzor_01_M->SpecialInfo.mappingInfo = (&dtInfo);
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
    RTWSfcnInfo *sfcnInfo = &wzor_01_M->NonInlinedSFcns.sfcnInfo;
    wzor_01_M->sfcnInfo = (sfcnInfo);
    rtssSetErrorStatusPtr(sfcnInfo, (&rtmGetErrorStatus(wzor_01_M)));
    rtssSetNumRootSampTimesPtr(sfcnInfo, &wzor_01_M->Sizes.numSampTimes);
    wzor_01_M->NonInlinedSFcns.taskTimePtrs[0] = &(rtmGetTPtr(wzor_01_M)[0]);
    rtssSetTPtrPtr(sfcnInfo,wzor_01_M->NonInlinedSFcns.taskTimePtrs);
    rtssSetTStartPtr(sfcnInfo, &rtmGetTStart(wzor_01_M));
    rtssSetTFinalPtr(sfcnInfo, &rtmGetTFinal(wzor_01_M));
    rtssSetTimeOfLastOutputPtr(sfcnInfo, &rtmGetTimeOfLastOutput(wzor_01_M));
    rtssSetStepSizePtr(sfcnInfo, &wzor_01_M->Timing.stepSize);
    rtssSetStopRequestedPtr(sfcnInfo, &rtmGetStopRequested(wzor_01_M));
    rtssSetDerivCacheNeedsResetPtr(sfcnInfo,
      &wzor_01_M->ModelData.derivCacheNeedsReset);
    rtssSetZCCacheNeedsResetPtr(sfcnInfo,
      &wzor_01_M->ModelData.zCCacheNeedsReset);
    rtssSetBlkStateChangePtr(sfcnInfo, &wzor_01_M->ModelData.blkStateChange);
    rtssSetSampleHitsPtr(sfcnInfo, &wzor_01_M->Timing.sampleHits);
    rtssSetPerTaskSampleHitsPtr(sfcnInfo, &wzor_01_M->Timing.perTaskSampleHits);
    rtssSetSimModePtr(sfcnInfo, &wzor_01_M->simMode);
    rtssSetSolverInfoPtr(sfcnInfo, &wzor_01_M->solverInfoPtr);
  }

  wzor_01_M->Sizes.numSFcns = (8);

  /* register each child */
  {
    (void) memset((void *)&wzor_01_M->NonInlinedSFcns.childSFunctions[0], 0,
                  8*sizeof(SimStruct));
    wzor_01_M->childSfunctions = (&wzor_01_M->
      NonInlinedSFcns.childSFunctionPtrs[0]);

    {
      int_T i;
      for (i = 0; i < 8; i++) {
        wzor_01_M->childSfunctions[i] =
          (&wzor_01_M->NonInlinedSFcns.childSFunctions[i]);
      }
    }

    /* Level2 S-Function Block: wzor_01/<S3>/RT-DAC Safety Alert (tank_safetyalert) */
    {
      SimStruct *rts = wzor_01_M->childSfunctions[0];

      /* timing info */
      time_T *sfcnPeriod = wzor_01_M->NonInlinedSFcns.Sfcn0.sfcnPeriod;
      time_T *sfcnOffset = wzor_01_M->NonInlinedSFcns.Sfcn0.sfcnOffset;
      int_T *sfcnTsMap = wzor_01_M->NonInlinedSFcns.Sfcn0.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_01_M->NonInlinedSFcns.blkInfo2[0]);
      }

      ssSetRTWSfcnInfo(rts, wzor_01_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_01_M->NonInlinedSFcns.methods2[0]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_01_M->NonInlinedSFcns.methods3[0]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_01_M->NonInlinedSFcns.statesInfo2[0]);
      }

      /* outputs */
      {
        ssSetPortInfoForOutputs(rts,
          &wzor_01_M->NonInlinedSFcns.Sfcn0.outputPortInfo[0]);
        _ssSetNumOutputPorts(rts, 1);

        /* port 0 */
        {
          _ssSetOutputPortNumDimensions(rts, 0, 1);
          ssSetOutputPortWidth(rts, 0, 1);
          ssSetOutputPortSignal(rts, 0, ((real_T *) &wzor_01_B.RTDACSafetyAlert));
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC\nSafety Alert");
      ssSetPath(rts, "wzor_01/Tank3/RT-DAC Safety Alert/RT-DAC Safety Alert");
      ssSetRTModel(rts,wzor_01_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_01_M->NonInlinedSFcns.Sfcn0.params;
        ssSetSFcnParamsCount(rts, 2);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_01_P.RTDACSafetyAlert_P1_Size);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_01_P.RTDACSafetyAlert_P2_Size);
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

    /* Level2 S-Function Block: wzor_01/<S2>/RT-DAC Frequencies (tank_frequencies) */
    {
      SimStruct *rts = wzor_01_M->childSfunctions[1];

      /* timing info */
      time_T *sfcnPeriod = wzor_01_M->NonInlinedSFcns.Sfcn1.sfcnPeriod;
      time_T *sfcnOffset = wzor_01_M->NonInlinedSFcns.Sfcn1.sfcnOffset;
      int_T *sfcnTsMap = wzor_01_M->NonInlinedSFcns.Sfcn1.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_01_M->NonInlinedSFcns.blkInfo2[1]);
      }

      ssSetRTWSfcnInfo(rts, wzor_01_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_01_M->NonInlinedSFcns.methods2[1]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_01_M->NonInlinedSFcns.methods3[1]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_01_M->NonInlinedSFcns.statesInfo2[1]);
      }

      /* outputs */
      {
        ssSetPortInfoForOutputs(rts,
          &wzor_01_M->NonInlinedSFcns.Sfcn1.outputPortInfo[0]);
        _ssSetNumOutputPorts(rts, 1);

        /* port 0 */
        {
          _ssSetOutputPortNumDimensions(rts, 0, 1);
          ssSetOutputPortWidth(rts, 0, 5);
          ssSetOutputPortSignal(rts, 0, ((real_T *) wzor_01_B.RTDACFrequencies));
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC\nFrequencies");
      ssSetPath(rts, "wzor_01/Tank3/RT-DAC Frequencies/RT-DAC Frequencies");
      ssSetRTModel(rts,wzor_01_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_01_M->NonInlinedSFcns.Sfcn1.params;
        ssSetSFcnParamsCount(rts, 2);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_01_P.RTDACFrequencies_P1_Size);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_01_P.RTDACFrequencies_P2_Size);
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

    /* Level2 S-Function Block: wzor_01/<S4>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_01_M->childSfunctions[2];

      /* timing info */
      time_T *sfcnPeriod = wzor_01_M->NonInlinedSFcns.Sfcn2.sfcnPeriod;
      time_T *sfcnOffset = wzor_01_M->NonInlinedSFcns.Sfcn2.sfcnOffset;
      int_T *sfcnTsMap = wzor_01_M->NonInlinedSFcns.Sfcn2.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_01_M->NonInlinedSFcns.blkInfo2[2]);
      }

      ssSetRTWSfcnInfo(rts, wzor_01_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_01_M->NonInlinedSFcns.methods2[2]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_01_M->NonInlinedSFcns.methods3[2]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_01_M->NonInlinedSFcns.statesInfo2[2]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_01_M->NonInlinedSFcns.Sfcn2.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_01_M->NonInlinedSFcns.Sfcn2.UPtrs0;
          sfcnUPtrs[0] = &wzor_01_B.SaturationControlPump;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_01/Tank3/RT-DAC PCI PWM Pump/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_01_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_01_M->NonInlinedSFcns.Sfcn2.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_01_P.RTDACPCIPWM_P1_Size);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_01_P.RTDACPCIPWM_P2_Size);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_01_P.RTDACPCIPWM_P3_Size);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_01_P.RTDACPCIPWM_P4_Size);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_01_P.RTDACPCIPWM_P5_Size);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_01_P.RTDACPCIPWM_P6_Size);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_01_P.RTDACPCIPWM_P7_Size);
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

    /* Level2 S-Function Block: wzor_01/<S5>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_01_M->childSfunctions[3];

      /* timing info */
      time_T *sfcnPeriod = wzor_01_M->NonInlinedSFcns.Sfcn3.sfcnPeriod;
      time_T *sfcnOffset = wzor_01_M->NonInlinedSFcns.Sfcn3.sfcnOffset;
      int_T *sfcnTsMap = wzor_01_M->NonInlinedSFcns.Sfcn3.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_01_M->NonInlinedSFcns.blkInfo2[3]);
      }

      ssSetRTWSfcnInfo(rts, wzor_01_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_01_M->NonInlinedSFcns.methods2[3]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_01_M->NonInlinedSFcns.methods3[3]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_01_M->NonInlinedSFcns.statesInfo2[3]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_01_M->NonInlinedSFcns.Sfcn3.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_01_M->NonInlinedSFcns.Sfcn3.UPtrs0;
          sfcnUPtrs[0] = &wzor_01_B.SaturationControlValve1;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_01/Tank3/RT-DAC PCI PWM Valve 1/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_01_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_01_M->NonInlinedSFcns.Sfcn3.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_01_P.RTDACPCIPWM_P1_Size_a);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_01_P.RTDACPCIPWM_P2_Size_p);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_01_P.RTDACPCIPWM_P3_Size_h);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_01_P.RTDACPCIPWM_P4_Size_i);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_01_P.RTDACPCIPWM_P5_Size_m);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_01_P.RTDACPCIPWM_P6_Size_i);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_01_P.RTDACPCIPWM_P7_Size_p);
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

    /* Level2 S-Function Block: wzor_01/<S6>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_01_M->childSfunctions[4];

      /* timing info */
      time_T *sfcnPeriod = wzor_01_M->NonInlinedSFcns.Sfcn4.sfcnPeriod;
      time_T *sfcnOffset = wzor_01_M->NonInlinedSFcns.Sfcn4.sfcnOffset;
      int_T *sfcnTsMap = wzor_01_M->NonInlinedSFcns.Sfcn4.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_01_M->NonInlinedSFcns.blkInfo2[4]);
      }

      ssSetRTWSfcnInfo(rts, wzor_01_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_01_M->NonInlinedSFcns.methods2[4]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_01_M->NonInlinedSFcns.methods3[4]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_01_M->NonInlinedSFcns.statesInfo2[4]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_01_M->NonInlinedSFcns.Sfcn4.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_01_M->NonInlinedSFcns.Sfcn4.UPtrs0;
          sfcnUPtrs[0] = &wzor_01_B.SaturationControlValve2;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_01/Tank3/RT-DAC PCI PWM Valve 2/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_01_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_01_M->NonInlinedSFcns.Sfcn4.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_01_P.RTDACPCIPWM_P1_Size_p);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_01_P.RTDACPCIPWM_P2_Size_k);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_01_P.RTDACPCIPWM_P3_Size_a);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_01_P.RTDACPCIPWM_P4_Size_j);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_01_P.RTDACPCIPWM_P5_Size_h);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_01_P.RTDACPCIPWM_P6_Size_k);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_01_P.RTDACPCIPWM_P7_Size_i);
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

    /* Level2 S-Function Block: wzor_01/<S7>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_01_M->childSfunctions[5];

      /* timing info */
      time_T *sfcnPeriod = wzor_01_M->NonInlinedSFcns.Sfcn5.sfcnPeriod;
      time_T *sfcnOffset = wzor_01_M->NonInlinedSFcns.Sfcn5.sfcnOffset;
      int_T *sfcnTsMap = wzor_01_M->NonInlinedSFcns.Sfcn5.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_01_M->NonInlinedSFcns.blkInfo2[5]);
      }

      ssSetRTWSfcnInfo(rts, wzor_01_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_01_M->NonInlinedSFcns.methods2[5]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_01_M->NonInlinedSFcns.methods3[5]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_01_M->NonInlinedSFcns.statesInfo2[5]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_01_M->NonInlinedSFcns.Sfcn5.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_01_M->NonInlinedSFcns.Sfcn5.UPtrs0;
          sfcnUPtrs[0] = &wzor_01_B.SaturationControlValve3;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_01/Tank3/RT-DAC PCI PWM Valve 3/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_01_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_01_M->NonInlinedSFcns.Sfcn5.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_01_P.RTDACPCIPWM_P1_Size_g);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_01_P.RTDACPCIPWM_P2_Size_j);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_01_P.RTDACPCIPWM_P3_Size_o);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_01_P.RTDACPCIPWM_P4_Size_g);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_01_P.RTDACPCIPWM_P5_Size_j);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_01_P.RTDACPCIPWM_P6_Size_i4);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_01_P.RTDACPCIPWM_P7_Size_b);
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

    /* Level2 S-Function Block: wzor_01/<S8>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_01_M->childSfunctions[6];

      /* timing info */
      time_T *sfcnPeriod = wzor_01_M->NonInlinedSFcns.Sfcn6.sfcnPeriod;
      time_T *sfcnOffset = wzor_01_M->NonInlinedSFcns.Sfcn6.sfcnOffset;
      int_T *sfcnTsMap = wzor_01_M->NonInlinedSFcns.Sfcn6.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_01_M->NonInlinedSFcns.blkInfo2[6]);
      }

      ssSetRTWSfcnInfo(rts, wzor_01_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_01_M->NonInlinedSFcns.methods2[6]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_01_M->NonInlinedSFcns.methods3[6]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_01_M->NonInlinedSFcns.statesInfo2[6]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_01_M->NonInlinedSFcns.Sfcn6.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_01_M->NonInlinedSFcns.Sfcn6.UPtrs0;
          sfcnUPtrs[0] = &wzor_01_B.SaturationControlValve4;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_01/Tank3/RT-DAC PCI PWM Valve 4/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_01_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_01_M->NonInlinedSFcns.Sfcn6.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_01_P.RTDACPCIPWM_P1_Size_d);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_01_P.RTDACPCIPWM_P2_Size_g);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_01_P.RTDACPCIPWM_P3_Size_n);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_01_P.RTDACPCIPWM_P4_Size_g2);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_01_P.RTDACPCIPWM_P5_Size_g);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_01_P.RTDACPCIPWM_P6_Size_io);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_01_P.RTDACPCIPWM_P7_Size_a);
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

    /* Level2 S-Function Block: wzor_01/<S9>/RT-DAC PCI PWM  (tank_pwm) */
    {
      SimStruct *rts = wzor_01_M->childSfunctions[7];

      /* timing info */
      time_T *sfcnPeriod = wzor_01_M->NonInlinedSFcns.Sfcn7.sfcnPeriod;
      time_T *sfcnOffset = wzor_01_M->NonInlinedSFcns.Sfcn7.sfcnOffset;
      int_T *sfcnTsMap = wzor_01_M->NonInlinedSFcns.Sfcn7.sfcnTsMap;
      (void) memset((void*)sfcnPeriod, 0,
                    sizeof(time_T)*1);
      (void) memset((void*)sfcnOffset, 0,
                    sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      /* Set up the mdlInfo pointer */
      {
        ssSetBlkInfo2Ptr(rts, &wzor_01_M->NonInlinedSFcns.blkInfo2[7]);
      }

      ssSetRTWSfcnInfo(rts, wzor_01_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &wzor_01_M->NonInlinedSFcns.methods2[7]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &wzor_01_M->NonInlinedSFcns.methods3[7]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &wzor_01_M->NonInlinedSFcns.statesInfo2[7]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &wzor_01_M->NonInlinedSFcns.Sfcn7.inputPortInfo[0]);

        /* port 0 */
        {
          real_T const **sfcnUPtrs = (real_T const **)
            &wzor_01_M->NonInlinedSFcns.Sfcn7.UPtrs0;
          sfcnUPtrs[0] = &wzor_01_B.SaturationControlValve5;
          ssSetInputPortSignalPtrs(rts, 0, (InputPtrsType)&sfcnUPtrs[0]);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidth(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "RT-DAC PCI\nPWM\n");
      ssSetPath(rts, "wzor_01/Tank3/RT-DAC PCI PWM Valve 5/RT-DAC PCI PWM ");
      ssSetRTModel(rts,wzor_01_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* parameters */
      {
        mxArray **sfcnParams = (mxArray **)
          &wzor_01_M->NonInlinedSFcns.Sfcn7.params;
        ssSetSFcnParamsCount(rts, 7);
        ssSetSFcnParamsPtr(rts, &sfcnParams[0]);
        ssSetSFcnParam(rts, 0, (mxArray*)wzor_01_P.RTDACPCIPWM_P1_Size_i);
        ssSetSFcnParam(rts, 1, (mxArray*)wzor_01_P.RTDACPCIPWM_P2_Size_jl);
        ssSetSFcnParam(rts, 2, (mxArray*)wzor_01_P.RTDACPCIPWM_P3_Size_nz);
        ssSetSFcnParam(rts, 3, (mxArray*)wzor_01_P.RTDACPCIPWM_P4_Size_b);
        ssSetSFcnParam(rts, 4, (mxArray*)wzor_01_P.RTDACPCIPWM_P5_Size_d);
        ssSetSFcnParam(rts, 5, (mxArray*)wzor_01_P.RTDACPCIPWM_P6_Size_ig);
        ssSetSFcnParam(rts, 6, (mxArray*)wzor_01_P.RTDACPCIPWM_P7_Size_ac);
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
  wzor_01_M->Sizes.numContStates = (0);/* Number of continuous states */
  wzor_01_M->Sizes.numY = (0);         /* Number of model outputs */
  wzor_01_M->Sizes.numU = (0);         /* Number of model inputs */
  wzor_01_M->Sizes.sysDirFeedThru = (0);/* The model is not direct feedthrough */
  wzor_01_M->Sizes.numSampTimes = (1); /* Number of sample times */
  wzor_01_M->Sizes.numBlocks = (27);   /* Number of blocks */
  wzor_01_M->Sizes.numBlockIO = (12);  /* Number of block outputs */
  wzor_01_M->Sizes.numBlockPrms = (156);/* Sum of parameter "widths" */
  return wzor_01_M;
}

/*========================================================================*
 * End of Classic call interface                                          *
 *========================================================================*/
