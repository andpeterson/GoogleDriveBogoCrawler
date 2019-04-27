import requests
import random
import time
seq = "1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

def main():
    while(True):
        string = randomString(33)
        URL = "https://drive.google.com/file/d/" + string + "/view?usp=sharing"
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


def randomString(len):
    string = ""
    for i in range(len):
        string += (random.choice(seq))
    return string


main()

