import unit

class Dwarf(unit.Unit):
    def __init__(self):
        unit.Unit.__init__(self)
        self.name = "Dwarf1"
        self.ai = None
    
    def update(self,dt):
        if self.ai is not None:
            self.ai.timestep(dt)
    
    def rename(self,newName):
        self.name = newName
