
from .._interfaces import ITTSServer

class SampleTTSServer(ITTSServer):
    """ Sample TTS Server """

    def is_available(self) -> bool:
        return True
    
    def trans(self, text: str, **kwargs) -> str | bytes:
        return f"https;//example.com/tts/result/{text}.wav"
    
    async def trans_async(self, text: str, **kwargs) -> str | bytes:
        return f"https;//example.com/tts/result/{text}.wav"