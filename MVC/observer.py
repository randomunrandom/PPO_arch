from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """
    abstract metaclass for all observers
    * https://docs.python.org/3/library/abc.html
    """

    @abstractmethod
    def model_changed(self):
        """
        will be called every time the model changes
        """
        raise NotImplementedError("method `model_change` should be implemented")
