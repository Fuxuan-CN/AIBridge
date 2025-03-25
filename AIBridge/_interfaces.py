
from abc import ABC, abstractmethod
from ._data_model import Message , StreamMessage, AsyncStreamMessage

class IAIAdapter(ABC):
    """ AI适配器接口 """

    @abstractmethod
    def send(self, message: str) -> Message:
        """ 发送消息 """
        pass

    @abstractmethod
    def send_stream(self, message: str) -> StreamMessage:
        """ 发送流式消息 """
        pass

    @abstractmethod
    async def send_async(self, message: str) -> Message:
        """ 异步发送消息 """
        pass

    @abstractmethod
    async def send_stream_async(self, message: str) -> AsyncStreamMessage:
        """ 异步发送流式消息 """
        pass