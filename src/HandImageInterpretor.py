from BotDirective import BotDirective
from IDirectiveInterpretor import IDirectiveInterpretor
import cv2
from cvzone.HandTrackingModule import HandDetector

@IDirectiveInterpretor.register
class HandImageInterpretor:
    def __init__(self):
        pass

    def get_image(self):
        pass

    def interpret(self) -> BotDirective:
        pass

print(cv2.__version__)
