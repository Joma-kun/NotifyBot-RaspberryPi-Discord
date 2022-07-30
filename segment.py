import RPi.GPIO as GPIO
import time
import importlib

GPIO.setmode(GPIO.BCM)
sw_pin = 4
GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

global flag
flag = 0

    
#7seg
seg_num = {"A": 17, "B": 27, "C": 22, "D": 23, "E": 24, "F": 25, "G": 5}
GPIO.setup(seg_num["A"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["B"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["C"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["D"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["E"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["F"], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg_num["G"], GPIO.OUT, initial=GPIO.LOW)

def print_calling():
    cnt = 0
    while True:
        #C
        GPIO.output(seg_num["A"], GPIO.HIGH)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
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
        if flag == 2:
            break
        time.sleep(0.5)
        cnt += 1
        if cnt > 10:
            flag = 3
            break

def print_welcome():
    global flag
    while True:
        #W
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.HIGH)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.LOW)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        time.sleep(0.5)
        #E
        GPIO.output(seg_num["A"], GPIO.HIGH)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        time.sleep(0.5)
        #L
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        time.sleep(0.5)
        #C
        GPIO.output(seg_num["A"], GPIO.HIGH)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        time.sleep(0.5)
        #O
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.HIGH)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.LOW)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        time.sleep(0.5)
        #M
        GPIO.output(seg_num["A"], GPIO.HIGH)
        GPIO.output(seg_num["B"], GPIO.HIGH)
        GPIO.output(seg_num["C"], GPIO.HIGH)
        GPIO.output(seg_num["D"], GPIO.LOW)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.LOW)
        time.sleep(0.5)
        #E
        GPIO.output(seg_num["A"], GPIO.HIGH)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        time.sleep(0.5)
        cnt += 1
        if cnt > 5:
            flag = 0
            break

def print_sorry():
    global flag
    while True:
        #S
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.HIGH)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.LOW)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        if flag == 0:
            break
        time.sleep(0.5)
        #O
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.HIGH)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.LOW)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        if flag == 0:
            break
        time.sleep(0.5)
        #R
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.LOW)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.LOW)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        if flag == 0:
            break
        time.sleep(0.5)
        #R
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.LOW)
        GPIO.output(seg_num["C"], GPIO.LOW)
        GPIO.output(seg_num["D"], GPIO.LOW)
        GPIO.output(seg_num["E"], GPIO.HIGH)
        GPIO.output(seg_num["F"], GPIO.LOW)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        if flag == 0:
            break
        time.sleep(0.5)
        #Y
        GPIO.output(seg_num["A"], GPIO.LOW)
        GPIO.output(seg_num["B"], GPIO.HIGH)
        GPIO.output(seg_num["C"], GPIO.HIGH)
        GPIO.output(seg_num["D"], GPIO.HIGH)
        GPIO.output(seg_num["E"], GPIO.LOW)
        GPIO.output(seg_num["F"], GPIO.HIGH)
        GPIO.output(seg_num["G"], GPIO.HIGH)
        if flag == 0:
            break
        time.sleep(0.5)
        cnt += 1
        if cnt > 10:
            flag = 0
            break
        
        
def print_none():
    GPIO.output(seg_num["A"], GPIO.LOW)
    GPIO.output(seg_num["B"], GPIO.LOW)
    GPIO.output(seg_num["C"], GPIO.LOW)
    GPIO.output(seg_num["D"], GPIO.LOW)
    GPIO.output(seg_num["E"], GPIO.LOW)
    GPIO.output(seg_num["F"], GPIO.LOW)
    GPIO.output(seg_num["G"], GPIO.LOW)
