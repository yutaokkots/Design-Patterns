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
    │saveMemento()    │   │     │ SetState()     │
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
It can keep a list of past memento states and cause the originator to return to them.

## **Example Implementation of Memento pattern**

```
    ┌─────────────────────┐     ┌────────────────┐      ┌─────────────────┐
    │AbstractOriginator   │     │AbstractMemento │      │AbstractCaretaker│
    ├─────────────────────┤     ├────────────────┤      └──────┬──────────┘
    │SetMemento(Memento m)│     │ GetState()     │             △
    │saveMemento()        │     │ SetName()      │             │
    │exemplary_change()   │     └─────┬──────────┘             │
    └──────────┬──────────┘           △                        │
               △                      │                        │
    ┌──────────┴──────────┐     ┌─────┴──────────┐      ┌──────┴─────────┐
    │  Originator         │     │    Memento     │<---<>│   Caretaker    │
    ├─────────────────────┤     ├────────────────┤      ├────────────────┤
    │SetMemento(Memento m)├ ─ ─>│ GetState()     │      │ backup()       │
    │saveMemento()        │     │ SetState()     │      │ undo()         │
    │exemplary_change()   │     ├────────────────┤      │ showHistory()  │
    ├─────────────────────┤     │ state          │      └────────────────┘
    │state                │     └────────────────┘  
    └─────────────────────┘ 
```

Example of an originator class. 

```
originator.py

"""Originator class for the memento pattern."""
from abc import ABC, abstractmethod
from random import sample
from memento import AbstractMemento, Memento
from string import ascii_letters

class AbstractOriginator(ABC):
    """Originator class for the memento pattern."""

    @staticmethod
    def _generate_random_string(length:int=10) -> str:
        return "".join(sample(ascii_letters, length))

    @abstractmethod
    def save_memento(self) -> None:
        ...

    @abstractmethod
    def set_memento(self, memento) -> None:
        ...

    @abstractmethod
    def exemplary_state_change(self) -> None:
        ...

class Originator(AbstractOriginator):
    """Originator concrete class that interacts with the memento."""

    _state = None

    def __init__(self, state: str) -> None:
        self._state = state

    def save_memento(self) -> Memento:
        """Saves the current state as a memento and returns it."""
        return Memento(self._state)

    def set_memento(self, memento:AbstractMemento) -> None:
        """Sets the state of a memento to the current state in originator."""
        self._state = memento.get_state()
        print(f"Originator: state has been set to {self._state}")

    def exemplary_state_change(self) -> None:
        """Change in state of originator."""
        print("Something to effect the state.")
        self._state = self._generate_random_string(15)
        print(f"Originator: state has been set to {self._state}")
```

Example of a memento class. 
```
memento.py

"""Memento class for the memento design pattern."""

from abc import ABC, abstractmethod
from datetime import datetime
class AbstractMemento(ABC):
    """Abstract base class for Memento class."""

    @abstractmethod
    def get_state(self):
        ...
    
    @abstractmethod
    def get_name(self):
        ...

class Memento(AbstractMemento):
    """Concrete Memento class for memento design pattern"""
    def __init__(self, state:str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        """The Originator uses this method to restore their state."""
        return self._state

    def get_date(self):
        """Gets the date that the memento was created."""
        return self._date
    
    def get_name(self):
        """Gets the name of the memento."""
        return f"{self._date} / ({self._state[0:9]}...)"
```

Example of a caretaker class. 
```
caretaker.py

"""Caretaker classes for the memento design pattern."""
from abc import ABC, abstractmethod
from originator import AbstractOriginator

class AbstractCaretaker(ABC):
    """Abstract base class for the caretaker class. 
    
    The Caretaker class has no access to the originator's state.
    """

    @abstractmethod
    def backup(self) -> None:
        ...

    @abstractmethod
    def undo(self) -> None:
        ...

    @abstractmethod
    def show_history(self) -> None:
        ...

class Caretaker(AbstractCaretaker):
    """Concrete Caretaker class."""
    def __init__(self, originator: AbstractOriginator):
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        """Backup of a memento is created by saving into a list, self._mementos."""
        self._mementos.append(self._originator.save_memento())

    def undo(self) -> None:
        """returns the memento to the previous state."""
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        print(f"Restoring the state to {memento}")
        try: 
            self._originator.set_memento(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        """Prints out a history of previous mementos."""
        print(f"Caretaker: here is the list of mementos: {self._mementos}")
        for m in self._mementos:
            print(m.get_name)
```

Example of the main class. 
```
main.py

"""main file for running the memento design pattern."""
from originator import Originator
from caretaker import Caretaker

def main():
    orig = Originator("Initialization")
    care = Caretaker(orig)
    
    care.backup()

    orig.exemplary_state_change()
    care.backup()

    orig.exemplary_state_change()
    care.backup()

    orig.exemplary_state_change()
    care.backup()

    care.show_history()

    care.undo()

    care.undo()
    
    care.undo()

if __name__ == "__main__":

    main()

    """
        Something to effect the state.
        Originator: state has been set to JKxPpHsAouqwURM
        Something to effect the state.
        Originator: state has been set to XTtfhMusjZCNSbg
        Something to effect the state.
        Originator: state has been set to VPodpgytkEFYHmc
        Caretaker: here is the list of mementos: [<memento.Memento object at 0x1060d2090>, <memento.Memento object at 0x106197890>, <memento.Memento object at 0x10619cb90>, <memento.Memento object at 0x10619cc50>]
        <bound method Memento.get_name of <memento.Memento object at 0x1060d2090>>
        <bound method Memento.get_name of <memento.Memento object at 0x106197890>>
        <bound method Memento.get_name of <memento.Memento object at 0x10619cb90>>
        <bound method Memento.get_name of <memento.Memento object at 0x10619cc50>>
        Restoring the state to <memento.Memento object at 0x10619cc50>
        Originator: state has been set to VPodpgytkEFYHmc
        Restoring the state to <memento.Memento object at 0x10619cb90>
        Originator: state has been set to XTtfhMusjZCNSbg
        Restoring the state to <memento.Memento object at 0x106197890>
        Originator: state has been set to JKxPpHsAouqwURM
    """
```
<hr/>

<sup>[1]</sup> Freeman *et al.*. Head First Design Patterns. 2004. p625.