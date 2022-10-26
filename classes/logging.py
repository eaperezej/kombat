from typing import List


class GameLog:
    logs: List[str]

    def __init__(self) -> None:
        self.logs = []

    def info(self, message: str) -> None:
        self.logs.append(message)

    def trace(self) -> List[str]:
        return self.logs
