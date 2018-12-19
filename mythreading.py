# Opens 5 threads with timestamps. Each thread makes a simple mathematical operation. Works in Python 2 and 3 (at least x2 faster)

import threading
import datetime

threads = []

def worker(counter):
    """thread worker function"""
    y=0

    for i in range(3000000):
        y+=i
    print('Thread: ',threads[counter])
    print('Stop: ',datetime.datetime.now())
    print('----------------------------------')
    return

for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    threads.append(t)
    print('Thread: ',threads[i])
    print('Start:  ',datetime.datetime.now())
    print('----------------------------------')
    t.start()

