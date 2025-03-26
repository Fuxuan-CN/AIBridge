

class AIBridgeException(Exception):
    """ Base class for all AIBridge exceptions. """
    pass

class TTSServerException(AIBridgeException):
    """ Raised when there is an error with the TTS server. """
    pass