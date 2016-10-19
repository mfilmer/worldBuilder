import pygame.sprite

class Unit(pygame.sprite.DirtySprite):
    def __init__(self,newSkin=None,health=100):
        super().__init__()
        self.setSkin(newSkin)
        self.health = health
    
    def draw(self):
        # Only need to draw if there is actually a skin
        if skin is not None:
            pass
    
    def setSkin(self,newSkin):
        if newSkin is None:
            self.image = None
            self.rect = None
        else:
            self.image = newSkin
            self.rect = newSkin.get_rect()
