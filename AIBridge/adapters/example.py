
import asyncio
from .._data_model import Message, StreamMessage, AsyncStreamMessage, StreamMsgChunk
from .._interfaces import IAIAdapter

class SimpleAIAdapter(IAIAdapter):
    """ 简单的 AI 适配器实现 """

    def send(self, message: str) -> Message:
        """ 同步发送消息 """
        response: Message = {
            "role": "assistant",
            "content": f"{message}"
        }
        return response

    def send_stream(self, message: str) -> StreamMessage:
        """ 同步发送流式消息 """
        def stream_generator():
            for i in range(len(message)):
                chunk: StreamMsgChunk = {
                    "role": "assistant",
                    "content": f"{message[i]}",
                    "is_end": i == len(message) - 1
                }
                yield chunk
        return stream_generator()

    async def send_async(self, message: str) -> Message:
        """ 异步发送消息 """
        await asyncio.sleep(1)  # 模拟异步处理
        response: Message = {
            "role": "assistant",
            "content": f"Received: {message}"
        }
        return response

    async def send_stream_async(self, message: str) -> AsyncStreamMessage:
        """ 异步发送流式消息 """
        async def async_stream_generator():
            for i in range(len(message)):
                await asyncio.sleep(1)  # 模拟异步处理
                chunk: StreamMsgChunk = {
                    "role": "assistant",
                    "content": f"{message[i]}",
                    "is_end": i == len(message) - 1
                }
                yield chunk
        return async_stream_generator()