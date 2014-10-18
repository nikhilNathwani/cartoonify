import Image
import time
import sys
import numpy as np
from scipy.cluster.vq import kmeans2

def kMeans(img,k):
	#convert image to list of rgb pixel values
	pil_img= img.load()
	width= img.size[0]
	height= img.size[1]
	pixels= []
	for i in range(width):
		for j in range(height):
			pixels.append(list(pil_img[i,j]))
	pixels= np.array(pixels)

	#perform kMeans algorithm
	centroids,labels= kmeans2(pixels,k)
	centroids= [[int(x) for x in vector] for vector in centroids]
	
	#convert kMeans results into new image
	for i in range(width):
		for j in range(height):
			pil_img[i,j]= tuple(centroids[labels[i*height+j]])
	img.show()

if __name__=="__main__":
	start= time.time()
	kMeans(Image.open(sys.argv[1]),int(sys.argv[2]))
	print "Time taken:", time.time()-start
