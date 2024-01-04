# S.O.L.I.D. Principles 

In 2004 or thereabouts, [Michael Feathers](https://michaelfeathers.silvrback.com) sent me an email saying that if I rearranged the principles, their first words would spell the word SOLID - and thus the SOLID principles were born.<sup>[1]</sup>

<hr/>

$~~~~~~$ **<u>S</u>ingle Responsibility Principle** - *There should never be more than one reason for a class to change.*

$~~~~~~$ **<u>O</u>pen-Closed Principle** - *A module should be open for extension but closed for modification.*

$~~~~~~$ **<u>L</u>iskov Substitution Principle** - *Subclasses should be substitutable for their base classes.*

$~~~~~~$ **<u>I</u>nterface Segregation Principle** - *Many client specific interfaces are better than one general purpose interface.*

$~~~~~~$ **<u>D</u>ependency Inversion Principle** - *Depend upon Abstractions. Do not depend upon concretions.*

<hr/>

<div align="center">

## **The Single Responsibility Principle (SRP)**


***There should never be more than one reason for a class to change.***

</div>

$~~~~~~~~~~~$ "<ins>A Responsibility is a person</ins>. It's not something that the code does; it's a ***person*** - a person who wants to make a change in the code.

$~~~~~~~~~~~$ "'My code has a responsibilty to that business guy who wants the rules changed. My code has a responsibilty to that clerk who wants the format changed.'

$~~~~~~~~~~~$ "... The Single Responsibility Principle says: any module should be responsible to only ***one person***." <sup>[4]</sup>

<br/>

The single responsibility principle states that every module, class, or function in code should have only one responsibility, and only one reason for the code to be modified.

***Separation of concerns*** -> different aspects or responsibilities of a system should be handled by different classes. (Edsger Dijkstra)

Cohesion refers to how closely the methods and properties of a class are related. SRP contributes to achieving ***high cohesion*** by ensuring that a class's methods are related to a single responsibility.

<div align="center">

## **The Open-Closed Principle (OCP)**

***A module should be open for extension but closed for modification.*** 
Bertrand Meyer

</div>

Change the behavior of the modules without changing the source code of the modules.

*i.e.* write modules so they can be extended, without having to modify them. 

### Dynamic polymorphism (run-time polymorphism)

    method overriding

```
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

# Example of dynamic polymorphism
shapes = [Circle(), Square()]

for shape in shapes:
    shape.draw()
```

### Static polymorphism (compile-time polymorphism)
    method overloading, operator overloading
    templates or generics
    the add method is defined with different parameter types, and the correct version of the method is determined at runtime based on the argument types.

```
class MathOperations:
    def add(self, a, b):
        return a + b

# Example of static polymorphism
math = MathOperations()

result_int = math.add(5, 7)
result_float = math.add(3.5, 2.5)

print(result_int)    # Output: 12
print(result_float)  # Output: 6.0
```

<div align="center">

## **Liskov Substitution Principle (LSP)**

***Subclasses should be substitutable for their base classes.*** Barbara Liskov

</div>

$~~~~~~~~~~~$ "A subtype should behave like a super type as far as you can tell by using the super type methods. So it wasn't that it couldn't behave differently, it's just that as long as you limited your interaction with its ojects to the super type methods, you would get the behavior you expected... Technically it's called behavioral subtyping - subtypes behave like super types." - [Barbara Liskov](https://www.youtube.com/watch?app=desktop&v=-Z-17h3jG0A) <sup>[2]</sup>

<br>

"Derived classes should be substitutable for their base classes. That is, a user of a base class should continue to function properly if a derivative of that base class is passed to it."

Derived methods should expect no more and provide no less:
A derived class is substitutible if its preconditions are no stronger than the base class method.
A derived class is substitutible if its postconditions are no weaker than the base class method.




<div align="center">

## **The Interface Segregation Principle (ISP)**

***Many client specific interfaces are better than one general purpose interface.***

</div>

<div align="center">

## **The Dependency Inversion Principle (DIP)**

***Depend upon Abstractions. Do not depend upon concretions.***

</div>

<hr>

## **Separation of Concerns**

Let me try to explain to you, what to my taste is characteristic for all intelligent thinking. It is, that one is willing to study in depth an aspect of one's subject matter in isolation for the sake of its own consistency, all the time knowing that one is occupying oneself only with one of the aspects. We know that a program must be correct and we can study it from that viewpoint only; we also know that it should be efficient and we can study its efficiency on another day, so to speak. In another mood we may ask ourselves whether, and if so: why, the program is desirable. But nothing is gained —on the contrary!— by tackling these various aspects simultaneously. It is what I sometimes have called **"the separation of concerns"**, which, even if not perfectly possible, is yet the only available technique for effective ordering of one's thoughts, that I know of. This is what I mean by "focussing one's attention upon some aspect": it does not mean ignoring the other aspects, it is just doing justice to the fact that from this aspect's point of view, the other is irrelevant. It is being one- and multiple-track minded simultaneously. <sup>[3]</sup> 
Edsger W. Dijkstra. 

<hr>

<sup>[1]</sup> Martin, Robert Cecil (2018). Clean Architecture: A Craftsman's Guide to Software Structure and Design. p. 58. ISBN 9780134494166.

<sup>[2]</sup> Liskov, Barbara. Interview by Tom van Vleck for the Association for Computing Machinery on April 20, 2016 https://www.youtube.com/watch?app=desktop&v=-Z-17h3jG0A Retrieved Dec. 30, 2023.

<sup>[3]</sup> Dijkstra, Edsger W. On the role of scientific thought. Transcribed by Richard Walker. https://www.cs.utexas.edu/users/EWD/transcriptions/EWD04xx/EWD447.html. 30th August 1974. Last revised on Mon, 25 Oct 2010. Retrieved Dec. 30, 2023.

<sup>[4]</sup> Martin, Robert Cecil. The Single Responsibility Principle. gnbitcom. https://www.youtube.com/watch?app=desktop&v=Gt0M_OHKhQE Published June 3, 2014.