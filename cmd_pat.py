from abc import ABC, abstractmethod
from dataclasses import dataclass

class Command(ABC):
    @abstractmethod
    def do(self):
        ...
    @abstractmethod
    def undo(self):
        ...