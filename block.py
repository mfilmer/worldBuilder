import pygame

class Block(pygame.sprite.DirtySprite):
    def __init__(self,position,health=100):
        super().__init__()
        self.image = self.skin
        self.rect = self.image.get_rect(center=position)
        self.position = position
        self.health = health

class Wood(Block):
    skin = pygame.image.load('images/blocks/wood.png')

class Stone(Block):
    skin = pygame.image.load('images/blocks/stone.png')

class Dirt(Block):
    skin = pygame.image.load('images/blocks/dirt.png')
