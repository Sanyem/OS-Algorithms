import matplotlib.pyplot as matlabPlot
import functools,random
q,list_1=[],[]
print("we take length of queue as 8")
print("Taking queue as [98,183,37,122,14,124,65,67]")
print("Taking starting starting_head as 53")
length=8
q=[98,183,37,122,14,124,65,67]
starting_head=53
for _ in range(0,length):
    list_1.append(abs(starting_head-q[_]))
print(list_1)
for _ in range(0,length):
    for b in range(_,length):
        if(list_1[_]>list_1[b]):
            temporary=list_1[_]
            list_1[_]=list_1[b]
            list_1[b]=temporary
            temporary=q[_]
            q[_]=q[b]
            q[b]=temporary
print(list_1)
print(q)
find=0
list_2=[starting_head]
for _ in range(0,length):
    find=find+abs(starting_head-q[_])
    starting_head=q[_]
    list_2.append(starting_head)
print(list_2)    
print("seek time - " + str(find))
print("average -  " + str(find/float(length)))
matlabPlot.plot(list_2[0:],marker='x',color='green',label='starting_head movement')
matlabPlot.legend(loc='upper left')
matlabPlot.ylabel('Disk I/O requests')
matlabPlot.yticks(list_2[0:],list_2[0:])
matlabPlot.style.use('ggplot')
matlabPlot.show()