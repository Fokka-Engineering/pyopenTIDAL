from openTIDAL import lib, ffi, enums

class search (object):
    contentError = "OTContentContainer returned NULL."
    def cleanup (self, content):
        lib.OTDeallocContainer (content, enums.types.CONTENT_CONTAINER)
    
    def __standard (self, session, suffix, query, limit, offset, threadHandle):
        content = lib.OTServiceSearch (session, suffix, query,
                                       limit, offset, threadHandle)
        if content != ffi.NULL:
            return content
        else:
            raise Exception (contentError) 

    def all (self, session, query, limit, offset, threadHandle):
        return self.__standard (session, ffi.NULL, query.encode('utf-8'),
                                   limit, offset, threadHandle)

    def albums (self, session, query, limit, offset, threadHandle):
        return self.__standard (session, 'albums'.encode('utf-8'), query.encode('utf-8'),
                                   limit, offset, threadHandle)

    def tracks (self, session, query, limit, offset, threadHandle):
        return self.__standard (session, 'tracks'.encode('utf-8'), query.encode('utf-8'),
                                   limit, offset, threadHandle)

    def videos (self, session, query, limit, offset, threadHandle):
        return self.__standard (session, 'videos'.encode('utf-8'), query.encode('utf-8'),
                                   limit, offset, threadHandle)

    def artists (self, session, query, limit, offset, threadHandle):
        return self.__standard (session, 'artists'.encode('utf-8'), query.encode('utf-8'),
                                   limit, offset, threadHandle)

    def playlists (self, session, query, limit, offset, threadHandle):
        return self.__standard (session, 'playlists'.encode('utf-8'), query.encode('utf-8'),
                                   limit, offset, threadHandle)

    def topHit (self, session, query, limit, offset, threadHandle):
        return self.__standard (session, 'top-hits'.encode('utf-8'), query.encode('utf-8'),
                                   limit, offset, threadHandle)
