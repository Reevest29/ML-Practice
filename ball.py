# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).
import random 
import math
from prey import Prey

class Ball(Prey):
    radius = 5 
    def __init__(self,pos):
        angle = (math.pi*random.randint(1,360)/180)
        Prey.__init__(self,pos[0],pos[1],10,10,angle,5)
    def update(self):
        #self.randomize_angle()
        self.move()
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius,self._y-Ball.radius,\
                           self._x+Ball.radius,self._y+Ball.radius, fill="#000000")
        