from openTIDAL import lib, ffi

class json (object):
    def getObjectItem (self, jsonContainer, string):
        element = lib.OTJsonGetObjectItem (jsonContainer, string.encode('utf-8'))
        return element

    def getArrayItem (self, jsonContainer, index):
        element = lib.OTJsonGetArrayItem (jsonContainer, index)
        return element

    def getArraySize (self, jsonContainer):
        value = lib.OTJsonGetArraySize (jsonContainer)
        return value 

    def hasObjectItem (self, jsonContainer, string):
        value = lib.OTJsonHasObjectItem (jsonContainer, string.encode('utf-8'))
        return value
   
    def getString (self, jsonContainer):
        cstring = lib.OTJsonGetStringValue (jsonContainer)
        if cstring != ffi.NULL:
            return ffi.string(cstring).decode('utf-8')
        else:
            return None

    def getObjectItemString (self, jsonContainer, string):
        cstring = lib.OTJsonGetObjectItemStringValue (jsonContainer, string.encode('utf-8'))
        if cstring != ffi.NULL:
            return ffi.string(cstring).decode('utf-8')
        else:
            return None

    def getNumber (self, jsonContainer):
        value = lib.OTJsonGetNumberValue (jsonContainer)
        return value 

    def getObjectItemNumber (self, jsonContainer, string):
        value = lib.OTJsonGetObjectItemNumberValue (jsonContainer, string.encode('utf-8'))
        return value 

    def isInvalid (self, jsonContainer):
        value = lib.OTJsonIsInvalid (jsonContainer)
        return bool(value)

    def isFalse (self, jsonContainer):
        value = lib.OTJsonIsFalse (jsonContainer)
        return bool(value)

    def isTrue (self, jsonContainer):
        value = lib.OTJsonIsTrue (jsonContainer)
        return bool(value)

    def isBool (self, jsonContainer):
        value = lib.OTJsonIsBool (jsonContainer)
        return bool(value)

    def isNull (self, jsonContainer):
        value = lib.OTJsonIsNull (jsonContainer)
        return bool(value)

    def isNumber (self, jsonContainer):
        value = lib.OTJsonIsNumber (jsonContainer)
        return bool(value)

    def isString (self, jsonContainer):
        value = lib.OTJsonIsString (jsonContainer)
        return bool(value)

    def isArray (self, jsonContainer):
        value = lib.OTJsonIsArray (jsonContainer)
        return bool(value)

    def isObject (self, jsonContainer):
        value = lib.OTJsonIsObject (jsonContainer)
        return bool(value)

    def isRaw (self, jsonContainer):
        value = lib.OTJsonIsRaw (jsonContainer)
        return bool(value)
