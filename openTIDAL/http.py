from openTIDAL import lib, ffi, enums

class http (object):
    def default (self):
            return ffi.NULL
    
    def new (self):
        handle = lib.OTHttpThreadHandleCreate ()
        if handle != ffi.NULL:
            return handle
        else:
            raise Exception ("Creating HTTP handle failed.")
    
    def cleanup (self, handle):
        lib.OTHttpThreadHandleCleanup (handle)
