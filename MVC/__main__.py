#!/usr/bin/env python3.7

from .model import Model
from .controller import Controller
from .view import View

m = Model()
c = Controller(m)
v = View(m)

if __name__ == "__main__":
    v(30)
