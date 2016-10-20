from abc import ABCMeta, abstractmethod
import random

class Ai(object):
    __metaclass__ = ABCMeta
    def __init__(self,unit):
        self.unit = unit
    
    @abstractmethod
    def timestep(self,dt):
        pass

class Wander(Ai):
    def __init__(self,unit):
        Ai.__init__(self,unit)
        self.velocity = [0, 0]
        random.seed()
        self.randstate = random.getstate()
    
    def timestep(self,dt):
        random.setstate(self.randstate)
        randnum = random.random()
        if self.velocity[0] == 0:
            if randnum > 0.95:
                self.velocity[0] = random.choice([-1,1])
        else:
            if randnum > 0.3:
                self.velocity[0] = 0
        self.randstate = random.getstate()
        
        self.unit.deltamove((self.velocity[0]*dt, self.velocity[1]*dt))
        self.unit.dirty = 1
