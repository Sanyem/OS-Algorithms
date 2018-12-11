import matplotlib.pyplot as matlab_plot
import functools
import random
page_fault,frame_number = [],[]
page_array,frame_list,time_array=[],[],[]
def LRU_pageReplacement (length):
    minimum=time_array[0]
    place=0
    for x in range(0,length):
        if(time_array[x]<minimum):
            minimum=time_array[x]
            place=x
    return place
cr=0
total_faults=0
print("pages")
page_array = [20, 13, 9, 14, 12, 17, 5, 2, 16, 7, 14, 7, 8, 7, 13]
length = 15
print(page_array)
for g in range(1,8):
	print("Frames")
	print(g)
	frame_list = []
	total_faults = 0
	h = g
	for x in range(1,h+1):
	    frame_list.append(-1)
	print(page_array)
	for x in range(0,length):
	    check=0
	    check_2=0
	    for y in range(0,h):
	        if(frame_list[y] == page_array[x]):
	            cr = cr+1
	            time_array.append(cr)
	            check=1
	            check_2=1
	            break
	    if ( check== 0 ):
	        for y in range(0,h):
	            if(frame_list[y] == -1):
	                cr = cr+1
	                total_faults=total_faults+1
	                frame_list[y]=page_array[x]
	                time_array.append(cr)
	                check_2=1
	                break
	    if (check_2 == 0):
	        place=LRU_pageReplacement(h)
	        cr = cr+1
	        total_faults=total_faults+1
	        frame_list[place]=page_array[x]
	        time_array[place]=cr
	    print(frame_list)
	print("total page_array total_faults "),
	print(total_faults)
	page_fault.append(total_faults)
	frame_number.append(g)
matlab_plot.plot(frame_number[0:],page_fault[0:],marker='x',color='green',label='page_array total_faults')
matlab_plot.legend(loc='upper left')
matlab_plot.xlabel('No. of frames')
matlab_plot.ylabel('page_array total_faults')
matlab_plot.xticks(frame_number[0:],frame_number[0:])
matlab_plot.style.use('ggplot')
matlab_plot.show()