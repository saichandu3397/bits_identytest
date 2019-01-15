import numpy as np 
array=np.random.randint(8)
N=8
p=0.5
array2=np.random.choice(a=['True','False'],size=N,p=[p,1-p])
outputarray=[]
j=0
for i in range(8):
	if(array2[i]=='True'):
		outputarray[j]=array[i]
		j=j+1
print(outputarray)