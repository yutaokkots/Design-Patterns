# Visitor

Visitor allows defining a new operation without changing the classes of the elements on which it operates. <sup>[1]</sup> 

Separates **the algorithm** from the **object structure**.
This separation allows new operations to be added to existing object structures without modifying the structures.

Add capabilities to a composite of objects, where encapsulation is not important. <sup>[2]</sup> 

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

<hr/>
<sup>[1]</sup> Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John (1995). Design Patterns. Massachusetts: Addison-Wesley. p.331. ISBN 0-201-63361-2. Retrieved 2023-12-13.

<sup>[2]</sup> Freeman *et al.*. Head First Design Patterns. 2004. p628.