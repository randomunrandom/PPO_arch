from base_controller import BaseController
from model import Model


class Controller(BaseController):
    """
    controller for updating sum
    """

    def __init__(self, model: Model):
        super().__init__()
        self.model: Model = model
        self.model.add_controller(self)

    def model_changed(self):
        a: float = self.model.a
        b: float = self.model.b
        a_b_sum: float = a + b
        if self.model.sum != a_b_sum:
            self.model.sum = a_b_sum
