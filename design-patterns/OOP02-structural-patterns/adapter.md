# Adapter

## General diagrams for a class Adapter and object Adapter

### **Class Adapter**
Multiple Inheritance style implementation.
```
                         Interface-
┌──────┐    ┌───────────┐Target cannot  ┌───────────────────┐
│client├───>│InterTarget│call adaptee   │ Adaptee           │
└──────┘    ├───────────┤directly.      ├───────────────────┤ 
            │ request() │• • • • • • • >│ specificRequest() │
            └───┬───────┘               └────────┬──────────┘
                △   ┌────────────────△ (inheritance)     
            ┌───┴───┴───┐
            │ Adapter   │ 
            ├───────────┤ 
            │ request() │ 
            └───────────┘
```
### **Object Adapter**
Composition style implementation.
```
                         Interface-
┌──────┐    ┌───────────┐Target cannot  ┌───────────────────┐
│client├───>│InterTarget│call adaptee ┌>│ Adaptee           │
└──────┘    ├───────────┤directly.    │ ├───────────────────┤ 
            │ request() │• • • • • • >│ │ specificRequest() │
            └─────┬─────┘             │ └───────────────────┘
                  △                   │    
            ┌─────┴─────┐             │(association)   
            │ Adapter   ├─────────────┘
            ├───────────┤The Adapter instantiates Adaptee 
            │ request() │class inside the Adapter (through
            └───────────┘the constructor). Creates an Object.
```

## Important notes about Adapters

1. Can be confused with:
* **Adapter** - making two interfaces that are not compatible, compatible.
* **Facade** - taking complex interactions into a simplified interface. 
* **Proxy** - calling a substitute, and substitute calls the target.
* **Decorator** - adding a behavior to an object without modifying the object.

2. The intent of using adapters is to make two interfaces interoperable. The intent of adapters is ***not to change the underlying behavior*** of the InterfaceTarget. 
