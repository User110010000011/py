from multiprocessing import Process,Pipe,Lock
import os,json
from logging import LogRecord
# record=LogRecord()
# extra=record.extra['']
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
    
def f(conn):
    # info('function f')
    # print('hello', name)
    msg=conn.send("message recieved from f() method")
    # msg.encode('utf-8') #//optional
    conn.close()

if __name__ == '__main__':
    info('main line')
    send_conn,recv_conn=Pipe()
    p = Process(target=f, args=(send_conn,))
    p.start()
    recieved_message=recv_conn.recv()
    print(recieved_message)
    # reply=recieved_message.decode("utf-8")
    p.join()