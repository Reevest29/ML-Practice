# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions

from prey import Prey
from blackhole import Black_Hole
import model

class Pulsator(Black_Hole): 
    counter_constant = 30
    def __init__(self,pos):
        Black_Hole.__init__(self,pos)
        self.counter = 30
    def update(self):
        victims = model.find(lambda x: isinstance(x, Prey) and x in self)
        if victims:
            for i in victims:
                model.remove(i)
                w,h = self.get_dimension()
                self.set_dimension(w+1, h+1)
                self.radius = (1/2)*w
                self.counter = Pulsator.counter_constant
                
        else:
            #print(self.counter)
            self.counter-=1
            if self.counter == 0:
                w,h = self.get_dimension()
                #print("here")
                self.set_dimension(w-1, h-1)
                self.radius = (1/2)*w
                if self.get_dimension() == (0,0):
                    model.remove(self)
                self.counter = Pulsator.counter_constant
         
        