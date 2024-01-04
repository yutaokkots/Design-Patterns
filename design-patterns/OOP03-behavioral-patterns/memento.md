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

**<ins>Memento</ins>** stores internal state of the Originator object.

It protects against access by objects other than the originator. Mementos have effectively two interfaces. Caretaker sees a narrow interface to the Memento—it can only pass the memento to other objects. Originator, in contrast, sees a wide interface, one that lets it access all the data necessary to restore itself to its previous state.

**<ins>Originator</ins>** creates a memento containing a snapshot of its current internal state.

It uses the memento to restore its internal state.

**<ins>Caretaker</ins>** is responsible for the memento's safekeeping.

It never operates on or examines the contents of a memento.
<hr/>

<sup>[1]</sup> Freeman *et al.*. Head First Design Patterns. 2004. p625.