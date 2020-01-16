from typing import List, Any, NoReturn
from observer import Observer


class Model:
    """
    model for storing data and updating observers
    """

    def __init__(self):
        self._a_: float = 0
        self._b_: float = 0
        self._sum_: float = 0

        self._observers_: List[Observer] = []

    @property
    def a(self) -> float:
        return self._a_

    @a.setter
    def a(self, val: float):
        self._a_: float = val
        self.notify_observers()

    @property
    def b(self) -> float:
        return self._b_

    @b.setter
    def b(self, value: float):
        self._b_: float = value
        self.notify_observers()

    @property
    def sum(self) -> float:
        return self._sum_
    
    @sum.setter
    def sum(self, value: float):
        self._sum_: float = value
        self.notify_observers()

    def add_observer(self, observer: Observer):
        if not isinstance(observer, Observer):
            raise ValueError("observer should inherit from Observer class")
        self._observers_.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers_.remove(observer)

    def notify_observers(self):
        for x in self._observers_:
            x.model_changed()
