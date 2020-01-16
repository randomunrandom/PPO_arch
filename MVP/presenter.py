from base_presenter import BasePresenter
from model import Model
from view import View


class Presenter(BasePresenter):
    def __init__(self, model: Model):
        super().__init__()
        self.model: Model = model
        self.model.add_presenter(self)
        self._a_: float = self.model.a
        self._b_: float = self.model.b
        self._sum_: float = self.model.a + self.model.b

    @property
    def a(self) -> float:
        return self._a_

    @a.setter
    def a(self, val: float):
        if val != self._a_:
            self._a_ = val
            self.model.a = val

    @property
    def b(self) -> float:
        return self._b_

    @b.setter
    def b(self, val: float):
        if val != self._b_:
            self._b_ = val
            self.model.b = val

    @property
    def sum(self) -> float:
        self._sum_ = self._a_ + self._b_
        return self._sum_

    # @sum.setter
    # def sum(self, val: float):
        # if val == self._sum_:
        #     self._sum_ = val

    def model_changed(self):
        update_view: bool = False
        if self.a != self.model.a:
            self.a = self.model.a
            update_view = True
        if self.b != self.model.b:
            self.b = self.model.b
            update_view = True
        if self.sum != self.model.a + self.model.b:
            self.model.sum = self.model.a + self.model.b
            update_view = True
        if update_view:
            self.view(self)
