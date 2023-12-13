# Classes

The class specifies the object's internal data and representation (**class attributes**), and the operations the object can perform (**class methods**).

|`ClassName`|
:-------------
|`Operation1()`<br/> `Type Operation2()`|
|`InstanceVariable1` <br/> `Type InstanceVariable2`|

**Instantiation** - Objects are created by instantiating a class. The process of instantiating a class **allocates memory** storage for the object's internal data and associates the operations with the data. 

```
| ParentClass |
 -------------
| Operation() |

       |
       △
       |

| ChildClass |
 -------------
| Operation()|

```

**Inheritance** - The subclass inherits the definitions of all data and operations that is defined by the parent class.

**Abstract Class** - is a common interface for a parent class too its subclasses. Abstract classes cannot be instantiated, but rather serves to help define its implementation for the subclasses. On a related note, **abstract methods** are operations that are declared but not implemented. 

**Concrete Class** - the 'opposite' of an Abstract class - a class that is implemented

**Method Override** - the act of creating class methods that modify the operations of the parent class to be customized for the subclass. 

```
  |AbstractClass|
   -------------
  | Operation() |

         |
         △
         |

| ConcreteSubclass |
 ------------------
|    Operation()   |
```

**Mixin Class** - provides an optional interface or functionality to the subclass. It is "mixed in" with the parent class to create the subclas. 
