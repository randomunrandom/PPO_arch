#!/usr/bin/env python3.7

from controller import Controller
from model import Model
from view import View

m = Model()
c = Controller(m)
v = View(m)

if __name__ == "__main__":
    v(30)
