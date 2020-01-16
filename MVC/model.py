from typing import Any, List, NoReturn

from base_controller import BaseController


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
        self._a_ = val
        self.upd_controller()

    @property
    def b(self) -> float:
        return self._b_

    @b.setter
    def b(self, value: float):
        self._b_ = value
        self.upd_controller()

    @property
    def sum(self) -> float:
        return self._sum_

    @sum.setter
    def sum(self, value: float):
        self._sum_ = value
        self.upd_controller()

    def add_controller(self, controller: BaseController):
        if not isinstance(controller, BaseController):
            raise ValueError("controller should inherit from Controller class")
        self._controllers_.append(controller)

    def del_controller(self, controller: BaseController):
        self._controllers_.remove(controller)

    def upd_controller(self):
        for o in self._controllers_:
            o.model_changed()
