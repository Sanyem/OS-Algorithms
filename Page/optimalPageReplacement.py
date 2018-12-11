import matplotlib.pyplot as matlab_plot
import functools
import random
pages_faults_array,frame_numbers_array,page_list = [],[],[]
frame_list,temporary_array,faults_array=[],[],[]
print("pages:")
page_list = [20, 13, 9, 14, 12, 17, 5, 2, 16, 7, 14, 7, 8, 7, 13]
length = 15
print(page_list)    
for g in range(1,8):
	print("NUMBER OF FRAMES : ")
	print(g)
	frame_list=[]
	faults_array = 0
	h=g
	for x in range(0,h):
	    frame_list.append(-1)
	for x in range(0,length):
	    check,check_1=0,0
	    for y in range(0,h):
	        if(frame_list[y] == page_list[x]):
	            check=1
	            check_1=1
	            break
	    if check== 0:
	        for y in range(0,h):
	            if(frame_list[y] == -1):
	                faults_array=faults_array+1
	                frame_list[y]=page_list[x]
	                check_1=1
	                break
	    if check_1 == 0:
	        check_2=0
	        for y in range(0,h):
	            temporary_array.append(-1)
	            for k in range(x+1,h):
	                if (frame_list[y] == page_list[k]):
	                    temporary_array[y]=k
	                    break
	        for y in range(0,h):
	            if (temporary_array[y] == -1):
	                place=y
	                check_2=1
	                break
	        if(check_2==0):
	            mr=temporary_array[0]
	            place=0
	            for y in range(1,h):
	                if(temporary_array[y]>mr):
	                    mr=temporary_array[y]
	                    place=y
	        frame_list[place]=page_list[x]
	        faults_array=faults_array+1
	    print(frame_list)
	print("total page_list faults_array "),
	print(faults_array)
	pages_faults_array.append(faults_array)
	frame_numbers_array.append(g)
matlab_plot.plot(frame_numbers_array[0:],pages_faults_array[0:],marker='x',color='green',label='page faults_array')
matlab_plot.legend(loc='upper left')
matlab_plot.xlabel('No. of frames')
matlab_plot.ylabel('page_list faults_array')
matlab_plot.xticks(frame_numbers_array[0:],frame_numbers_array[0:])
matlab_plot.style.use('ggplot')
matlab_plot.show()