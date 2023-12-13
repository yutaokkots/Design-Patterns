# Structural Patterns

## Adapter Pattern

An Adapter allows incompatible interfaces to work together by providing a wrapper that converts the interface of a class into another interface that a client expects. It helps integrate existing systems and classes that otherwise couldn't collaborate.

## Bridge Pattern

A Bridge separates abstraction from implementation, allowing both to evolve independently. It is useful when you want to avoid a permanent binding between an abstraction and its implementation, providing flexibility in changing either without affecting the other.

## Composite Pattern

A Composite composes objects into tree structures to represent part-whole hierarchies. It allows clients to treat individual objects and compositions of objects uniformly, simplifying the client code and enabling the creation of complex structures.

## Decorator Pattern

A Decorator attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality, allowing behavior to be added incrementally and facilitating the creation of complex combinations of behaviors.

## Facade Pattern

A Facade provides a unified interface to a set of interfaces in a subsystem, making it easier to use. It simplifies a complex system by providing a higher-level interface, which is more convenient for clients.

## Flyweight Pattern

A Flyweight minimizes memory usage or computational expenses by sharing as much as possible with related objects. It is particularly useful when dealing with a large number of similar objects, helping improve performance and reduce resource consumption.

## Proxy Pattern

A Proxy provides a surrogate or placeholder for another object to control access to it. It is useful in scenarios where you want to add an extra layer of control, such as lazy loading, access control, or logging, without modifying the actual object.