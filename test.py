import multiprocessing
import time,os

def print(name):
    pid = os.getpid()
    ppid = os.getppid()
    print("My PID is %s, my Partent PID is%s, i am begining to work" % (pid,ppid))
    print("My name is %s" % name)
    time.sleep(5)
    print("I am done")


if __name__ =="__main__":
    # print("I am their, Father. My pid is %s" % (os.getpid()))
    print('Parent process %s.' % os.getpid())
    # p = multiprocessing.Pool()
    # for i in range(10):
    #     p.apply_async(print,args = [i,])
    # p.close()
    # print("第一次打印")
    # p.join()
    # print("第二次打印")