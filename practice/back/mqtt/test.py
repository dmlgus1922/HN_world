import air_mongo
from multiprocessing import Process, Queue
import time

def main():
    air_queue = Queue()

    p1 = Process(name="get_air", target=air_mongo.air_mongo, args=(air_queue,))

    p1.start()
    p1.join()

    while True:
        time.sleep(10)
        data = air_queue.get()
        air_queue.put(data)
        print(data)

if __name__ == '__main__':
    main()