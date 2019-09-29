# Black_Hole is derived from only Simulton: each updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import math
import model
class Black_Hole(Simulton):
    radius = 10
    def __init__(self,pos):
        Simulton.__init__(self,pos[0],pos[1],Black_Hole.radius*2,Black_Hole.radius*2)
    def update(self):
        #print(Prey)
        victims = model.find(lambda x: isinstance(x, Prey) and x in self)
        #print(victims)
        if victims:
            
            for i in victims:
                if i != self:
                    model.remove(i)
        return len(victims) -1
                
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius,self._y-self.radius,\
                           self._x+self.radius,self._y+self.radius, fill="#000000")
    def __contains__(self,item):
        x = abs(self._x - item._x) <= self.radius
        y = abs(self._y - item._y) <= self.radius
        return x and y
        