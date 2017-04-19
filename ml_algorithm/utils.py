from PIL import Image
import numpy as np
import os

def write_encode(arr,file_name):
	with open(file_name,"w") as f:
		for i in range(arr.shape[0]):
			row=arr[i]
			strs=[str(int(row[j])) for j in range(row.shape[0])]
			f.write(",".join(strs))
			f.write("\n")

def read_image(file):
	with Image.open(file) as f:
		return np.array(f).flatten() #flatten the image's pix
def save_matrix(arr,file_name):
	write_encode(arr,file_name)
	
def save_format_matrix(arr,file_name):
	with open(file_name,"w") as f:
		for i in range(arr.shape[0]):
			row=arr[i]
			for j in range(row.shape[0]):
				if row[j]<10:
					f.write("00"+str(int(row[j]))+",")
				elif row[j]<100:
					f.write("0"+str(int(row[j]))+",")
				else:
					f.write(str(int(row[j]))+",")
				if j==27 or (j-27)%28==0:
					f.write("\n")

def load_matrix(file_name):
	return np.loadtxt(file_name,dtype=np.int,delimiter=",")

def load_original_model():
	model_arr=[]
	for j in range(10):
		model_file="models/original_train_matrix_"+str(j)+"_new"
		model_arr.append(load_matrix(model_file))
	model=np.array(model_arr)
	return model

def load_pca_model(dim):
	model_arr=[]
	for j in range(10):
		model_file="models/pca_train_matrix_"+str(j)+"_"+str(dim)
		model_arr.append(load_matrix(model_file))
	model=np.array(model_arr)
	return model

def load_kmeans_centers(dim,clusters):
	model_arr=[]
	for j in range(10):
		model_file="models/kmeans_"+str(clusters)+"_train_matrix_"+str(j)+"_"+str(dim)
		model_arr.append(load_matrix(model_file))
	model=np.array(model_arr)
	return model

def save_images_to_matrix(i,dir_name,dist):
	#dir_name="classified_train_data/"+str(i)
	for parent,dirs,files in os.walk(dir_name):
		total=[]
		sample=0
		for file_name in files:
			full_file_path = parent+"/"+file_name
			current=read_image(full_file_path)
			total.append(current)
			sample=sample+1
			#if sample>=100:
			#	break
		total_arr=np.array(total)
		save_matrix(total_arr,dist)