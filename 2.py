import numpy as np 
array=np.random.randint(5,4)
for i in range(5):
	for j in range(4):
		if (array[i][j]>50):
			array[i][j]=100

print(array)