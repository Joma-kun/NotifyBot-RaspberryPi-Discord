import RPi.GPIO as GPIO
import time
import segment


GPIO.setmode(GPIO.BCM)

#sw
segment.flag = 0
sw_pin = 4
GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def checkSW(pin):
    segment.flag += 1
    segment.flag %= 3

GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)

try:
    while True:
        if segment.flag == 1:
            segment.print_calling()
        elif segment.flag == 2:
            segment.print_wait()
        else:
            segment.print_none()
            time.sleep(1)

except KeyboardInterrupt:
    pass