import numpy as np 
array=np.random.randint(10)
for i in range(10):
	if(i%2!=0):
		array[i]=-10

print(array)