import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
def main():
    print(os.name)
    print("item exists:", str(path.exists("textfile.txt")))
    print("item is a file:", str(path.isfile("textfile.txt")))
    print("item is a dicectory:", str(path.isdir("textfile.txt")))

print("item's path:", path.realpath("textfile.txt"))
print("Item's path and name:", path.split("textfile.txt"))


t = time.ctime(path.getatime("textfile.txt"))
print(t)
print(datetime.datetime.fromtimestamp(path.getatime("textfile.txt")))


td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getatime("textfile.txt"))
print("It has been", td, "since the file was modified")
print("or,", td.total_seconds(),"Second")

if __name__ == "__main__":
    main()
