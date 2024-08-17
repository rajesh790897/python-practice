from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    now = datetime.now()
    print("Today date is ",today," And Now time is", now)


if __name__ == "__main__":
    main()