from abc import ABC, abstractmethod
from BotDirective import BotDirective

class IBotConnector(ABC):
    def __init__(self):
        self.current_directive = None

    @abstractmethod
    def connect(self):
        """
        Connect to the bot
        """
        pass
    
    @abstractmethod
    def disconnect(self):
        """
        Disconnect from the bot
        """
        pass
    
    @abstractmethod
    def send_directive(self):
        """
        Send a directive to the bot
        """
        pass
    
    @abstractmethod
    def get_state(self):
        """
        Get state info (any sensor or camera output) from the bot
        """
        pass
