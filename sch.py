#import schedule 
#import time 
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
## Functions setup 
#def sudo_placement(): 
#    print("Get ready for Sudo Placement at Geeksforgeeks") 
#    return schedule.CancelJob
#def good_luck(): 
#    print("Good Luck for Test") 
#    return schedule.CancelJob
#def work(): 
#    print("Study and work hard") 
#    return schedule.CancelJob
#def bedtime(): 
#    print("It is bed time go rest") 
#    return schedule.CancelJob
#def geeks(): 
#    print("Shaurya says Geeksforgeeks") 
#    return schedule.CancelJob
#schedule.clear()  
## Task scheduling 
## After every 10mins geeks() is called.  
#schedule.every(10).seconds.do(geeks) 
#
### After every hour geeks() is called. 
##schedule.every().hour.do(geeks) 
#  
## Every day at 12am or 00:00 time bedtime() is called. 
#schedule.every().day.at("11:41").do(bedtime) 
#  
#
#schedule.every().day.at("11:42").do(good_luck) 
## After every 5 to 10mins in between run work() 
##schedule.every(5).to(10).minutes.do(work) 
##  
### Every monday good_luck() is called 
##schedule.every().monday.do(good_luck) 
##  
### Every tuesday at 18:00 sudo_placement() is called 
##schedule.every().tuesday.at("18:00").do(sudo_placement) 
#  
## Loop so that the scheduling task 
## keeps on running all time. 
#while True: 
#  
#    # Checks whether a scheduled task  
#    # is pending to run or not 
#    schedule.run_pending() 
#    time.sleep(1) 
##    schedule.every(10).seconds.do(geeks) 

import time
from threading import Thread
import schedule 
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
tim = ['12:34', '12:35']
schedule.clear()
def call_google():
    print('done')
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    return schedule.CancelJob

def sleeper(i):
    print ("thread %s sleeps for 5 seconds" % i)
    schedule.every().day.at(i).do(call_google) 
    print ("thread %s woke up" % i)

for i in range(len(tim)):
    t = Thread(target=sleeper, args=(tim[i],))
    t.start()
#    t.join()
while True: 
#  
#    # Checks whether a scheduled task  
#    # is pending to run or not 
    schedule.run_pending() 
#    time.sleep(1) 
##    schedule.every(10).seconds.do(geeks)
