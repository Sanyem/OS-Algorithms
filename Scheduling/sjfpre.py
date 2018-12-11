import random
import numpy as numpyPlot
import matplotlib.pyplot as matlabPlot
inp=int(input())
pcs,burst_time=[],[]
for _ in range(inp):
    list_1=[]
    list_1.append(random.randint(1,10))  
    list_1.append(random.randint(0,inp+2)) 
    list_1.append(_+1)                   
    pcs.append(list_1)
    burst_time.append(list_1[0])
list_2,list_3=[0]*inp, [0]*inp
totalWaitingTime,totalTurnaroundTime,end=0,0,0
a,least,check=0,0,0
min=max(burst_time)+1
odr=[0]
list_4=[]
while(end!=inp):
    for b in range(inp):
        if((pcs[b][1] <= a) and (burst_time[b]<min) and (burst_time[b])):
            min=burst_time[b]
            least=b
            check=1;
    if(check==0):
        a+=1
        continue
    if(pcs[least][2] !=odr[-1]):
            odr.append(pcs[least][2])
            list_4.append(a)
    burst_time[least]-=1
    min=burst_time[least];
    if(min==0):
        min=max(burst_time)+1
    if(burst_time[least]==0):
        end+=1
        finish_time=a+1
        list_2[least]=finish_time-pcs[least][0]-pcs[least][1]
        if(list_2[least]<0):
            list_2[least]=0
    a+=1
list_4.append(a)
for _ in range(inp):
    list_3[_]=pcs[_][0]+list_2[_]
for _ in range(inp):
    totalWaitingTime=totalWaitingTime+list_2[_]
    totalTurnaroundTime+=list_3[_]
    print(pcs[_][2],pcs[_][0],pcs[_][1],list_2[_],list_3[_])
print("Order=",odr)
length=len(odr)
yaxis,xplot_1,xplot_2=[],[],[]
for _ in range(1,len(odr)):
    yaxis.append('P'+str(odr[_]))
    xplot_1.append(list_4[_-1])
    xplot_2.append(list_4[_])
matlabPlot.hlines(yaxis,xplot_1,xplot_2,linewidth=2,color='green')
matlabPlot.show()