import matplotlib.pyplot as matlab_plot
import functools
import random
def bubbleSort(q,length):
    for a in range(0,length-1):
        least = q[a]
        l = a
        for b in range(a+1,length):
            if(least > q[b]):
                least = q[b]
                l = b
        temp = q[l]
        q[l] = q[a]
        q[a] = temp
def CLOOK_disk(L,R,total_count,length,starting_head):
    get=0
    list_2 = []
    list_2.append(starting_head)
    j,i = total_count - 1,total_count + 1
    g,h=0,0
    while i < length + 1:
        list_2.append(R[g])
        g += 1
        i += 1
    list_2.append(199)
    list_2.append(0)
    while j > -1:
        list_2.append(L[j])
        j -= 1
        h += 1
    for a in range(0,len(list_2)):
        get=get+abs(starting_head-list_2[a])
        starting_head=list_2[a]
    print("Order of Scanning")
    print(list_2)
    print("Total Seek Time is " + str(get))
    print("Average Seek Time is " + str(get/float(length)))

    matlab_plot.plot(list_2[0:],marker='x',color='green',label='starting_head movement')
    matlab_plot.legend(loc='upper left')
    matlab_plot.ylabel('I/O requests')
    matlab_plot.yticks(list_2[0:],list_2[0:])
    matlab_plot.style.use('ggplot')
    matlab_plot.show()
def divide(q,length,starting_head):
    L = []
    R = []
    for a in range(0,length):
        if(q[a] > starting_head):
            break
    p,m = 0,length
    L.append(q[0])
    for matlab_plot in range(1,a):
        L.append(q[matlab_plot])
    k=a
    for x in range(k,length):
        R.append(q[x])
    L=L[::-1]
    CLOOK_disk(L,R,a,length,starting_head)
q=[]
list=[]
print("taking length of q = 8")
length=8
print("Taking the queue aas : 98,183,37,122,14,124,65,67")
q=[98,183,37,122,14,124,65,67]
print("Taking starting starting_head as 53")
starting_head=53
print(q)
bubbleSort(q,length)
divide(q,length,starting_head)
