from abc import ABC, abstractmethod
from BotDirective import BotDirective

class IDirectiveInterpretor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def interpret(self) -> BotDirective:
        """
        Poll event and interpret it into a BotDirective 
        """
        pass
