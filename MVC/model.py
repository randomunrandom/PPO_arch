from typing import Any, List, NoReturn

from .base_controller import BaseController


class Model:
    """
    model for storing data and updating observers
    """

    def __init__(self):
        self._a_: float = 0
        self._b_: float = 0
        self._sum_: float = 0

        self._controllers_: List[BaseController] = []

    @property
    def a(self) -> float:
        return self._a_

    @a.setter
    def a(self, val: float):
        self._a_: float = val
        self.upd_observers()

    @property
    def b(self) -> float:
        return self._b_

    @b.setter
    def b(self, value: float):
        self._b_: float = value
        self.upd_observers()

    @property
    def sum(self) -> float:
        return self._sum_

    @sum.setter
    def sum(self, value: float):
        self._sum_: float = value
        self.upd_observers()

    def add_observer(self, observer: BaseController):
        if not isinstance(observer, BaseController):
            raise ValueError("observer should inherit from Observer class")
        self._controllers_.append(observer)

    def del_observer(self, observer: BaseController):
        self._controllers_.remove(observer)

    def upd_observers(self):
        for o in self._controllers_:
            o.model_changed()
