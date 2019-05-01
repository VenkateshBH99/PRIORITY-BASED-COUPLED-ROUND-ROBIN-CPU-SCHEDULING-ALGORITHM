import matplotlib.pyplot as plt
import pandas as pd
Data=[]

Comp=[]
Gant=[]
Narr=[]
z=0

def fun5(RQ,TQ,j,Bavg,HBT,MDR,P,CT,wb):
	global z
	if len(RQ)==0:
		return CT
	Bavg=Bav(RQ)
	HBT=hbt(RQ)
	TQ=(Bavg+HBT)/RQ[0][4]
	if TQ<10:
		TQ=10
	RQ[0][2]-=TQ
	j=RQ[0][0]-1
	Gant.append([RQ[0][0],TQ])
	if RQ[0][2]>0:
		CT+=TQ
		q=RQ.pop(0)
		RQ.append(q)
	else:
		q=RQ.pop(0)
		q[2]+=TQ
		CT+=q[2]
		q[2]=CT
		Comp.append(q)
	#New Process arrive??
	if z<len(Narr):
		if Narr[z][1]<=CT or len(RQ)==0:
			if len(RQ)==0:
				CT=Narr[z][1]
			A=Narr[z][1]
			for i in range(z,len(Narr)):
				if Narr[i][1]<=CT:
					RQ.append([Narr[i][0],Narr[i][1],Narr[i][2],Narr[i][3],Narr[i][4],Narr[i][5]])
					z+=1
				else:
					break
			Bavg=Bav(RQ)
			HBT=hbt(RQ)
			MDR=mdr(RQ)
			fun1(RQ,Bavg,TQ,HBT,MDR,CT)
		else:
			CT=fun5(RQ,TQ,j,Bavg,HBT,MDR,P,CT,wb)
	else:
		CT=fun5(RQ,TQ,j,Bavg,HBT,MDR,P,CT,wb)

def fun4(RQ,TQ,j,Bavg,HBT,MDR,P,CT):
	global z
	if len(RQ)==0:
		return CT
	Bavg=Bav(RQ)
	HBT=hbt(RQ)
	TQ=(Bavg+HBT)/RQ[0][3]
	if TQ<10:
		TQ=10
	RQ[0][2]-=TQ
	j=RQ[0][0]-1
	Gant.append([RQ[0][0],TQ])
	if RQ[0][2]>0:
		CT+=TQ
		q=RQ.pop(0)
		RQ.append(q)
		
	else:
		q=RQ.pop(0)
		q[2]+=TQ
		CT+=q[2]
		q[2]=CT
		Comp.append(q)
	#New Process arrive??
	if z<len(Narr):
		if Narr[z][1]<=CT or len(RQ)==0:
			if len(RQ)==0:
				CT=Narr[z][1]
			A=Narr[z][1]
			for i in range(z,len(Narr)):
				if Narr[i][1]<=CT:
					RQ.append([Narr[i][0],Narr[i][1],Narr[i][2],Narr[i][3],Narr[i][4],Narr[i][5]])
					z+=1
				else:
					break
			Bavg=Bav(RQ)
			HBT=hbt(RQ)
			MDR=mdr(RQ)
			fun1(RQ,Bavg,TQ,HBT,MDR,CT)

		else:
			if (j+1)<len(RQ):
				CT=fun4(RQ,TQ,j,Bavg,HBT,MDR,P,CT)
			else:
				CT=fun3(RQ,TQ,j,Bavg,HBT,MDR,P,CT)
	else:
		if (j+1)<len(RQ):
			CT=fun4(RQ,TQ,j,Bavg,HBT,MDR,P,CT)
		else:
			CT=fun3(RQ,TQ,j,Bavg,HBT,MDR,P,CT)


def fun3(RQ,TQ,j,Bavg,HBT,MDR,P,CT):
	global z
	if len(RQ)==0:
		return CT
	RQ.sort(key=lambda k:k[2])
	CT=fun4(RQ,TQ,j,Bavg,HBT,MDR,P,CT)

def fun2(RQ,TQ,j,Bavg,HBT,MDR,P,CT,wp,wb):
	global z
	if len(RQ)==0:
		return CT
	if (wp[0][1]/wb[0][1])==1:
		TQ=Bavg/(RQ[0][4]*2)
	else:
		#Priority(1)==Wb(1)
		if P[0][1]==wb[0][1]:
			TQ=(Bavg+HBT)/RQ[0][4]
		else:
			TQ=(Bavg+MDR)/RQ[0][4]
	
	RQ[0][2]-=TQ
	j=RQ[0][0]-1
	Gant.append([RQ[0][0],TQ])
	if RQ[0][2]>0:
		CT+=TQ
		q=RQ.pop(0)
		RQ.append(q)
	else:
		q=RQ.pop(0)
		q[2]+=TQ
		CT+=q[2]
		q[2]=CT
		Comp.append(q)
	#New Process arrive??
	if z<len(Narr):
		if Narr[z][1]<=CT or len(RQ)==0:
			if len(RQ)==0:
				CT=Narr[z][1]
			A=Narr[z][1]
			for i in range(z,len(Narr)):
				if Narr[i][1]<=CT:
					RQ.append([Narr[i][0],Narr[i][1],Narr[i][2],Narr[i][3],Narr[i][4],Narr[i][5]])
					z+=1
				else:
					break
			Bavg=Bav(RQ)
			HBT=hbt(RQ)
			MDR=mdr(RQ)
			fun1(RQ,Bavg,TQ,HBT,MDR,CT)
		else:
			if (j+1)<len(RQ):
				CT=fun2(RQ,TQ,j,Bavg,HBT,MDR,P,CT,wp,wb)
			else:
				CT=fun3(RQ,TQ,j,Bavg,HBT,MDR,P,CT)
	else:
		if (j+1)<len(RQ):
			CT=fun2(RQ,TQ,j,Bavg,HBT,MDR,P,CT,wp,wb)
		else:
			CT=fun3(RQ,TQ,j,Bavg,HBT,MDR,P,CT)



def fun1(RQ,Bavg,TQ,HBT,MDR,CT):
	global z
	if len(RQ)>1:
		RQ.sort(key=lambda k:k[2])
		brr=[]
		wb=[]
		wp=[]
		P=[]
		for i in range(len(RQ)):
			brr.append(RQ[i]) #Temp queue
		su=1
		for i in range(len(RQ)):
			wb.append([RQ[i][0],su])
			RQ[i][4]=su
			su+=1
		temp=RQ[0][3]
		t="SAME"
		for i in range(1,len(RQ)):
			if temp!=RQ[i][3]:
				t="DIFF"
				break
		j=RQ[0][0]-1
		if t=="DIFF":
			RQ.sort(key=lambda k:k[3])
			su=1
			Bavg=Bav(RQ)
			HBT=hbt(RQ)
			MDR=mdr(RQ)
			for i in range(len(RQ)-1,-1,-1):
				#print(su,"-",RQ[i][0])
				P.append([RQ[i][0],RQ[i][3]])
				wp.append([RQ[i][0],su])
				RQ[i][5]=su
				su+=1
			j=RQ[0][0]-1
			#wp(1)/wb(1)==1
			CT=fun2(RQ,TQ,j,Bavg,HBT,MDR,P,CT,wp,wb)
		else:
			CT=fun5(RQ,TQ,j,Bavg,HBT,MDR,P,CT,wb)
	else:
		if len(RQ)==1:
			TQ=RQ[0][2]
			Gant.append([RQ[0][0],TQ])
			CT+=TQ
			q=RQ.pop(0)
			q[2]=CT
			Comp.append(q)
			CT=fun1(RQ,Bavg,TQ,HBT,MDR,CT)
		else:
			if z==len(Narr):
				return CT
			else:
				if Narr[z][1]>CT:
					CT=Narr[z][1]
				for i in range(z,len(Narr)):
					if Narr[i][1]<=CT:
						RQ.append([Narr[i][0],Narr[i][1],Narr[i][2],Narr[i][3],Narr[i][4],Narr[i][5]])
						z+=1
					else:
						break
				
				Bavg=Bav(RQ)
				HBT=hbt(RQ)
				MDR=mdr(RQ)
				fun1(RQ,Bavg,TQ,HBT,MDR,CT)


def Bav(RQ):
	if len(RQ)==0:
		return 0
	s=0
	for i in range(len(RQ)):
		s+=RQ[i][2]

	s=s/(len(RQ))
	return s

def hbt(RQ):
	ma=-10000
	for i in range(len(RQ)):
		if RQ[i][2]>ma:
			ma=RQ[i][2]
	return ma

def mdr(RQ):
	i=len(RQ)//2
	return RQ[i][2]

def Turnaround(Comp):
	TA=[]
	for i in Comp:
		TA.append([i[0],i[2]-i[1]])
	return TA

def waiting(TA,arr):
	WA=[]
	for i in range(len(arr)):
		WA.append([TA[i][0],TA[i][1]-arr[i][2]])
	return WA

def prin(arr,TA,WA,Gant):
	print("process  arrival  burst  priority  turnaround  waiting")
	for i in range(len(arr)):
		print(arr[i][0],"     ",arr[i][1],"     ",arr[i][2],"     ",arr[i][3],"     ",round(TA[i][1],2),"       ",round(WA[i][1],2))
	Tavg=0
	for i in TA:
		Tavg+=i[1]
	Tavg=Tavg/len(TA)
	Wavg=0
	for i in WA:
		Wavg+=i[1]
	Wavg=Wavg/len(WA)
	print("avg turnaround:",round(Tavg,2))
	print("avg waiting time:",round(Wavg,2))
	print("Number of context switching:",len(Gant)-1)
	Data.append([Tavg,Wavg,len(Gant)-1])
	


def calRR(drr):
	x=0
	tim=int(input("Enter the time quantum for simple RR:"))
	grr=[]
	trr=[]
	drr.sort(key=lambda k:k[1])
	match=drr[0][1]
	for i in range(len(drr)):
		if match==drr[i][1]:
			grr.append(drr[i])
			x+=1
		else:
			break
	y=x
	sum=grr[0][1]
	GC=[]
	while x<len(drr) or grr!=[]:
		if grr==[]:
			match=drr[x][1]
			for i in range(x,len(drr)):
				if match==drr[x][1]:
					grr.append(drr[i])
					y+=1
				else:
					break
			x=y
			sum+=grr[0][1]

		s=grr.pop(0)
		GC.append(s[0])
		if s[2]<=tim:
			sum+=s[2]
			s[2]=sum
			trr.append(s)
		else:
			sum+=tim
			s[2]-=tim
			for i in range(x,len(drr)):
				if drr[i][1]<=sum:
					grr.append(drr[i])
					y+=1
				else:
					break
			x=y
			grr.append(s)
		for i in range(x,len(drr)):
			if drr[i][1]<=sum:
				grr.append(drr[i])
				y+=1
			else:
				break
		x=y
	return [GC,trr]

#Improved Round Robin		
def calIRR(qrr):
	cho=input("Want to arrange priority 1 to 3?[Y/N]:")
	if cho=="y" or cho=="Y":
		print("Process  Priority")
		for i in range(len(qrr)):
			print(qrr[i][0],":",end=" ")
			pri=int(input())
			qrr[i][3]=pri
		print()

	x=0
	tim=int(input("Enter the time quantum for improved RR:"))
	HP=tim+(0.2*tim)
	MP=tim
	LP=tim-(0.2*tim)
	grr=[]
	trr=[]
	prr=[]
	index=[]
	#drr.sort(key=lambda K:k[3])
	drr=[]
	for i in range(len(qrr)):
		if qrr[i][3]==1:
			drr.append([qrr[i][0],qrr[i][1],qrr[i][2],qrr[i][3],LP])
		elif qrr[i][3]==2:
			drr.append([qrr[i][0],qrr[i][1],qrr[i][2],qrr[i][3],MP])
		elif qrr[i][3]==3:
			drr.append([qrr[i][0],qrr[i][1],qrr[i][2],qrr[i][3],HP])
		else:
			print("Priority not matched !!")
			exit(1)
	#print(drr)
	drr.sort(key=lambda k:k[1])
	match=drr[i][1]
	for i in range(len(drr)):
		prr.append(drr[i][2])
		
	m=max(prr)
	for i in range(len(drr)):
		if drr[i][2]<(m/4) and drr[i][1]==drr[0][1]:
			grr.append(drr[i])
			index.append(i)

	for i in range(len(drr)):
		if i not in index:
			match=drr[i][1]
			break

	for i in range(len(drr)):
		if match==drr[i][1]:
			if i not in index:
				grr.append(drr[i])
				x+=1
			else:
				x+=1
		else:
			break
	y=x
	sum=grr[0][1]
	GC=[]
	#print(grr)
	while x<len(drr) or grr!=[]:
		if grr==[]:
			for i in range(x,len(drr)):
				if drr[i][2]<(m/4):
					grr.append(drr[i])
					index.append(i)
			for i in range(x,len(drr)):
				if i not in index:
					match=drr[i][1]
					break

			for i in range(x,len(drr)):
				if match==drr[i][1]:
					if i not in index:
						grr.append(drr[i])
						y+=1
						flag=1
					else:
						y+=1
				else:
					break
			x=y
			
			sum+=grr[0][1]
		#grr.sort(key=lambda k:k[2])
		s=grr.pop(0)
		GC.append([s[0],s[4]])
		if s[2]<=s[4]:
			sum+=s[2]
			s[2]=sum
			trr.append(s)
		elif (s[2]>s[4] and s[2]<=(s[4]+(0.3*s[4]))) and s[3]==3:
			sum+=s[2]
			s[2]=sum
			trr.append(s)
		elif (s[2]>s[4] and s[2]<=(s[4]+(0.2*s[4]))) and (s[3]==1 or s[3]==2):
			sum+=s[2]
			s[2]=sum
			#print(s[0])
			trr.append(s) 
		else:
			sum+=s[4]
			s[2]-=s[4]
			grr.append(s)

		for i in range(x,len(drr)):
			if drr[i][1]<=sum:
				if drr[i][2]<(m/4):
					if grr==[]:
						grr.append(drr[i])
					else:
						grr.insert(0,drr[i])
					index.append(i)
					#print("hi:",grr)

		for i in range(x,len(drr)):
			if drr[i][1]<=sum:
				if i not in index:
					grr.append(drr[i])
					grr.sort(key=lambda k:k[0])
				y+=1
			else:
				break
		x=y
	#print(trr)
	return [GC,trr]


	
def main():
	global z
	n=int(input("Enter number of processes:"))
	if n<=0:
		exit(0)
	
	crr=[]
	drr=[]
	err=[]
	ch=int(input("1.Burst time\n2.Burst time and Priority\n3.arrival,Burst and Priority\nEnter your choice:"))
	if ch==1:
		for i in range(n):
			#print(i+1,":",end="")
			a=int(input())
			Narr.append([i+1,0,a,1,0,0])
			crr.append([i+1,0,a,1,0,0])#process,arrival,burst,priority,wb,wp
			drr.append([i+1,0,a,1,0,0])#process,arrival,burst,priority,wb,wp
			err.append([i+1,0,a,1,0,0])#process,arrival,burst,priority,wb,wp
	elif ch==2:
		for i in range(n):
			#print(i+1,":",end="")
			a=list(map(int,input().rstrip().split()))
			Narr.append([i+1,0,a[0],a[1],0,0])
			crr.append([i+1,0,a[0],a[1],0,0])#process,arrival,burst,priority,wb,wp
			drr.append([i+1,0,a[0],a[1],0,0])#process,arrival,burst,priority,wb,wp
			err.append([i+1,0,a[0],a[1],0,0])#process,arrival,burst,priority,wb,wp
	elif ch==3:
		for i in range(n):
			#print(i+1,":",end="")
			a=list(map(int,input().rstrip().split()))
			Narr.append([i+1,a[0],a[1],a[2],0,0])
			crr.append([i+1,a[0],a[1],a[2],0,0])#process,arrival,burst,priority,wb,wp
			drr.append([i+1,a[0],a[1],a[2],0,0])#process,arrival,burst,priority,wb,wp
			err.append([i+1,a[0],a[1],a[2],0,0])#process,arrival,burst,priority,wb,wp


	else:
		print("Wrong choice!!")
		exit(1)
	print()
	RQ=[] #Ready queue
	
	Narr.sort(key=lambda k:k[1])
	A=Narr[0][1]
	ind=[]
	CT=A
	while Narr[z][1]==A:
		RQ.append([Narr[z][0],Narr[z][1],Narr[z][2],Narr[z][3],Narr[z][4],Narr[z][5]])
		z+=1
		if z==len(Narr):
			break
		
	
	print("PCRR(Priority coupled Round Roubin:")

	Bavg=Bav(RQ)
	HBT=hbt(RQ)
	MDR=mdr(RQ)
	TQ=0
	fun1(RQ,Bavg,TQ,HBT,MDR,CT)
	
	TA=Turnaround(Comp)
	TA.sort(key=lambda k:k[0])
	WA=waiting(TA,crr)

	print("Gant chart:")
	for i in Gant:
		print(i[0],"-",round(i[1],2))
	prin(crr,TA,WA,Gant)

	#simple RR:
	print("-------------------")
	print("Simple RR:")
	res=calRR(drr)
	TA1=Turnaround(res[1])
	TA1.sort(key=lambda k:k[0])
	WA1=waiting(TA1,crr)
	print("Gant Chart:")
	print(res[0])
	prin(crr,TA1,WA1,res[0])

	#Improved RR:
	print("-------------------")
	print("Improved RR:")
	res=calIRR(err)
	TA2=Turnaround(res[1])
	TA2.sort(key=lambda k:k[0])
	WA2=waiting(TA2,crr)
	print("Gant Chart:")
	print(res[0])
	prin(crr,TA2,WA2,res[0])

	df=pd.DataFrame(Data,columns=["Turn","Waiting","context"])
	df.plot.bar()
	plt.bar(df["Turn"],df["Waiting"],df["context"])
	plt.xlabel("Round Roubin")
	plt.ylabel("Time")
	plt.show()
	



if __name__ == '__main__':
	main()

