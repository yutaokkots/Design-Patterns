# Observer

Also called PubSub (Publisher-Subscriber)

The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.<sup>[1]</sup>

## **UML diagram for Observer pattern**

```
    ┌───────────────────┐    ┌── each subject can have many observers
    │       (Interface) │    │      ┌────────────────┐  ┌────────────────┐
    │AbstractSubject    │    │      │     (Interface)│  │     (Interface)│
    ├───────────────────┤  observes │AbstractObserver│  │AbstractWhatever│
    │registerObserver() ├──────────>├────────────────┤  ├────────────────┤
    │removeObserver()   │           │ update()       │  │ display()      │
    │notifyObserver()   │           └────────┬───────┘  └────────┬───────┘ 
    └─────────┬─────────┘                    △                   △     
              △                              ├───────────────────┘
    ┌─────────┴─────────┐ subject   ┌────────┴──────────┐   example of
    │ConcreteSubject    │<──────────┤ConcreteObserver   │   composition 
    ├───────────────────┤           ├───────────────────┤
    │registerObserver() │           │update()           │
    │removeObserver()   │           │otherMethods()     │
    │notifyObserver()   │           │e.g. display()     │
    │getState()         │           └───────────────────┘
    │setState()         │
    └───────────────────┘

```

Inefficient/wrong code:

```
class CurrentConditionsDisplay:
    def __init__(self):
        self.temp = 0
        self.humidity = 0
        self.pressure = 0
    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure

class StatisticDisplay:
    def __init__(self):
        self.temp = 0
        self.humidity = 0
        self.pressure = 0
    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure

class ForecastDisplay:
    def __init__(self):
        self.temp = 0
        self.humidity = 0
        self.pressure = 0
    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure

class WeatherData:
    def __init__(self):
        self.current_conditions_display = CurrentConditionsDisplay()
        self.statistic_display = StatisticDisplay()
        self.forecast_display = ForecastDisplay()

    def measurements_changed():
        temp = getTemperature()
        humidity = gethumidity()
        pressure = getPressure()
        self.current_conditions_display.update(temp, humidity, pressure)
        self.statistic_display.update(temp, humidity, pressure)
        self.forecast_display.update(temp, humidity, pressure)
    ## other implementations

```

## Example of the above using the Observer Pattern

```
subject.py

"""Abstract class for the Subject (Publisher) for the Observer Pattern"""
from abc import ABC, abstractmethod
from observer import Observer
from typing import List

class Subject(ABC):
    """Abstract Base Class for the Subject / Publisher."""

    @abstractmethod
    def register_observer(self, observer: Observer):
        """Registers an observer."""
        pass

    @abstractmethod
    def remove_observer(self, observer:Observer):
        """Removes the observer."""
        pass

    @abstractmethod
    def notify_observers(self):
        """Notifies all observers"""
        pass

class WeatherData(Subject):
    """Concrete class for the WeatherData using Subject abstract base class."""
    def __init__(self):
        self.observers: List[any] = []
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer:Observer) -> None:
        i:int = self.observers.index(observer)
        if i >= 0:
            self.observers.pop(i)

    def notify_observers(self) -> None:
        for i in range(len(self.observers)):
            observer: Observer = self.observers[i]
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self) -> None:
        self.notify_observers()

    def set_measurements(self, temperature:float, humidity:float, pressure:float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

```

```
observer.py

"""Abstract base class for the Observer (Subscriber) for the Observer pattern"""
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temp:float, humidity:float, pressure:float):
        pass

```

```
displayelement.py

"""Abstract base class for the Display Element."""
from abc import ABC, abstractmethod
from observer import Observer
from subject import Subject

class DisplayElement(ABC):
    """Abstract Base Class for the display element that displays weather events."""
    
    @abstractmethod
    def display(self):
        pass

class CurrentConditionsDisplay(Observer, DisplayElement):
    """Concrete class for displaying the current conditions."""

    def __init__(self, weather_data:Subject):
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0
        self.heat_index: float = 0.0
        self.weather_data: Subject = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature:float, humidity:float, pressure:float) -> None:
        """Update method for updating the instance's temp, humidity, and pressure information."""
        self.temperature = temperature
        self.humidity = humidity
        self.heat_index = round(self.compute_heat_index(self.temperature, self.humidity), 2)
        self.display()

    def display(self) -> None:
        """Display method for displaying current conditions."""
        print(f"""Current conditions:
temperature: {self.temperature}°F
humidity: {self.humidity}
heat index: {self.heat_index}\n""")

    def compute_heat_index(self, t:float, rh:float):
        index = ((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) +
            (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) +
            (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
            (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *  
            (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) +
            (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +     
            0.000000000843296 * (t * t * rh * rh * rh)) -
            (0.0000000000481975 * (t * t * t * rh * rh * rh)))
        return index
```

```
weatherstation.py

"""WeatherStation class."""
from subject import WeatherData
from displayelement import CurrentConditionsDisplay

class WeatherStation:
    """WeatherStation class for creating an instance of a Weather Station."""

    def __init__(self):
        self.weather_data: WeatherData = WeatherData()
        self.current_display:CurrentConditionsDisplay = CurrentConditionsDisplay(self.weather_data)
```

```
main.py

from weatherstation import WeatherStation

def main():
    w = WeatherStation()
    w.current_display.update(80, 65, 30.4)

    w.current_display.update(82, 70, 29.2)

    w.current_display.update(78, 90, 29.2)

    """
    Output from above code:
    
    Current conditions:
    temperature: 80°F
    humidity: 65
    heat index: 82.96

    Current conditions:
    temperature: 82°F
    humidity: 70
    heat index: 86.9

    Current conditions:
    temperature: 78°F
    humidity: 90
    heat index: 83.65
    """

if __name__ == "__main__":
    main()
```
<hr/>

<sup>[1]</sup> Freeman *et al.*. Head First Design Patterns 2004.