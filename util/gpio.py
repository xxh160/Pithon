import RPi.GPIO as GPIO

AIN1 = 12
AIN2 = 13
BIN1 = 20
BIN2 = 21
ENA = 6
ENB = 26
IR = 17
TRIG = 22
ECHO = 27
BUZZER = 4


def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(IR, GPIO.IN)
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(AIN2, GPIO.OUT)
    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(BUZZER, GPIO.OUT)


def cleanup():
    GPIO.cleanup()
