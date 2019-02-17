from datetime import datetime
import requests
import time

def check_internet():
    try:
        r = requests.get("http://bbc.co.uk", timeout=1)
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.ConnectionError:
        return False
    return True

if __name__ == '__main__':
    while(True):
        result = check_internet()
        if result:
            print("[{}] OK".format(datetime.now()))
        else:
            print("[{}] Fail".format(datetime.now()))

        time.sleep(5)
