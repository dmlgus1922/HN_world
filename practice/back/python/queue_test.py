import threading
import queue
import time

def test(q):
    print('두번째 스레드 시작')

    def inner_thread():
        print('inner_thread 시작')
        time.sleep(1)
        q.put('main stop!')

    
    i = threading.Thread(target=inner_thread)
    i.start()

    time.sleep(2)

def test2():
    print('첫 번째 스레드 시작\n')
    time.sleep(1)
    t = threading.Thread(target=test, args=(q,))
    t.start()


q = queue.Queue()

test2()


while True:
    time.sleep(0.1)
    print('main running')
    if not q.empty():
        print(q.get())
        break