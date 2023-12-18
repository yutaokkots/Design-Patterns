# Factory Method

The Factory Method is a creational design pattern, where the Factory acts as an interface for creating an object. 

The Factory class encapsulates the business logic for creating an object.

If subclasses that inherit from the Factory are further defined, these subclasses can include modifications such that its instantiated objects have modified behaviors/characteristics. 

In other words, in the Factory Method pattern, the class that creates an object, and the decision on when and how to create an object are separated.
The classes defer instantiation to subclasses; the subclasses actually create the object. 

## UML Diagram
The entire point here is to create an **instance of a ConcreteProduct** (bottom-left).
**ConcreteProduct** sublcass is a variation of the **Product** class. 

The **ConcreteCreator** is responsible for the logic behind the creation of the **instance of a ConcreteProduct**. 
And incidentally, ConcreteCreator is a subclass of **Creator**, where Creator is an abstraction of the creation process. 

```
    ┌───────────────┐       ┌───────────────────┐
    │ Product       │       │ Creator           │
    ├───────────────┤       ├───────────────────┤
    │               │       │ factoryMethod()   │
    └───────┬───────┘       │ anOperation()     │
            △               └─────────┬─────────┘
            │                         △  
    ┌───────┴───────┐       ┌─────────┴─────────┐
    │ConcreteProduct│<──────│ ConcreteCreator   │
    ├───────────────┤       ├───────────────────┤
    │               │       │ factoryMethod()   │
    └───────────────┘       └───────────────────┘
                the ConcreteCreator makes the
                ConcreteProduct. 
```

## Background Example
The following LanguageLocalizer classes are shown to represent the difference between a standard class creation process, and the introduction of a Factory method design pattern. "Localizer" here is referring to "localization" or 'l10n' used in adapting languages for different locales or target markets. 

The Following LanguageLocalizater classes contain 

an attribute, `self.translations` (a small dictionary of words); and 

a method, `localize()`:

```
class FrenchLocalizer:
    """FrenchLocalizer class - translates certain words from En to Fr."""

    def __init__(self):
        self.translations = {"car": "voiture",
                             "bike": "vélo",
                             "motorcycle": "moto",
                             "crosswalk": "passage clouté"
                             }

    def localize(self, msg):
        return self.translations.get(msg, msg)
```

```
class SpanishLocalizer:
    """SpanishLocalizer class - translates certain words from En to Es."""

    def __init__(self):
        self.translations = {"car": "coche", 
                             "bike": "bicicleta",
                             "motorcycle":"motocicleta",
                             "crosswalk": "paso de peatones"
                             }
 
    def localize(self, msg):
        return self.translations.get(msg, msg)
```

```
class JapaneseLocalizer:
    """JapaneseLocalizer class - translates certain words from En to Ja."""

    def __init__(self):
        self.translations = {"car": "自動車", 
                             "bike": "自転車",
                             "motorcycle":"オートバイ",
                             "crosswalk": "横断歩道"
                             }
 
    def localize(self, msg):
        return self.translations.get(msg, msg)
```

```
class EnglishLocalizer:
    """EnglishLocalizer class is used to return the word as is."""

    def localize(self, msg):
        return msg
```
These classes can be represented by boxes, as follows:

```
┌─────────────────┐┌─────────────────┐┌─────────────────┐┌─────────────────┐ 
│ FrenchLocalizer ││SpanishLocalizer ││JapaneseLocalizer││ EnglishLocalizer│ 
├─────────────────┤├─────────────────┤├─────────────────┤├─────────────────┤ 
│self.translations││self.translations││self.translations││    localize()   │  
│    localize()   ││    localize()   ││    localize()   │└─────────────────┘ 
└─────────────────┘└─────────────────┘└─────────────────┘        
```

In order to instantiate the above classes, it might be accomplished in the following manner:

```
f = FrenchLocalizer()
e = EnglishLocalizer()
s = SpanishLocalizer()
j = JapaneseLocalizer()
```
And once instantiated, the method, `localize()` can be called in the following manner:
```
message = ["bike", "motorcycle", "crosswalk"]

print(f.localize("bike"))                       #   "vélo"
print(j.localize(message[2]))                   #   "横断歩道"
for m in message:                               
    print(s.localize(m))                        #   "bicicleta" 
                                                #   "motocicleta" 
                                                #   "paso de peatones"
```

## Using the Factory design pattern 

In an example of implementing the **Factory design pattern**, another class called LanguageFactory is introduced. The LanguageFactory encapsulates the business logic required to create one of the language Localizer objects (FrenchLocalizer, EnglishLocalizer, JapaneseLocalizer, SpanishLocalizer).

```
def LanguageFactory(language="English"):
    """Factory class for the Localizers."""

    localizers = {
        "French":FrenchLocalizer,
        "English":EnglishLocalizer,
        "Japanese":JapaneseLocalizer,
        "Spanish":SpanishLocalizer,
    }
    return localizers[language]()
```
The LanguageFactory is a subclass of the LanguageLocalizer classes. 
It includes a parameter to take in the type of Language to use. Therefore, the Factory class, when instantiated, produces a different type of Localizer depending on how it is defined when instantiated. 
```
┌─────────────────┐┌─────────────────┐┌─────────────────┐┌─────────────────┐ 
│ FrenchLocalizer ││SpanishLocalizer ││JapaneseLocalizer││ EnglishLocalizer│ 
├─────────────────┤├─────────────────┤├─────────────────┤├─────────────────┤ 
│self.translations││self.translations││self.translations││    localize()   │  
│    localize()   ││    localize()   ││    localize()   │└────────┬────────┘ 
└────────┬────────┘└────────┬────────┘└────────┬────────┘         │
         △                  △                  △                  △  
         └──────────────────┴───────┬──────────┴──────────────────┘
                                    │ 
                            ┌───────┴───────┐
                            │ Factory class │
                            ├───────────────┤
                            │ localizer()   │
                            └───────────────┘
```
Rather than instantiating the LanguageLocalizer class directly. 

(e.g. `f = FrenchLocalizer()`)

The following code instantiates the LanguageFactory class. 
```
f = LanguageFactory("French")
e = LanguageFactory("English")
s = LanguageFactory("Spanish")
j = LanguageFactory("Japanese")
```
The `localize()` method is called from the Factory rather than the LanguageLocalizer class directly.

```
message = ["bike", "motorcycle", "crosswalk"]

print(f.localize("bike"))                       #   "vélo"
print(j.localize(message[2]))                   #   "横断歩道"
for m in message:                               
    print(s.localize(m))                        #   "bicicleta" 
                                                #   "motocicleta" 
                                                #   "paso de peatones"
```

<hr>
