# Creational Patterns

**Creational design patterns** deal with the mechanisms of **object creation**, or abstracting the **instantiation process**. 

- A *class creational pattern* uses inheritance to vary the class it has instantiated. 
- An *object creational pattern* delegates instantiation to another object.

## Design Pattern Table

|<span style='color: blue;'>|Creational</span>|Structural|Behavioral|
|---|---|---|---|
|**class**|factory|adapter|interpretor<br/> template method|
|**object**|abstract<br/> builder<br/> prototype<br/> singleton|adapter<br/> bridge<br/> composite<br/> decorator<br/> facade<br/> flyweight<br/> proxy|chain of responsibility<br/> command<br/> iterator<br/> mediator<br/> memento<br/> observer<br/> state<br/> strategy<br/> visitor|

## Factory Method Pattern

The factory method pattern defines an interface for creating an object but allows subclasses to alter the type of objects that will be created. It promotes loose coupling between the creator and the products, providing flexibility in instantiating different types of objects.

## Abstract Factory Pattern

Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. It allows the system to be independent of how its objects are created, composed, and represented, promoting flexibility in object creation.

## Builder Pattern

The Builder Pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations. This pattern helps manage the construction of complex objects step by step and facilitates the creation of varied products.

## Prototype Pattern

The Prototype Pattern creates new objects by copying an existing object known as the prototype. This approach is useful when the cost of creating an object is more expensive than copying an existing one. It enhances performance and promotes object reuse.

## Singleton Pattern

The Singleton Pattern ensures a class has only one instance and provides a global point of access to that instance. It is useful when exactly one object is needed to coordinate actions across the system, like a configuration manager or a logging service.