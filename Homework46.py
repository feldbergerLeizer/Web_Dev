import random
class Die:
   
    def __init__(self,sides ):
        self._sides = sides
        
    def roll(self):
        return random.randint(1,self._sides)

myDie = Die(6)
print(myDie.roll())

class sixSided(Die):
    def __init__(self):
        super().__init__(6)

myDie =sixSided()
print(myDie.roll())
       