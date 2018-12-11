import pandas as pandasPlot
import matplotlib.pyplot as matlabPlot
import random
inp=int(input())
pcs,burst_time=[],[]
for _ in range(0,inp):
 pcs.insert(_,_+1)
 burst_time.append(random.randint(0,10))
print(burst_time)
prt=random.sample(range(1,inp+1),inp)
print(prt)
wait_time=[]
length=len(prt)
for _ in range(0,length-1):
 for k in range(0,length-_-1):
  if(prt[k]>prt[k+1]):
   temporary=prt[k]
   prt[k]=prt[k+1]
   prt[k+1]=temporary
   temporary=burst_time[k]
   burst_time[k]=burst_time[k+1]
   burst_time[k+1]=temporary
   temporary=pcs[k]
   pcs[k]=pcs[k+1]
   pcs[k+1]=temporary
wait_time.insert(0,0) 
for _ in range(1,len(pcs)+1):
 wait_time.insert(_,wait_time[_-1]+burst_time[_-1])
print(wait_time)
avgwt=0
avgwt=float(sum(wait_time))/inp
print(avgwt)
pandasPlot.DataFrame(wait_time).T.plot.barh(stacked=True)
matlabPlot.show()
