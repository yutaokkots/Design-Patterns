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

<hr>

<sup>[1]</sup> Eric Freeman, Elisabeth Robson, Bert Bates, Kathy Sierra. (2004). Head First Design Patterns. p 622. ISBN-13: 978-0-596-00712-6.

<sup>[2]</sup> Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John (1995). Design Patterns. p 273. Massachusetts: Addison-Wesley. ISBN 0-201-63361-2.

<sup>[3]</sup> Mediator. https://refactoring.guru/design-patterns/mediator. Retrieved Dec. 31, 2023.
