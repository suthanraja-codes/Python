import threading
import time

def update_db():
    print("updating Database...")
    time.sleep(5)
    print("Updated Database Successfully")

def num_count(num):
    for i in range(1,num+1):
        print(i)


threaded = threading.Thread(target=update_db)
threaded.start()
num_count(10)
print(threading.active_count())
print(threading.enumerate())
threaded.join()

print("Bye")