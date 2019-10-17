from win10toast import ToastNotifier
import time

def work_countdown(n=52):
    while n > 0:
        n = n - 1
        time.sleep(60)
        if n == 0:
            toaster = ToastNotifier()
            toaster.show_toast("Rest for 17 minutes!!!","Rest 17 minutes to get focused")
            print ("Rest for 17 minutes!!!")
            break

def rest_countdown(n=17):
    while n > 0:
        n = n - 1
        time.sleep(60)
        if n == 0:
            toaster = ToastNotifier()
            toaster.show_toast("The rest is over!!!","Let's continue working")
            print("The rest is over!!!")
            break
           
while True:
    rest_countdown()
    work_countdown()
