from typing import Any, List, NoReturn

from base_presenter import BasePresenter


class Model:
    """
    Model with interface for storing data and
        communicating with observers
    """

    def __init__(self):
        self._a_: float = 0
        self._b_: float = 0
        self._sum_: float = 0

        self._presenters_: List[BasePresenter] = []

    @property
    def a(self) -> float:
        return self._a_

    @a.setter
    def a(self, val: float):
        self._a_ = val
        self.upd_presenters()

    @property
    def b(self) -> float:
        return self._b_

    @b.setter
    def b(self, value: float):
        self._b_ = value
        self.upd_presenters()

    @property
    def sum(self) -> float:
        return self._sum_

    @sum.setter
    def sum(self, value: float):
        self._sum_ = value
        self.upd_presenters()

    def add_presenter(self, presenter: BasePresenter):
        if not isinstance(presenter, BasePresenter):
            raise ValueError("observer should inherit from Observer class")
        self._presenters_.append(presenter)

    def del_presenter(self, presenter: BasePresenter):
        self._presenters_.remove(presenter)

    def upd_presenters(self):
        for p in self._presenters_:
            p.model_changed()
