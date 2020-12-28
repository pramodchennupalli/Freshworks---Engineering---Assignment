import threading
import time
from threading import *

dict = {}

def create(key, value, timeout=0):
    if key in dict:
        print('error: This key already exists')
    else:
        if len(dict) < pow(1024, 3) and value <= 16 * pow(1024, 2):
            if(key.isalpha()):
                if timeout == 0:
                    li = [value, timeout]
                else:
                    li = [value, time.time() + timeout]
            else:
                print('error: Invalid Key (Note: key must contain only alphabet)')
        else:
            print('error: Memory limit exceeded')


def read(key):
    if key not in dict:
        print('error: Given key not found. Enter valid Key')

    else:

        p = dict[key]
        if p[1] != 0:
            if time.time() < p[1]:
                return str(key)+":"+str(p[0])
            else:
                print('error: time-to-live of', key, 'has expired')
        else:
            return str(key)+':'+str(p[0])
