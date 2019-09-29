# Hunter is derived from both the Mobile_Simulton and Pulsator classes;
#   each updates like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import math
import random
import model

class Hunter(Pulsator, Mobile_Simulton):
    Distance = 200
    def __init__(self,pos):
        Pulsator.__init__(self,pos)
        angle = (math.pi*random.randint(1,360)/180)
        Mobile_Simulton.__init__(self,pos[0],pos[1],self._width,self._height,angle,5)
    def update(self):
        Pulsator.update(self)
        self.move()
        targets = model.find(lambda x: isinstance(x, Prey) and self.distance((x._x,x._y)) <= Hunter.Distance)
        
        tar = {x: self.distance((x._x,x._y)) for x in targets}
       
        prey = [k for k,v in sorted(tar.items(),key = lambda x: x[1] )]
        #print("here",prey)
        if prey:
            prey = prey[0]
            x = prey._x - self._x
            y = prey._y - self._y
            angle = math.atan2(y,x)
            self._angle = angle
            
        
        
        