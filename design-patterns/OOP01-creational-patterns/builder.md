# Builder

"Separate the construction of a complex object from its representation so that the same construction process can create different representations"

## Terms

***`Director`*** - interfaces `Builder` -

***`Builder`*** - *interface only* - 

***`Concrete Builder`*** - *implementation of the interface*- 

***`Product`*** - 

```
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