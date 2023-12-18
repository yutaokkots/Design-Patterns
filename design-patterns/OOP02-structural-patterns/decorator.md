# Decorator

Decorators change the behavior of an object at runtime (and not at compile time); decorators attach additional responsibility to an object dynamically.

<ins>A decorator ***has a*** component and **is a** component.</ins>

Once the decorator/wrapper is set around the object, the decorator
itself can be used, and ***is*** the ***same type*** as the original object. That means that the decorator can be treated the same way as the original object.

Similarities with other patterns:

* The decorator pattern resembles a composite design pattern, though much simpler. 

* The decorator ***is*** the ***same type*** as the wrapped object, and this ***"is a"*** relationship resembles the proxy design pattern.

According to Gamma *et al.*, the second rule of *reusable* OOP is:
<div align="center">
<span style="color:darkred">

***Favor object composition over class inheritance.***

</span></div>

Inheritance is not conducive to code reuse or sharing behavior, because the subclass/instantiated object can only inherit the behavior of its parent class. 

The concept of ***composition***, and not inheritance, ***is used to share behavior***, and <ins>decorators *provide an alternative to subclassing* for extending functionality</ins>.

**Decorators use composition to extend functionality.**

```
    ┌─────────────────────────┐
    │    DecoratorTwo         │    
    │ ┌─────────────────────┐ │
    │ │  DecoratorOne       │ │ 
    │ │ ┌─────────────────┐ │ │
    │ │ │Object/Component │ │ │     
    │ │ │attributes       │ │ │ 
    │ │ │methods()        │ │ │ 
    │ │ └─────────────────┘ ├─│─  ─ ─  ─ ─ ┐ 
    │ └─────────────────────┘ │             
    └───────┬─────────────────┘            │
                                           
            │                              │
             
    ┌─────────────────────────┐            │
    │    DecoratorTwo         │     ┌─────────────────────┐ 
    │                         │     │  DecoratorOne       │ 
    │                         │     │                     │ 
    │                         │     │                     │      
    │                         │     │                     │  
    │                         │     │                     │  
    │                         │     │                     │ 
    │                         │     └─────────────────────┘ 
    └─────────────────────────┘        Use this decorator,
      Use this decorator,              it has the same type
      it has the same type             as the Object/Component
      as the Object/Component
```

## **Incorrect way to set variations:**
### ***Class explosion***
```
                ┌───────────────────┐ 
                │ AbstractBeverage  │
                ├───────────────────┤
                │ description()     │
                │                   │
                │ @abstractmethod   │ 
                │ cost()            │
                └──┬───┬───┬───┬───┬┘
                   △   △   △   △   △ ─── ...  
        ┌──────────┘┌──┘   └──┐└──────────┐
   ┌────┴───┐ ┌─────┴───┐ ┌───┴─────┐ ┌───┴────┐
   │coffee  │ │coffee   │ │coffee   │ │espresso│
   │w cream │ │w/hazel  │ │w milk   │ │        │
   └────────┘ └─────────┘ └─────────┘ └────────┘
```

### ***Boolean values + conditional statements***
```
                ┌───────────────────┐ 
                │ AbstractBeverage  │
                ├───────────────────┤
                │ self.hasMilk:bool │
                │ self.hasCream:bool│
                │ self.hasSyrup:bool│
                │ self.isEsp:bool   │ 
                | self.x1EspSh:bool |
                | self.x2EspSh:bool |
                | self.x3EspSh:bool |
                │        ...        │
                │ @abstractmethod   │ 
                │ cost()            │
                └──┬───┬───┬────┬──┬┘
                   △   △   △    △  △ ─── ... 
        ┌──────────┘   └─┐ └───┐└──────────┐
   ┌────┴─────────┐┌─────┴───┐┌┴────────┐ ┌┴───────┐
   │coffee        ││coffee   ││coffee   │ │espresso│
   │w cream       ││w/hazel  ││w milk   │ │        │
   ├──────────────┤├─────────┤├─────────┤ ├────────┤   
   │self.hasMilk  ││  ...    ││  ...    │ │  ...   │      
   │       = False│└─────────┘└─────────┘ └────────┘       
   │self.hasCream │                                          
   │       = True │
   │self.hasSyrup │                                           
   │       = False│                                            
   │self.isEsp    │                                      
   │       = False│ 
   │self.x1EspSh  │                                      
   │       = False│   
   │self.x2EspSh  │                                      
   │       = False│   
   │self.x3EspSh  │                                      
   │       = False│        
   │      ...     │
   │parentMethod()│                                       
   └──────────────┘    
```
Coding like the above examples is problematic because:

(1) it violates the Interface Segregation Principle.

<div align="center">
<span style="color:darkred">

***No code should be forced to depend on methods it does not use.***

</span></div>

The subclasses (Drinks) are forced to inherit parent class methods (Beverage), that a subclass may not ever use or is not applicable. 

(2) in order to later change customizations for the subclasses, the parent class must be edited. More boolean values must be added. 

Adding additional code to the parent class in order to customize subclasses can lead to unwieldly code. 

## **Using a Decorator in the above Beverage example**

Using a decorator can be applied to the above example, but **may not be the most suitable**. See below.  

Introduce a condiment decorator (AddOnDecorator).

AddOnDecorator ***is a Beverage*** and ***has a Beverage***. 

```
        ┌───────────────────┐        ┌───────────────────┐
        │ CaramelDecorator  │─────┐  │ SoyMilkDecorator  │─┐
        ├───────────────────┤     │  ├───────────────────┤ │
        │ getDescription()  │     │  │ getDescription()  │ │
        │                   │     │  │                   │ │
        │ @abstractmethod   │     │  │ @abstractmethod   │ │
        │ cost() # cost =  1│     │  │ cost()  # cost = 2│ │
        └───────────────────┘     │  └───────────────────┘ │
        ┌───────────────────┐     │                        │
        │ AbstractBeverage  │───┐ │                        │
        ├───────────────────┤   │ │                        │
        │ description()     │   │ │                        │
        │                   │   │ │                        │
        │ @abstractmethod   │   │ │                        │
        │ cost()            │   │ │                        │
        └───────────────────┘   │ │                        │
                                │ │                        │
┌─────────────────────────────┐ │ │                        │
│    SoyMilkDecorator         │─│─│────────────────────────┘
│ ┌────────────────────────┐  │ │ │
│ │  CaramelDecorator      │──│─│─┘ 
│ │ ┌────────────────────┐ │  │ │ 
│ │ │Decaf Coffee #cost=3│─│─ │─┘    cost = 3 + 1 + 2
│ │ └────────────────────┘ │  │           = 6
│ └────────────────────────┘  │             
└─────────────────────────────┘
```
Decorators are used to represent the original Beverage object having additional responsibilities. 

In this example, the decorator may not be the most suitable implementation. Instead, it may be more appropriate to pass in qualities (AddOns) during the creation of the object. Possibly use the iterator pattern to obtain information about the passed-in items to total costs. A decorator may instead be used for various cup-sizes or to include the tax. 

## **Using a Decorator in Python**

[PEP 318](https://peps.python.org/pep-0318/) defines a number of syntaxes for decorators. 

```
    def exampleFunction(nums, target, ...):
        return [n * target in n for nums]

    func = declarator2(declarator1(exampleFunction))
```
```
    @declarator2
    @declarator1
    def exampleFunction(nums, target, ...):
        pass
```

- Use a decorator to deprecate code. 
- Use a decorator to determine code execution time. 

The following is an example of using a decorator to print out the execution time of a code.

```
    function-based decorator
    ./timeDecorator.py

    import time
    from functools import wraps             # decorator factory
    from typing import Callable             

    def timer(funct:Callable) -> Callable:
        @wraps(funct)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = funct(*args, **kwargs)
            end = time.time()
            print(f"{funct.__name__}: Execution time - {end - start}")
            return result
        return wrapper
```

```
    ./two_Sum.py

    from typing import List
    from timeDecorator import timer

    class Solution:
        @timer                              # @timer decorator added
        def two_sum_slow(self, nums:List[int], target:int) -> List[int]:
            for i in range(len(nums)):
                diff = target - nums[i]
                for j in range(i + 1, len(nums)):
                    if diff == nums[j]:
                        return [i, j]

        @timer                              # @timer decorator added
        def two_sum_fast(self, nums:List[int], target:int) -> List[int]:
            memo = {}
            for i in range(len(nums)):
                diff = target - nums[i]
                if diff not in memo.keys():
                    memo[nums[i]] = i
                else:
                    return [i, memo[diff]]

    lst = [2,7,11,15]
    s = Solution()
    answer01 = s.two_sum_slow(lst, 9)
    print(answer01)

    s = Solution()
    answer02 = s.two_sum_fast(lst, 9)
    print(answer02)
```

When the above code is executed, the @timer decorator, which wraps the Solution class methods, prints out the amount of time it took to execute the Solution class method. 

The following is a comparison of what is printed out in the command line when the @timer decorator is absent, or when it is present. 

```
    command line (without @timer decorator)
    % python3 twoSum.py

    two_sum_slow: [0, 1]
    two_sum_fast: [1, 0]
```

```
    command line (with @timer decorator)
    % python3 twoSum.py

    two_sum_slow: Execution time - 3.0994415283203125e-06
    two_sum_slow: [0, 1]
    two_sum_fast: Execution time - 3.0994415283203125e-06
    two_sum_fast: [1, 0]
```

