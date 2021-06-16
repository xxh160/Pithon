from lib.pithon import Pithon
from util.gpio import init_gpio, cleanup

if __name__ == "__main__":
    init_gpio()
    car = Pithon()
    car.start()
    cleanup()
