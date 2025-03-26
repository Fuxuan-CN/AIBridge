
from ._data_model import Message, StreamMessage, AsyncStreamMessage
from ._interfaces import IAIAdapter, ITTSServer
from .exceptions import TTSServerException

class AIBridge:
    """
    AI 桥接器
    """
    def __init__(self,
        adapter: type[IAIAdapter],
        tts_server: type[ITTSServer] | None = None,
        tts_kwargs: dict[str, str | int | None | float | bool] = {},
        **kwargs
    ) -> None:
        self.adapter = adapter(**kwargs)
        self.tts = tts_server(**tts_kwargs) if tts_server else None
        self.ai_reply: list[Message] = []

    def _cache_reply(self, message: Message) -> None:
        self.ai_reply.append(message)
        if len(self.ai_reply) > 100:
            self.ai_reply.pop(0)
    
    def send(self, message: str) -> Message:
        resp = self.adapter.send(message)
        self._cache_reply(resp)
        return resp
    
    def send_stream(self, message: str) -> StreamMessage:
        for chunk in self.adapter.send_stream(message):
            self._cache_reply(chunk)
            yield chunk
    
    async def send_async(self, message: str) -> Message:
        resp = await self.adapter.send_async(message)
        self._cache_reply(resp)
        return resp
    
    async def send_stream_async(self, message: str) -> AsyncStreamMessage:
        async for chunk in await self.adapter.send_stream_async(message):
            self._cache_reply(chunk)
            yield chunk
    
    def voice(self) -> str | bytes:
        if not self.tts:
            raise TTSServerException("TTS server is not available")
        if not self.tts.is_available():
            raise TTSServerException("TTS server is not available")
        return self.tts.trans(self.ai_reply[-1]['content'])
    
    async def voice_async(self) -> str | bytes:
        if not self.tts:
            raise TTSServerException("TTS server is not available")
        if not self.tts.is_available():
            raise TTSServerException("TTS server is not available")
        return await self.tts.trans_async(self.ai_reply[-1]['content'])
       