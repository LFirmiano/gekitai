import pygame
import pygame_menu
from game.start_server import Server
from game.create_player import Client

class Interface:
    def __init__(self):
        # self.start_server()
        self.create_surface()

    def start_server(self):
        Server()

    def create_player(self):
        Client()

    def create_surface(self):
        pygame.init()
        surface = pygame.display.set_mode((600, 400))

        menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

        menu.add.button('New Player', self.create_player)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(surface)

    def set_difficulty(self, value, difficulty):
        print(value)
        # Do the job here !
        pass

    def start_the_game(self):
        print("jonas")
        # Do the job here !
        pass