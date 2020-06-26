/*
 * sbs_custom_hardware.h
 *
 *  Created on: Jun 2nd, 2020
 *      Author: Yarib Nevarez
 */
#ifndef SBS_CUSTOM_HARDWARE_H_
#define SBS_CUSTOM_HARDWARE_H_

#ifdef XSBS_ACCELERATOR_64

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Include Files *********************************/
#include "sbs_hardware.h"
#include "xsbs_accelerator_64.h"
/***************** Macros (Inline Functions) Definitions *********************/

/**************************** Type Definitions *******************************/

/************************** Constant Definitions *****************************/

/************************** Variable Definitions *****************************/

/************************** Function Prototypes ******************************/

extern SbsHardware SbsHardware_custom;

#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif

#endif /* SBS_CUSTOM_HARDWARE_H_ */
