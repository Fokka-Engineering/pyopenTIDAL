from openTIDAL import lib, ffi, enums

class auth(object):
    contentError = "OTContentContainer returned NULL."
    def __return (self, content):
        if content != ffi.NULL:
            return content
        else:
            raise Exception (contentError)
    
    def cleanup (self, content):
        lib.OTDeallocContainer (content, enums.types.CONTENT_CONTAINER)

    def getDeviceCode (self, session, threadHandle):
        content = lib.OTServiceGetDeviceCode (session, threadHandle)
        return self.__return (content)

    def getBearerToken (self, session, deviceCode, threadHandle):
        content = lib.OTServiceGetBearerToken (session, deviceCode.encode('utf-8'), threadHandle)
        return self.__return (content)

    def logout (self, session, threadHandle):
        status = lib.OTServiceLogout (session, threadHandle)
        return status

    def refreshBearerToken (self, session, refreshToken, threadHandle):
        content = lib.OTServiceRefreshBearerToken (session, refreshToken.encode('utf-8'), threadHandle)
        return self.__return (content)
