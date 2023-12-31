# Abstract Factory

The Abstract Factory is a creational design pattern that directly takes one or more parameters such that subclasses can be customized based on them. Families of related or dependent objects can be created.

". . . maybe you could pursue a lowest-common-denominator strategy, and require all interfaces to take in the parameters you need for just one of the implementations" <sup>[1]</sup>

An abstract factory is a ***set of factory methods***. 

The Factory Method pattern is useful for creating a single object, while the Abstract Factory pattern is useful for creating multiple objects.

## UML Diagram

```
┌───────────────┐           ┌───────────────────┐
│ ProductA      │           │ Factory           │
├───────────────┤           ├───────────────────┤
└───────┬───────┘           │ getProductA()     │
        △                   │ getProductB()     │
    ┌───┴────────────┐      └─────┬───┬───┬─────┘
    │ConcreteProductA│<┐          △   △   △    
    ├────────────────┤ │          │   │   │ 
    └────────────────┘ │  ┌───────┴───┼───┼───┐ <─────┐                 
┌───────────────┐      │  │ ┌─────────┴───┼───┴─┐ <───┤ 
│ ProductB      │      │  │ │ ┌───────────┴─────┴─┐ <─┤
├───────────────┤      ├──┼─┼─┤ ConcreteFactory1  │   │
└───────┬───────┘      │  │ │ ├───────────────────┤   │
        △              │  └─┤ │ getProductA()     │   │
    ┌───┴────────────┐ │    └─┤ getProductB()     │   │
    │ConcreteProductB│<┘      └───────────────────┘   │
    ├────────────────┤                                │
    └────────────────┘          Each ConcreteFactory ─┘
                                 creates a family of
                                    related products
```

## Using the Abstract Factory design pattern 

The following `AbstractLocalizer` and Localizer classes demonstrate an Abstract Factory design pattern. "Localizer" here is referring to "localization" or 'l10n' used in adapting languages for different locales or target markets. 

In this example, a website that is compatible with different regions is being created. When in a certain region of the world, the website displays text in the language that is predominantly used in that region. 

The `AbstractLocalizer` allows objects to be passed into it (as parameters) to create subclasses that are customized for the parameter. 

For instance, the following `AbstractLocalizer` defines an Abstract Factory to create other subclasses for language localization. 


The `AbstractLocalizer` itself cannot return anything substantial with the `localize()` function, as it depends on its abstraction by a subclass. 

```
class AbstractLocalizer:
    def __init__(self, language="English", lang_dictionary={}):
        self.language:str = language
        self.translations: Dict[str:str]  = lang_dictionary

    def localize(self):
        raise NotImplementedError("Subclasses must implement the localize method.")
```
The `AbstractLocalizer` is represented below.

```
                ┌─────────────────┐
                │AbstractLocalizer│
                ├─────────────────┤
                │self.language    │
                │self.translations│
                │localize()       │
                └─────────────────┘
```

The other language Localizers are written in the following code, and inherit the properties of the AbstractLocalizer. 

```
class SpanishLocalizer(AbstractLocalizer):
    def __init__(self, lang_dictionary=None):
        super().__init__("Spanish", lang_dictionary)

    def localize(self, key:str) -> str:
        return self.translations.get(key, f"No translation for '{key}' found.")
```
```
class ChineseLocalizer(AbstractLocalizer):
    def __init__(self, lang_dictionary=None):
        super().__init__("Chinese", lang_dictionary)

    def localize(self, key:str) -> str:
        return self.translations.get(key, f"No translation for '{key}' found.")
```
```
class EnglishLocalizer(AbstractLocalizer):
    def __init__(self, lang_dictionary=None):
        super().__init__("English", lang_dictionary)

    def localize(self, key:str) -> str:
        return key
    
```
As a result, the subclasses, `SpanishLocalizer`, `ChineseLocalizer`, and `EnglishLocalizer` are created from the Abstract Factory, `AbstractLocalizer`.

When each of these subclasses are instantiated, it takes parameters (in this case, a `lang_dictionary`) that is a customized version of the `AbstractLocalizer` parent class.

```
                ┌─────────────────┐
                │AbstractLocalizer│
                ├─────────────────┤
                │self.language    │
                │self.translations│
                │localize()       │
                └───────┬─────────┘
                        △ 
                        │
        ┌───────────────┴───┬──────────────────┐
┌───────┴─────────┐┌────────┴────────┐┌────────┴────────┐
│ChineseLocalizer ││SpanishLocalizer ││EnglishLocalizer │
├─────────────────┤├─────────────────┤├─────────────────┤
│self.language    ││self.language    ││self.language    │
│self.translations││self.translations││self.translations│
│localize()       ││localize()       ││localize()       │
└─────────────────┘└─────────────────┘└─────────────────┘      
```

In the example of localizing a website for a Spanish-speaking audience, the site may include pages that have different categories of words. 

The `SpanishLocalizer` may be instantiated with the following categorical dictionaries. 

```
activities_es = {
    "run": "correr", 
    "swim": "nadar",
    "paddle":"remar",
    "rock climbing": "escalada de roca",
    "play volleyball": "jugar voleibol",
}

transportation_es = {
    "car": "coche", 
    "bike": "bicicleta",
    "motorcycle":"motocicleta",
    "crosswalk": "paso de peatones"
}

es_activi = SpanishLocalizer(activities_es)

es_transp = SpanishLocalizer(transportation_es)

print(es_activi.localize("rock climbing"))          # escalada de roca

print(es_transp.localize("crosswalk"))              # paso de peatones
```
Each of the `SpanishLocalizer` instances, `es_activi` and `es_transp` can be called to translate specific terms for the related categorical dictionaries. 

The `es_activi` and `es_transp` objects are part of the family of spanish Localizer objects. 

These are relateed because, conversely, creating a ChineseLocalizer object among the SpanishLocalizer objects would be inapplicable. 

Additionally, a subclass of the `AbstractLocalizer` that is more customizeable may be created:

```
class LanguageLocalizer(AbstractLocalizer):
    def __init__(self, language, lang_dictionary=None):
        super().__init__(language, lang_dictionary)

    def localize(self, key:str) -> str:
        return self.translations.get(key, f"No translation for '{key}' found.")
```
```
                ┌─────────────────┐
                │AbstractLocalizer│
                ├─────────────────┤
                │self.language    │
                │self.translations│
                │localize()       │
                └───────┬─────────┘
                        △ 
                        │
                ┌───────┴─────────┐
                │LanguageLocalizer│
                ├─────────────────┤
                │self.language    │
                │self.translations│
                │localize()       │
                └─────────────────┘
````
Instantiating the `LanguageLocalizer` above involves inputting both the `language` and the dictionary into the paremeter. 

```
activities_cn = {
    "run": "跑步", 
    "swim": "游泳",
    "paddle":"划船",
    "rock climbing": "攀岩",
    "play volleyball": "打排球",
}

cn_activi = LanguageLocalizer("Chinese", activities_cn)
print(cn_activi.localize("paddle"))                        # "划船"   
```
This introduces flexibiliy to the localizer object that is created. 

## Additional Notes

<div align="center">

### **Abstract Factory**

| Advantages | Disadvantages |
| ---------- | ------------- |
| - Abstracts the process of object creation (and introducing flexibility, modularity, and variation to the created objects).<br/> - Consistency and comptaibility of the objects created. <br/> - Details of the factory are encapsulated; the system can be extended or changed without affecting existing code. <br/>|- If multiple factories must be managed, it could lead to scalability and complexity issues.<br/> Creating and managing multiple factory objects can lead to runtime overhead.|
</div>

<hr>

<sup>[1]</sup> "AbstractFactory" Portland Pattern Repository. http://wiki.c2.com/?AbstractFactory. September 8, 2013. Retrieved Dec. 30, 2023.