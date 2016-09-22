import xbmc
import xbmcaddon  
    
def to_utf8(text):
    result = text
    if isinstance(text, unicode):
        result = text.encode('utf-8')
        pass

    return result

def to_unicode(text):
    result = text
    if isinstance(text, str):
        result = text.decode('utf-8')
        pass

    return result

def show_notification(message, header='', image_uri='', time_milliseconds=5000):

    __addon__ = xbmcaddon.Addon()

    _header = header
    if not _header:
        _header = __addon__.getAddonInfo('name')
        pass
    _header = to_utf8(_header)

    _image = image_uri
    if not _image:
        _image = __addon__.getAddonInfo('icon')
        pass

    _message = to_unicode(message)
    _message = _message.replace(',', ' ')
    _message = to_utf8(_message)
    _message = _message.replace('\n', ' ')

    xbmc.executebuiltin(
        "Notification(%s, %s, %d, %s)" % (_header, _message, time_milliseconds, _image))
    pass