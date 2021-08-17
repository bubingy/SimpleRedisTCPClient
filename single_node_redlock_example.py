# coding=utf-8

from typing import Any
from RedisTCPClient import RedisTCPClient

class SingleNodeRedlock:
    def __init__(self, host: str, port: int) -> None:
        self.session = RedisTCPClient(host, int(port))

    def accquire(self, key: str, value: Any, expire: int) -> None:
        # TODO
        result = self.session.run_command(
            f'SET {key} {value} NX PX {expire}'
        )

    def release(self, key: str, value: Any) -> None:
        # TODO
        pass