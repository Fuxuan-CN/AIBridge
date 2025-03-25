
from typing import (Literal,
    Any, 
    TypedDict, 
    Generator,
    AsyncGenerator,
    Optional,
)

class Message(TypedDict):
    """ 模型响应的消息 """
    role: Literal['user', 'assistant', 'system', 'tool']
    content: Optional[Any]

class StreamMsgChunk(TypedDict):
    """ 用于分割消息流的消息块 """
    role: Literal['user', 'assistant', 'system', 'tool']
    content: Optional[Any]
    is_end: bool

StreamMessage = Generator[StreamMsgChunk]
""" 模型响应的消息流 """

AsyncStreamMessage = AsyncGenerator[StreamMsgChunk]
""" 异步模型响应的消息流 """