from abc import ABC, abstractmethod
from BotDirective import BotDirective

class IDirectiveInterpretor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def poll_directive(self) -> BotDirective:
        """
        Poll event and interpret it into a BotDirective 
        """
        pass
