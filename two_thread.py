import time
from threading import Thread 

def f(i):
	while i>0:
		i-=1

c = 10**8
start=time.time()
#t1=thread.start_new_thread( f, (c/2, ) )
#t2=thread.start_new_thread( f, (c/2, ) )
t1 = Thread(target=f,args = (c//2,))
t2 = Thread(target=f,args = (c//2,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(end-start)