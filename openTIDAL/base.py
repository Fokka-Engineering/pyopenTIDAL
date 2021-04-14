from openTIDAL import lib, ffi, enums

class base(object):
    contentError = "OTContentContainer returned NULL."
    def cleanup (self, content):
        lib.OTDeallocContainer (content, enums.types.CONTENT_CONTAINER)

    def getStandard (self, session, prefix, suffix, contentId, limit, offset, threadHandle):
        if suffix == None:
            csuffix = ffi.NULL
        else:
            csuffix = suffix.encode('utf-8')

        content = lib.OTServiceGetStandard (session, prefix.encode('utf-8'), csuffix,
                                            contentId.encode('utf-8'), limit, offset, threadHandle)

        if content != ffi.NULL:
            return content
        else:
            raise Exception (contentError)
  
    def getPage (self, session, suffix, contentId, limit, offset, threadHandle):
        content = lib.OTServiceGetPage (session, suffix.encode('utf-8'), contentId.encode('utf-8'),
                                        limit, offset, threadHandle)
        if content != ffi.NULL:
            return content
        else:
            raise Exception (contentError)
