#!/usr/bin/env python3.7

from model import Model
from presenter import Presenter
from view import View

m = Model()
p = Presenter(m)
v = View(p)

if __name__ == "__main__":
    v(30)
