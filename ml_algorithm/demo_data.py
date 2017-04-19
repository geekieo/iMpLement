# -*- coding: utf-8 -*-  
import numpy as np
import utils
import matplotlib.pyplot as plt
import time

def create_train_data1(size):
	mu,sigma=0,2.4
	rarray=np.random.normal(mu,sigma,size*2).reshape(size,2)*10
	return rarray

def create_train_data2(size):
	mu,sigma=5,1.0
	rarray=np.random.normal(mu,sigma,size*2).reshape(size,2)*10
	return rarray

def create_train_data3(size):
	mu,sigma=-5,1.0
	rarray=np.random.normal(mu,sigma,size*2).reshape(size,2)*10
	return rarray

def load_model(i,dim,model_file):
	others=None
	for j in range(10):
		current=utils.load_matrix(model_file)
		if j==i:
			target=current
		elif others is None:
			others=current
		else:
			temp=np.vstack((others,current))
			others=temp
	return target,others