# Abstract Factory

The Abstract Factory is a creational design pattern that directly takes one or more parameters such that subclasses can be customized based on the Abstract Factory. 

## Using the Abstract Factory design pattern 

The following `AbstractLocalizer` and Localizer classes demonstrate an Abstract Factory design pattern. "Localizer" here is referring to "localization" or 'l10n' used in adapting languages for different locales or target markets. 

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

cn = LanguageLocalizer("Chinese", activities_cn)
print(cn.localize("paddle"))                        # "划船"   
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