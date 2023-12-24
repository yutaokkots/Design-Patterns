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

## Definitions and UML diagram

**Context** - class that encapsulates the state and delegates state-specific behavior to the current state object. 

**State** -  An interface or abstract class that declares methods representing the various state-specific behaviors.

**ConcreteState** - Classes that implement the State interface and provide specific implementations for the state-specific behavior


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

### General characteristics of Context, State, and ConcreteState

| Context |  |
| ------- | ------- |
| current_state_ref | holds the current state of the context |
| set_state()       | allows changing the current state to a new state |
| get_state()       | retrives information about the current state |
| request()        | methods that delegate specific operations/requests to the current state, and allows the context to perform state-specific behaviors without knowing the details of how each state implements it |

| State |  |
| ------- | ------- |
| abstract_methods() | declaration of methods that represent state-specific behaviors so that all concrete states have a consistent interface. |
| context_ref| (optional) - allows the state to interact with the context if needed. |

| ConcreteState |  |
| ------- | ------- |
| methods() | specific implementations for state-specific behaviors that are inherited from the State interface |
| context_ref| (optional) - allows the state to interact with the context if needed. |

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

<hr/>

## **Example 1 - State design pattern with a light-switch/lightbulb**

The following code in this section can be placed into a single document in order (e.g. ['`lightbulb.py`'](lightbulb.py) and run.)

<div align="center">

**import statements**

</div>

```
from time import sleep
from abc import ABC, abstractmethod
```

<div align="center">

**abstract state class definition**

</div>

The abstract state class declares methods and attributes representing the various state-specific behaviors. In this example, it contains an abstract method called `do_action` that the concrete classes inherit. It also contains the ability to define the related Context, using `@property` and a method here called  `context()`. 

Methods
-------
do_action
    the shared action among the concrete classes.

Attributes
----------
@property

context() : property

the context reference, declared as a method but 
defined as a @property

```
class AbstractLightState(ABC):
    """Abstract base class for Light State"""

    @property
    def context(self):
        """Defines a 'context()' property. 
        
        The @property decorator turns this 'context()' method to be 
        accessible as a read-only attribute.
        """
        return self.context

    @context.setter
    def context(self, context) -> None:
        """Defines the 'setter' of the context
        
        The '@context.setter' decorator refers to the 'self.context()'
        property defined above. 'self.context()' is now a 'property' due to
        the @property decorator. The @property decorater provides the 
        ".setter" method, which reads (inside the file, builtins.pyi):
            class property:
                ...
                def setter(self, __fset: Callable[[Any, Any], None]) -> property: ...
                ...
        """
        self._context = context

    @abstractmethod
    def do_action(self) -> None:
        pass
```

<div align="center">

**state objects (e.g. On and Off state)**

</div>

The state(s) represents a specific condition or situation in the system.

```
class LightOn(AbstractLightState):
    """State class for switch on"""
    def __init__(self):
        self.status = "ON"

    def do_action(self):
        for i in range(1, 11):
            print(f"\rLight is 💡 {self.status} {i}", end="")
            sleep(0.1)
        print("\n")
```

```
class LightOff(AbstractLightState):
    """State class for switch off"""
    def __init__(self):
        self.status = "OFF"

    def do_action(self):
        for i in range(1, 11):
            print(f"\rLight is {self.status} {i}", end="")
            sleep(0.1)
        print("\n")
```

<div align="center">

**Context**

</div>

```
class LightContext:
    """The context class for the light."""

    ## References the current state of this context; a class attribute.
    current_state_ref = None

    def __init__(self, 
            state1: AbstractLightState, 
            state2: AbstractLightState) -> None:
        self.set_state(state1)
        self.curr_state = "1"
        self.state_dict = {"1": state1, "0": state2}

    def set_state(self, state: AbstractLightState):
        self.current_state_ref = state
        self.current_state_ref.context = self

    def get_state(self):
        return self.current_state_ref

    def request(self):
        self.current_state_ref.do_action()

    def switch(self):
        if self.current_state_ref:
            if self.curr_state == "1":
                self.set_state(self.state_dict["0"])
                self.curr_state = "0"
            else:
                self.set_state(self.state_dict["1"])
                self.curr_state = "1"
```
<div align="center">

**Example implementation**

</div>

```
if __name__ == "__main__":
    # sets the LightContext to LightOn() state
    light = LightContext(LightOn(), LightOff())     
    cycles = 10
    print("Starting:\n")
    light.request()
    for i in range(cycles):
        light.switch()
        light.request()
```
If the above code is placed in a single file and run, the following exemplary output is expected:

```
Starting:

Light is 💡 ON 10       # each number from 1 -> 10 is printed 

Light is OFF 10

Light is 💡 ON 10

Light is OFF 10

Light is 💡 ON 10

Light is OFF 10

Light is 💡 ON 10

Light is OFF 10

Light is 💡 ON 10

Light is OFF 10

Light is 💡 ON 10
```
<hr/>

## **Example 2 - FSM pattern with a light-switch/lightbulb** 

The following code can be placed into a single document in order (e.g. ['`lightbulb_fsm.py`'](lightbulb_fsm.py) and run.)

<div align="center">

**import statements**

</div>

```
from random import randint
from time import time, sleep
from abc import ABC, abstractmethod
```

<div align="center">

**abstract class definition**

</div>

```
class AbstractLight(ABC):
    """Abstract base class for Light-related classes."""
    
    @abstractmethod
    def execute(self):
        "Abstract method for execute method."
        pass
```

<div align="center">

**state objects (e.g. On and Off state)**

</div>

The state(s) represents a specific condition or situation in the system.

```
class LightOn(AbstractLight):
    """State class for switch in on state."""

    def execute(self):
        print("Light is 💡 ON")
```

```
class LightOff(AbstractLight):
    """State class for switch in off state."""

    def execute(self):
        print("Light is OFF")
```

<div align="center">

**transition objects (e.g. Transition)**

</div>

A transition is a change from one state to another triggered by a specific event or condition

```
class Transition(AbstractLight):
    """Defines the class for transitioning (switching) between ON and OFF.
    
    A transition is a relationship between a source state and a target state. It may be part of a compound transition, which takes the state machine from one state configuration to another, representing the complete response of the state machine to an occurrence of an event of a particular type.
    """
    def __init__(self, to_state):
        self.to_state = to_state
    
    def execute(self):
        print(f"transitioning to {self.to_state}")
```

<div align="center">

**Finite State Machine**

</div>

A FSM models the behavior of a system by representing it as a finite set of states, transitions between states, and associated actions or behaviors.

```
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
        """ """
        if self.trans:
            self.trans.execute()
            self.set_state(self.trans.to_state)
            self.trans = None
        self.curr_state.execute()
```

<div align="center">

**The object that incorporates the FSM (e.g. LightBulb)**

</div>

```
class LightBulb:
    """The light bulb/switch object."""

    def __init__(self):
        self.fsm = LightFSM(self)
        self.LightOn = True
```
<div align="center">

**Example implementation**

</div>

```
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
        if randint(0,2):            # randomly activates 66% chance.
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
```

If the above code is placed in a single file and run, the following exemplary output is expected:

```
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
```