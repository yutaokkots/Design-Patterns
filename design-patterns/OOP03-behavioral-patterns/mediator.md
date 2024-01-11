# Mediator

The Mediator Pattern centralize complex communications and control between related objects. <sup>[1]</sup>

Mediators help to centralize the control logic, where

* parts can inform the Mediator when their state changes.
* parts can respond to requests from the Mediator.

The intent of the mediator pattern is to define an object that encapsulates how a set of objects interact.

Mediator promotes loose coupling, by keeping objects from referring to each other explicitly, and allows varying their interaction independently. <sup>[2]</sup>

The mediator interface declares a method used by components to notify the mediator about various events. The mediator may react to these events and pass the execution to other components. <sup>[3]</sup>

## **Mediator UML diagram** 

```
┌───────────────────┐              ┌───────────────────┐
│AbstractMediator   │  <───────────│AbstractColleague  │
├───────────────────┤              ├───────────────────┤
│ mediate()         │              │ getState()        │
└─────────┬─────────┘              └────────┬──────────┘
          △                                 △   
          │                       ┌─────────┴─────────────┐
┌─────────┴─────────┐   ┌─────────┴─────────┐   ┌─────────┴─────────┐
│ConcreteMediator   ├──>│ConcreteColleague1 │┌─>│ConcreteColleague1 │
├───────────────────┤─┐ ├───────────────────┤│  ├───────────────────┤
│ mediate()         │ │ │ getState()        ││  │ getState()        │
│   ...             │ │ │   ...             ││  │   ...             │
└───────────────────┘ │ └───────────────────┘│  └───────────────────┘
                      └──────────────────────┘
```     

### **Example of Inefficient implementation** <sup>[1]</sup>

A house filled with devices (Alarm, CoffeePot, Sprinkler, Calendar) where the devices depend on one another. 

```
Turn off Alarm ─┐
┌───────────────┘
└─> coffeeMaker─┐
┌───────────────┘
└─> turn off sprinkler 15 min before shower─┐
┌───────────────────────────────────────────┘
└─> set alarm early on trash day─┐
┌────────────────────────────────┘
└─> check calendar . . . 

┌───────────────────┐  ┌───>┌─────> ┌───────────────────┐
│Alarm              │<─┼┐<──┼─────┐ │CoffeePot          │
├───────────────────┤  ││   │     │ ├───────────────────┤
│onEvent():         │  ││   │     │ │onEvent():         │
│   checkCalendar() ├──┼┼─┬─┼─────┼─┤   checkCalendar() │
│   checkSprinkler()├──┼┼─│─┼───┐ └─┤   checkAlarm()    │
│   startCoffee()   ├──┘│ │ │   │   │   ...             │
│   ...             │   │ │ │   │   └───────────────────┘
└───────────────────┘   │ │ │   │                       
                        │ │ │   │ 
┌───────────────────┐   │ │ │   │   ┌───────────────────┐
│Calendar           │<──┼─┤ │ ┌>└──>│Sprinkler          │
├───────────────────┤   │ │ │ │     ├───────────────────┤
│onEvent():         │   │ │ │ │     │onEvent():         │
│   checkDayOfWeek()│   │ └─┼─┼─────┤   checkCalendar() │
│   doSprinkler()   ├───┼───┼─┘     │   checkShower()   │
│   doCoffee()      ├───┼───┘       │   checkWeather()  │
│   doAlarm()       ├───┘           │   checkTemp()     │
│   ...             │               │   ...             │
└───────────────────┘               └───────────────────┘
```
With the mediator pattern, the above may look like this:

```
┌───────────────────┐                ┌───────────────────┐
│AlarmColleague     │                │CoffeePotColleague │
├───────────────────┤                ├───────────────────┤
│mediator()         ├──┐          ┌──┤mediator()         │
└───────────────────┘  │          │  └───────────────────┘
                ┌──────┘          └──────────┐
                │   ┌───────────────────┐    │   
                │   │ConcreteMediator   │    │
                │   ├───────────────────┤    │  
                └──>│mediate()          │<───┘ 
                ┌──>└──┬─────────────┬──┘<────────┐
                │      │             └────────────┼─────────┐
                └──────┼─┐        ┌───────────────┘         │ 
┌───────────────────┐  │ │        │  ┌───────────────────┐  │
│CalendarColleague  │  │ │        │  │SprinklerColleague │  │
├───────────────────┤<─┘ │        │  ├───────────────────┤  │
│mediator()         ├────┘        └──┤mediator()         │<─┘
└───────────────────┘                └───────────────────┘
```

## **Other real-world examples** 

* Pilots of aircraft that approach or depart the airport control area don’t communicate directly with each other. <u>Instead, they speak to an air traffic controller</u>, who sits in a tall tower somewhere near the airstrip. Without the air traffic controller, pilots would need to be aware of every plane in the vicinity of the airport, discussing landing priorities with a committee of dozens of other pilots. <sup>[3]</sup>

## **Mediator Pattern Example**

The following files are an example of a Mediator handles several components. 

Here, a mediator detects something that happens in the components. 

Event -> Mediator -> Scheduler -> Mediator -> Confirmation


```
abstract_mediator.py

""" Abstract mediator class for Mediator design pattern."""
from abc import ABC, abstractmethod

class AbstractMediator(ABC):
    """Abstract Mediator class.
    
    Centralize complex communications and control between related objects.
    """

    @abstractmethod
    def notify(self, sender:object, event:str) -> None:
        ...
```

``` 
mediator.py

"""Mediator class"""
from abstract_mediator import AbstractMediator

class Mediator(AbstractMediator):
    def __init__(self, 
                    event_component, 
                    scheduler_component,
                    confirmation_component) -> None:
    
        self._event_component = event_component
        self._scheduler_component = scheduler_component
        self._confirmation_component = confirmation_component

    def notify(self, sender:object=None, event:str=None) -> None:
        if event == "new_event":
            print("Event has detected a 'new_event', which triggers:")
            self._scheduler_component.signal()
        elif event == "schedule":
            print("Scheduler has detected a 'schedule', which triggers:")
            self._confirmation_component.signal()
```

Component classes

```
abstract_component.py

"""Abstract Base class for a Component of a mediator design pattern."""
from abc import ABC, abstractmethod

class AbstractComponent(ABC):
    @abstractmethod
    def signal(self) -> None:
        ...
```

```
component.py

"""A component class for a Component of a mediator design pattern."""
from abstract_component import AbstractComponent
from mediator import Mediator

class Component(AbstractComponent):
    def __init__(self, mediator: Mediator = None) -> None:
        """Initializes the mediator if available during instantiation."""
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        """Mediator property returned."""
        return self._mediator
    
    @mediator.setter
    def mediator(self,  mediator:Mediator) -> None:
        """Sets a mediator instance to self._mediator."""
        self._mediator = mediator
```

Specific components

```
event.py

"""An event component/concrete class """
from component import Component

class Event(Component):
    def __init__(self):
        self.class_name = __class__.__name__

    def signal(self) -> None:
        print(f"{self.class_name} is scheduling an event.")
        self._mediator.notify(self, event="new_event")
```

```
scheduler.py

"""A scheduler component/concrete class """
from component import Component

class Scheduler(Component):
    def __init__(self):
        self.class_name = __class__.__name__

    def signal(self) -> None:
        print(f"{self.class_name} is scheduling an event.")
        self._mediator.notify(self, event="schedule")
```

```
confirmation.py

"""A confirmation component/concrete class """
from component import Component

class Confirmation(Component):
    def __init__(self):
        self.class_name = __class__.__name__

    def signal(self) -> None:
        print(f"{self.class_name} is sending a notification of confirmation.")
```

The code to run the example

```
main.py

from event import Event
from scheduler import Scheduler
from confirmation import Confirmation
from mediator import Mediator

def main():
    c1 = Event()
    c2 = Scheduler()
    c3 = Confirmation()
    mediator = Mediator(c1, c2, c3)
    c1._mediator = mediator
    c2._mediator = mediator
    c3._mediator = mediator

    print("Trigger Event.")
    c1.signal()

if __name__ == "__main__":
    main()
```

Expected output
```
        Trigger Event.
        Event is scheduling an event.
        Event has detected a 'new_event', which triggers:
        Scheduler is scheduling an event.
        Scheduler has detected a 'schedule', which triggers:
        Confirmation is sending a notification of confirmation.
```

<hr>

<sup>[1]</sup> Eric Freeman, Elisabeth Robson, Bert Bates, Kathy Sierra. (2004). Head First Design Patterns. p 622. ISBN-13: 978-0-596-00712-6.

<sup>[2]</sup> Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John (1995). Design Patterns. p 273. Massachusetts: Addison-Wesley. ISBN 0-201-63361-2.

<sup>[3]</sup> Mediator. https://refactoring.guru/design-patterns/mediator. Retrieved Dec. 31, 2023.
