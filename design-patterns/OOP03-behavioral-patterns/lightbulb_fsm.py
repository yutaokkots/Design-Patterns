"""Lightbulb classes to demonstrate state design pattern.

Rewrote the code from https://www.youtube.com/watch?v=E45v2dD3IQU 
to include more recent Python patterns.
"""
from random import randint
from time import time
from abc import ABC, abstractmethod

##================================

class AbstractLight(ABC):
    """Abstract base class for Light-related classes."""
    
    @abstractmethod
    def execute(self):
        "Abstract method for execute."
        ...

##================================

class LightOn(AbstractLight):
    """State class for switch on"""

    def execute(self):
        print("Light is 💡 ON")

class LightOff(AbstractLight):
    """State class for switch off"""

    def execute(self):
        print("Light is OFF")


##================================

class Transition(AbstractLight):
    """Defines the class for transitioning (switching) between ON and OFF.
    
    A transition is a relationship between a source state and a target state. It may be part of a compound transition, which takes the state machine from one state configuration to another, representing the complete response of the state machine to an occurrence of an event of a particular type.
    """
    def __init__(self, to_state):
        self.to_state = to_state
    
    def execute(self):
        print(f"transitioning to {self.to_state}")

##================================

class LightFSM:
    """The finite state machine (FSM) class responsible for the light-related states and events. 
    
    Main entity driving a collection of states together with regions, transitions and events.
    """
    def __init__(self, light_obj):
        self.lightObj = light_obj
        self.states_dict = {}        # all of the possible states are stored.
        self.transitions_dict = {}
        self.curr_state = None   # stores current state. 
        self.trans = None       # stores the current transition

    def set_state(self, state_name):
        self.curr_state = self.states_dict.get(state_name)

    def transition(self, transition_name):
        self.trans = self.transitions_dict.get(transition_name)

    def execute(self):
        if self.trans:
            self.trans.execute()
            self.set_state(self.trans.to_state)
            self.trans = None
        self.curr_state.execute()

##================================

class LightBulb:
    """The light bulb/switch object."""

    def __init__(self):
        self.fsm = LightFSM(self)
        self.LightOn = True

##================================

if __name__ == "__main__":
    light = LightBulb()

    light.fsm.states_dict["On"] = LightOn()     #initialize the "ON" state instance. 
    light.fsm.states_dict["Off"] = LightOff()   #initialize the "OFF" state instance.
    light.fsm.transitions_dict["toOn"] = Transition("On")   #initializes "ON" Transition instance.
    light.fsm.transitions_dict["toOff"] = Transition("Off") #initializes "OFF" Transition instance.

    light.fsm.set_state("On")               # sets the 'curr_state' to "ON" state instance

    cycles = 10
    print("Starting:\n")
    for i in range(cycles):
        startTime = time()
        timeInterval = 2
        while (startTime + timeInterval > time()):  # continues for 1 cycles/sec
            pass
        print(f"Step {i + 1}:")
        if randint(0,2):
            if light.LightOn:
                light.fsm.transition("toOff")
                light.LightOn = False
            else:
                light.fsm.transition("toOn")
                light.LightOn = True
        else:
            print("Nothing happened.")
        light.fsm.execute()
        print("\n")

"""
Starting:
Step 1:
transitioning to Off
Light is OFF


Step 2:
transitioning to On
Light is 💡 ON


Step 3:
Nothing happened.
Light is 💡 ON


Step 4:
transitioning to Off
Light is OFF


Step 5:
Nothing happened.
Light is OFF


Step 6:
transitioning to On
Light is 💡 ON


Step 7:
Nothing happened.
Light is 💡 ON


Step 8:
transitioning to Off
Light is OFF


Step 9:
Nothing happened.
Light is OFF


Step 10:
Nothing happened.
Light is OFF
"""