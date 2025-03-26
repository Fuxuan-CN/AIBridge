
from abc import ABC, abstractmethod
from ._data_model import Message , StreamMessage, AsyncStreamMessage

class ITTSServer(ABC):
    """ 文本转语音服务器接口 """

    @abstractmethod
    def is_available(self) -> bool:
        """ 检查服务器是否可用 """
        pass

    @abstractmethod
    def trans(self, text: str | None, **kwargs) -> str | bytes:
        """ 文本转语音 """
        pass

    @abstractmethod
    async def trans_async(self, text: str | None, **kwargs) -> str | bytes:
        """ 异步文本转语音 """
        pass

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

    @abstractmethod
    def voice(self) -> str | bytes:
        """ 获取当前语音 """
        pass

    @abstractmethod
    async def voice_async(self) -> str | bytes:
        """ 异步获取当前语音 """
        pass
