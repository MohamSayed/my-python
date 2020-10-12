import time
import multiprocessing as mp


def sub_function():
    print("sub function")


def do_something(q):
    print("do_something: started")
    time.sleep(1.0)
    for data in iter(q.get, None):
        print(f"do_something: {data}")
        if(data == "sub_function"):
            sub_function()
        elif data == "stop":
            print("do_something: received stop signal from the queue")
            pass
    print("do_something: finished")


if __name__ == '__main__':
    command = mp.Queue()
    p1 = mp.Process(target=do_something, args=[command])
    st = time.perf_counter()
    p1.start()

    command.put(1)
    command.put(2)
    command.put(3)
    command.put(4)
    command.put("sub_function")
    command.put("stop")
    # put(ing) to stop iter(...) function
    command.put(None)
    p1.join()
    ft = time.perf_counter()
    print(f"finish time: { ft - st }")
