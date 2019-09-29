# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
import random
import math
import model

class Floater(Prey): 
    radius = 5
    def __init__(self,pos):
        angle = (math.pi*random.randint(1,360)/180)
        Prey.__init__(self,pos[0],pos[1],Floater.radius*2,Floater.radius*2,angle,5)
    def update(self):
        if random.random() < .3:
            self.set_speed(self.get_speed() + random.choice([-.5,.5]))
            if self.get_speed() < 3:
                self.set_speed(3.5)
            if self.get_speed() > 7:
                self.set_speed(6.5)
            self.randomize_angle()
        self.move()
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius,self._y-Floater.radius,\
                           self._x+Floater.radius,self._y+Floater.radius, fill="#FF0000")
