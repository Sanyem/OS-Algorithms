import random
import numpy as numpyPlot
import matplotlib.pyplot as matlabPlot
import copy
inp=int(input())
btm,atm,a=[],[],[]
for _ in range(inp):
    btm.append(random.randint(1,10))
    atm.append(random.randint(0,inp+2)) 
print(btm, atm)
btm_1=copy.deepcopy(btm)
begin,end,time=[],[],0
time_quantum=int(input())
while(1):
    check=0
    for i in range(inp):
        if(btm[i]>0 and atm[i]<=time):         
            if btm[i]>time_quantum:
                a.append(i)
                begin.append(time)
                time+=time_quantum
                btm[i]-=time_quantum
                check=1
            else:
                a.append(i)
                time+=btm[i]
                btm[i]=0
                begin.append(time)
                check=1
            end.append(time)
    if(check==0):
        time+=1
    if(sum(btm)==0):
        break
print(time)
matlabPlot.hlines(a,begin,end,linewidth=2,color='green')
matlabPlot.yticks(a)
matlabPlot.xlabel('time')
matlabPlot.ylabel('Process Number')
matlabPlot.show()