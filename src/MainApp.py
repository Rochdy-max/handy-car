import sys
import cv2 as cv
from BotDirective import BotDirective
from IBotConnector import IBotConnector
from IDirectiveInterpretor import IDirectiveInterpretor
from IloRobotConnector import IloRobotConnector
from HandImageInterpretor import HandImageInterpretor

class MainAppMeta(type):
    _instances = dict()

    def __new__(mcls, *args, **kwargs):
        cls = super().__new__(mcls, *args, **kwargs)

        def new(cls):
            if cls not in mcls._instances:
                inst = object.__new__(cls)
                mcls._instances[cls] = inst
            return mcls._instances[cls]
        
        cls.__new__ = new
        return cls

class MainApp(metaclass=MainAppMeta):
    @property
    def bot_connector(self):
        return self._bot_connector

    @bot_connector.setter
    def bot_connector(self, value):
        if not isinstance(value, IBotConnector):
            raise AttributeError("value is not an instance of valid type: %s" % IBotConnector.__name__)
        self._bot_connector = value

    @property
    def directive_interpretor(self):
        return self._directive_interpretor

    @directive_interpretor.setter
    def directive_interpretor(self, value):
        if not isinstance(value, IDirectiveInterpretor):
            raise AttributeError("value is not an instance of valid type: %s" % IDirectiveInterpretor.__name__)
        self._directive_interpretor = value

    def config(self):
        pass

    def loop(self):
        current_directive = self.directive_interpretor.poll_directive()
        self.bot_connector.send_directive(current_directive)

    def main(self, argv):
        self.bot_connector = IloRobotConnector()
        vcap = cv.VideoCapture(0)
        self.directive_interpretor = HandImageInterpretor(vcap, display_cap=True)
        self.config()
        while True:
            try:
                self.loop()
            except KeyboardInterrupt:
                break
        return 0

if __name__ == "__main__":
    app = MainApp()
    sys.exit(app.main(sys.argv))
