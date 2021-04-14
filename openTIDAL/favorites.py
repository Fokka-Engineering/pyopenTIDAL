from openTIDAL import lib, ffi, enums

class favorites(object):
    contentError = "OTContentContainer returned NULL."
    def cleanup (self, content):
        lib.OTDeallocContainer (content, enums.types.CONTENT_CONTAINER)

    def get (self, session, suffix, limit, offset, order, orderDirection, threadHandle):
        content = lib.OTServiceGetFavorites (session, suffix.encode('utf-8'), limit, offset,
                                             order.encode('utf-8'), orderDirection.encode('utf-8'),
                                             threadHandle)
        if content != ffi.NULL:
            return content
        else:
            raise Exception (self.contentError)
   
    def deleteItem (self, session, suffix, itemId, threadHandle):
        status = lib.OTServiceDeleteFavorite (session, suffix.encode('utf-8'), itemId.encode('utf-8'),
                                              threadHandle)
        return status

    def addItem (self, session, suffix, itemId, onArtifactNotFound, threadHandle):
        status = lib.OTServiceAddFavorite (session, suffix.encode('utf-8'), itemId.encode('utf-8'),
                                           onArtifactNotFound.encode('utf-8'), threadHandle)
        return status

    def addItems (self, session, suffix, itemIds, onArtifactNotFound, threadHandle):
        carray = []
        for artefact in itemIds:
            carray.append(ffi.new("char []", artefact.encode('utf-8')))
        status = lib.OTServiceAddFavorites (session, suffix.encode('utf-8'), carray, len(carray),
                                            onArtifactNotFound.encode('utf-8'), threadHandle)
        return status
