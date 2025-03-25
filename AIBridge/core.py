
from ._data_model import Message, StreamMessage, AsyncStreamMessage
from ._interfaces import IAIAdapter

class AIBridge:
    """
    AI 桥接器
    """
    def __init__(self,
        adapter: type[IAIAdapter],
        **kwargs
    ) -> None:
        self.adapter = adapter(**kwargs)

    def send(self, message: str) -> Message:
        return self.adapter.send(message)
    
    def send_stream(self, message: str) -> StreamMessage:
        return self.adapter.send_stream(message)
    
    async def send_async(self, message: str) -> Message:
        return await self.adapter.send_async(message)
    
    async def send_stream_async(self, message: str) -> AsyncStreamMessage:
        return await self.adapter.send_stream_async(message)