# Behavioral Patterns

## Chain of Responsibility

The Chain of Responsibility Pattern allows requests to be passed along a chain of handlers. It allows multiple objects to handle a request without the sender needing to know which object will ultimately process the request, promoting flexibility and decoupling.

## Command

The Command Pattern turns a request into a stand-alone object, containing all the information about the request. It allows for parameterization of objects, queuing of requests, and supporting undoable operations.

## Interpreter

The Interpreter Pattern defines a grammar for interpreting the sentences in a language and provides an interpreter to interpret the sentences. It is useful for creating language interpreters or compilers.

## Iterator

The Iterator Pattern provides a way to access elements of an aggregate object sequentially without exposing its underlying representation. It simplifies the traversal of collections and allows for uniform access to the elements.

## Mediator

The Mediator Pattern defines an object that centralizes communication between other objects, thus reducing direct connections between them. It promotes loose coupling by allowing objects to interact without having explicit references to each other.

## Memento

The Memento Pattern captures and externalizes an object's internal state so that the object can be restored to this state later. It provides a mechanism for undoing operations or restoring an object to a previous state.

## Observer

The Observer Pattern defines a one-to-many dependency between objects, ensuring that when one object changes its state, all its dependents are notified and updated automatically. It promotes a loosely coupled design where the subject and observers are independent entities.

## State

The State Pattern allows an object to alter its behavior when its internal state changes. It enables an object to change its behavior at runtime without changing its class, improving maintainability and flexibility.

## Strategy

The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows the client to choose the appropriate algorithm at runtime, promoting flexibility in selecting and using algorithms.

## Template method

The Template Method Pattern defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure. It provides a way to define the algorithm's structure while allowing variations in the implementation.

## Visitor

The Visitor Pattern represents an operation to be performed on the elements of an object structure. It lets you define a new operation without changing the classes of the elements on which it operates, promoting extensibility.