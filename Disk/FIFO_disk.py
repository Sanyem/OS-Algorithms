import matplotlib.pyplot as matlab_plot
import functools
import random
q=[]
frame=[]
last = []
length=8
print("input q"),
q = [98,183,37,122,14,124,65,67]
print(q)
print("taking starting starting_head as 53"),
starting_head = 53
print(starting_head)
starting=abs(starting_head-q[0])
for a in range(1,length):
    starting=starting+abs(q[a-1]-q[a])
print("Total Seek Time : " + str(starting))
print("Average Seek Time : " + str(starting/float(length)))
last = [starting_head]
for a in range(0,length):
	last.append(q[a])
matlab_plot.plot(last[0:],marker='x',color='green',label='starting_head movement')
matlab_plot.legend(loc='upper left')
matlab_plot.ylabel('Disk I/O requests')
matlab_plot.yticks(last[0:],last[0:])
matlab_plot.style.use('ggplot')
matlab_plot.show() 