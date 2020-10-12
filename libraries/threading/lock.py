import time
import threading


class work(threading.Thread):
    def __init__(self, tname, tid ):
        threading.Thread.__init__(self)
        self.tid = tid
        self.tname = tname

    def run(self):
        lock.acquire
        job(self.tname, self.tid)
        lock.release()


def job(tname, tid):
    for i in range(1000):
        print("name: " + tname + " - id: " + str(tid) + ": " + str(i))
        time.sleep(1)


w = work("eat", 1)
w2 = work("play", 2)
lock  = threading.Semaphore()
w.start()
w2.start()
