from BotDirective import BotDirective
from IBotConnector import IBotConnector

@IBotConnector.register
class IloRobotConnector(IBotConnector):
    def __init__(self):
        pass

    def connect(self) -> bool:
        pass
    
    def disconnect(self) -> bool:
        pass
    
    def send_directive(self, directive: BotDirective) -> bool:
        match directive:
            case BotDirective.GO_FORWARD:
                print("Go Forward")
            case BotDirective.GO_BACKWARD:
                print("Go Backward")
            case BotDirective.TURN_LEFT:
                print("Turn Left")
            case BotDirective.TURN_RIGHT:
                print("Turn Right")
            case BotDirective.STOP:
                print("Stop")
        return True
    
    def get_state(self):
        pass
