from openTIDAL import lib, ffi

class session (object):
    def __init__ (self):
        self.handle = lib.OTSessionInit()
        if self.handle == ffi.NULL:
            raise Exception ("Initialising OTSessionContainer failed. Heap allocation error.")
    
    def getHandle (self):
        return self.handle

    def login (self, location):
        status = lib.OTSessionLogin (self.handle, location.encode('utf-8'))
        if status == -1:
            raise Exception ("Parsing openTIDAL configuration file failed.")

    def clientPair (self, clientId, clientSecret):
        status = lib.OTSessionClientPair (self.handle, clientId.encode('utf-8'), clientSecret.encode('utf-8'))
        if status == -1:
            raise Exception ("Allocating clientPair failed.")
    
    def verbose (self, enabled):
        lib.OTSessionVerbose (self.handle, enabled)

    def changeQuality (self, quality):
        lib.OTSessionChangeQuality (self.handle, quality)
    
    def writeChanges (self):
        status = lib.OTSessionWriteChanges (self.handle)
        if status == -1:
            raise Exception ("Updating openTIDAL configuration file failed.")
    
    def manualRefresh (self):
        lib.OTSessionRefresh (self.handle)
    
    def createConfig (self, location):
        status = lib.OTPersistentCreate (self, location.encode('utf-8'))
        if status == -1:
            raise Exception ("Creating openTIDAL configuration file failed")

    def cleanup (self):
        lib.OTSessionCleanup (self.handle)
