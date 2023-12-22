# Composite

A composite design pattern enables a composite of objects and single objects to be treated uniformly. 

Objects are composed into a tree structure to represent part-whole heirarchies.

How the Composite pattern is different from the Decorator pattern

```
                ┌────┐ 
                │  C │ <- composite node (C)
                └┬──┬┘ 
                /    \
            ┌────┐   ┌────┐
            │  C │   │  C │ 
            └┬──┬┘   └┬──┬┘
            /   |     |   \
       ┌────┐ ┌────┐┌────┐┌────┐
       │  L │ │  C ││  L ││  L │ <- leaves (L)
       └────┘ └──┬─┘└────┘└────┘
                  \
                 ┌────┐
                 │  L │
                 └────┘

```


```
            ┌───────────────┐ 
            │ Component     │ 
            ├───────────────┤ 
            │ Operation()   │<─────────────┐
            └─────┬──┬──────┘              │
                  △  △                     │
                  │  │                     │
        ┌─────────┘  └────────┐            │
┌───────┴───────┐     ┌───────┴───────┐    │
│ Leaf          │     │ Component     │<>──┘
├───────────────┤     ├───────────────┤ 
│ Operation()   │     │ Operation()   │ 
└───────────────┘     └───────────────┘ 
```

Coding principle: whenever an object can be made immutable, keep it immutable; whenever changing an object's state can be avoided, avoid changing its state.

Useful for representing data in a heirarchical structure. 