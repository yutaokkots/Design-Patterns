# Prototype

The Prototype method is a creational design method. 

A prototypical instance (already instantiated) is cloned to create new objects. 

* avoids using subclasses (e.g. that are found in the factory method). 
* avoids using the `new` keyword (e.g. in C++, which is an expensive operation - can be hundreds of machine calls)
    - prototype does not invoke `new` on a hard-coded class name

Instead:

* calls `clone()` method on prototype; or
* calls a factory method to create a derived class (provide a parameter to designate the particular derived class); or
* calls `clone()` method through a mechanism provided by another design pattern. 

## Background Example

A traditional approach to copying an existing object involves -> 

> creating a new object of the same class and manually copying the values and applying the functionalities of the original object. 

However, there are challenges with this approach:

**Accessibility of Fields**: Some fields of the original object may be private or protected, making it challenging to directly access and copy their values from outside the object.

**Dependency on Other Classes**: The process of copying an object may involve dependencies on the internal implementation of the class, making your code dependent on the details of that class. This is generally considered undesirable in software development because it can lead to tight coupling and maintenance issues.

## Prototype Example

With Prototype patterns, a prototypical instance (*i.e.* an object that has already been instantiated from a class) is cloned. 

And example is with the following Person Abstract class, and the Teacher concrete class and Student concrete class. 

```
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name) -> None:
        self.name = name
    
    @abstractmethod             # clone() and display() are abstract methods.
    def clone(self):            # Designating abstract methods ensures that
        ...                     #   concrete classes provide a concrete 
                                #   implementation of these methods -   
    @abstractmethod             #   explicit design intent.
    def display(self):             
        ...

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name;
```

```
                ┌─────────────────┐
                │  AbstractPerson │
                ├─────────────────┤
                │self.name        │
                │clone() - abstr  │
                │display() - abstr│
                │get_name()       │
                │set_name()       │
                └─────────────────┘
```
The Teacher and Student classes are concrete subclasses of the Person class
```
import copy
from person import Person

class Teacher(Person):
    def __init__(self, name:str, course: str) -> None:
        super().__init__(name)
        self._course = course
    
    def clone(self):
        return copy.copy(self)
    
    def display(self):
        print("Teacher was cloned:")
        print("--------------------")
        print(f"Name: {self.name}")
        print(f"Teaches: {self._course}")
        return super().display
    
    def get_course(self) -> str:
        return self._course

    def set_course(self, course: str) -> None:
        self._course = course
```
```
import copy
from person import Person
from teacher import Teacher

class Student(Person):
    def __init__(self, name, teacher:Teacher) -> None:
        super().__init__(name)
        self._teacher = teacher

    def clone(self):
        return copy.deepcopy(self)
    
    def display(self):
        print("Student was cloned:")
        print("--------------------")
        print(f"Student Name: {self.name}")
        print(f"Enrolled in: {self._teacher.get_course()}")
        print(f"Taught by: {self._teacher.get_name()}")
        return super().display
```
The Teacher and Student concrete subclasses are created from the Person Class.

The Abstract Person class has an abstract method, `clone()`. 

Further inside the Teacher and Student subclasses,`clone()` is defined. 
    Teacher.clone() creates a shallow copy (copy.copy(self))
    Student.clone() creates a deep copy (copy.deepcopy(self))

```
                ┌───────────────────┐
                │  AbstractPerson   │
                ├───────────────────┤
                │self.name          │
                │clone() - abstrM   │
                │display() - abstrM │
                │get_name()         │
                │set_name()         │
                └───────┬───┬───────┘
                        △   △
concretePrototype   ┌───┘   └───────────┐   concretePrototype
    ┌───────────────┴───────┐       ┌───┴───────────────────────┐
    │      Teacher          │       │     Student               │
    ├───────────────────────┤       ├───────────────────────────┤
    │self.name (super)      │       │self.name (super)          │
    │self.course            │       │self.teacher               │
    │clone() (clone.clone())│       │clone() (clone.deepclone())│
    │display()              │       │display()                  │
    │get_course()           │       └───────────────────────────┘
    │set_course()           │               .
    └───────────────────────┘   once instantiated, call clone()
            .                   to create a copy 
            .                   (rather than creating a new instance) 
            .                               .
            .                               .   
┌ - - - - - ┴ - - - - - - - - - - - ┐       .
| teacher = Teacher("Sean Cambpell",|       .        
|     "Creational Design Patterns   |       .        
|     in Python")                   |       .        
├ - - - - - - - - - - - - - - - - - ┤       .       
|self.name = "Sean Cambpell"        |       .       
|self.course = "Creational De..."   |       .       
|clone()                            |       .       
|display()                          |       .       
└ - - - - - - - - - - - - - - - - - ┘       .       
        ^       ┌ - - - - - - - - - - - - - ┴ - ┐
        |       | student = Student("Emma       | 
        └ - - - ┤     Ortebana", teacher)       | 
                ├ - - - - - - - - - - - - - - - ┤
                |self.name = "Emma Ortebana"    |
                |self.teacher = "Sean Cambpell" |
                |clone()                        | <─┐
                |display()                      |   │
                └ - - - - - - - - - - - - - - - ┘   │
                  ┌ - - - - - - - - - - - - - - - ┐ │
                  | studentClone = student.clone()├─┘
                  ├ - - - - - - - - - - - - - - - ┤
                  |self.name = "Emma Ortebana"    |
                  |self.teacher = "Sean Cambpell" |
                  |clone()                        |
                  |display()                      |
                  └ - - - - - - - - - - - - - - - ┘
```
The following is an example of calling the clone() method.

```
teacher = Teacher("Sean Cambpell", "Creational Design Patterns in Python")
teacherClone = teacher.clone()
teacherClone.display()

student = Student("Emma Ortebana", teacherClone)
studentClone = student.clone()
studentClone.display()

# modify the teacher clone:
teacherClone.set_course("Python Fundamentals")
studentClone.display()
```

### Advantages:

**Flexible Object Structure**: The Prototype pattern supports the instantiation of complex, user-defined structures, particularly useful in applications building objects from parts and subparts. For example, adding a subcircuit as a prototype allows the creation of circuits with varying structures.

**Specifying New Objects by Varying Values**: The Prototype pattern allows the definition of new object behaviors in dynamic systems by specifying variable values (object composition), avoiding the need for creating new classes. Users can effectively define new "classes" by instantiating existing ones, reducing the overall number of required classes.

**Configuring an Application with Classes Dynamically:** In certain run-time environments that support dynamic class loading, the Prototype pattern plays a crucial role. It allows applications to create instances of dynamically loaded classes without static constructor references. The runtime environment automatically generates instances upon loading and registers them with a prototype manager, enabling the request for instances of newly loaded classes, even those not originally linked with the program. 

**Dynamic object integration - Adding and Removing Products at Run-time**: Prototypes facilitate the integration of a new concrete product class into a system by allowing the registration of a prototypical instance with the client. This offers greater flexibility compared to other creational patterns, as clients can dynamically install and remove prototypes, during run-time.

**Reduced Subclass Proliferation and Complexity**: Unlike other Creational Design Patterns may lead to a proliferation of subclasses, the Prototype Design Pattern helps eliminate this proliferation issue. Prototypes allow new objects to be created without the need for an excessive number of subclasses, simplifying management in large projects.

**Elimination of Creator Class Hierarchy** In contrast to the Factory Method pattern, the Prototype pattern facilitates object creation by cloning a prototype, eliminating the need for a Creator class hierarchy. This is especially beneficial in languages like C++ where classes are not treated as first-class objects.

### Disadvantages:

**Abstraction Support**: The Prototype Design Pattern facilitates abstraction by concealing the concrete implementation details of a class.

**Resource Overhead**: Depending on the project's scale and the number of objects in use, the Prototype Design Pattern may lead to a potential waste of resources at a lower level. This could be considered overkill for projects with a minimal number of objects.

### Applicability:

**Independence from Concrete Class**: The Prototype method provides a way to implement new objects without relying on the specific details of the concrete class.

**Problem Resolution**: The Prototype method addresses recurring and complex problems in software development.