# -*- coding: utf-8 -*-  
import numpy as np
import utils
import matplotlib.pyplot as plt
import time
import demo_data as ddata
import numpy.random as random
import sys

def sigmoid(x):
	return (1.0/(1+np.exp(-x)))

def train_internal(raw, label):
	ones=np.ones((raw.shape[0],1))
	data=np.hstack((ones,raw))
	samples,dims=np.shape(data)
	num = 500
	wes = np.ones((dims,1))
	history=[]
	alpha=0.001
	for j in range(num):
		h = sigmoid(np.dot(data,wes))
		error = label - h
		wes = wes + alpha*np.dot(data.transpose(),error)
		history.append(wes)
	out_history=np.array(history)
	return wes,out_history

def train_internal1(raw, label,num=150):
	ones=np.ones((raw.shape[0],1))
	data=np.hstack((ones,raw))
	samples,dims=np.shape(data)
	wes = np.ones(dims)
	history=[]
	for j in range(num):
		dataIndex = list(range(samples))
		for i in range(samples):
			alpha=4/(1.0+j+i)+0.001
			randIndex=int(random.uniform(0,len(dataIndex)))
			h = sigmoid(sum(data[randIndex]*wes))
			error = (label[randIndex] - h)
			wes = wes + alpha*error*data[randIndex]
			del(dataIndex[randIndex])
			history.append(wes)
			out_history=np.array(history)
	return wes,out_history
def predict(weights,points):
	result=[]
	for p in points:
		if np.sum(np.dot(p, weights[1:]))+weights[0] > 0:
			result.append(1)
		else:
			result.append(0)
	return np.array(result)

def plot_fit2(data1,data2,weights1,his):
	x1=data1.transpose()[0]
	y1=data1.transpose()[1]
	x2=data2.transpose()[0]
	y2=data2.transpose()[1]
	fig = plt.figure()
	ax = fig.add_axes([0.1, 0.1, 0.4, 0.7])
	ax.scatter(x1,y1,c='r',alpha=1,s=20)
	ax.scatter(x2,y2,c='g',alpha=0.5,s=50)

	min_x=np.min([np.min(x1),np.min(x2)])
	max_x=np.max([np.max(x1),np.max(x2)])
	min_y=np.min([np.min(y1),np.min(y2)])
	max_y=np.max([np.max(y1),np.max(y2)])
	x=np.arange(int(min_x),int(max_x),1)
	len_x=x.shape[0]
	h = 1
	xx, yy = np.meshgrid(np.arange(min_x, max_x, h), np.arange(min_y, max_y, h))
	Z=predict(weights1,np.c_[xx.ravel(), yy.ravel()])
	Z = Z.reshape(xx.shape)
	plt.contourf(xx,yy,Z,cmap=plt.cm.Spectral,alpha=0.3)
	ax = plt.subplot(333)
	ax.plot(his[:,0])
	plt.ylabel('X0')
	ax = plt.subplot(336)
	ax.plot(his[:,1])
	plt.ylabel('X1')
	ax = plt.subplot(339)
	ax.plot(his[:,2])
	plt.ylabel('X2')
	plt.show()

def train(data1,data2,label1,label2):
	data=np.vstack((data1,data2))
	label=np.vstack((label1,label2))
	weights,his=train_internal1(data,label)
	return weights,his



def train_2_group():
	data1=ddata.create_train_data1(20)
	data2=ddata.create_train_data2(20)
	label1=np.zeros((data1.shape[0],1))
	label2=np.ones((data2.shape[0],1))
	weights1,his=train(data1,data2,label1,label2)
	print(weights1)
	plot_fit2(data1,data2,weights1,his)

if __name__ == "__main__":
	train_2_group()