#include "extcode.h"
#ifdef __cplusplus
extern "C" {
#endif

/*!
 * Say_hello
 */
void __cdecl Say_hello(char name[], char output[], int32_t output_len);

MgErr __cdecl LVDLLStatus(char *errStr, int errStrLen, void *module);

void __cdecl SetExecuteVIsInPrivateExecutionSystem(Bool32 value);

#ifdef __cplusplus
} // extern "C"
#endif

