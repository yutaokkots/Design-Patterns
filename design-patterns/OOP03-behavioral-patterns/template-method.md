# Template Method

The algorithm's invariant operations are defined in the Abstracted class, and variable and specific operattions are further specified in the subclasses. 

## **UML diagram for Template Pattern**

```
    ┌───────────────────────┐
    │AbstractTemplate       │
    ├───────────────────────┤       ┌───────────────────────┐
    │TemplateMethod()    <─ ┼ ─ ─ ─ ┤ ...                   │
    │PrimitiveOperation1()  │       │PrimitiveOperation1()  │     
    │PrimitiveOperation2()  │       │ ...                   │
    └──────────┬────────────┘       │PrimitiveOperation2()  │
               △                    │ ...                   │
    ┌──────────┴────────────┐       └───────────────────────┘
    │ConcreteTemplate       │
    ├───────────────────────┤
    │PrimitiveOperation1()  │
    │PrimitiveOperation2()  │
    └───────────────────────┘
```
The ConcreteTemplate class relies on the AbstractTemplate to implement the **invariant steps**. 

## **UML diagram for Template example**
Example of template method with coffee. 

```
                ┌───────────────────────┐
                │AbstractBeverage       │
                ├───────────────────────┤
                │TemplateMethod()       │
                │PrimitiveOperation1()  │ 
                │@abstractmethod        │   
                │PrimitiveOperation2()  │
                │PrimitiveOperation3()  │
                │@abstractmethod        │   
                │PrimitiveOperation4()  │
                └──────────┬────────────┘
                           △             
                ┌──────────┴────────────┐
    ┌───────────┴───────────┐   ┌───────┴───────────────┐
    │ConcreteTemplateCoffee │   │ConcreteTemplateTea    │
    ├───────────────────────┤   ├───────────────────────┤
    │PrimitiveOperation2()  │   │PrimitiveOperation2()  │
    │PrimitiveOperation4()  │   │PrimitiveOperation4()  │
    └───────────────────────┘   └───────────────────────┘
```

Abstract Template Class
```
abstract_template.py

from abc import ABC, abstractmethod

class AbstractTemplateCaffeineBeverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print(f"Heat up water to 100°C")

    @abstractmethod
    def brew(self):
        ...

    def pour_in_cup(self):
        print("Pour beverage into cup.")

    @abstractmethod
    def add_condiments(self):
        ...
```

Concrete Template Class for Coffee
```
template_coffee.py

from abstract_template import AbstractTemplateCaffeineBeverage

class ConcreteCoffee(AbstractTemplateCaffeineBeverage):
    def brew(self):
        print("Hot-water passed through filter containing ground coffee.")

    def add_condiments(self):
        print("Milk added to coffee.")
```

Concrete Template Class for Tea
```
template_tea.py

from abstract_template import AbstractTemplateCaffeineBeverage

class ConcreteTea(AbstractTemplateCaffeineBeverage):
    def brew(self):
        print("Tea-bag placed in hot-water and brewing.")

    def add_condiments(self):
        print("Lemon added to tea.")
```

Execution of the program:

```
main.py

"""Main doc for Template Method Design Pattern."""
from template_coffee import ConcreteCoffee
from template_tea import ConcreteTea

def main():
    coffee = ConcreteCoffee()
    coffee.prepare_recipe()
    """
        Heat up water to 100°C
        Hot-water passed through filter containing ground coffee.
        Pour beverage into cup.
        Milk added to coffee.  
    """
    tea = ConcreteTea()
    tea.prepare_recipe()
    """
        Heat up water to 100°C
        Tea-bag placed in hot-water and brewing.
        Pour beverage into cup.
        Lemon added to tea.
    """

if __name__ == "__main__":
    main()

```