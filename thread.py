from threading import *
from time import sleep


class work(Thread):
    def worker_function(self):
        print("Worker thread is running")
        sleep(2)


class person(Thread):
    def person_function(self):
        print("Person is running")
        sleep(2)


# Create two thread objects
t1 = work()
t2 = person()

t1.worker_function()
t2.person_function()

print("Both threads have finished")


def worker_function():
    print("Worker thread is running")

thread.start_new_thread(worker_function, ())

