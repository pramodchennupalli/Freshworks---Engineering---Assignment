import time

dic = {}


def create(key, value, timeout=0):
    if key in dic:
        print('error: This key already exists')
    else:
        if len(dic) < pow(1024, 3) and value <= 16 * pow(1024, 2):
            if key.isalpha():
                if timeout == 0:
                    li = [value, timeout]
                else:
                    li = [value, time.time() + timeout]
                if len(key) <= 32:
                    dic[key] = li
            else:
                print('error: Invalid Key (Note: key must contain only alphabet)')
        else:
            print('error: Memory limit exceeded')


def read(key):
    if key not in dic:
        print('error: Given key not found. Enter valid Key')
    else:
        p = dic[key]
        if p[1] != 0:
            if time.time() < p[1]:
                return str(key) + ":" + str(p[0])
            else:
                print('error: time-to-live of', key, 'has expired')
        else:
            return str(key) + ':' + str(p[0])


def delete(key):
    if key not in dic:
        print('error: Given key not found. Enter valid Key')
    else:
        p = dic[key]
        if p[1] != 0:
            if time.time() < p[1]:
                del dic[key]
                print('Deleted Successfully !!')
            else:
                print('error: time-to-live of', key, 'has expired')
        else:
            del p[key]
            print('Deleted Successfully !!')

