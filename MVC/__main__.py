#!/usr/bin/env python3.7

from observer import Observer
from model import Model
from view import View
from controller import Controller

m = Model()
c = Controller(m)
m.add_observer(c)
v = View(m)
m.add_observer(v)


if __name__ == "__main__":
    v(30)
