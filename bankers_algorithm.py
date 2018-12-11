import matplotlib.pyplot as matlab_plot
print("Enter testcases for bankers algo")
for _ in range(int(input())):
	list_1,list_2,list_3=[],[],[]
	print("Resources Available:-")
	resources_available = int(input())
	max = []
	print("instances for each resource")
	available_list = []
	for a in range(resources_available):
		max.append(int(input()))
		available_list.append(max[a])
	print("processes in queue - ")
	proc = int(input())
	allocation_table,max_table,need_table,processes_left,safe_order=[],[],[],[],[]	
	print("Enter resource instance allocated, max required, need")
	for a in range(proc):
		list_2.append(a)
		list_3.append('Process-'+str(a))
		print("Process ",a)
		print("Enter resources allocated")
		allocation_table.append(list(map(int,input().split(' '))))
		print("Enter the maxium resources required")
		max_table.append(list(map(int,input().split(' '))))
		l = []
		for b in range(resources_available):
			l.append(max_table[a][b]-allocation_table[a][b])
		need_table.append(l)
		if(need_table[a].count(0)==resources_available):
			processes_left.append(1)
			list_1.append(0)
		else:
			processes_left.append(0)
			list_1.append(0)
	for a in range(proc):
		for b in range(resources_available):
			available_list[b] =available_list[b]-allocation_table[a][b]
	print(available_list)
	a=0
	while(True):
		if(processes_left.count(1)==proc):
			break
		elif(a>100*proc):
			print("DEADLOCK!")
			break
		else:
			q = a%proc
			if(q not in safe_order):
				if(need_table[q].count(0)!=resources_available):
					flag = 0
					for b in range(resources_available):
						if(need_table[q][b]<=available_list[b]):
							flag += 1
					if(flag==resources_available):
						for x in range(resources_available):
							need_table[q][x]=0
							available_list[x]+=allocation_table[q][x]
						processes_left[q]=1 
						list_1[q] = a
						safe_order.append(q)
						a=a+1
					else:
						a=a+1
				else:
					a=a+1
			else:
				a=a+1
	print(safe_order)
	matlab_plot.plot(list_2,list_1,marker='x',color='blue',label='time')
	matlab_plot.legend(loc='top left')
	matlab_plot.xlabel('Process no.')
	matlab_plot.ylabel('time')
	matlab_plot.title('Implementing Bankers Algo.',color='green')
	matlab_plot.xticks(list_2,list_3)
	matlab_plot.style.use('ggplot')
	matlab_plot.show()