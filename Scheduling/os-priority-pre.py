import random
import copy
import matplotlib.pyplot as matlabplot
length=int(input("Enter the no. of process : "))
prty=random.sample(range(1,length+1),length)
ar_time, bur_time, pcs=[],[],[]
bur_time_1=copy.deepcopy(bur_time)
for x in range(0,length):
    ar_time.append(random.randint(1,length+2))
    bur_time.append(random.randint(1,10))
    pcs.append("P"+str(x))
print()
for x in range(length-1):
    for y in range(x+1,length):
        if prty[x]>prty[y]:
            temporary=prty[x]
            prty[x]=prty[y]
            prty[y]=temporary
            temporary=bur_time[x]
            bur_time[x]=bur_time[y]
            bur_time[y]=temporary
            temporary=ar_time[x]
            ar_time[x]=ar_time[y]
            ar_time[y]=temporary
            temporary_1=pcs[x]
            pcs[x]=pcs[y]
            pcs[y]=temporary_1
on=max(ar_time)
order,op,fn=[],[],[]
bur_time_1=copy.deepcopy(bur_time)
time=0
while(time<on):
    check=0
    for x in range(0,length):
        if ar_time[x]<=time and bur_time[x]:
            op.append(time)
            time+=1
            bur_time[x]-=1
            order.append(pcs[x])
            fn.append(time)
            check=1
            break
    if check==0:
        time+=1
for x in range(length):
    order.append(pcs[x])
    op.append(time)
    time+=bur_time[x]
    fn.append(time)
on_1=min(ar_time)
ok=['0']
for x in range(len(order)):
    if ok[-1]!=order[x]:
        ok.append(order[x])
print("Process Burst TimeArrival Time Priority")
for x in range(length):
    k=order.index("P"+str(x))
    k1=pcs.index("P"+str(x))
    print(order[k]+"  "+str(bur_time_1[k1])+"  "+str(ar_time[k1])+"  "+str(prty[k1]))
print("order =",ok[1:])
matlabplot.hlines(order,op,fn,linewidth=15)
matlabplot.show()
