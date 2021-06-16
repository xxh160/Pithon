import RPi.GPIO as GPIO

from util.gpio import BUZZER


def beep_on():
    GPIO.output(BUZZER, GPIO.HIGH)


def beep_off():
    GPIO.output(BUZZER, GPIO.LOW)
