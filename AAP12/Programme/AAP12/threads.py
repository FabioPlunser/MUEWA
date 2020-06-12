import threading 
from time import sleep

def count_to(thread_name="default", count_to=10, sleep_time=1.0):
    for i in range(count_to):
        print("Thread %s: %d" %(thread_name, i))
        sleep(sleep_time)


for thread_number in range(3):
    t = threading.Thread(target=count_to, args=(str(thread_number), 10)) # a thread ia an object
    t.start() #start this thread
    sleep(2) #wait before starting the next one