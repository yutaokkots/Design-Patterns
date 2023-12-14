# Overview on Design Patterns

> One thing expert designers know not to do is solve every problem from first principles. Rather, they reuse solutions that have worked for them in the past. When they find a good solution, they use it again and again. Such experience is part of what makes them experts. Consequently, you'll find recurring patterns of classes and communicating objects in many object-oriented systems. These patterns solve specific design problems and make object-oriented designs more flexible, elegant, and ultimately reusable. They help designers reuse successful designs by basing new designs on prior experience. A designer who is familiar with such patterns can apply them immediately to design problems without having to rediscover them. [1]

>[Design patterns are] *descriptions of communicating objects and classes that are customized to solve a general design problem in a particular contex*.[2]

## Importance of Design Patterns

- Because design patterns encapsulate solutions to recurring problems, conceptualizing and understanding patterns allows for an **abstraction for reasoning about designs**. 
- The patterns integrate and encapsulate **best practices** that have been proven to work. 
- Bridges the gap between high level design concepts with implementation allowing for easier **transition between design and development**. 
- Having a common **design vocabulary** allows common language for discussion among developers.
- Patterns enable **documentation** of explicit solutions to common problems.

## Elements of a design pattern

- **pattern name**: describes (1) the design pattern (in a one or two words); (2) the solution; and (3) its consequences.
- **problem**: describes when to apply the pattern. 
- **solution**: describes the elements that make up the design, relationships, responsibilities, and collaboration.
- **consequences**: describes the results and tradeoffs of applying the pattern.

## Design Pattern Categorization

||Creational|Structural|Behavioral|
|---|---|---|---|
|**class**|factory|adapter|interpretor<br/> template method|
|**object**|abstract factory<br/> builder<br/> prototype<br/> singleton|adapter<br/> bridge<br/> composite<br/> decorator<br/> facade<br/> flyweight<br/> proxy|chain of responsibility<br/> command<br/> iterator<br/> mediator<br/> memento<br/> observer<br/> state<br/> strategy<br/> visitor|





[1] Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John (1995). Design Patterns. Massachusetts: Addison-Wesley. p.1. ISBN 0-201-63361-2. Retrieved 2023-12-13.

[2] Gamma *et. al.* p.3.

additional resources: https://github.com/faif/python-patterns