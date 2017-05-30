import time

def f(i):
	while i>0:
		i-=1

c = 10**8
start=time.time()
f(c)
end = time.time()
print(end-start)