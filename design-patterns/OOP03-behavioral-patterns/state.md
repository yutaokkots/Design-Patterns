# State

Allows an object to alter its behavior when its internal state changes. 

A way to create a 'state machine' in Object Oriented Programming. 

### A finite state machine (FSM)

1. has a fixed number of states
2. can only be in one state at a time
3. each state is responsible for doing one thing
4. the active state receives inputs and responds

## Example
Imagine a NYC subway turnstile:
```
STATES: closed, open
            edit: added 'processing' state
actions: enter(), payOK(), payFailed()

                           enter()
payFailed() ┌──> closed <-----------> open <─┐ payOK()
            └────┘ │ ^     payOK()    ^ └────┘
                   │ │                │ 
                   │ └───┐            │ 
                   └──> processing ───┘
        ┌─┐       ┌─┐       ┌─┐    
        ├─┤       ├─┤       ├─┤   
        │ │       │*│       │*│     
        │ │       │*│       │*│     
        ├─┤       ├─┤       ├─┤     
        │ \ ======│ \ ======│ \     
        │  │      │  │      │  │  
        │  │      │  │      │  │  
        ┴──┴──────┴──┴──────┴──┴─  
```     

|       | enter | payOK | payFailed |
|-------|-------|-------|-----------|
|closed |closed | open  | closed    |
|open   |closed | open  | open      |
|process|   -   |       |    -      |


"If the object is in _____ state, and it receives this action, what happens to the state?"


Context - the thing that can have state

State - 

```

┌───────────────┐         ┌─────────────────┐
│ Context       │         │ State           │
│  (Turnstile)  │         │ (TurnstileState)│
├───────────────┤         ├─────────────────┤
│ request()     │ ──────> │ handle()        │
│ ex.           │         │  ex.            │
│   enter()     │         │    enter()      │
│   pay()       │         │    pay()        │
│   payOk()     │         │    payOk()      │
│   payFailed() │         │    payFailed()  │    
│changeState(   │         │                 │
│ TurnstileState│         │                 │
│)              │         │                 │    
└───────────────┘         └────────┬────────┘
                                   △
                         ┌─────────┴─────────┐
                        ┌┤ ConcreteStateA    │
                        ││ (OpenGateState)   │
                       ┌┤├───────────────────┤
                       │├│ handle()          │
                       ├││      (spec. impl) │
                       │││   ex.             │
                       │││      enter()      │
                       │││      pay()        │
                       │││      payOk()      │
                       │││      payFailed()  │
                       ││└───────────────────┘
                       │└───────────────────┘
                       └───────────────────┘


```
<hr>

### How to represent states

1. use enumerators (simple objects)

```
    class Player:
        enum States{
            Idle,
            Walking,
            Falling,
            Jumping
        }
        var has_double_jumped = false;
        var current_state = State.Idle

        func input(event):
            switch current_state:
                State.Idle:
                    input_idling(event)
                State.Walking:
                    input_walking(event)
                State.Jumping:
                    input_jumping(event)
                State.Falling:
                    input_falling(event)
```

2. state pattern
    a. create a generic State interface
    b. implement the interface with a class per state
    c. let the parent entity delegate logic to the active state
    d. provide a way for states to transition to one another


## Example of State pattern with light bulbs


```
from random import randint
from time import time, sleep

##================================

State = type("State", (object,), {}) #creates a State base class

class LightOn(State):
    def Execute(self):
        print("Light is on")

class LightOff(State):
    def Execute(self):
        print("Light is off")

##================================

class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print(f"Transitioning to {self.toState}") 

##================================

class SimpleFSM(object):
    def __init__(self, char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.currState = None
        self.trans = None

    def SetState(self, stateName):
        self.currState = self.states[stateName]

    def Transition(self, transName):
        self.trans = self.transitions[transName]

    def Execute(self):
        if (self.trans):
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.trans = None
        self.currState.Execute()

##================================

class Char(object):
    def __init__(self):
        self.FSM = SimpleFSM(self)
        self.LightOn = True

##================================

if __name__ == "__main__":
    light = Char()

    light.FSM.states["On"] = LightOn()
    light.FSM.states["Off"] = LightOff()
    light.FSM.transitions["toOn"] = Transition("On")
    light.FSM.transitions["toOff"] = Transition("Off")

    light.FSM.SetState("On")

    for i in range(20):
        startTime = time()
        timeInterval = 1
        print(startTime)
        print(light.LightOn)
        while (startTime + timeInterval > time()):  
            pass
        if randint(0,2):
            if light.LightOn:
                light.FSM.Transition("toOff")
                light.LightOn = False
            else:
                light.FSM.Transition("toOn")
                light.LightOn = True

```