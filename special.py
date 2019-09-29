# A Special or Comet is a Prey and black hole; it updates by moving in a straight
#   line and displays as yellow circle with a radius
#   of 4 (width/height 8), speeds up when ever it hits something.
import random 
import math
from prey import Prey
from blackhole import Black_Hole

class Special(Prey,Black_Hole):
    radius = 4 
    def __init__(self,pos):
        angle = (math.pi*random.randint(1,360)/180)
        Prey.__init__(self, pos[0], pos[1], Special.radius*2, Special.radius*2,angle,5)
    def update(self):
        #self.randomize_angle()
        self.move()
        speed_factor = Black_Hole.update(self)
        self._speed += speed_factor
    def display(self,canvas):
        canvas.create_oval(self._x-Special.radius,self._y-Special.radius,\
                           self._x+Special.radius,self._y+Special.radius, fill="#FFFF00")