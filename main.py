import RPi.GPIO as GPIO
import time
import segment

GPIO.setmode(GPIO.BCM)

#sw
segment.flag = 0
sw_pin = 4
GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#led
led_pin = 21
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

#detect switch press
def checkSW(pin):
    segment.flag += 1
    segment.flag %= 3

GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)

#main
try:
    print("ONLINE")
    while True:
        if segment.flag == 1:
            GPIO.output(led_pin, GPIO.HIGH)
            #segment.print_calling()
            import bot
        elif segment.flag == 2:
            GPIO.output(led_pin, GPIO.LOW)
            segment.print_welcome()
        elif segment.flag == 3:
            GPIO.output(led_pin, GPIO.LOW)
            segment.print_sorry()
        else:
            GPIO.output(led_pin, GPIO.LOW)
            segment.print_none()
            time.sleep(1)

except KeyboardInterrupt:
    pass