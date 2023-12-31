"""Lightbulb classes to demonstrate state design pattern"""

from time import sleep
from abc import ABC, abstractmethod

##================================

class AbstractLightState(ABC):
    """Abstract base class for Light State"""

    @property
    def context(self):
        """Defines a 'context()' property. 
        
        The @property decorator turns this 'context()' method to be 
        accessible as a read-only attribute.
        """
        return self.context

    @context.setter
    def context(self, context) -> None:
        """Defines the 'setter' of the context
        
        The '@context.setter' decorator refers to the 'self.context()'
        property defined above. 'self.context()' is now a 'property' due to 
        the @property decorator. The @property decorater provides the ".setter"
        method, which reads:

        in builtins.pyi
            class property:
                ...
                def setter(self, __fset: Callable[[Any, Any], None]) -> property: ...
                ...
        """
        self._context = context

    @abstractmethod
    def do_action(self) -> None:
        ...

##================================

class LightOn(AbstractLightState):
    """State class for switch on"""
    def __init__(self):
        self.status = "ON"

    def do_action(self):
        for i in range(1, 11):
            print(f"\rLight is 💡 {self.status} {i}", end="")
            sleep(0.1)
        print("\n")


class LightOff(AbstractLightState):
    """State class for switch off"""
    def __init__(self):
        self.status = "OFF"

    def do_action(self):
        for i in range(1, 11):
            print(f"\rLight is {self.status} {i}", end="")
            sleep(0.1)
        print("\n")

##================================

class LightContext:
    """The context class for the light."""

    """References the current state of this context; a class attribute."""
    current_state_ref = None

    def __init__(self, state1: AbstractLightState, state2: AbstractLightState) -> None:
        self.set_state(state1)
        self.curr_state = "1"
        self.state_dict = {"1": state1, "0": state2}

    def set_state(self, state: AbstractLightState):
        self.current_state_ref = state
        self.current_state_ref.context = self

    def get_state(self):
        return self.current_state_ref

    def request(self):
        self.current_state_ref.do_action()

    def switch(self):
        if self.current_state_ref:
            if self.curr_state == "1":
                self.set_state(self.state_dict["0"])
                self.curr_state = "0"
            else:
                self.set_state(self.state_dict["1"])
                self.curr_state = "1"

if __name__ == "__main__":
    light = LightContext(LightOn(), LightOff())     # sets the LightContext to LightOn() state
    cycles = 10
    print("Starting:\n")
    light.request()
    for i in range(cycles):
        light.switch()
        light.request()

