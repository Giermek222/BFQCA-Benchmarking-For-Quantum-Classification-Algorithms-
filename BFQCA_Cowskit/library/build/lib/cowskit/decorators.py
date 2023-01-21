from typing import Any

class BasicDecorator:
    def __init__(self, *args: Any, **kwds: Any) -> None:
        pass
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

class VirtualHandle(BasicDecorator):
    pass

class MustCallSuper(BasicDecorator):
    pass