from multiprocessing import Pool
import time
def f(i):
	while i>0:
		i-=1


c = 10**8
start=time.time()
T = 4
if __name__ == '__main__':
    pool = Pool(T)
    args =[]
    for x in range(T):
        args+=[c/T]
    pool.map_async(f, args)
    pool.close()
    pool.join()

end = time.time()
print(end-start)