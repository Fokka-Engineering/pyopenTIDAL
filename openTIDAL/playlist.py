from openTIDAL import lib, ffi, enums

class playlist(object):
    contentError = "OTContentContainer returned NULL."
    def cleanup (self, content):
        lib.OTDeallocContainer (content, enums.types.CONTENT_CONTAINER)

    def create (self, session, title, description, threadHandle):
        content = lib.OTServiceCreatePlaylist (session, title.encode('utf-8'), description.encode('utf-8'),
                                               threadHandle)
        if content != ffi.NULL:
            return content
        else:
            raise Exception (self.contentError)

    def deleteItem (self, session, contentId, index, threadHandle):
        status = lib.OTServiceDeletePlaylistItem (session, contentId.encode('utf-8'), index, threadHandle)
        return status

    def moveItem (self, session, contentId, index, toIndex, threadHandle):
        status = lib.OTServiceMovePlaylistItem (session, contentId.encode('utf-8'), index, toIndex,
                                                threadHandle)
        return status

    def addItem (self, session, contentId, itemId, onArtifactNotFound, onDupes, threadHandle):
        status = lib.OTServiceAddPlaylistItem (session, contentId.encode('utf-8'), itemId.encode('utf-8'),
                                               onArtifactNotFound.encode('utf-8'), onDupes.encode('utf-8'),
                                               threadHandle)
        return status
    
    def addItems (self, session, contentId, itemIds, onArtifactNotFound, onDupes, threadHandle):
        carray = []
        for artefact in itemIds:
            carray.append(ffi.new("char []", artefact.encode('utf-8')))
        status = lib.OTServiceAddPlaylistItems (session, contentId.encode('utf-8'), carray, len(carray),
                                                onArtifactNotFound.encode('utf-8'), onDupes.encode('utf-8'),
                                                threadHandle)
        return status
