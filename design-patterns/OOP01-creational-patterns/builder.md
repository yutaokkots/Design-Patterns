# Builder

"Separate the construction of a complex object from its representation so that the same construction process can create different representations." <sup>[1]</sup>

*i.e.* Builder pattern focuses on constructing a complex object step by step. It decouples the representation from the process of constructing the complex object, so that the **same construction process** can be used for **different representations**.

A builder may be needed when an object cannot be produced in one step. 

## Terms

***`Director`*** - interfaces `Builder`; aggregation relationship - A director object is instantiated, and its `construct()` method is called. The `construct()` method calls a specific Concrete Builder, and calls methods of the Concrete Builder in a specific order. A `getResult()` method of the Concrete Builder object retrieves the Product. 

***`Builder`*** - *interface only* - an abstract base class, and defines the steps to correctly create a Product.

***`Concrete Builder`*** - *implementation of the Builder* - a concrete buider is specialized to create a particular complex Product.

***`Product`*** - the complex object to be created.

```
    Director class                   Builder class
    ┌────────────────┐  builder     ┌──────────────┐ 
    │Director        │<>────────────┤Builder       │
    ├────────────────┤              ├──────────────┤ 
    │builder:Builder │              │buildpart()   │ 
    │construct()     │              └───────┬──────┘ 
    └─────────────\──┘                      △      
                   \                        │
                    ╵               ┌───────┴────────────┐      ┌───────┐
                    ╵               │ConcreteBuilder     │- - - ┤Product│
      this.builder.buildPart()      ├────────────────────┤      └───────┘
                                    │buildpart()         │
                                    │getResult(): Product│
                                    └────────────────────┘
```


<hr>
[1] Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John (1995). Design Patterns. Massachusetts: Addison-Wesley. p.97. ISBN 0-201-63361-2. Retrieved 2023-12-13.