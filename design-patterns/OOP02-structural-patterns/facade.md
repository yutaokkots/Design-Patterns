# Façade

A facade is a unified interface for a set of interfaces in a subsystem. A Facade is a class that contains methods to invoke methods in other classes. 

## Exemplary Diagram
```
A highly decoupled system:
          ┌───────┐                       ┌───────┐
          ├───────┤      ┌───────┐        ├───────┤
          │       │      ├───────┤      / │       │
          └───────┘      │       │    /   └───────┘
               \         └───────┘  /      │
                \        /      │ /        │
        ┌───────────────────────────────────────────────┐
        │          \   /       /│    ┌───────┐          │ 
        │       ┌───────┐    /       ├───────┤          │   
        │       ├───────┤  /    │    │       │          │   
        │       │       │ ─ ── ─ ─ ─ └───────┘          │   
        │       └───────┘       │      /     \          │   
        │         /        \          /       ┌───────┐ │   
        │   ┌───────┐       \   │    /        ├───────┤ │  
        │   ├───────┤ ─ ── ─ ┌───────┐        │       │ │  
        │   │       │        ├───────┤ ─ ─ ── └───────┘ │  
        │   └───────┘        │       │                  │ 
        │                    └───────┘                  │ 
        └───────────────────────────────────────────────┘
Simplifies to:
              ┌───────┐                   ┌───────┐
              ├───────┤      ┌───────┐    ├───────┤
              │       │\     ├───────┤   /│       │
              └───────┘ \    │       │  / └───────┘
                         \   └──┬────┘ /  
                          \┌────┴────┐/ 
        ┌──────────────────┤  Facade ├──────────────────┐
        │                  └────┬────┘ ┌───────┐        │ 
        │       ┌───────┐ /           \├───────┤        │   
        │       ├───────┤/      │      │       │        │   
        │       │       │ ─ ── ─ ─ ─   └───────┘        │   
        │       └───────┘       │      /     \          │   
        │         /        \          /       ┌───────┐ │   
        │   ┌───────┐       \   │    /        ├───────┤ │  
        │   ├───────┤ ─ ── ─ ┌───────┐        │       │ │  
        │   │       │        ├───────┤ ─ ─ ── └───────┘ │  
        │   └───────┘        │       │                  │ 
        │                    └───────┘                  │ 
        └───────────────────────────────────────────────┘
```

## Principle of Least Knowledge - Law of Demeter

The principle of least knowledge - recommendation that objects should avoid accessing the internal data and methods of other objects.

Given an object, **only methods that belong to** the following should be invoked.

(1) the object itself;

(2) objects passed as a parameter to the method;

(3) any object that the method creates/instantiates; or

(4) any components of the object ("has-a" relationships)

<hr>

Freeman, Eric; Robson, Elisabeth; Bates, Bert; Sierra, Kathy. (2004). Head First Design Patterns. California: O'Reilly Media. ISBN: 978-0-596-00712-6. 