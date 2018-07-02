class MyFile():
	
	def readhighScore(self):
		myfile=open("highScore.txt","r")
		line=myfile.readline()
		all_List=[]
		while (line!=''):
			lis=line.split("#")
			all_List.append(lis)
			line=myfile.readline()
		myfile.close()
		return all_List
		
	def writeName(self,name):
		myfile=open("highScore.txt","a")
		myfile.write(name+"#0#0")
		myfile.write("\n")
		myfile.close()
		
	def writeScoreLevel(self,name,score,level):
		myfile=open("highScore.txt","r")
		line=myfile.readline()
		index=-1
		i=0
		NewScore=0
		while line!='':
			print line
			lis=line.split("#")
			if(lis[0]==name):
				NewScore=int(lis[1])+score
				index=i
			i+=1
			line=myfile.readline()
		myfile.close()
		myfile=open("highScore.txt","r")
		str_file=myfile.read()
		lis_add=[]
		start=0
		end=0
		i=0
		print str_file
		while i < len(str_file):
			if(str_file[i]=='\n'):
				lis_add.append(str_file[start:i])
				print lis_add
				print str_file[start:i]
				start=i
			i+=1
		print lis_add
		myfile.close()
		myfile=open("highScore.txt","w")
		lis_add.pop(index)
		lis_add.insert(index,name+"#"+str(NewScore)+"#"+str(level))
		for i in lis_add:
			myfile.write(i)
		myfile.close()
			

"""f=MyFile();

while(True):
	x=input('enter')
	if(x==1):
		print f.readhighScore()
	elif(x==2):
		f.writeScoreLevel("safaa",12,"palsten")
	else:
		f.writeName("loza")
"""

	

