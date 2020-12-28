import time
from threading import *

import CRD_operations as crd

crd.create('pramod', 77)  # with no time-to-live property

crd.create('bhaskar', 16, 3600)  # with time-to-live property

print(crd.read('pramod'))  # returns the value for respective key

print(crd.read('bhaskar'))  # return the value for respective key

crd.delete('pro')  # return error because key not existed in database

crd.delete('bhaskar')  # return delete respective key from database

t1 = Thread(target=(crd.create or crd.read or crd.delete))  # as per the operation
t1.start()
time.sleep(1)
t2 = Thread(target=(crd.create or crd.read or crd.delete))  # as per the operation
t2.start()
time.sleep(1)
