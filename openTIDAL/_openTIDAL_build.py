from cffi import FFI
import glob
ffibuilder = FFI()

header_file = "openTIDAL/api.processed.h"
source_files = glob.glob("openTIDAL/Source/*.c")
source_files_service = glob.glob("openTIDAL/Source/OTService/*.c")

for i in source_files_service:
    source_files.append(i)

with open(header_file) as fh:
    header = fh.read()

ffibuilder.cdef(header)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("openTIDAL._openTIDAL",
r"""
     #include "api.h"
""",
    include_dirs=['openTIDAL'],
    sources=source_files,
    libraries=['curl'])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
