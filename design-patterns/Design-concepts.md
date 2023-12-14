# Design Concepts

## Compile-time vs Run-time 

The code structure is frozen at ***compile-time***; it consists of classes in fixed inheritance relationships.

A program's ***run-time*** structure consists of rapidly changing networks of communicating objects. 

```
┌───────────────┐              ┌───────────────┐ 
│  Object       │              │ Object        │
│  Aggregation  ├─────────────>┤ Acquaintance  │
└───────────────┘              └───────────────┘ 
```
| object aggregation| acquaintance| | 
| -- | -- | -- |
| - A form of association where one class is composed of or contains another class.<br/>- Represents a "has-a" relationship.<br/>-Object aggregation is typically expressed through class compositions where one class contains an instance of another class. | -One class is aware of another class, but it doesn't necessarily imply ownership or containment. <br/> -Objects of one class may interact with objects of another class without being composed of them. <br/>-Acquaintance is often expressed through method signatures, function parameters, or class declarations indicating that one class is aware of another.| **compile-time** |
|-The aggregated object's lifecycle is often managed by the aggregating object. If the aggregating object is destroyed, the aggregated object may also be destroyed|-Objects are aware of each other, and they may collaborate or communicate during the program's execution. However, there might not be a strict containment relationship.| **run-time** |
||Composite, Decorator (both Structural Patterns)|examples|

## Designing for Change 

Redesign is a risk and is expensive.

### Redesign causes and Design Patterns to prevent redesign:

|    | Reason for Redesign<sup>[1]</sup> | Design Pattern that prevent redesign |  
| -- | ------------------- | -- | 
|  1 | **Creating an object by specifying a class explicitly**. Specifying a class name when you create an object commits you to a particular implementation instead of a particular interface.  | Factory Method<sup>C-(cl)</sup>  <br/> Abstract Factory<sup>C-(ob)</sup> <br> Prototype<sup>C-(ob)</sup> | 
|  2 | **Dependence on specific operations**. When you specify a particular operation, you commit to one way of satisfying a request. By avoiding hard-coded requests, you make it easier to change the way a request gets satisfied both at compile-time and at run-time. | Chain of Responsibility<sup>B-(ob)</sup> <br/> Command<sup>B-(ob)</sup> |
|  3 | **Dependence on hardware and software platform**. External operating system interfaces and application programming interfaces (APIs) are different on different hardware and software platforms. Software that depends on a particular platform will be harder to port to other platforms. It may even be difficult to keep it up to date on its native platform. It's important therefore to design your system to limit its platform dependencies.  | Abstract Factory<sup>C-(ob)</sup>  <br/> Bridge<sup>S-(ob)</sup>| 
|  4 | **Dependence on object representations or implementations**. Clients that know how an object is represented, stored, located, or implemented might need to be changed when the object changes. Hiding this information from clients keeps changes from cascading. | Abstract Factory<sup>B-(ob)</sup> <br/> Bridge<sup>S-(ob)</sup> <br/> Memento<sup>B-(ob)</sup> <br/> Proxy<sup>S-(ob)</sup>| 
|  5 | **Algorithmic dependencies.** Algorithms are often extended, optimized, and replaced during development and reuse. Objects that depend on an algorithm will have to change when the algorithm changes. Therefore algorithms that are likely to change should be isolated. | Builder<sup>C-(ob)</sup> <br/> Iterator<sup>B-(ob)</sup> <br/> Strategy<sup>B-(ob)</sup> <br/> Template Method<sup>B-(cl)</sup> <br/> Visitor<sup>B-(ob)</sup> |
|  6 | **Tight coupling.** Classes that are tightly coupled are hard to reuse in isolation, since they depend on each other. Tight coupling leads to monolithic systems, where you can't change or remove a class without understanding and changing many other classes. The system becomes a dense mass that's hard to learn, port, and maintain. <br/> Loose coupling increases the probability that a class can be reused by itself and that a system can be learned, ported, modified, and extended more easily. Design patterns use techniques such as abstract coupling and layering to promote loosely coupled systems.| Abstract Factory<sup>C-(ob)</sup> <br/> Bridge<sup>S-(ob)</sup> <br/> Chain of Responsibility<sup>B-(ob)</sup> <br/>Command<sup>B-(ob)</sup> <br/> Facade<sup>S-(ob)</sup> <br/> Mediator<sup>B-(ob)</sup> <br/> Observer<sup>B-(ob)</sup> <br/> | 
|  7 | **Extending functionality by subclassing.** Customizing an object by subclassing often isn't easy. Every new class has a fixed implementation overhead (initialization, finalization, etc.). Defining a subclass also requires an in-depth understanding of the parent class. For example, overriding one operation might require overriding another. An overridden operation might be required to call an inherited operation. And subclassing can lead to an explosion of classes, because you might have to introduce many new subclasses for even a simple extension. <br/> Object composition in general and delegation in particular provide flexible alter- natives to inheritance for combining behavior. New functionality can be added to an application by composing existing objects in new ways rather than by defining new subclasses of existing classes. On the other hand, heavy use of object com- position can make designs harder to understand. Many design patterns produce designs in which you can introduce customized functionality just by defining one subclass and composing its instances with existing ones.| Bridge<sup>S-(ob)</sup> <br/> Chain of Responsibility<sup>B-(ob)</sup> <br/> Composite<sup>S-(ob)</sup> <br/>Decorator<sup>S-(ob)</sup><br/> Observer<sup>B-(ob)</sup> <br/> Strategy<sup>B-(ob)</sup>|
|  8 | **Inability to alter classes conveniently.** Sometimes you have to modify a class that can't be modified conveniently. Perhaps you need the source code and don't have it (as may be the case with a commercial class library). Or maybe any change would require modifying lots of existing subclasses. Design patterns offer ways to modify classes in such circumstances. |Adapter<sup>S-(cl)</sup> <br/> Decorator<sup>S-(ob)</sup> <br/>Visitor<sup>B-(ob)</sup> | 


<hr/>

## Resources

[1] Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John (1995). Design Patterns. Massachusetts: Addison-Wesley. p.24. ISBN 0-201-63361-2. Retrieved 2023-12-13.