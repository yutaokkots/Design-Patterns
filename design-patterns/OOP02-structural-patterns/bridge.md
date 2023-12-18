# Bridge

The intent of the bridge pattern is to decouple an abstraction from its implementation so that the two can vary independently. 

```
    ┌───────────────┐           ┌───────────────────┐
    │ Abstraction   │  Bridge   │Implementor        │
    ├───────────────┤ ────────> ├───────────────────┤
    │               │           │                   │
    └───────┬───────┘           └─────────┬─────────┘
            △                             △   
            │                             │
    ┌───────┴───────────┐       ┌─────────┴─────────┐
   ┌┤ConcreteAbstraction│      ┌┤ConcreteImplementor│
  ┌┤├───────────────────┤     ┌┤├───────────────────┤
  │││                   │     │││                   │
  ││└───────────────────┘     ││└───────────────────┘
  │└───────────────────┘      │└───────────────────┘
  └───────────────────┘       └───────────────────┘
```
### Example

In this example, a page that dynamically displays information about an Artist, Album, Author, and Book is being created.

There are two ways to display the information - as a long-form view and a short-form view. 
```
            ┌───────────────┐
            │ ViewClass     │
            ├───────────────┤
            │ show()        │
            └───────────────┘

Display Set
        ┌────────┐    ┌────────────┐
        │150 x   │    │   image    │ long-form
        │    150 │    │ 300        │ view
        ├────────┤    │     x      │ ┘
        │ title  │    │       300  │
        └────────┘    ├────────────┤
    short-form ┘      │  200 char  │
        view          └────────────┘ 
```
The way to display the information is consistent, but there are two sizes. 

On the other hand, Artist, Album, Author, and Book may all have different properties. 

example:
```
            ┌───────────────┐
            │ResourceClass  │
            ├───────────────┤
            │snippet()      │
            └───────────────┘
Information Set
┌───────────────┐ ┌───────────────┐
│ Artist        │ │ Album         │
├───────────────┤ ├───────────────┤
│ name          │ │ name          │
│ discography   │ │ songList      │
│ bio           │ │ description   │
│ image         │ │ image         │
└───────────────┘ └───────────────┘
┌───────────────┐ ┌───────────────┐
│ Book          │ │ Author        │
├───────────────┤ ├───────────────┤
│ name          │ │ name          │
│ pubDate       │ │ boolList      │
│ synopsis      │ │ bio           │
│ image         │ │ image         │
└───────────────┘ └───────────────┘
```
It is useful to use the bridge pattern - the bridge associates the abstraction (the structure of the data) and implementation (how the data are displayed), even if they are decoupled from each other. 

Reminiscent of a Cartesian Product:
```
Display Set:            Information Set:
                │   Artist  Album   Book    Author
long-form view  │     Ar-L   Al-L    Bo-L    Au-L  
short-form view │     Ar-S   Al-S    Bo-S    Au-S

```

```
    ┌───────────────┐           ┌───────────────────┐
    │   Views       │  Bridge   │ Resource          │
    ├───────────────┤ ────────> ├───────────────────┤
    │stringShow()   │           │ snippet()         │        
    └───────┬───────┘           │ image()           │
            │                   │ title()           │
            △                   │ url()             │                        
            │                   └─────────┬─────────┘
            │                             △   
            │                             │
    ┌───────┴───────────┐       ┌─────────┴─────────┐
   ┌┤LongFormView       │      ┌┤ArtistResource     │
  ┌┤├───────────────────┤     ┌┤├───────────────────┤
  │││stringShow         │     │││snippet(),image()..│
  ││└───────────────────┘     ││└───────────────────┘
  │└───────────────────┘      │└───────────────────┘
  └───────────────────┘       └───────────────────┘
```