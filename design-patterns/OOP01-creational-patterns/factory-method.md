# Factory Method

The Factory Method is a creational design pattern, where a Factory acts as an interface for creating an object. 
If subclasses that inherit from the Factory are further defined, these subclasses can include modifications such its instantiated objects have modified behaviors/characteristics. 

## Background Example
The following LanguageLocalizer classes are shown to represent the difference between a standard class creation process, and the introduction of a Factory method design pattern.

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

In an example of implementing the **Factory design pattern**, another class called Factory is introduced. 

```
def Factory(language="English"):
    """Factory class for the Localizers."""

    localizers = {
        "French":FrenchLocalizer,
        "English":EnglishLocalizer,
        "Japanese":JapaneseLocalizer,
        "Spanish":SpanishLocalizer,
    }
    return localizers[language]()
```
The Factory is a subclass of the LanguageLocalizer classes. 
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

The following code instantiated the Factory class. 
```
f = Factory("French")
e = Factory("English")
s = Factory("Spanish")
j = Factory("Japanese")
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
