import pygame

class Block(pygame.sprite.DirtySprite):
    defaultHealing = 0
    maxHealth = 100
    def __init__(self,position,health=100):
        super().__init__()
        self.rect = self.image.get_rect(center=position)
        self.position = position
        self.currentHealth = self.maxHealth

class Wood(Block):
    image = pygame.image.load('images/blocks/wood.png')
    maxHealth = 100

class Stone(Block):
    image = pygame.image.load('images/blocks/stone.png')
    maxHealth = 500

class Dirt(Block):
    image = pygame.image.load('images/blocks/dirt.png')
    maxHealth = 50
    defaultHealing = 1
