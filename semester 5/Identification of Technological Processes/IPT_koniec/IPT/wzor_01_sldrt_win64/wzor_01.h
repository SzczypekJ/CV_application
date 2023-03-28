/*
 * wzor_01.h
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

#ifndef RTW_HEADER_wzor_01_h_
#define RTW_HEADER_wzor_01_h_
#include <string.h>
#include <stddef.h>
#ifndef wzor_01_COMMON_INCLUDES_
# define wzor_01_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "zero_crossing_types.h"
#include "simstruc.h"
#include "fixedpoint.h"
#include "dt_info.h"
#include "ext_work.h"
#include "sldrtdef.h"
#endif                                 /* wzor_01_COMMON_INCLUDES_ */

#include "wzor_01_types.h"

/* Shared type includes */
#include "multiword_types.h"
#include "rt_defines.h"
#include "rt_nonfinite.h"

/* Macros for accessing real-time model data structure */
#ifndef rtmGetBlkStateChangeFlag
# define rtmGetBlkStateChangeFlag(rtm) ((rtm)->ModelData.blkStateChange)
#endif

#ifndef rtmSetBlkStateChangeFlag
# define rtmSetBlkStateChangeFlag(rtm, val) ((rtm)->ModelData.blkStateChange = (val))
#endif

#ifndef rtmGetBlockIO
# define rtmGetBlockIO(rtm)            ((rtm)->ModelData.blockIO)
#endif

#ifndef rtmSetBlockIO
# define rtmSetBlockIO(rtm, val)       ((rtm)->ModelData.blockIO = (val))
#endif

#ifndef rtmGetChecksums
# define rtmGetChecksums(rtm)          ((rtm)->Sizes.checksums)
#endif

#ifndef rtmSetChecksums
# define rtmSetChecksums(rtm, val)     ((rtm)->Sizes.checksums = (val))
#endif

#ifndef rtmGetConstBlockIO
# define rtmGetConstBlockIO(rtm)       ((rtm)->ModelData.constBlockIO)
#endif

#ifndef rtmSetConstBlockIO
# define rtmSetConstBlockIO(rtm, val)  ((rtm)->ModelData.constBlockIO = (val))
#endif

#ifndef rtmGetContStateDisabled
# define rtmGetContStateDisabled(rtm)  ((rtm)->ModelData.contStateDisabled)
#endif

#ifndef rtmSetContStateDisabled
# define rtmSetContStateDisabled(rtm, val) ((rtm)->ModelData.contStateDisabled = (val))
#endif

#ifndef rtmGetContStates
# define rtmGetContStates(rtm)         ((rtm)->ModelData.contStates)
#endif

#ifndef rtmSetContStates
# define rtmSetContStates(rtm, val)    ((rtm)->ModelData.contStates = (val))
#endif

#ifndef rtmGetDataMapInfo
# define rtmGetDataMapInfo(rtm)        ()
#endif

#ifndef rtmSetDataMapInfo
# define rtmSetDataMapInfo(rtm, val)   ()
#endif

#ifndef rtmGetDefaultParam
# define rtmGetDefaultParam(rtm)       ((rtm)->ModelData.defaultParam)
#endif

#ifndef rtmSetDefaultParam
# define rtmSetDefaultParam(rtm, val)  ((rtm)->ModelData.defaultParam = (val))
#endif

#ifndef rtmGetDerivCacheNeedsReset
# define rtmGetDerivCacheNeedsReset(rtm) ((rtm)->ModelData.derivCacheNeedsReset)
#endif

#ifndef rtmSetDerivCacheNeedsReset
# define rtmSetDerivCacheNeedsReset(rtm, val) ((rtm)->ModelData.derivCacheNeedsReset = (val))
#endif

#ifndef rtmGetDirectFeedThrough
# define rtmGetDirectFeedThrough(rtm)  ((rtm)->Sizes.sysDirFeedThru)
#endif

#ifndef rtmSetDirectFeedThrough
# define rtmSetDirectFeedThrough(rtm, val) ((rtm)->Sizes.sysDirFeedThru = (val))
#endif

#ifndef rtmGetErrorStatusFlag
# define rtmGetErrorStatusFlag(rtm)    ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatusFlag
# define rtmSetErrorStatusFlag(rtm, val) ((rtm)->errorStatus = (val))
#endif

#ifndef rtmGetFinalTime
# define rtmGetFinalTime(rtm)          ((rtm)->Timing.tFinal)
#endif

#ifndef rtmSetFinalTime
# define rtmSetFinalTime(rtm, val)     ((rtm)->Timing.tFinal = (val))
#endif

#ifndef rtmGetFirstInitCondFlag
# define rtmGetFirstInitCondFlag(rtm)  ()
#endif

#ifndef rtmSetFirstInitCondFlag
# define rtmSetFirstInitCondFlag(rtm, val) ()
#endif

#ifndef rtmGetIntgData
# define rtmGetIntgData(rtm)           ()
#endif

#ifndef rtmSetIntgData
# define rtmSetIntgData(rtm, val)      ()
#endif

#ifndef rtmGetMdlRefGlobalTID
# define rtmGetMdlRefGlobalTID(rtm)    ()
#endif

#ifndef rtmSetMdlRefGlobalTID
# define rtmSetMdlRefGlobalTID(rtm, val) ()
#endif

#ifndef rtmGetMdlRefTriggerTID
# define rtmGetMdlRefTriggerTID(rtm)   ()
#endif

#ifndef rtmSetMdlRefTriggerTID
# define rtmSetMdlRefTriggerTID(rtm, val) ()
#endif

#ifndef rtmGetModelMappingInfo
# define rtmGetModelMappingInfo(rtm)   ((rtm)->SpecialInfo.mappingInfo)
#endif

#ifndef rtmSetModelMappingInfo
# define rtmSetModelMappingInfo(rtm, val) ((rtm)->SpecialInfo.mappingInfo = (val))
#endif

#ifndef rtmGetModelName
# define rtmGetModelName(rtm)          ((rtm)->modelName)
#endif

#ifndef rtmSetModelName
# define rtmSetModelName(rtm, val)     ((rtm)->modelName = (val))
#endif

#ifndef rtmGetNonInlinedSFcns
# define rtmGetNonInlinedSFcns(rtm)    ((rtm)->NonInlinedSFcns)
#endif

#ifndef rtmSetNonInlinedSFcns
# define rtmSetNonInlinedSFcns(rtm, val) ((rtm)->NonInlinedSFcns = (val))
#endif

#ifndef rtmGetNumBlockIO
# define rtmGetNumBlockIO(rtm)         ((rtm)->Sizes.numBlockIO)
#endif

#ifndef rtmSetNumBlockIO
# define rtmSetNumBlockIO(rtm, val)    ((rtm)->Sizes.numBlockIO = (val))
#endif

#ifndef rtmGetNumBlockParams
# define rtmGetNumBlockParams(rtm)     ((rtm)->Sizes.numBlockPrms)
#endif

#ifndef rtmSetNumBlockParams
# define rtmSetNumBlockParams(rtm, val) ((rtm)->Sizes.numBlockPrms = (val))
#endif

#ifndef rtmGetNumBlocks
# define rtmGetNumBlocks(rtm)          ((rtm)->Sizes.numBlocks)
#endif

#ifndef rtmSetNumBlocks
# define rtmSetNumBlocks(rtm, val)     ((rtm)->Sizes.numBlocks = (val))
#endif

#ifndef rtmGetNumContStates
# define rtmGetNumContStates(rtm)      ((rtm)->Sizes.numContStates)
#endif

#ifndef rtmSetNumContStates
# define rtmSetNumContStates(rtm, val) ((rtm)->Sizes.numContStates = (val))
#endif

#ifndef rtmGetNumDWork
# define rtmGetNumDWork(rtm)           ((rtm)->Sizes.numDwork)
#endif

#ifndef rtmSetNumDWork
# define rtmSetNumDWork(rtm, val)      ((rtm)->Sizes.numDwork = (val))
#endif

#ifndef rtmGetNumInputPorts
# define rtmGetNumInputPorts(rtm)      ((rtm)->Sizes.numIports)
#endif

#ifndef rtmSetNumInputPorts
# define rtmSetNumInputPorts(rtm, val) ((rtm)->Sizes.numIports = (val))
#endif

#ifndef rtmGetNumNonSampledZCs
# define rtmGetNumNonSampledZCs(rtm)   ((rtm)->Sizes.numNonSampZCs)
#endif

#ifndef rtmSetNumNonSampledZCs
# define rtmSetNumNonSampledZCs(rtm, val) ((rtm)->Sizes.numNonSampZCs = (val))
#endif

#ifndef rtmGetNumOutputPorts
# define rtmGetNumOutputPorts(rtm)     ((rtm)->Sizes.numOports)
#endif

#ifndef rtmSetNumOutputPorts
# define rtmSetNumOutputPorts(rtm, val) ((rtm)->Sizes.numOports = (val))
#endif

#ifndef rtmGetNumPeriodicContStates
# define rtmGetNumPeriodicContStates(rtm) ((rtm)->Sizes.numPeriodicContStates)
#endif

#ifndef rtmSetNumPeriodicContStates
# define rtmSetNumPeriodicContStates(rtm, val) ((rtm)->Sizes.numPeriodicContStates = (val))
#endif

#ifndef rtmGetNumSFcnParams
# define rtmGetNumSFcnParams(rtm)      ((rtm)->Sizes.numSFcnPrms)
#endif

#ifndef rtmSetNumSFcnParams
# define rtmSetNumSFcnParams(rtm, val) ((rtm)->Sizes.numSFcnPrms = (val))
#endif

#ifndef rtmGetNumSFunctions
# define rtmGetNumSFunctions(rtm)      ((rtm)->Sizes.numSFcns)
#endif

#ifndef rtmSetNumSFunctions
# define rtmSetNumSFunctions(rtm, val) ((rtm)->Sizes.numSFcns = (val))
#endif

#ifndef rtmGetNumSampleTimes
# define rtmGetNumSampleTimes(rtm)     ((rtm)->Sizes.numSampTimes)
#endif

#ifndef rtmSetNumSampleTimes
# define rtmSetNumSampleTimes(rtm, val) ((rtm)->Sizes.numSampTimes = (val))
#endif

#ifndef rtmGetNumU
# define rtmGetNumU(rtm)               ((rtm)->Sizes.numU)
#endif

#ifndef rtmSetNumU
# define rtmSetNumU(rtm, val)          ((rtm)->Sizes.numU = (val))
#endif

#ifndef rtmGetNumY
# define rtmGetNumY(rtm)               ((rtm)->Sizes.numY)
#endif

#ifndef rtmSetNumY
# define rtmSetNumY(rtm, val)          ((rtm)->Sizes.numY = (val))
#endif

#ifndef rtmGetOdeF
# define rtmGetOdeF(rtm)               ()
#endif

#ifndef rtmSetOdeF
# define rtmSetOdeF(rtm, val)          ()
#endif

#ifndef rtmGetOdeY
# define rtmGetOdeY(rtm)               ()
#endif

#ifndef rtmSetOdeY
# define rtmSetOdeY(rtm, val)          ()
#endif

#ifndef rtmGetOffsetTimeArray
# define rtmGetOffsetTimeArray(rtm)    ((rtm)->Timing.offsetTimesArray)
#endif

#ifndef rtmSetOffsetTimeArray
# define rtmSetOffsetTimeArray(rtm, val) ((rtm)->Timing.offsetTimesArray = (val))
#endif

#ifndef rtmGetOffsetTimePtr
# define rtmGetOffsetTimePtr(rtm)      ((rtm)->Timing.offsetTimes)
#endif

#ifndef rtmSetOffsetTimePtr
# define rtmSetOffsetTimePtr(rtm, val) ((rtm)->Timing.offsetTimes = (val))
#endif

#ifndef rtmGetOptions
# define rtmGetOptions(rtm)            ((rtm)->Sizes.options)
#endif

#ifndef rtmSetOptions
# define rtmSetOptions(rtm, val)       ((rtm)->Sizes.options = (val))
#endif

#ifndef rtmGetParamIsMalloced
# define rtmGetParamIsMalloced(rtm)    ()
#endif

#ifndef rtmSetParamIsMalloced
# define rtmSetParamIsMalloced(rtm, val) ()
#endif

#ifndef rtmGetPath
# define rtmGetPath(rtm)               ((rtm)->path)
#endif

#ifndef rtmSetPath
# define rtmSetPath(rtm, val)          ((rtm)->path = (val))
#endif

#ifndef rtmGetPerTaskSampleHits
# define rtmGetPerTaskSampleHits(rtm)  ()
#endif

#ifndef rtmSetPerTaskSampleHits
# define rtmSetPerTaskSampleHits(rtm, val) ()
#endif

#ifndef rtmGetPerTaskSampleHitsArray
# define rtmGetPerTaskSampleHitsArray(rtm) ((rtm)->Timing.perTaskSampleHitsArray)
#endif

#ifndef rtmSetPerTaskSampleHitsArray
# define rtmSetPerTaskSampleHitsArray(rtm, val) ((rtm)->Timing.perTaskSampleHitsArray = (val))
#endif

#ifndef rtmGetPerTaskSampleHitsPtr
# define rtmGetPerTaskSampleHitsPtr(rtm) ((rtm)->Timing.perTaskSampleHits)
#endif

#ifndef rtmSetPerTaskSampleHitsPtr
# define rtmSetPerTaskSampleHitsPtr(rtm, val) ((rtm)->Timing.perTaskSampleHits = (val))
#endif

#ifndef rtmGetPeriodicContStateIndices
# define rtmGetPeriodicContStateIndices(rtm) ((rtm)->ModelData.periodicContStateIndices)
#endif

#ifndef rtmSetPeriodicContStateIndices
# define rtmSetPeriodicContStateIndices(rtm, val) ((rtm)->ModelData.periodicContStateIndices = (val))
#endif

#ifndef rtmGetPeriodicContStateRanges
# define rtmGetPeriodicContStateRanges(rtm) ((rtm)->ModelData.periodicContStateRanges)
#endif

#ifndef rtmSetPeriodicContStateRanges
# define rtmSetPeriodicContStateRanges(rtm, val) ((rtm)->ModelData.periodicContStateRanges = (val))
#endif

#ifndef rtmGetPrevZCSigState
# define rtmGetPrevZCSigState(rtm)     ((rtm)->ModelData.prevZCSigState)
#endif

#ifndef rtmSetPrevZCSigState
# define rtmSetPrevZCSigState(rtm, val) ((rtm)->ModelData.prevZCSigState = (val))
#endif

#ifndef rtmGetRTWExtModeInfo
# define rtmGetRTWExtModeInfo(rtm)     ((rtm)->extModeInfo)
#endif

#ifndef rtmSetRTWExtModeInfo
# define rtmSetRTWExtModeInfo(rtm, val) ((rtm)->extModeInfo = (val))
#endif

#ifndef rtmGetRTWGeneratedSFcn
# define rtmGetRTWGeneratedSFcn(rtm)   ((rtm)->Sizes.rtwGenSfcn)
#endif

#ifndef rtmSetRTWGeneratedSFcn
# define rtmSetRTWGeneratedSFcn(rtm, val) ((rtm)->Sizes.rtwGenSfcn = (val))
#endif

#ifndef rtmGetRTWLogInfo
# define rtmGetRTWLogInfo(rtm)         ()
#endif

#ifndef rtmSetRTWLogInfo
# define rtmSetRTWLogInfo(rtm, val)    ()
#endif

#ifndef rtmGetRTWRTModelMethodsInfo
# define rtmGetRTWRTModelMethodsInfo(rtm) ()
#endif

#ifndef rtmSetRTWRTModelMethodsInfo
# define rtmSetRTWRTModelMethodsInfo(rtm, val) ()
#endif

#ifndef rtmGetRTWSfcnInfo
# define rtmGetRTWSfcnInfo(rtm)        ((rtm)->sfcnInfo)
#endif

#ifndef rtmSetRTWSfcnInfo
# define rtmSetRTWSfcnInfo(rtm, val)   ((rtm)->sfcnInfo = (val))
#endif

#ifndef rtmGetRTWSolverInfo
# define rtmGetRTWSolverInfo(rtm)      ((rtm)->solverInfo)
#endif

#ifndef rtmSetRTWSolverInfo
# define rtmSetRTWSolverInfo(rtm, val) ((rtm)->solverInfo = (val))
#endif

#ifndef rtmGetRTWSolverInfoPtr
# define rtmGetRTWSolverInfoPtr(rtm)   ((rtm)->solverInfoPtr)
#endif

#ifndef rtmSetRTWSolverInfoPtr
# define rtmSetRTWSolverInfoPtr(rtm, val) ((rtm)->solverInfoPtr = (val))
#endif

#ifndef rtmGetReservedForXPC
# define rtmGetReservedForXPC(rtm)     ((rtm)->SpecialInfo.xpcData)
#endif

#ifndef rtmSetReservedForXPC
# define rtmSetReservedForXPC(rtm, val) ((rtm)->SpecialInfo.xpcData = (val))
#endif

#ifndef rtmGetRootDWork
# define rtmGetRootDWork(rtm)          ((rtm)->ModelData.dwork)
#endif

#ifndef rtmSetRootDWork
# define rtmSetRootDWork(rtm, val)     ((rtm)->ModelData.dwork = (val))
#endif

#ifndef rtmGetSFunctions
# define rtmGetSFunctions(rtm)         ((rtm)->childSfunctions)
#endif

#ifndef rtmSetSFunctions
# define rtmSetSFunctions(rtm, val)    ((rtm)->childSfunctions = (val))
#endif

#ifndef rtmGetSampleHitArray
# define rtmGetSampleHitArray(rtm)     ((rtm)->Timing.sampleHitArray)
#endif

#ifndef rtmSetSampleHitArray
# define rtmSetSampleHitArray(rtm, val) ((rtm)->Timing.sampleHitArray = (val))
#endif

#ifndef rtmGetSampleHitPtr
# define rtmGetSampleHitPtr(rtm)       ((rtm)->Timing.sampleHits)
#endif

#ifndef rtmSetSampleHitPtr
# define rtmSetSampleHitPtr(rtm, val)  ((rtm)->Timing.sampleHits = (val))
#endif

#ifndef rtmGetSampleTimeArray
# define rtmGetSampleTimeArray(rtm)    ((rtm)->Timing.sampleTimesArray)
#endif

#ifndef rtmSetSampleTimeArray
# define rtmSetSampleTimeArray(rtm, val) ((rtm)->Timing.sampleTimesArray = (val))
#endif

#ifndef rtmGetSampleTimePtr
# define rtmGetSampleTimePtr(rtm)      ((rtm)->Timing.sampleTimes)
#endif

#ifndef rtmSetSampleTimePtr
# define rtmSetSampleTimePtr(rtm, val) ((rtm)->Timing.sampleTimes = (val))
#endif

#ifndef rtmGetSampleTimeTaskIDArray
# define rtmGetSampleTimeTaskIDArray(rtm) ((rtm)->Timing.sampleTimeTaskIDArray)
#endif

#ifndef rtmSetSampleTimeTaskIDArray
# define rtmSetSampleTimeTaskIDArray(rtm, val) ((rtm)->Timing.sampleTimeTaskIDArray = (val))
#endif

#ifndef rtmGetSampleTimeTaskIDPtr
# define rtmGetSampleTimeTaskIDPtr(rtm) ((rtm)->Timing.sampleTimeTaskIDPtr)
#endif

#ifndef rtmSetSampleTimeTaskIDPtr
# define rtmSetSampleTimeTaskIDPtr(rtm, val) ((rtm)->Timing.sampleTimeTaskIDPtr = (val))
#endif

#ifndef rtmGetSimMode
# define rtmGetSimMode(rtm)            ((rtm)->simMode)
#endif

#ifndef rtmSetSimMode
# define rtmSetSimMode(rtm, val)       ((rtm)->simMode = (val))
#endif

#ifndef rtmGetSimTimeStep
# define rtmGetSimTimeStep(rtm)        ((rtm)->Timing.simTimeStep)
#endif

#ifndef rtmSetSimTimeStep
# define rtmSetSimTimeStep(rtm, val)   ((rtm)->Timing.simTimeStep = (val))
#endif

#ifndef rtmGetStartTime
# define rtmGetStartTime(rtm)          ((rtm)->Timing.tStart)
#endif

#ifndef rtmSetStartTime
# define rtmSetStartTime(rtm, val)     ((rtm)->Timing.tStart = (val))
#endif

#ifndef rtmGetStepSize
# define rtmGetStepSize(rtm)           ((rtm)->Timing.stepSize)
#endif

#ifndef rtmSetStepSize
# define rtmSetStepSize(rtm, val)      ((rtm)->Timing.stepSize = (val))
#endif

#ifndef rtmGetStopRequestedFlag
# define rtmGetStopRequestedFlag(rtm)  ((rtm)->Timing.stopRequestedFlag)
#endif

#ifndef rtmSetStopRequestedFlag
# define rtmSetStopRequestedFlag(rtm, val) ((rtm)->Timing.stopRequestedFlag = (val))
#endif

#ifndef rtmGetTaskCounters
# define rtmGetTaskCounters(rtm)       ()
#endif

#ifndef rtmSetTaskCounters
# define rtmSetTaskCounters(rtm, val)  ()
#endif

#ifndef rtmGetTaskTimeArray
# define rtmGetTaskTimeArray(rtm)      ((rtm)->Timing.tArray)
#endif

#ifndef rtmSetTaskTimeArray
# define rtmSetTaskTimeArray(rtm, val) ((rtm)->Timing.tArray = (val))
#endif

#ifndef rtmGetTimePtr
# define rtmGetTimePtr(rtm)            ((rtm)->Timing.t)
#endif

#ifndef rtmSetTimePtr
# define rtmSetTimePtr(rtm, val)       ((rtm)->Timing.t = (val))
#endif

#ifndef rtmGetTimingData
# define rtmGetTimingData(rtm)         ((rtm)->Timing.timingData)
#endif

#ifndef rtmSetTimingData
# define rtmSetTimingData(rtm, val)    ((rtm)->Timing.timingData = (val))
#endif

#ifndef rtmGetU
# define rtmGetU(rtm)                  ((rtm)->ModelData.inputs)
#endif

#ifndef rtmSetU
# define rtmSetU(rtm, val)             ((rtm)->ModelData.inputs = (val))
#endif

#ifndef rtmGetVarNextHitTimesListPtr
# define rtmGetVarNextHitTimesListPtr(rtm) ((rtm)->Timing.varNextHitTimesList)
#endif

#ifndef rtmSetVarNextHitTimesListPtr
# define rtmSetVarNextHitTimesListPtr(rtm, val) ((rtm)->Timing.varNextHitTimesList = (val))
#endif

#ifndef rtmGetY
# define rtmGetY(rtm)                  ((rtm)->ModelData.outputs)
#endif

#ifndef rtmSetY
# define rtmSetY(rtm, val)             ((rtm)->ModelData.outputs = (val))
#endif

#ifndef rtmGetZCCacheNeedsReset
# define rtmGetZCCacheNeedsReset(rtm)  ((rtm)->ModelData.zCCacheNeedsReset)
#endif

#ifndef rtmSetZCCacheNeedsReset
# define rtmSetZCCacheNeedsReset(rtm, val) ((rtm)->ModelData.zCCacheNeedsReset = (val))
#endif

#ifndef rtmGetZCSignalValues
# define rtmGetZCSignalValues(rtm)     ((rtm)->ModelData.zcSignalValues)
#endif

#ifndef rtmSetZCSignalValues
# define rtmSetZCSignalValues(rtm, val) ((rtm)->ModelData.zcSignalValues = (val))
#endif

#ifndef rtmGet_TimeOfLastOutput
# define rtmGet_TimeOfLastOutput(rtm)  ((rtm)->Timing.timeOfLastOutput)
#endif

#ifndef rtmSet_TimeOfLastOutput
# define rtmSet_TimeOfLastOutput(rtm, val) ((rtm)->Timing.timeOfLastOutput = (val))
#endif

#ifndef rtmGetdX
# define rtmGetdX(rtm)                 ((rtm)->ModelData.derivs)
#endif

#ifndef rtmSetdX
# define rtmSetdX(rtm, val)            ((rtm)->ModelData.derivs = (val))
#endif

#ifndef rtmGetChecksumVal
# define rtmGetChecksumVal(rtm, idx)   ((rtm)->Sizes.checksums[idx])
#endif

#ifndef rtmSetChecksumVal
# define rtmSetChecksumVal(rtm, idx, val) ((rtm)->Sizes.checksums[idx] = (val))
#endif

#ifndef rtmGetDWork
# define rtmGetDWork(rtm, idx)         ((rtm)->ModelData.dwork[idx])
#endif

#ifndef rtmSetDWork
# define rtmSetDWork(rtm, idx, val)    ((rtm)->ModelData.dwork[idx] = (val))
#endif

#ifndef rtmGetOffsetTime
# define rtmGetOffsetTime(rtm, idx)    ((rtm)->Timing.offsetTimes[idx])
#endif

#ifndef rtmSetOffsetTime
# define rtmSetOffsetTime(rtm, idx, val) ((rtm)->Timing.offsetTimes[idx] = (val))
#endif

#ifndef rtmGetSFunction
# define rtmGetSFunction(rtm, idx)     ((rtm)->childSfunctions[idx])
#endif

#ifndef rtmSetSFunction
# define rtmSetSFunction(rtm, idx, val) ((rtm)->childSfunctions[idx] = (val))
#endif

#ifndef rtmGetSampleTime
# define rtmGetSampleTime(rtm, idx)    ((rtm)->Timing.sampleTimes[idx])
#endif

#ifndef rtmSetSampleTime
# define rtmSetSampleTime(rtm, idx, val) ((rtm)->Timing.sampleTimes[idx] = (val))
#endif

#ifndef rtmGetSampleTimeTaskID
# define rtmGetSampleTimeTaskID(rtm, idx) ((rtm)->Timing.sampleTimeTaskIDPtr[idx])
#endif

#ifndef rtmSetSampleTimeTaskID
# define rtmSetSampleTimeTaskID(rtm, idx, val) ((rtm)->Timing.sampleTimeTaskIDPtr[idx] = (val))
#endif

#ifndef rtmGetVarNextHitTimeList
# define rtmGetVarNextHitTimeList(rtm, idx) ((rtm)->Timing.varNextHitTimesList[idx])
#endif

#ifndef rtmSetVarNextHitTimeList
# define rtmSetVarNextHitTimeList(rtm, idx, val) ((rtm)->Timing.varNextHitTimesList[idx] = (val))
#endif

#ifndef rtmIsContinuousTask
# define rtmIsContinuousTask(rtm, tid) 0
#endif

#ifndef rtmGetErrorStatus
# define rtmGetErrorStatus(rtm)        ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
# define rtmSetErrorStatus(rtm, val)   ((rtm)->errorStatus = (val))
#endif

#ifndef rtmIsSampleHit
# define rtmIsSampleHit(rtm, sti, tid) ((rtm)->Timing.sampleHits[(rtm)->Timing.sampleTimeTaskIDPtr[sti]])
#endif

#ifndef rtmGetStopRequested
# define rtmGetStopRequested(rtm)      ((rtm)->Timing.stopRequestedFlag)
#endif

#ifndef rtmSetStopRequested
# define rtmSetStopRequested(rtm, val) ((rtm)->Timing.stopRequestedFlag = (val))
#endif

#ifndef rtmGetStopRequestedPtr
# define rtmGetStopRequestedPtr(rtm)   (&((rtm)->Timing.stopRequestedFlag))
#endif

#ifndef rtmGetT
# define rtmGetT(rtm)                  (rtmGetTPtr((rtm))[0])
#endif

#ifndef rtmSetT
# define rtmSetT(rtm, val)                                       /* Do Nothing */
#endif

#ifndef rtmGetTFinal
# define rtmGetTFinal(rtm)             ((rtm)->Timing.tFinal)
#endif

#ifndef rtmSetTFinal
# define rtmSetTFinal(rtm, val)        ((rtm)->Timing.tFinal = (val))
#endif

#ifndef rtmGetTPtr
# define rtmGetTPtr(rtm)               ((rtm)->Timing.t)
#endif

#ifndef rtmSetTPtr
# define rtmSetTPtr(rtm, val)          ((rtm)->Timing.t = (val))
#endif

#ifndef rtmGetTStart
# define rtmGetTStart(rtm)             ((rtm)->Timing.tStart)
#endif

#ifndef rtmSetTStart
# define rtmSetTStart(rtm, val)        ((rtm)->Timing.tStart = (val))
#endif

#ifndef rtmGetTaskTime
# define rtmGetTaskTime(rtm, sti)      (rtmGetTPtr((rtm))[(rtm)->Timing.sampleTimeTaskIDPtr[sti]])
#endif

#ifndef rtmSetTaskTime
# define rtmSetTaskTime(rtm, sti, val) (rtmGetTPtr((rtm))[sti] = (val))
#endif

#ifndef rtmGetTimeOfLastOutput
# define rtmGetTimeOfLastOutput(rtm)   ((rtm)->Timing.timeOfLastOutput)
#endif

#ifdef rtmGetRTWSolverInfo
#undef rtmGetRTWSolverInfo
#endif

#define rtmGetRTWSolverInfo(rtm)       &((rtm)->solverInfo)

/* Definition for use in the target main file */
#define wzor_01_rtModel                RT_MODEL_wzor_01_T

/* Block signals (auto storage) */
typedef struct {
  real_T Pump;                         /* '<Root>/Constant' */
  real_T RTDACSafetyAlert;             /* '<S3>/RT-DAC Safety Alert' */
  real_T RTDACFrequencies[5];          /* '<S2>/RT-DAC Frequencies' */
  real_T Fcn;                          /* '<S1>/Fcn' */
  real_T Fcn1;                         /* '<S1>/Fcn1' */
  real_T Fcn2;                         /* '<S1>/Fcn2' */
  real_T SaturationControlPump;        /* '<S1>/Saturation Control Pump' */
  real_T SaturationControlValve1;      /* '<S1>/Saturation Control Valve 1' */
  real_T SaturationControlValve2;      /* '<S1>/Saturation Control Valve 2' */
  real_T SaturationControlValve3;      /* '<S1>/Saturation Control Valve 3' */
  real_T SaturationControlValve4;      /* '<S1>/Saturation Control Valve 4' */
  real_T SaturationControlValve5;      /* '<S1>/Saturation Control Valve 5' */
} B_wzor_01_T;

/* Block states (auto storage) for system '<Root>' */
typedef struct {
  struct {
    void *LoggedData;
  } Tank_PWORK;                        /* '<Root>/Tank' */

  struct {
    void *LoggedData;
  } Scope_PWORK;                       /* '<S1>/Scope' */

  struct {
    void *LoggedData;
  } Scope1_PWORK;                      /* '<S1>/Scope1' */

  struct {
    void *LoggedData;
  } Scope2_PWORK;                      /* '<S1>/Scope2' */
} DW_wzor_01_T;

/* Backward compatible GRT Identifiers */
#define rtB                            wzor_01_B
#define BlockIO                        B_wzor_01_T
#define rtP                            wzor_01_P
#define Parameters                     P_wzor_01_T
#define rtDWork                        wzor_01_DW
#define D_Work                         DW_wzor_01_T

/* Parameters (auto storage) */
struct P_wzor_01_T_ {
  real_T Constant_Value;               /* Expression: 0
                                        * Referenced by: '<Root>/Constant'
                                        */
  real_T RTDACSafetyAlert_P1_Size[2];  /* Computed Parameter: RTDACSafetyAlert_P1_Size
                                        * Referenced by: '<S3>/RT-DAC Safety Alert'
                                        */
  real_T RTDACSafetyAlert_P1;          /* Expression: BaseAddress
                                        * Referenced by: '<S3>/RT-DAC Safety Alert'
                                        */
  real_T RTDACSafetyAlert_P2_Size[2];  /* Computed Parameter: RTDACSafetyAlert_P2_Size
                                        * Referenced by: '<S3>/RT-DAC Safety Alert'
                                        */
  real_T RTDACSafetyAlert_P2;          /* Expression: T0
                                        * Referenced by: '<S3>/RT-DAC Safety Alert'
                                        */
  real_T RTDACFrequencies_P1_Size[2];  /* Computed Parameter: RTDACFrequencies_P1_Size
                                        * Referenced by: '<S2>/RT-DAC Frequencies'
                                        */
  real_T RTDACFrequencies_P1;          /* Expression: BaseAddress
                                        * Referenced by: '<S2>/RT-DAC Frequencies'
                                        */
  real_T RTDACFrequencies_P2_Size[2];  /* Computed Parameter: RTDACFrequencies_P2_Size
                                        * Referenced by: '<S2>/RT-DAC Frequencies'
                                        */
  real_T RTDACFrequencies_P2;          /* Expression: T0
                                        * Referenced by: '<S2>/RT-DAC Frequencies'
                                        */
  real_T RTDACPCIPWM_P1_Size[2];       /* Computed Parameter: RTDACPCIPWM_P1_Size
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P1;               /* Expression: BaseAddress
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_Size[2];       /* Computed Parameter: RTDACPCIPWM_P2_Size
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2;               /* Expression: ChanIdx
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_Size[2];       /* Computed Parameter: RTDACPCIPWM_P3_Size
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3;               /* Expression: ChanMode
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_Size[2];       /* Computed Parameter: RTDACPCIPWM_P4_Size
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4;               /* Expression: ChanPresc
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_Size[2];       /* Computed Parameter: RTDACPCIPWM_P5_Size
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5;               /* Expression: SetOutputsFlag
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_Size[2];       /* Computed Parameter: RTDACPCIPWM_P6_Size
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6;               /* Expression: SetOutputsValue
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_Size[2];       /* Computed Parameter: RTDACPCIPWM_P7_Size
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7;               /* Expression: T0
                                        * Referenced by: '<S4>/RT-DAC PCI PWM '
                                        */
  real_T SaturationControlPump_UpperSat;/* Expression: 1
                                         * Referenced by: '<S1>/Saturation Control Pump'
                                         */
  real_T SaturationControlPump_LowerSat;/* Expression: 0
                                         * Referenced by: '<S1>/Saturation Control Pump'
                                         */
  real_T RTDACPCIPWM_P1_Size_a[2];     /* Computed Parameter: RTDACPCIPWM_P1_Size_a
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P1_c;             /* Expression: BaseAddress
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_Size_p[2];     /* Computed Parameter: RTDACPCIPWM_P2_Size_p
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_f;             /* Expression: ChanIdx
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_Size_h[2];     /* Computed Parameter: RTDACPCIPWM_P3_Size_h
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_d;             /* Expression: ChanMode
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_Size_i[2];     /* Computed Parameter: RTDACPCIPWM_P4_Size_i
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_c;             /* Expression: ChanPresc
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_Size_m[2];     /* Computed Parameter: RTDACPCIPWM_P5_Size_m
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_b;             /* Expression: SetOutputsFlag
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_Size_i[2];     /* Computed Parameter: RTDACPCIPWM_P6_Size_i
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_i;             /* Expression: SetOutputsValue
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_Size_p[2];     /* Computed Parameter: RTDACPCIPWM_P7_Size_p
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_m;             /* Expression: T0
                                        * Referenced by: '<S5>/RT-DAC PCI PWM '
                                        */
  real_T Valve1_Value;                 /* Expression: 0
                                        * Referenced by: '<Root>/Valve 1'
                                        */
  real_T SaturationControlValve1_UpperSat;/* Expression: 1
                                           * Referenced by: '<S1>/Saturation Control Valve 1'
                                           */
  real_T SaturationControlValve1_LowerSat;/* Expression: 0
                                           * Referenced by: '<S1>/Saturation Control Valve 1'
                                           */
  real_T RTDACPCIPWM_P1_Size_p[2];     /* Computed Parameter: RTDACPCIPWM_P1_Size_p
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P1_f;             /* Expression: BaseAddress
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_Size_k[2];     /* Computed Parameter: RTDACPCIPWM_P2_Size_k
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_g;             /* Expression: ChanIdx
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_Size_a[2];     /* Computed Parameter: RTDACPCIPWM_P3_Size_a
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_i;             /* Expression: ChanMode
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_Size_j[2];     /* Computed Parameter: RTDACPCIPWM_P4_Size_j
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_l;             /* Expression: ChanPresc
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_Size_h[2];     /* Computed Parameter: RTDACPCIPWM_P5_Size_h
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_c;             /* Expression: SetOutputsFlag
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_Size_k[2];     /* Computed Parameter: RTDACPCIPWM_P6_Size_k
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_h;             /* Expression: SetOutputsValue
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_Size_i[2];     /* Computed Parameter: RTDACPCIPWM_P7_Size_i
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_k;             /* Expression: T0
                                        * Referenced by: '<S6>/RT-DAC PCI PWM '
                                        */
  real_T Valve2_Value;                 /* Expression: 0
                                        * Referenced by: '<Root>/Valve 2'
                                        */
  real_T SaturationControlValve2_UpperSat;/* Expression: 1
                                           * Referenced by: '<S1>/Saturation Control Valve 2'
                                           */
  real_T SaturationControlValve2_LowerSat;/* Expression: 0
                                           * Referenced by: '<S1>/Saturation Control Valve 2'
                                           */
  real_T RTDACPCIPWM_P1_Size_g[2];     /* Computed Parameter: RTDACPCIPWM_P1_Size_g
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P1_d;             /* Expression: BaseAddress
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_Size_j[2];     /* Computed Parameter: RTDACPCIPWM_P2_Size_j
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_d;             /* Expression: ChanIdx
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_Size_o[2];     /* Computed Parameter: RTDACPCIPWM_P3_Size_o
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_g;             /* Expression: ChanMode
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_Size_g[2];     /* Computed Parameter: RTDACPCIPWM_P4_Size_g
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_d;             /* Expression: ChanPresc
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_Size_j[2];     /* Computed Parameter: RTDACPCIPWM_P5_Size_j
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_d;             /* Expression: SetOutputsFlag
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_Size_i4[2];    /* Computed Parameter: RTDACPCIPWM_P6_Size_i4
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_m;             /* Expression: SetOutputsValue
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_Size_b[2];     /* Computed Parameter: RTDACPCIPWM_P7_Size_b
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_f;             /* Expression: T0
                                        * Referenced by: '<S7>/RT-DAC PCI PWM '
                                        */
  real_T Valve3_Value;                 /* Expression: 0
                                        * Referenced by: '<Root>/Valve 3'
                                        */
  real_T SaturationControlValve3_UpperSat;/* Expression: 1
                                           * Referenced by: '<S1>/Saturation Control Valve 3'
                                           */
  real_T SaturationControlValve3_LowerSat;/* Expression: 0
                                           * Referenced by: '<S1>/Saturation Control Valve 3'
                                           */
  real_T RTDACPCIPWM_P1_Size_d[2];     /* Computed Parameter: RTDACPCIPWM_P1_Size_d
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P1_e;             /* Expression: BaseAddress
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_Size_g[2];     /* Computed Parameter: RTDACPCIPWM_P2_Size_g
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_l;             /* Expression: ChanIdx
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_Size_n[2];     /* Computed Parameter: RTDACPCIPWM_P3_Size_n
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_du;            /* Expression: ChanMode
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_Size_g2[2];    /* Computed Parameter: RTDACPCIPWM_P4_Size_g2
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_j;             /* Expression: ChanPresc
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_Size_g[2];     /* Computed Parameter: RTDACPCIPWM_P5_Size_g
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_k;             /* Expression: SetOutputsFlag
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_Size_io[2];    /* Computed Parameter: RTDACPCIPWM_P6_Size_io
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_c;             /* Expression: SetOutputsValue
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_Size_a[2];     /* Computed Parameter: RTDACPCIPWM_P7_Size_a
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_a;             /* Expression: T0
                                        * Referenced by: '<S8>/RT-DAC PCI PWM '
                                        */
  real_T Valve4_Value;                 /* Expression: 0
                                        * Referenced by: '<S1>/Valve 4'
                                        */
  real_T SaturationControlValve4_UpperSat;/* Expression: 1
                                           * Referenced by: '<S1>/Saturation Control Valve 4'
                                           */
  real_T SaturationControlValve4_LowerSat;/* Expression: 0
                                           * Referenced by: '<S1>/Saturation Control Valve 4'
                                           */
  real_T RTDACPCIPWM_P1_Size_i[2];     /* Computed Parameter: RTDACPCIPWM_P1_Size_i
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P1_g;             /* Expression: BaseAddress
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_Size_jl[2];    /* Computed Parameter: RTDACPCIPWM_P2_Size_jl
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P2_n;             /* Expression: ChanIdx
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_Size_nz[2];    /* Computed Parameter: RTDACPCIPWM_P3_Size_nz
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P3_b;             /* Expression: ChanMode
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_Size_b[2];     /* Computed Parameter: RTDACPCIPWM_P4_Size_b
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P4_f;             /* Expression: ChanPresc
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_Size_d[2];     /* Computed Parameter: RTDACPCIPWM_P5_Size_d
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P5_e;             /* Expression: SetOutputsFlag
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_Size_ig[2];    /* Computed Parameter: RTDACPCIPWM_P6_Size_ig
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P6_n;             /* Expression: SetOutputsValue
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_Size_ac[2];    /* Computed Parameter: RTDACPCIPWM_P7_Size_ac
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T RTDACPCIPWM_P7_h;             /* Expression: T0
                                        * Referenced by: '<S9>/RT-DAC PCI PWM '
                                        */
  real_T Valve5_Value;                 /* Expression: 0
                                        * Referenced by: '<S1>/Valve 5'
                                        */
  real_T SaturationControlValve5_UpperSat;/* Expression: 1
                                           * Referenced by: '<S1>/Saturation Control Valve 5'
                                           */
  real_T SaturationControlValve5_LowerSat;/* Expression: 0
                                           * Referenced by: '<S1>/Saturation Control Valve 5'
                                           */
};

/* Real-time Model Data Structure */
struct tag_RTM_wzor_01_T {
  const char_T *path;
  const char_T *modelName;
  struct SimStruct_tag * *childSfunctions;
  const char_T *errorStatus;
  SS_SimMode simMode;
  RTWExtModeInfo *extModeInfo;
  RTWSolverInfo solverInfo;
  RTWSolverInfo *solverInfoPtr;
  void *sfcnInfo;

  /*
   * NonInlinedSFcns:
   * The following substructure contains information regarding
   * non-inlined s-functions used in the model.
   */
  struct {
    RTWSfcnInfo sfcnInfo;
    time_T *taskTimePtrs[1];
    SimStruct childSFunctions[8];
    SimStruct *childSFunctionPtrs[8];
    struct _ssBlkInfo2 blkInfo2[8];
    struct _ssSFcnModelMethods2 methods2[8];
    struct _ssSFcnModelMethods3 methods3[8];
    struct _ssStatesInfo2 statesInfo2[8];
    struct {
      time_T sfcnPeriod[1];
      time_T sfcnOffset[1];
      int_T sfcnTsMap[1];
      struct _ssPortOutputs outputPortInfo[1];
      uint_T attribs[2];
      mxArray *params[2];
    } Sfcn0;

    struct {
      time_T sfcnPeriod[1];
      time_T sfcnOffset[1];
      int_T sfcnTsMap[1];
      struct _ssPortOutputs outputPortInfo[1];
      uint_T attribs[2];
      mxArray *params[2];
    } Sfcn1;

    struct {
      time_T sfcnPeriod[1];
      time_T sfcnOffset[1];
      int_T sfcnTsMap[1];
      struct _ssPortInputs inputPortInfo[1];
      real_T const *UPtrs0[1];
      uint_T attribs[7];
      mxArray *params[7];
    } Sfcn2;

    struct {
      time_T sfcnPeriod[1];
      time_T sfcnOffset[1];
      int_T sfcnTsMap[1];
      struct _ssPortInputs inputPortInfo[1];
      real_T const *UPtrs0[1];
      uint_T attribs[7];
      mxArray *params[7];
    } Sfcn3;

    struct {
      time_T sfcnPeriod[1];
      time_T sfcnOffset[1];
      int_T sfcnTsMap[1];
      struct _ssPortInputs inputPortInfo[1];
      real_T const *UPtrs0[1];
      uint_T attribs[7];
      mxArray *params[7];
    } Sfcn4;

    struct {
      time_T sfcnPeriod[1];
      time_T sfcnOffset[1];
      int_T sfcnTsMap[1];
      struct _ssPortInputs inputPortInfo[1];
      real_T const *UPtrs0[1];
      uint_T attribs[7];
      mxArray *params[7];
    } Sfcn5;

    struct {
      time_T sfcnPeriod[1];
      time_T sfcnOffset[1];
      int_T sfcnTsMap[1];
      struct _ssPortInputs inputPortInfo[1];
      real_T const *UPtrs0[1];
      uint_T attribs[7];
      mxArray *params[7];
    } Sfcn6;

    struct {
      time_T sfcnPeriod[1];
      time_T sfcnOffset[1];
      int_T sfcnTsMap[1];
      struct _ssPortInputs inputPortInfo[1];
      real_T const *UPtrs0[1];
      uint_T attribs[7];
      mxArray *params[7];
    } Sfcn7;
  } NonInlinedSFcns;

  /*
   * ModelData:
   * The following substructure contains information regarding
   * the data used in the model.
   */
  struct {
    void *blockIO;
    const void *constBlockIO;
    void *defaultParam;
    ZCSigState *prevZCSigState;
    real_T *contStates;
    int_T *periodicContStateIndices;
    real_T *periodicContStateRanges;
    real_T *derivs;
    void *zcSignalValues;
    void *inputs;
    void *outputs;
    boolean_T *contStateDisabled;
    boolean_T zCCacheNeedsReset;
    boolean_T derivCacheNeedsReset;
    boolean_T blkStateChange;
    void *dwork;
  } ModelData;

  /*
   * Sizes:
   * The following substructure contains sizes information
   * for many of the model attributes such as inputs, outputs,
   * dwork, sample times, etc.
   */
  struct {
    uint32_T checksums[4];
    uint32_T options;
    int_T numContStates;
    int_T numPeriodicContStates;
    int_T numU;
    int_T numY;
    int_T numSampTimes;
    int_T numBlocks;
    int_T numBlockIO;
    int_T numBlockPrms;
    int_T numDwork;
    int_T numSFcnPrms;
    int_T numSFcns;
    int_T numIports;
    int_T numOports;
    int_T numNonSampZCs;
    int_T sysDirFeedThru;
    int_T rtwGenSfcn;
  } Sizes;

  /*
   * SpecialInfo:
   * The following substructure contains special information
   * related to other components that are dependent on RTW.
   */
  struct {
    const void *mappingInfo;
    void *xpcData;
  } SpecialInfo;

  /*
   * Timing:
   * The following substructure contains information regarding
   * the timing information for the model.
   */
  struct {
    time_T stepSize;
    uint32_T clockTick0;
    uint32_T clockTickH0;
    time_T stepSize0;
    time_T tStart;
    time_T tFinal;
    time_T timeOfLastOutput;
    void *timingData;
    real_T *varNextHitTimesList;
    SimTimeStep simTimeStep;
    boolean_T stopRequestedFlag;
    time_T *sampleTimes;
    time_T *offsetTimes;
    int_T *sampleTimeTaskIDPtr;
    int_T *sampleHits;
    int_T *perTaskSampleHits;
    time_T *t;
    time_T sampleTimesArray[1];
    time_T offsetTimesArray[1];
    int_T sampleTimeTaskIDArray[1];
    int_T sampleHitArray[1];
    int_T perTaskSampleHitsArray[1];
    time_T tArray[1];
  } Timing;
};

/* Block parameters (auto storage) */
extern P_wzor_01_T wzor_01_P;

/* Block signals (auto storage) */
extern B_wzor_01_T wzor_01_B;

/* Block states (auto storage) */
extern DW_wzor_01_T wzor_01_DW;

/* Model entry point functions */
extern void wzor_01_initialize(void);
extern void wzor_01_output(void);
extern void wzor_01_update(void);
extern void wzor_01_terminate(void);

/*====================*
 * External functions *
 *====================*/
extern wzor_01_rtModel *wzor_01(void);
extern void MdlInitializeSizes(void);
extern void MdlInitializeSampleTimes(void);
extern void MdlInitialize(void);
extern void MdlStart(void);
extern void MdlOutputs(int_T tid);
extern void MdlUpdate(int_T tid);
extern void MdlTerminate(void);

/* Real-time Model object */
extern RT_MODEL_wzor_01_T *const wzor_01_M;

/*-
 * These blocks were eliminated from the model due to optimizations:
 *
 * Block '<S1>/Sum3' : Unused code path elimination
 * Block '<S1>/Sum4' : Unused code path elimination
 * Block '<S1>/Tank 4 Bias' : Unused code path elimination
 * Block '<S1>/Tank 4 Scale' : Unused code path elimination
 * Block '<S1>/Tank 5 Bias' : Unused code path elimination
 * Block '<S1>/Tank 5 Scale' : Unused code path elimination
 */

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'wzor_01'
 * '<S1>'   : 'wzor_01/Tank3'
 * '<S2>'   : 'wzor_01/Tank3/RT-DAC Frequencies'
 * '<S3>'   : 'wzor_01/Tank3/RT-DAC Safety Alert'
 * '<S4>'   : 'wzor_01/Tank3/RT-DAC PCI PWM Pump'
 * '<S5>'   : 'wzor_01/Tank3/RT-DAC PCI PWM Valve 1'
 * '<S6>'   : 'wzor_01/Tank3/RT-DAC PCI PWM Valve 2'
 * '<S7>'   : 'wzor_01/Tank3/RT-DAC PCI PWM Valve 3'
 * '<S8>'   : 'wzor_01/Tank3/RT-DAC PCI PWM Valve 4'
 * '<S9>'   : 'wzor_01/Tank3/RT-DAC PCI PWM Valve 5'
 */
#endif                                 /* RTW_HEADER_wzor_01_h_ */