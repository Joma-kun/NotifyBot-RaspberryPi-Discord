import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

#sw
flag = 0
sw_pin = 4
GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#7seg
seg_num = {"A": 17, "B": 27, "C": 22, "D": 23, "E": 24, "F": 24, "G": 5}
GPIO.setup(seg_num["A"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["B"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["C"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["D"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["E"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["F"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["G"], GPIO.OUT, initial=GPIO.LOW)

def print_calling():
    while True:
        #C
        GPIO.output(seg_num["A"], GPIO.HIGH)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 2:
            break
        time.sleep(0.5)
        #A
        GPIO.output(seg_num["A"], GPIO.HIGH)
        GPIO.output(seg_num["B"], GPIO.HIGH)
        GPIO.output(seg_num["C"], GPIO.HIGH)
        GPIO.output(seg_num["D"], GPIO.LOW)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 2:
            break
        time.sleep(0.5)
        #L
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 2:
            break
        time.sleep(0.5)
        #L
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 2:
            break
        time.sleep(0.5)
        #I
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.LOW)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 2:
            break
        time.sleep(0.5)
        #N
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.HIGH)
        GPIO.output(seg_num["D"], GPIO.LOW)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.LOW)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 2:
            break
        time.sleep(0.5)
        #G
        GPIO.output(seg_num["A"], GPIO.HIGH)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.HIGH)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 2:
            break
        time.sleep(0.5)

def print_wait():
    while True:
        #W
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.HIGH)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.LOW)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 0:
            break
        time.sleep(0.5)
        #A
        GPIO.output(seg_num["A"], GPIO.HIGH)
        GPIO.output(seg_num["B"], GPIO.HIGH)
        GPIO.output(seg_num["C"], GPIO.HIGH)
        GPIO.output(seg_num["D"], GPIO.LOW)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 0:
            break
        time.sleep(0.5)
        #I
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.LOW)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 0:
            break
        time.sleep(0.5)
        #T
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)
        if flag == 0:
            break
        time.sleep(0.5)

def checkSW(pin):
    global flag
    flag += 1
    flag %= 3

GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=checkSW, bouncetime=200)

try:
    while True:
        if flag == 1:
            print_calling()
        elif flag == 2:
            print_wait()
        else:
            time.sleep(1)

except KeyboardInterrupt:
    pass