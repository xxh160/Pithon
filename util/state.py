from enum import Enum, unique


@unique
class State(Enum):
    set_param = 1
    auto_run = 2
    manual = 3
