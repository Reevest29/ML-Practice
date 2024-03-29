import controller, sys
import model   # Pass a reference to model to each update call in update_all

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
names = ['Ball',"Floater","Black_Hole","Pulsator","Hunter","Special"]                                                                                                  
last_click = ''
simultons = []
click_position = ()
step = False
is_repeating = False
cycle_count = 0
#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    simultons.clear()
    display_all()


#start running the simulation
def start ():
    global is_repeating
    is_repeating = True


#stop running the simulation (freezing it)
def stop ():
    global is_repeating
    is_repeating = False


#tep just one update in the simulation
def step ():
    global step
    step = True


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global last_click
    last_click = kind
    #print(last_click)

#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    click_position = (int(x),int(y))
    #print(x,y)
    #print(last_click+f"({x},{y})")
    if last_click in names:
        exec('add('+last_click+f"({click_position}))")
    if last_click == 'Remove':
        for i in simultons:
            if i.contains(click_position):
                remove(i)
    


#add simulton s to the simulation
def add(s):
    simultons.append(s)
    display_all()

# remove simulton s from the simulation    
def remove(s):
    simultons.remove(s)
    display_all()

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    new = []
    for i in simultons:
        if (p(i)):
            new.append(i)
    return new

#call update for each simulton in the simulation (passing model as an argument)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    cycle_count +=1
    for i in simultons:
        i.update()
    
#delete from the canvas each simulton being simulated; afterward call display on each
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for i in controller.the_canvas.find_all():
        controller.the_canvas.delete(i)
    for i in simultons:
        i.display(controller.the_canvas)
        
    controller.the_progress.config(text = f"{cycle_count} updates/{len(simultons)} simultons")