from BotDirective import BotDirective
from IBotConnector import IBotConnector

@IBotConnector.register
class IloRobotConnector:
    def __init__(self):
        pass

    def connect(self):
        pass
    
    def disconnect(self):
        pass
    
    def send_directive(self):
        pass
    
    def get_state(self):
        pass
