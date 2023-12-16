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
## Applicability 

Use the **Builder** pattern when <sup>[2]</sup>:

* the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled.

* the construction process must allow different representations for the object that's constructed.

## Comparison between Abstract Factory and Builder
```
    Abstract Factory                        Builder
                └───────────────┬──────────────┘
                      constructs│complex objects
                            ┌───┴───┐
                            │       ├─constructs a 
            emphasis on ────┘       ├─complex object
            a family of             ├─step 
        product objects             ├─by
                │                   ├─step
       product returned             │
            immediately         Builder returns product
                                        as final step.
``` 

"Abstract Factory is similar to Builder in that it too may construct complex objects. The primary difference is that the Builder pattern focuses on constructing a complex object step by step. Abstract Factory's emphasis is on families of product objects (either simple or complex). Builder returns the product as a final step, but as far as the Abstract Factory pattern is concerned, the product gets returned immediately." <sup>[3]</sup>

<hr>

[1] Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John (1995). Design Patterns. Massachusetts: Addison-Wesley. p.97. ISBN 0-201-63361-2. Retrieved 2023-12-13.

[2] Gamma *et. al.* p.98.

[3] Gamma *et. al.* p.105.