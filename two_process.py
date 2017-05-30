from multiprocessing import Process
import time

def f(i):
	while i>0:
		i-=1


c = 10**8
start=time.time()

if __name__ == '__main__':
    p = Process(target=f, args=(c//2,))
    p2 = Process(target=f, args=(c//2,))
    #p3 = Process(target=f, args=(c//2,))
    #p4 = Process(target=f, args=(c//2,))
    
    p.start()
    p2.start()
    #p3.start()
    #p4.start()
    
    p.join()
    p2.join()
    #p3.join()
    #p4.join()

end = time.time()
print(end-start)