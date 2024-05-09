import sys
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
    def __init__(self) -> None:
        self.bot_connector = None
        self.directive_interpretor = None

    def main(self, argv):
        return 0

    def config(self):
        pass

    def loop(self):
        pass

if __name__ == "__main__":
    app = MainApp()
    sys.exit(app.main(sys.argv))
