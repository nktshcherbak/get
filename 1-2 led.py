import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.OUT)


GPIO.output(18, GPIO.input(15))