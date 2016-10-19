import unit

class Dwarf(unit.Unit):
    def __init__(self):
        super().__init__()
        self.name = "Dwarf1"
    
    def rename(self,newName):
        self.name = newName
