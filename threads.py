import threading
import time,sys
from base64 import b64encode,b64decode
# word="ezio auditore frenze"
# encoded=b64encode(word.encode('utf-8'))
# sys.stdin("")
# print(encoded)
# decoded=b64decode(encoded.decode('utf-8'))
# print(decoded)
lock=threading.Lock()#to make the 1 use of thread resource each time.
event=threading.Event()
def thread_function(value):
  with lock:
    print(f"thread {value} has the lock")
    time.sleep(5)
    print(f"thread {value} releasing the lock")
if __name__=='__main__':
    threads=[]
    for i in range(3):
       thread=threading.Thread(target=thread_function,args=(i,))
       threads.append(i)
       thread.start()#start each thread at time
    for i in threads:
        thread.join()  #release each thread lock