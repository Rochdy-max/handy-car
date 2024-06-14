from BotDirective import BotDirective
from IDirectiveInterpretor import IDirectiveInterpretor
from time import time
from pynput import keyboard

class KeyboardController:
    def __init__(self):
        self.current_dir = BotDirective.NOTHING
    
    def on_press(self, key):
        if key == keyboard.Key.up:
            self.current_dir = BotDirective.GO_FORWARD
        if key == keyboard.Key.down:
            self.current_dir = BotDirective.GO_BACKWARD
        if key == keyboard.Key.left:
            self.current_dir = BotDirective.TURN_LEFT
        if key == keyboard.Key.right:
            self.current_dir = BotDirective.TURN_RIGHT

    def on_release(self, key):
        if key == keyboard.Key.up:
            self.current_dir = BotDirective.NOTHING
        if key == keyboard.Key.down:
            self.current_dir = BotDirective.NOTHING
        if key == keyboard.Key.left:
            self.current_dir = BotDirective.NOTHING
        if key == keyboard.Key.right:
            self.current_dir = BotDirective.NOTHING


@IDirectiveInterpretor.register
class KeyboardKeyInterpretor(IDirectiveInterpretor):
    def __init__(self):
        self.controller = KeyboardController()
        self.listener = keyboard.Listener(
            on_press=self.controller.on_press,
            on_release=self.controller.on_release)
        self.listener.start()

    def poll_directive(self) -> BotDirective:
        if self.listener.is_alive():
            return self.controller.current_dir
