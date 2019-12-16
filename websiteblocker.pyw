import time
from datetime import datetime as dt

""" This is a website blocker script which blocks user given sites by redirecting them to a given IP address"""

host_path = r"C:\Windows\System32\drivers\etc\hosts" # this is the locations of the host file
host_temp = r"C:\Users\tmuza\Downloads\Tsoro Game\Website blocker\hosts"
redirect = "127.0.0.1" #redirect IP addresss
websites = ["www.facebook.com","facebook.com","www.youtube.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("Get Busy sir......")
        with open(host_temp, 'r+') as file: #r+ enables read and write to a file
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")

    else:
        with open(host_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(10)