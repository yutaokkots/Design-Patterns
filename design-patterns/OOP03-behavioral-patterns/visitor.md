# Visitor

Visitor allows defining a new operation (new method) without changing the classes of the elements on which it operates. <sup>[1]</sup> 

*i.e.* No need to add an entirely new method to each class such that it changes the composite. 

Separates **the algorithm** from the **object structure**.
This separation allows new operations to be added to existing object structures without modifying the structures.

Add capabilities to a composite of objects, where encapsulation is not important. <sup>[2]</sup> 

### Visitor

A Visitor pattern may generally consists of two key methods:

* visit() - implemented by the visitor, and used and called for every element of the data structure
* accept() - implemented by the visitable classes, allowing the Visitor to visit those classes. 


```
┌───────────┐               ┌───────────────────────┐
│Client     │               │AbstractVisitor        │
└───┬───────┘               ├───────────────────────┤
    │                       │VisitConcrElA(ConcrElA)│
    │                       │VisitConcrElB(ConcrElB)│
    │                       └──────────┬────────────┘
    │                                  △
    │                       ┌──────────┴────────────┐
    │       ┌───────────────┴───────┐   ┌───────────┴───────────┐
    │       │ConcreteVisitorA       │   │ConcreteVisitorA       │
    │       ├───────────────────────┤   ├───────────────────────┤
    │       │VisitConcrElA(ConcrElA)│   │VisitConcrElA(ConcrElA)│
    │       │VisitConcrElB(ConcrElB)│   │VisitConcrElB(ConcrElB)│
    │       └───────────────────────┘   └───────────────────────┘
    │   ┌──────────────────┐        ┌───────────────┐ 
    └──>│ObjectStructure   │----->  │Element        │
        └──────────────────┘        ├───────────────┤ 
                                    │Accept(Visitor)│ 
                                    └───────┬───────┘ 
                                            △
                                ┌───────────┴───────────┐
                    ┌───────────┴───────────┐   ┌───────┴───────────────┐
                    │ConcreteElementA       │   │ConcreteElementB       │
                    ├───────────────────────┤   ├───────────────────────┤
                    │Accept(Visitor v)      │   │Accept(Visitor v)      │
                    │OperationA             │   │OperationB             │
                    └───────────────────────┘   └───────────────────────┘
```

In the following example, 
```

```

<hr/>
<sup>[1]</sup> Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John (1995). Design Patterns. Massachusetts: Addison-Wesley. p.331. ISBN 0-201-63361-2. Retrieved 2023-12-13.

<sup>[2]</sup> Freeman *et al.*. Head First Design Patterns. 2004. p628.