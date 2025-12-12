
import logging
from threading import Thread, Lock, Condition, Semaphore
import time


def func(n):
    print(n)

def create_thread():
    th = Thread(target=func, args=(10,))
    th.start()

# thread join: Hold parent until thread is complete.
# th.join()

def create_lock(lock, n):

    print('started',n)
    lock.acquire()
    print('locked',n)
    time.sleep(n)
    lock.release()

    print('done',n)

def create_condition():
    c = Condition()
    c.acquire()
    c.wait()
    c.notify()
    c.release()

c = 0
def create_Semaphor(idx, s):
    global c
      # 2 thread can acquire this semaphor
    s.acquire()
    c+=1
    #s.wait()
    #s,notify()
    print(c)
    time.sleep(1)

    s.release()
    c-=1


if __name__ == "__main__":
    th = []
    s = Semaphore(0)
    for i in range(10):
        t = Thread(target=create_Semaphor, args=(i,s))
        t.start()

# if __name__ == "__main__":
#     lock = Lock()
#     th1 = Thread(target=create_lock, args=(lock,5))
#     th2 = Thread(target=create_lock, args=(lock,1))

#     #lock2 - Lock()
#     #th2 = Thread(target=create_lock, args=(lock2,1))

#     th1.start()
#     th2.start()

#     th1.join()
#     th2.join()

# RLock: n times lock aquire and n times release by the same thread.
# http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/

# Lock -> RLock -> Condition -> Semaphor

# wait()
#   condition.release()

#   lock = Lock()
#   lock.acquire() # first acquire
#   waiters.append(lock)

#   lock.acquire() # second acquire makes it wait
#   condition.acquire()
#   lock.release()

# notify()
#   lock = waiters.pop(0)
#   lock.release()


# Consume one item
# cv.acquire()
# while not an_item_is_available():
#     cv.wait()
# get_an_available_item()
# cv.release()


# # Produce one item
# cv.acquire()
# make_an_item_available()
# cv.notify()
# cv.release()



















# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     threads = list()
#     for index in range(3):
#         logging.info("Main    : create and start thread %d.", index)
#         x = Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()

#     for index, thread in enumerate(threads):
#         logging.info("Main    : before joining thread %d.", index)
#         thread.join()
#         logging.info("Main    : thread %d done", index)

