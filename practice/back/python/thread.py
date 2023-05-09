import threading
import time

def worker():
    print("Worker thread started")
    time.sleep(2)
    print("Worker thread finished")

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)
t1.start()
t2.start()
t1.join()  # t1 스레드가 종료될 때까지 대기
print("Main thread finished")