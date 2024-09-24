import json
try:
    import cv2 as cv
except: print("error import cv2")
from BotDirective import BotDirective
from IBotConnector import IBotConnector
from IDirectiveInterpretor import IDirectiveInterpretor
from IloRobotConnector import IloRobotConnector
from MbotConnector import MbotConnector
from HandImageInterpretor import HandImageInterpretor
from KeyboardKeyInterpretor import KeyboardKeyInterpretor

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

    def create_instances(self, robot, control):
        """
        Cette fonction initialise les attributs bot_connector et directive_interpretor selon les paramètres robot et control.
        
        :param robot: chaîne de caractères variant entre "MBOT2" et "ILO Robot"
        :type robot: str
        :param control: chaîne de caractères variant entre "Hand" et "Keyboard"
        :type control: str
        """
        if robot == "ILO Robot": self.bot_connector = IloRobotConnector()
        else: self.bot_connector = MbotConnector()

        if control == "Keyboard": self.directive_interpretor = KeyboardKeyInterpretor()
        else:
            vcap = cv.VideoCapture(0)
            self.directive_interpretor = HandImageInterpretor(vcap, display_cap=True)

        return (robot, control)

    def config(self):
        """
        Cette fonction initialise les attributs bot_connector et directive_interpretor selon la configuration dans le fichier config.json.
        """
        file_path = "config.json"
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                robot = data.get("Robot")
                control = data.get("Control")
                
                if robot is None or control is None:
                    raise ValueError("Les clés 'Robot' et 'Control' sont obligatoires dans le fichier JSON.")
                
                robot_options = ["MBOT2", "ILO Robot"]
                control_options = ["Hand", "Keyboard"]
                
                robot = next((r for r in robot_options if r.lower() == robot.lower()), None)
                control = next((c for c in control_options if c.lower() == control.lower()), None)
                
                if robot is None:
                    raise ValueError("La valeur pour 'Robot' dans le fichier JSON n'est pas valide.")
                if control is None:
                    raise ValueError("La valeur pour 'Control' dans le fichier JSON n'est pas valide.")
                
                self.create_instances(robot, control)
                return (True)
        except FileNotFoundError:
            print("Le fichier spécifié n'a pas été trouvé.")
        except json.JSONDecodeError:
            print("Le fichier spécifié n'est pas au format JSON valide.")
        except ValueError as e:
            print(e)
        return None

    def loop(self):
        current_directive = self.directive_interpretor.poll_directive()
        self.bot_connector.send_directive(current_directive)

    def main(self, argv):
        self.config()
        self.bot_connector.connect()
        while True:
            try:
                self.loop()
            except KeyboardInterrupt:
                break
        self.bot_connector.disconnect()
        return 0
