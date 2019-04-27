import requests
import random
import time
import sys
import signal
seq = "1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

def main():
    while(True):
        string = randomString(33)
        URL = "https://drive.google.com/file/d/" + string + "/view?usp=sharing"
        try:
            res = requests.get(url = URL)
            status = res.status_code
            if status == 200:
                file = open("200.txt", "a+")
                file.write(URL + "\n")
                file.close()
                print(URL)
            elif status == 500:
                file = open("500.txt", "a+")
                file.write(URL + "\n")
                file.close()
                print(str(status) + ": " + string)
            elif status == 404:
                print(str(status) + ": " + string)
            else:
                file = open("other.txt", "a+")
                file.write(URL + "\n")
                file.close()
                print(str(status) + ": " + string)
        except:
           print("Domain failed to connect")

def on_press(key):
    if key == 'q':
        sys.exit(1)
    
def randomString(len):
    string = ""
    for i in range(len):
        string += (random.choice(seq))
    return string

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught.".format(signal))
    if(signal == 2):
        print("Ctrl+C caught. Exiting...")
        exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

print("Starting crawler")
main()

