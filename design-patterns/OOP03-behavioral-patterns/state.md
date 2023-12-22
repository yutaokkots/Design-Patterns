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
