import pygame.sprite

class Block(pygame.sprit.DirtySprite):
    def __init__(self,skin,position,health=100):
        super().__init__()
        self.position = position
        self.skin = skin
        self.health = health
    
    def draw(self):
        pass
