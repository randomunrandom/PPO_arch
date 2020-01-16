#!/usr/bin/env python3.7

from observer import Observer
from model import Model
from view import View
from controller import Controller

m = Model()
c = Controller(m)
v = View(m)

if __name__ == "__main__":
    v(30)
