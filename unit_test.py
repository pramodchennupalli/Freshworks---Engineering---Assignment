import CRD_operations as crd

crd.create('pramod', 77) #with no time-to-live property

crd.create('bhaskar', 16, 3600) #with time-to-live property

crd.read('pramod') #returns the value for respective key

crd.read('bhaskar') #return the value for respective key

crd.delete('pro') #return error because key not existed in database

crd.delete('bhaskar') #return delete respective key from database

