/*
 * sbs_hardware_spike.c
 *
 *  Created on: Mar 3rd, 2020
 *      Author: Yarib Nevarez
 */
/***************************** Include Files *********************************/
#include "sbs_hardware_spike.h"
#include "stdlib.h"
#include "miscellaneous.h"
/***************** Macros (Inline Functions) Definitions *********************/

/**************************** Type Definitions *******************************/

/************************** Constant Definitions *****************************/

/************************** Variable Definitions *****************************/
static void * SbsHardware_fixedpoint_spike_new (void)
{
  return malloc (sizeof(XSbs_spike_unit));
}

static void SbsHardware_fixedpoint_spike_delete (void ** InstancePtr)
{
  if (InstancePtr && *InstancePtr)
  {
    free (*InstancePtr);
    *InstancePtr = NULL;
  }
}

static uint32_t  SbsHardware_fixedpoint_spike_InterruptSetHandler (void *instance,
                                                                   uint32_t ID,
                                                                   ARM_GIC_InterruptHandler handler,
                                                                   void * data)
{
  uint32_t status = ARM_GIC_connect (ID, handler, data);
  ASSERT (status == XST_SUCCESS);
  return status;
}

SbsHardware SbsHardware_fixedpoint_spike = {
  .new = SbsHardware_fixedpoint_spike_new,
  .delete = SbsHardware_fixedpoint_spike_delete,
  .Initialize = (int (*)(void *, u16)) XSbs_spike_unit_Initialize,

  .Start = (void (*)(void *)) XSbs_spike_unit_Start,
  .IsDone = (uint32_t(*)(void *)) XSbs_spike_unit_IsDone,
  .IsIdle = (uint32_t(*) (void *)) XSbs_spike_unit_IsIdle,
  .IsReady = (uint32_t(*) (void *)) XSbs_spike_unit_IsReady,
  .EnableAutoRestart = (void (*) (void *)) XSbs_spike_unit_EnableAutoRestart,
  .DisableAutoRestart = (void (*) (void *)) XSbs_spike_unit_DisableAutoRestart,
  .Get_return =         (uint32_t(*) (void *))  NULL,

  .Set_mode = (void (*) (void *, uint32_t )) NULL,
  .Get_mode = (uint32_t(*) (void *)) NULL,
  .Set_layerSize = (void (*) (void *, uint32_t )) XSbs_spike_unit_Set_layerSize,
  .Get_layerSize = (uint32_t(*) (void *)) XSbs_spike_unit_Get_layerSize,
  .Set_kernelSize = (void (*) (void *, uint32_t )) NULL,
  .Get_kernelSize = (uint32_t(*) (void *)) NULL,
  .Set_vectorSize = (void (*) (void *, uint32_t )) XSbs_spike_unit_Set_vectorSize,
  .Get_vectorSize = (uint32_t(*) (void *)) XSbs_spike_unit_Get_vectorSize,
  .Set_epsilon = (void (*) (void *, uint32_t )) NULL,
  .Get_epsilon = (uint32_t(*) (void *)) NULL,
  .Set_debug = (void (*) (void *, uint32_t )) NULL,
  .Get_debug = (uint32_t(*) (void *)) XSbs_spike_unit_Get_debug,

  .InterruptGlobalEnable = (void (*) (void *)) XSbs_spike_unit_InterruptGlobalEnable,
  .InterruptGlobalDisable = (void (*) (void *)) XSbs_spike_unit_InterruptGlobalDisable,
  .InterruptEnable = (void (*) (void *, uint32_t )) XSbs_spike_unit_InterruptEnable,
  .InterruptDisable = (void (*) (void *, uint32_t )) XSbs_spike_unit_InterruptDisable,
  .InterruptClear = (void (*) (void *, uint32_t )) XSbs_spike_unit_InterruptClear,
  .InterruptGetEnabled = (uint32_t(*) (void *)) XSbs_spike_unit_InterruptGetEnabled,
  .InterruptGetStatus = (uint32_t(*) (void *)) XSbs_spike_unit_InterruptGetStatus,

  .InterruptSetHandler = SbsHardware_fixedpoint_spike_InterruptSetHandler
};
/************************** Function Prototypes ******************************/

/************************** Function Definitions******************************/

