import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, name, model):
        super().__init__()


        # i have this idea to load the image based on the model such as model.png is the name of the model selected matching
        # the .png picture
        self.image = pygame.image.load( "resources/images/" + model + ".png").convert_alpha()
        self.rect = self.image.get_rect()