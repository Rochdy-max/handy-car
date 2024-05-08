from abc import ABC, abstractmethod
from BotDirective import BotDirective

class IBotConnector(ABC):
    def __init__(self):
        self.current_directive = None

    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def send_directive(self):
        pass
    
    @abstractmethod
    def get_state(self):
        pass
