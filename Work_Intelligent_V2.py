from win10toast import ToastNotifier
import time
import datetime

def work_countdown(n=52):
    print ("INFO " + str(datetime.datetime.now()) + " => StartWorking")
    while n > 0:
        n = n - 1
        time.sleep(60)
        if n == 0:
            toaster = ToastNotifier()
            toaster.show_toast("Rest for 17 minutes!!!","Rest 17 minutes to get focused")
            print ("INFO " + str(datetime.datetime.now()) + " => Rest for 17 minutes!!!")
            break

def rest_countdown(n=17):
    print ("INFO " + str(datetime.datetime.now()) + " => Init Rest")
    while n > 0:
        n = n - 1
        time.sleep(60)
        if n == 0:
            toaster = ToastNotifier()
            toaster.show_toast("The rest is over!!!","Let's continue working")
            print("INFO " + str(datetime.datetime.now()) + " => The rest is over!!!")
            break
           
while True:
    rest_countdown()
    work_countdown()
