import time
import multiprocessing as mp


def do_something():
    print("do_something: started")
    time.sleep(3.0)
    print("do_something: finished")


if __name__ == '__main__':
    p1 = mp.Process(target=do_something)
    st = time.perf_counter()
    p1.start()
    p1.join()
    ft = time.perf_counter()
    print(f"finished time: { ft - st }")
