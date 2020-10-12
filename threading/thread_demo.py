import time
from threading import Thread


class TestThread(Thread):
    def __init__(self, name='', *args, **kargs):
        Thread.__init__(self, name=name)

    def run(self):
        print("Thread is running: {}".format(self.name))
        time.sleep(5)

if __name__ == '__main__':
    test_thread = TestThread("x")
    test_thread.start()
    # You will got an error
    test_thread.start()
    print("Finished")
    