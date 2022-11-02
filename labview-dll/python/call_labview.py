"""
This module demonstrates calling a basic LabVIEW DLL function using CFFI.

This uses the ABI mode, in-line for simplicity to demonstrate the possibilities.

There is no practical reason the other modes can't work - this is just the easiest for a demo.
"""

from cffi import FFI

ffi = FFI()
ffi.cdef("""
    void Say_hello(char name[], char output[], int32_t output_len);
""")
module = ffi.dlopen("bin/LVFunctions.dll")
name = ffi.new("char[]", b"NI Connect")

OUTPUT_SIZE = 255
output = ffi.new("char[]",OUTPUT_SIZE)
module.Say_hello(name, output, OUTPUT_SIZE)

#marshal output
output_bytes = ffi.string(output)
print(output_bytes.decode("ascii"))
