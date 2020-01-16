from typing import Any, List

from model import Model
from base_presenter import BasePresenter

class View:
    """
    text-based terminal viewer and editor for given model
    """

    def __init__(self, presenter: BasePresenter):
        super().__init__()
        self.width: int = 100

        self.presenter: BasePresenter = presenter

    def __call__(self, width: int = 100):
        self.width = width
        a: str = str(self.presenter.a)
        b: str = str(self.presenter.b)
        a_b_sum: str = str(self.presenter.sum)
        width_per_cell: int = (self.width - 10) // 3
        print(f"|-{'-'*(width_per_cell*3 + 6)}-|")
        print(
            f"| a{' '*(width_per_cell-1)} | b{' '*(width_per_cell-1)} | sum{' '*(width_per_cell-3)} |"
        )
        print(f"|-{'-'*(width_per_cell*3 + 6)}-|")
        line = "| "
        if len(a) < width_per_cell:
            line += a + (" " * (width_per_cell - len(a)))
        else:
            line += a[: width_per_cell - 3] + "..."

        line += " | "

        if len(b) < width_per_cell:
            line += b + (" " * (width_per_cell - len(b)))
        else:
            line += b[: width_per_cell - 3] + "..."

        line += " | "

        if len(a_b_sum) < width_per_cell:
            line += a_b_sum + (" " * (width_per_cell - len(a_b_sum)))
        else:
            line += a_b_sum[: width_per_cell - 3] + "..."

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
                print(self.presenter.a)
            elif name == "b":
                print(self.presenter.b)
            elif name == "a_b_sum":
                print(self.presenter.sum)
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
                self.presenter.a = new_val
            elif name == "b":
                self.presenter.b = new_val
            else:
                print("unknown name")
            self(width)
        else:
            print("invalid foramt")
