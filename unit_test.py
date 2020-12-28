import CRD_operations as crd

crd.create('pramod', 77) #with no time-to-live property

crd.create('bhaskar', 16, 3600) #with time-to-live property

crd.read('pramod') #returns the value for respective key

crd.read('bhaskar') #return the value for respective key

crd.delete('pro') #return error because key not existed in database

crd.delete('bhaskar') #return delete respective key from database

t1 = Thread(target = (create or read or delete), args = (key, value, timeout)) #as per the operation
t1.start()
t1.sleep()
t2 = Thread(target = (create or read or delete), args = (key, value, timeout)) #as per the operation
t2.start()
t2.sleep()