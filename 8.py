import numpy as np
import tensorflow as tf 
from tensorflow import keras
import csv

array=[[129.0 106.0 159.0 195.0], 
[166.0 63.0 197.0 155.0], 
[196.0 85.0 226.0 182.0], 
[222.0 167.0 251.0 246.0] ]
feature=[[29.0 106.0 159.0],[166.0 63.0 197.0 ],[222.0 167.0 251.0 246.0]]
target=[[195.0],[155.0],[182.0],[246.0]]
def buildmodel():
	model=keras.Sequential([
		keras.layers.Dense(3,activation=tf.nn.relu,input_shape=(3,)),
		keras.layers.Dense(3,activation=tf.nn.relu),
		keras.layers.Dense(1)
		])
	model.compile(optimizer=tf.train.RmsPropOptimizer(),loss='mse',metrics=['mse'])
model=buildmodel()
history=model.fit(feature,target,epochs=10,verbose=0)
