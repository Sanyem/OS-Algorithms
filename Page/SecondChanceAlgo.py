import matplotlib.pyplot as matlab_plots
page_array,frame_array,pages_falts_list,frameno_list=[],[],[],[]
tf=[]
rp,c,compl=0,0,0
print("number of pages")
length=int(input())
print("page numbers")
for _ in range(0,length):
    page_array.append(int(input()))
    tf.append(0)
for a in range(1,8):
    print("number of frames")
    g=a
    print(a)
    frame_array = []
    for x in range(1,g+1):
        frame_array.append(0)
    for x in range(0,length):
        q=page_array[x]
        check1=0
        if(compl!=0):
            for y in range(0,compl):
                if(q==frame_array[y]):
                    check1=1
                    tf[y]=1
                    break
        if(check1!=1):
            pl=page_array[x]
            if(compl!=g):
                tf[compl]=1
                frame_array[compl]=pl
                compl=compl+1
            else:
                while(tf[rp]!=0):
                    tf[rp]=0
                    rp=rp+1
                    if(rp==g):
                        rp=0
                frame_array[rp]=pl
                tf[rp]=1

            print("elements in frame_array : ")
            print(frame_array)
            c=c+1
    print("Number of page_array faults "+ str(c-1))
    pages_falts_list.append(int(c-1))
    frameno_list.append(a)

matlab_plots.plot(frameno_list,pages_falts_list,marker='p',color='green',label='Page Faults')
matlab_plots.legend(loc='upper left')
matlab_plots.xlabel('Total Number of Frames')
matlab_plots.ylabel('Page Faults')
matlab_plots.xticks(frameno_list,frameno_list)
matlab_plots.style.use('ggplot')
matlab_plots.show()
