import functools
import random
import numpy as numpyPlot
import matplotlib.pyplot as matlabPlot
inp=int(input())
burst_time,pcs,g,h=[],[],[],[]
a,b=0,0
for _ in range(1,inp+1):
    burst_time.append(random.randint(1,10))
    pcs.append(_)
print (burst_time)
g.append(0)
for _ in range(0,inp-1):
    b=b+int(burst_time[_])
    g.append(b)
for _ in range(0,inp):
    a=int(burst_time[_])+g[_]
    h.append(a)
length = len(h)
ptm = [0]
for _ in range(0,length):
	ptm.append(h[_])
print(ptm)
aWaitingTm=functools.reduce(lambda x,y:x+y,g)
aTurnaroundTm=functools.reduce(lambda x,y:x+y,h)
print("Avg. waiting time is"),
print(aWaitingTm/inp)
print("Avg. turnaround time is "),
print(aTurnaroundTm/inp)
y,x1,x2=[],[],[]
for _ in range(1,length+1):
        y.append('P'+str(pcs[_-1]))
        x1.append(ptm[_-1])
        x2.append(ptm[_])
matlabPlot.hlines(y,x1,x2,linewidth=2,color='green')
matlabPlot.show()