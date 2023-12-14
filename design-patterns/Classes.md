# Classes
## Definitions and Explanations

The **class** specifies the object's internal data and representation (**class attributes**), and the operations the object can perform (**class methods**).
```
            ┌───────────────────────┐
            │       ClassName       │
            ├───────────────────────┤
            │      Operation1()     │
            │   Type Operation2()   │
            ├───────────────────────┤
            │   InstanceVariable1   │
            │Type InstanceVariable2 │
            └───────────────────────┘
```
**Instantiation** - Objects are created by instantiating a class. The process of instantiating a class **allocates memory** storage for the object's internal data and associates the operations with the data. 

```
            ┌─────────────┐
            │ ParentClass │
            ├─────────────┤
            │ Operation() │
            └──────┬──────┘
                   │
                   △
                   │
            ┌──────┴──────┐
            │ ChildClass  │
            ├─────────────┤
            │ Operation() │
            └─────────────┘
```
## Class Inheritance
**Inheritance** - The subclass inherits the definitions of all data and operations that is defined by the parent class. Inheritance is a mechanism for extending an application's functionality by reusing functionality in parent classes.

**Abstract Class** - is a common interface for a parent class too its subclasses. Abstract classes cannot be instantiated, but rather serves to help define its implementation for the subclasses. On a related note, **abstract methods** are operations that are declared but not implemented. 

**Concrete Class** - the 'opposite' of an Abstract class - a class that is implemented

**Method Override** - the act of creating class methods that modify the operations of the parent class to be customized for the subclass. 

```
            ┌─────────────────┐
            │  AbstractClass  │
            ├─────────────────┤
            │   Operation()   │
            └────────┬────────┘
                     │
                     △
                     │
            ┌────────┴────────┐
            │ConcreteSubclass │
            ├─────────────────┤
            │   Operation()   │
            └─────────────────┘
```

**Mixin Class** - provides an optional interface or functionality to the subclass. It is "mixed in" with the parent class to create the subclass. 
```
        ┌─────────────────────┐   ┌─────────────────────┐
        │    ExistingClass    │   │        Mixin        │
        ├─────────────────────┤   ├─────────────────────┤
        │ ExistingOperation() │   │   MixinOperation()  │
        └──────────┬──────────┘   └──────────┬──────────┘
                   │                         │
                   △─────────┐   ┌───────────△
                             │   │
                    ┌────────┴───┴────────┐
                    │   AugmentedClass    │
                    ├─────────────────────┤
                    │ ExistingOperation() │
                    │  MixinOperation()   │ 
                    └─────────────────────┘
```
### Benefits of Inheritance

The abstract class is the interface between the parent class and subclass. 
By manipulating the abstract, there are two benefits <sup>[1]</sup>:

1. Clients remain unaware of the specific types of objects they use, as long as objects adhere to the interface. 
2. Clients remain unaware of the classes that implement these objects; clients only know about the abstract classes defining the interface. 

<ins>The first principle of reusable Object-Oriented Design:</ins>

>***Program to an interface, not an implementation***

**Composition** - new functionality is obtained by assembling or composing objects to get more complex functionality. Composition is an alternative to inheritance. 

### Class Inheritance vs Class Composition
| |Inheritance|Composition|
|--|--|--|
|Advantages| -Supported directly by programming language; <br>-Defined statically at compile time;<br>-Makes it easier to modify the implementation being reused | Defined dynamically at run time via objects requiring references to other objects; <br>-Composition requires objects to be designed carefully to interface with other objects, and thus does not break encapsulation; <br>-Fewer implementation dependencies because an object's implementation is written around the interface |
|Disadvantages| -Cannot change the implementation at run time; <br> -Parent classes often define at least part of their subclasses' representation; <br>-Because the parent class reveals or exposes the details of its implementation to subclass, it is said to "break encapsulation"|-System's behavior will depend on the interrelationship among objects, instead of being defined in one class|

<ins>The second principle of reusable Object-Oriented Design:</ins>

>***Favor object composition over class inheritance***

### Class Composition and Delegation

**Delegation** - a pattern that allows an object to pass on certain responsibilities or tasks to another object. Delegation allows class composition to work in a way that is as powerful as class inheritance.

A <ins>**receiving object**</ins> receives a request or has a task to perform, but instead of handling the task directly, it delegates the task to another object. The <ins>**delegate object**</ins> performs the task on behalf of the receiving object.

"Deferring requests" in inheritance:
```
            ┌─────────────┐
            │ ParentClass │
            ├─────────────┤
            │operationA() ├──────┐
            └──────┬──────┘      │
                   │         inheriting behavior
                   △             │ 
                   │             │
            ┌──────┴──────┐      │
            │ ChildClass  │      │
            ├─────────────┤      │
            │operationB() │ <────┘ 
            └─────────────┘
```
"Delegating requests" in delegation:
```
            (receiver)                      (delegate)
    ┌─────────────┐               ┌─────────────┐   
    │  SomeClass  │               │AnotherClass │   
    ├─────────────┤               ├─────────────┤   
    │operationA() ├─────────────> │ operationA()│
    └──────┬──────┘               │ attributes  │  
           │                      └─────────────┘ 
           │
    return AnotherClass -> operationA
```
*A receiver (which receives a request) passes itself to the delegate (on behalf of receiver) to let the delegated operation refer to the receiver.*

Delegation allows ***behaviors to be composed at run-time***, and change the way it is composed. 

| composition | -might use->| delegation | |
|--|--|--|--|
|  A design principle where a class contains an object of another class as a part. The containing class is composed of, or has a reference to, the contained class | Composition can incorpoate delegation.-> | A design pattern that allows an object to pass on certain responsibilities or tasks to another object  | |
|  |  | -Delegation allows ***behaviors to be composed at run-time***, and change the way it is composed.<br/>-It can be a good design choice only when it simplifies more than it complicates.  | **Advantages**|
|  |  |  -Dynamic, highly parameterized software is harder to understand than more static software <br/> -Run-time inefficiencies| **Disadvantages**|

**State**, **Strategy**, and **Visitor** (<ins>Behavioral</ins> design patterns) require Delegation.

**Mediator** and **Chain of Responsibility** (<ins>Behavioral</ins> design patterns), and **Bridge** (<ins>Structural</ins> design pattern) use Delegation.

### Class Inheritance vs Parameteryzed types

**Parameteryzd types** are objects where the type is defined as a parameter at the point of use. 

| Language | Term | Example |
| -- | -- | -- |
| C++       | Templates |`template <typename T>` <br/> `class MyClass {`<br/> `··// code` <br/> `}`|
| Java      | Generics  | `public class MyClass<T> {` <br/> `··// code` <br/> `}`|
| Python    | Generics  | `from typing import TypeVar, Generic` <br/> `T = TypeVar('T')` <br/> `class MyContainer(Generic[T]):` <br/> `····# code`|
| Javascript| Generics  | no built in support |
| Typescript| Generics  |  `class MyClass<T> {` <br/> `··// code` <br/> `}` |
| Ruby      | Generics  | `require 'dry-types'` <br/> `module Types` <br> `··include Dry::Types.module` <br/> `end` <br/> `class MyContainer` <br/> `··include Types` <br/> `··# code` <br/> `end`|

Parameterized types are a third way (in addition to class inheritance and object composition) to compose behavior in object-oriented systems.


## Summary

***"Program to an interface, not an implementation"***

***"Favor object composition over class inheritance"***

***Class Inheritance***

***Composition*** and relatedly, ***delegation***

***Type Parameteryzation***


<hr/>
## Resources
[1] Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John (1995). Design Patterns. Massachusetts: Addison-Wesley. p.18. ISBN 0-201-63361-2. Retrieved 2023-12-13.