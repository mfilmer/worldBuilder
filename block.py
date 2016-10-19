import pygame

class Block(pygame.sprite.DirtySprite):
    def __init__(self,position,health=100):
        super().__init__()
        self.position = position
        self.health = health

class Wood(Block):
    skin = pygame.image.load('images/blocks/wood.png')
    def __init__(self,position):
        super().__init__(position)
        self.image = self.skin
        self.rect = self.image.get_rect(center=position)
