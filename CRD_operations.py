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

