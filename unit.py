import pygame.sprite

class Unit(pygame.sprite.DirtySprite):
    def __init__(self,newSkin=None,health=100):
        super().__init__()
        self.setSkin(newSkin)
        self.health = health
    
    def deltamove(self,deltapos):
        dx,dy = deltapos
        self.rect.move_ip(dx,dy)
    
    def setAi(self,aiClass):
        self.ai = aiClass(self)
    
    def setSkin(self,newSkin):
        if newSkin is None:
            self.image = None
            self.rect = None
        else:
            self.image = newSkin
            self.rect = newSkin.get_rect()
