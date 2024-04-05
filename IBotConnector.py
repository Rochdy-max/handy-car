from BotDirective import BotDirective

class IBotConnector:
    def __init__(self):
        self.current_directive = None
        
    def connect(self):
        pass
    
    def disconnect(self):
        pass
    
    def send_directive(self):
        pass
    
    def get_state(self):
        pass

