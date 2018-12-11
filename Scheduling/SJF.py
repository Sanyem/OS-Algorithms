import functools
import random
import numpy as numpyPlot
import matplotlib.pyplot as matlabPlot
inp=int(input())
btm,pcs,list_1,list_2 = [],[],[],[]
t,s=0,0
for _ in range(1,inp+1):
     btm.append(random.randint(1,10))
     pcs.append(_)
print(pcs,btm)
print('after sorting')
for _ in range(0,inp):
	for q in range(0,inp):
		if(btm[_] < btm[q]):
			temporary = btm[_]
			btm[_] = btm[q]
			btm[q] = temporary
			temporary = pcs[_]
			pcs[_] = pcs[q]
			pcs[q] = temporary
print (btm,pcs)
list_1.append(0)
for q in range(0,inp-1):
    s=s+int(btm[q])
    list_1.append(s)
for q in range(0,inp):
    t=int(btm[q])+list_1[q]
    list_2.append(t)
length = len(list_2)
protime = [0]
for _ in range(0,length):
	protime.append(list_2[_])
print(protime)
aWaitTime=functools.reduce(lambda x,y:x+y,list_1)
aTurnTime=functools.reduce(lambda x,y:x+y,list_2)
print("avg. waiting time "),
print(aWaitTime/inp)
print("avg. turnaround time "),
print(aTurnTime/inp)
list_3,list_4,list_5 = [],[],[]
for _ in range(1,length+1):
        list_3.append('P'+str(pcs[_-1]))
        list_4.append(protime[_-1])
        list_5.append(protime[_])
matlabPlot.hlines(list_3,list_4,list_5,linewidth=2,color='green')
matlabPlot.show()