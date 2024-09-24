from BotDirective import BotDirective
from IBotConnector import IBotConnector

@IBotConnector.register
class MbotConnector(IBotConnector):
    _move_speed = 50
    _stop_speed = 0

    def __init__(self):
        pass

    def connect(self):
        import cyberpi
        self.cyberpi = cyberpi
    
    def disconnect(self):
        # Disconnect
        self.cyberpi.stop_all()
    
    def send_directive(self, directive):
        match directive:
            case BotDirective.NOTHING:
                # Nothing to do
                pass
            case BotDirective.GO_FORWARD:
                # Go Forward
                self.cyberpi.mbot2.forward(speed=self._move_speed)
            case BotDirective.GO_BACKWARD:
                # Go Backward
                self.cyberpi.mbot2.backward(speed=self._move_speed)
            case BotDirective.TURN_LEFT:
                # Turn Left
                self.cyberpi.mbot2.turn_left(speed=self._move_speed)
            case BotDirective.TURN_RIGHT:
                # Turn Right
                self.cyberpi.mbot2.turn_right(speed=self._move_speed)
            case BotDirective.STOP:
                # No movement
                self.cyberpi.mbot2.forward(speed=self._stop_speed)
    
    def get_state(self):
        pass
