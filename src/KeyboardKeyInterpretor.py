from BotDirective import BotDirective
from IDirectiveInterpretor import IDirectiveInterpretor
from time import time
from pynput import keyboard


class KeyboardController:
    """
    Cette classe nous permet de lire les touches du clavier qui ont été touchés, particulièrement les touches directives haut, bas, gauche et droite.

    :ivar current_dir: Le premier nombre.
    :type current_dir: BotDirective
    """
    def __init__(self):
        self.current_dir = BotDirective.NOTHING
    
    def on_press(self, key):
        """
        Cette fonction change la valeur de current_dir selon la touche du clavier qui a été ou qui est pressée.

        :param key: La touche du clavier pressée.
        """
        if key == keyboard.Key.up:
            self.current_dir = BotDirective.GO_FORWARD
        if key == keyboard.Key.down:
            self.current_dir = BotDirective.GO_BACKWARD
        if key == keyboard.Key.left:
            self.current_dir = BotDirective.TURN_LEFT
        if key == keyboard.Key.right:
            self.current_dir = BotDirective.TURN_RIGHT

    def on_release(self, key):
        """
        Cette fonction change la valeur de current_dir à BotDirective.NOTHING si l'une des touches directionnelles a été lachée.

        :param key: La touche du clavier lachée.
        """
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
    """
    Cette classe nous permet d'envoyer les directives au robot.

    :ivar controller: La classe nous permettant de lire les touches du clavier. 
    :type controller: KeyboardController
    :ivar listener:
    :type listener:
    """
    def __init__(self):
        self.controller = KeyboardController()
        self.listener = keyboard.Listener(
            on_press=self.controller.on_press,
            on_release=self.controller.on_release)
        self.listener.start()

    def poll_directive(self) -> BotDirective:
        """
        Cette fonction nous permet d'envoyer les directives au robot.
        
        :return: La direction que prendra le robot.
        :rtype: BotDirective
        """
        if self.listener.is_alive():
            return self.controller.current_dir
