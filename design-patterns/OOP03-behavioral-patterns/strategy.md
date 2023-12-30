# Strategy

The strategy pattern includes a family of algorithms that are encapsulated such that they are interchangeable (even during runtime). Strategy uses encapsulation for inheriting behavior. 

At run time, the code instructs which family of algorithms to use. 

### The strategy pattern uses **composition**. 

*Gamma et al.* wrote the second rule of reusable OOP as follows:

<span style="color:darkred">

***Favor object composition over class inheritance.***

</span>

This relationship is a HAS-A type relationship (as opposed to an IS-A relationship).

```
    ┌───────────────────────────┐       ┌──────────────────────┐
    │AbstractCharacter          │       │ Abstract (Interface) │
    ├───────────────────────────┤ HAS-A │ WeaponBehavior       │
    │self.weapon_behavior       ├─────> ├──────────────────────┤
    │     = weapon              │       │ useWeapon()          │
    ├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┤       └──┬───────────────────┘ 
    │fight()                    │          △
    ├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┤          │ interface
  ┌─│setWeapon(w:WeaponBehav):  │          ├ ─ ┬ ─ ┐                  
  │ │   self.weapon_behavior = w│   ┌──────┴───┼───┼─┐                      
  │ └──────────┬────────────────┘   │SwordBehav│or │ │                       
  │            △ inheritance        ├ ─ ┌──────┴───┼─┴──┐        
  │            ├───┬───┐            │   │AxeBehavio│    │               
  │     ┌──────┴───┼───┼─┐          └───├ ─ ┌──────┴────┴───┐               
  │     │  Troll   │   │ │              │   │KnifeBehavior  │               
  │     ├ ─ ┌──────┴───┼─┴──┐           └───├───────────────┤         
  │     │   │  Queen   │    │               │useWeapon()    │              
  │     └───├ ─ ┌──────┴────┴───┐           └───────────────┘             
  │         │   │  King         │      
  │         └───├───────────────┤       
  │             │fight()        │       
  │             └───────────────┘       
  │
  └ the setWeapon() method allows the type of weapon to be
        interchangeable at run-time.
```

## **Example with Ducks**

This example is similar to an example shown in <ins>Head First Design Patterns</ins> by Freeman *et al.*

```
abstract_duck.py

"""Defines the AbstractDuck class."""
from abc import ABC, abstractmethod

class AbstractDuck(ABC):
    """Abstract base class for a Duck."""

    def __init__(self, fly_behav, quack_behav):
        """Defines the reference variables"""
        self.fly_behavior = fly_behav
        self.quack_behavior = quack_behav

    def set_fly_behavior(self, fly_behav):
        """Allows setting the 'fly_behavior' ref. variable at run-time."""
        self.fly_behavior = fly_behav

    def set_quack_behavior(self, quack_behav):
        """Allows setting the 'quack_behavior' ref. variable at run-time."""
        self.quack_behavior = quack_behav

    @abstractmethod
    def perform_fly(self):
        """Defines the fly method."""
        pass

    @abstractmethod
    def perform_quack(self):
        """Defines the quack method."""
        pass

    @abstractmethod
    def float(self):
        """Defines the float method."""
        pass

    @abstractmethod
    def display(self):
        """Defines the display method"""
        pass

```

The following three duck classes inherit from the `AbstractDuck` class

```
mallard_duck.py

"""Defines the MallardDuck class."""
from abstract_duck import AbstractDuck
from abstract_fly import Fly
from abstract_quack import Quack
from duck_graphics import mallard_duck

class MallardDuck(AbstractDuck):
    """A MallardDuck Concrete class. """
    def __init__(self):
        super().__init__(Fly(), Quack())

    def perform_fly(self):
        """Implements the Fly behavior"""
        self.fly_behavior.fly()

    def perform_quack(self):
        """Implements the Quack behavior"""
        self.quack_behavior.quack()

    def float(self):
        """Implementation of a float method."""
        print("Floating in the waters of Sloan's lake")

    def display(self):
        """Displays an image of this duck"""
        print(mallard_duck)

```

```
rubber_duck.py

"""Defines the RubberDuck class."""
from abstract_duck import AbstractDuck
from abstract_fly import FlyIgnore
from abstract_quack import Squeak
from duck_graphics import rubber_duck

class RubberDuck(AbstractDuck):
    """A RubberDuck Concrete class. """

    def __init__(self):
        super().__init__(FlyIgnore(), Squeak())

    def perform_fly(self):
        """Implements the FlyIgnore behavior"""
        self.fly_behavior.fly()

    def perform_quack(self):
        """Implements the Squeak behavior"""
        self.quack_behavior.quack()

    def float(self):
        """Implementation of a float method."""
        print("::calmly floating in the bathtub::")

    def display(self):
        """Displays an image of this duck"""
        print(rubber_duck)

```


```
quiet_duck.py

"""Defines the QuietDuck class."""
from abstract_duck import AbstractDuck
from abstract_fly import FlapWings
from abstract_quack import MuteQuack
from duck_graphics import quiet_duck

class QuietDuck(AbstractDuck):
    """A QuietDuck Concrete class. """
    def __init__(self):
        super().__init__(FlapWings(), MuteQuack())

    def perform_fly(self):
        """Implements the FlapWings behavior"""
        self.fly_behavior.fly()

    def perform_quack(self):
        """Implements the MuteQuack behavior"""
        self.quack_behavior.quack()

    def float(self):
        """Implementation of a float method."""
        print("The waters are nice.")

    def display(self):
        """Displays an image of this duck"""
        print(quiet_duck)

```

The following two files show a family of related behaviors, for 'fly' and 'quack'.

```
abstract_fly.py

"""Fly classes for Flying and related family behaviors."""
from abc import ABC, abstractmethod

class AbstractFly(ABC):
    """Abstract base class for Fly behavior"""
    @abstractmethod
    def fly(self):
        pass

class Fly(AbstractFly):
    """Fly class for regular flying behavior."""
    def fly(self):
        print("::flying behavior::")

class FlapWings(AbstractFly):
    """FlapWings class for just flapping wings behavior."""
    def fly(self):
        print("::flap wings::")

class FlyIgnore(AbstractFly):
    """FlyIgnore class for ignoring behavior."""
    def fly(self):
        print(". . .")

```

```
abstract_quack.py

"""Quack classes for Quacking and related family behaviors."""
from abc import ABC, abstractmethod

class AbstractQuack(ABC):
    """Abstract base class for Quack behavior"""
    
    @abstractmethod
    def quack(self):
        pass

class Quack(AbstractQuack):
    """Quack class for regular quacking behavior."""
    def quack(self):
        print("QUACK!")

class Squeak(AbstractQuack):
    """Squeak class for squeaking behavior."""
    def quack(self):
        print("SQUEAK!")

class MuteQuack(AbstractQuack):
    """Mute class for muted behavior."""
    def quack(self):
        print(". . .")

```

The above code can be represented in the following diagram:

```
    ┌───────────────────────────┐       ┌──────────────────────┐
    │AbstractDuck               │       │          (Interface) │
    ├───────────────────────────┤ HAS-A │ AbstractFly          │
    │self.fly_behavior=fly_behav├─────> ├──────────────────────┤
    │self.qua_behavior=qua_behav├─┐     │ fly()                │
    ├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┤ │     └──┬───────────────────┘ 
    │perform_fly()              │ │        △ interface
    │perform_quack()            │ │        ├ ─ ┬ ─ ┐                         
    ├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┤ │ ┌──────┴───┼───┼─┐                      
  ┌─│setFlyBehav(f:Fly):        │ │ │FlyIgnore │   │ │                         
  │ │   self.fly_behavior = f   │ │ ├ ─ ┌──────┴───┼─┴──┐        
  ├─│setQuackBehav(q:Quack):    │ │ │   │FlapWings │    │               
  │ │   self.qua_behavior = q   │ │ └───├ ─ ┌──────┴────┴───┐               
  │ └──────┬────────────────────┘ │     │   │Fly            │               
  │        △ inheritance          │     └───├───────────────┤         
  │        ├───┬───┐              │         │fly()          │              
  │ ┌──────┴───┼───┼─┐            │         └───────────────┘             
  │ │QuietDuck │   │ │            │HAS-A 
  │ ├ ┌────────┴───┼─┴──┐         │     ┌──────────────────────┐   
  │ │ │RubberDuck  │    │         │     │          (Interface) │   
  │ └─├ ┌──────────┴────┴───┐     │     │ AbstractQuack        │   
  │   │ │MallardDuck        │     └───> ├──────────────────────┤      
  │   └─├───────────────────┤           │ quack()              │       
  │     │def __init__(self):│           └──┬───────────────────┘        
  │     │   super().        │              △ interface      
  │     │   __init__(Fly(), │              ├ ─ ┬ ─ ┐           
  │     │         Quack())  │           ┌──┴───┼───┼─┐      
  │     └───────────────────┘           │MuteQu│ck │ │        
  │                                     ├ ─ ┌──┴───┼─┴─┐        
  │                                     │   │Squeak│   │    
  │                                     └───├ ─ ┌──┴───┴───┐               
  │                                         │   │Quack     │               
  │                                         └───├──────────┤         
  │                                             │quack()   │              
  │                                             └──────────┘ 
  └ the setFlyBehav() and setQuackBehav() methods allows the type of fly or 
    type of quack to be changed at run-time.
```