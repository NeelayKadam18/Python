import schedule
import time
import datetime

def Fun():
    print("Inside Fun")
    print("Inside fun at the time : ", datetime.datetime.now())

def main():
    print("Inside Task Scheduler")
    print("Current time is : ",datetime.datetime.now())
    schedule.every(1).minutes.do(Fun)

    while(True):                        # unconditional infinite loop
        schedule.run_pending()          # checks for pending work
        time.sleep(1)                   # 1 sec

if __name__ == "__main__":
    main()