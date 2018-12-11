import matplotlib.pyplot as matlab_plots
import functools
import random
faultPages = []
frame_number = []
page_array=[]
print("taking total number of pages as")
page_array = [20, 13, 9, 14, 12, 17, 5, 2, 16, 7, 14, 7, 8, 7, 13]
length = 15
print(page_array)
for a in range(1,8):
	print("total no. of frames"),
	print(a)
	frame_array=[]
	g=a
	for y in range(0,g):
	    frame_array.append(-1)
	x=0
	op=0
	for y in range(0,length):
	    aval=0
	    for k in range(0,g):
	        if(frame_array[k]==page_array[y]):
	            aval=1
	    if(aval == 0):
	        frame_array[x]=page_array[y]
	        x=(x+1)%g
	        op=op+1
	        print(frame_array ),
	    print("length")

	print("page fault is: "),
	print(op)
	faultPages.append(op)
	frame_number.append(a)
matlab_plots.plot(frame_number[0:],faultPages[0:],marker='x',color='green',label='page_array faults')
matlab_plots.legend(loc='upper left')
matlab_plots.xlabel('No. of frames')
matlab_plots.ylabel('page_array faults')
matlab_plots.xticks(frame_number[0:],frame_number[0:])
matlab_plots.style.use('ggplot')
matlab_plots.show()