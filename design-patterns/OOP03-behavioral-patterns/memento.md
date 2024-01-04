# Memento

also known as 'Token'

The memento design pattern is useful for returning an object to one of its previous states.<sup>[1]</sup>

Goals:

- Saving the important state of a system’s key object.
- Maintaining the key object’s encapsulation.


## **UML diagram for Memento pattern**

```
    ┌─────────────────────┐     ┌────────────────┐      ┌────────────────┐   
    │Originator           │     │    Memento     │<---<>│   Caretaker    │
    ├─────────────────────┤     ├────────────────┤      └────────────────┘
    │SetMemento(Memento m)├ ─ ─>│ GetState()     │
    │createMemento()  │   │     │ SetState()     │
    ├─────────┼───────┼───┤     ├────────────────┤
    │state    │       │   │     │ state          │   
    └─────────┼───────┼───┘     └────────────────┘  
              │     ┌─┴──────────────────────┐─┐
              │     │state = m -> GetState() └─┤
              │     └──────────────────────────┘
    ┌─────────┴───────────────┐─┐
    │return new Memento(state)└─┤
    └───────────────────────────┘
```

<hr/>

<sup>[1]</sup> Freeman *et al.*. Head First Design Patterns. 2004. p625.