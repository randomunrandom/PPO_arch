from typing import Any, List

from base_controller import BaseController
from model import Model


class View(BaseController):
    """
    text-based terminal viewer and editor for given model
    """

    def __init__(self, model: Model):
        super().__init__()
        self.width: int = 100

        self.model: Model = model
        self.model.add_controller(self)
        self.a: str = str(self.model.a)
        self.b: str = str(self.model.b)
        self.sum: str = str(self.model.sum)

    def __call__(self, width: int = 100):
        self.width = width
        width_per_cell: int = (self.width - 10) // 3
        print(f"|-{'-'*(width_per_cell*3 + 6)}-|")
        print(
            f"| a{' '*(width_per_cell-1)} | b{' '*(width_per_cell-1)} | sum{' '*(width_per_cell-3)} |"
        )
        print(f"|-{'-'*(width_per_cell*3 + 6)}-|")
        line = "| "
        if len(self.a) < width_per_cell:
            line += self.a + (" " * (width_per_cell - len(self.a)))
        else:
            line += self.a[: width_per_cell - 3] + "..."

        line += " | "

        if len(self.b) < width_per_cell:
            line += self.b + (" " * (width_per_cell - len(self.b)))
        else:
            line += self.b[: width_per_cell - 3] + "..."

        line += " | "

        if len(self.sum) < width_per_cell:
            line += self.sum + (" " * (width_per_cell - len(self.sum)))
        else:
            line += self.sum[: width_per_cell - 3] + "..."
        line += " |"

        print(line)
        print(f"|-{'-'*(width_per_cell*3 + 6)}-|")
        print()
        print("to change variable type it's name and new value")
        print("to view variable type it's name")

        try:
            raw_inp: str = input()
            try:
                inp: List[Any] = raw_inp.split(" ")
            except EOFError:
                inp = [raw_inp]
        except KeyboardInterrupt:
            print("\nexiting")
            exit()
        if len(inp) == 1:
            name: str = str(inp[0])
            if name == "a":
                print(self.model.a)
            elif name == "b":
                print(self.model.b)
            elif name == "sum":
                print(self.model.sum)
            else:
                print("unknown name")
            self(self.width)
        elif len(inp) == 2:
            name: str = str(inp[0])
            try:
                new_val: float = float(inp[1])
            except ValueError:
                print("wrong value")
                self(self.width)

            if name == "a":
                self.model.a = new_val
            elif name == "b":
                self.model.b = new_val
            else:
                print("unknown name")
                self(self.width)
        else:
            print("invalid foramt")

    def model_changed(self):
        self.a: str = str(self.model.a)
        self.b: str = str(self.model.b)
        self.sum: str = str(self.model.sum)
        self(self.width)
