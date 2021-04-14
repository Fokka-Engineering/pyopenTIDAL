from openTIDAL import lib, ffi, enums

class stream (object):
    contentError = "OTContentContainer returned NULL."
    def cleanup (self, content):
        lib.OTDeallocContainer (content, enums.types.CONTENT_STREAM_CONTAINER)

    def getTrackStream (self, session, contentId, isPreview, threadHandle):
        content = lib.OTServiceGetStream (session, 'tracks'.encode('utf-8'), contentId.encode('utf-8'),
                                          isPreview, threadHandle)
        if content != ffi.NULL:
            return content
        else:
            raise Exception (self.contentError)

    def getVideoStream (self, session, contentId, isPreview, threadHandle):
        content = lib.OTServiceGetStream (session, 'videos'.encode('utf-8'), contentId.encode('utf-8'),
                                          isPreview, threadHandle)
        if content != ffi.NULL:
            return content
        else:
            raise Exception (self.contentError)
