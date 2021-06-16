from threading import Thread

from lib.alphabot import AlphaBot2
from lib.buzzer import beep_on, beep_off
from lib.led import led
from util.ultrasonic import distance
from util.infrared import get_key
from util.state import State


class Pithon:

    def __init__(self):
        # drive
        self.drive = AlphaBot2()
        # state
        self.state = State.set_param
        # pwm
        self.PWM = 50
        # buzzer
        self.beep = False

    def exec(self, key):
        if self.state == State.set_param:
            return
        if key == 0:
            if self.state == State.auto_run:
                dis = distance()
                print(dis)
                if dis <= 20:
                    self.drive.right()
                else:
                    self.drive.forward()
            return
        # manual
        # 前进 后退 左转 右转 停止 加速 减速
        last = self.state
        self.state = State.manual
        if key == 0x18:
            self.drive.forward()
        elif key == 0x08:
            self.drive.left()
        elif key == 0x1c:
            self.drive.stop()
        elif key == 0x5a:
            self.drive.right()
        elif key == 0x52:
            self.drive.backward()
        elif key == 0x15:
            # speed up
            if self.PWM + 10 < 101:
                self.PWM += 10
                self.drive.setPWMA(self.PWM)
                self.drive.setPWMB(self.PWM)
                print(self.PWM)
        elif key == 0x07:
            # slow down
            if self.PWM - 10 > -1:
                self.PWM = self.PWM - 10
                self.drive.setPWMA(self.PWM)
                self.drive.setPWMB(self.PWM)
                print(self.PWM)
        else:
            self.state = last

    def listen(self):
        key = get_key()
        if key is None:
            self.exec(0)
            return 0
        print("key num: " + str(key))
        if key == 70:
            return 1
        if self.state == State.set_param:
            if key == 69:
                led()
                pass
            if key == 71:
                if self.beep is False:
                    beep_on()
                    self.beep = True
                else:
                    beep_off()
                    self.beep = False
            if key == 67:
                self.state = State.auto_run
                self.PWM = 15
                self.drive.setPWMA(self.PWM)
                self.drive.setPWMB(self.PWM)
        elif self.state == State.auto_run:
            if key == 67:
                self.state = State.set_param
                self.drive.stop()
            else:
                self.state = State.manual
                self.exec(key)
        else:
            print("manual")
            if key == 67:
                self.state = State.set_param
                self.drive.stop()
            else:
                self.exec(key)
        return 0

    def listen_wrapper(self):
        while self.listen() != 1:
            # print(self.state)
            pass

    def start(self):
        t = Thread(target=self.listen_wrapper)
        t.start()
        t.join()
