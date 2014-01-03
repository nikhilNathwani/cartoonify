import Image
import math
import random
 
thresh= 50

color_classes=[]
colors_in_class=[]

def norm(a,b):
	s=0
	for i in range(len(a)):
		s += math.pow(a[i]-b[i],2)
	return math.sqrt(s)

def recompute_mean(curr,lst,toAdd):
	ret= [0,0,0]
	for i in range(3):
		ret[i]= (curr[i]*len(lst)+toAdd[i])/(len(lst)+1)
	return ret

def regulizer(img):
	global color_classes, colors_in_class
	pixels = img.load()
	classes_per_pixel= [[0 for x in xrange(img.size[0])] for y in xrange(img.size[1])]
	for i in range(img.size[0]):    # for every pixel:
		for j in range(img.size[1]):
			print i,j
			#print i,j
			found_match= False
			for ind,color in enumerate(color_classes):
				if norm(pixels[i,j],color) <= thresh:
					found_match= True
					if random.randint(0,50)==7:
						color_classes[ind]= recompute_mean(color_classes[ind],colors_in_class[ind],pixels[i,j])
					colors_in_class[ind] += [pixels[i,j]]
					classes_per_pixel[i][j]= ind
					#print color,"is a match for", pixels[i,j]
					#print "Color classes:",len(color_classes), "Colors in that class", len(colors_in_class[ind])
					break
			if not found_match:
				color_classes += [pixels[i,j]]
				colors_in_class += [[pixels[i,j]]]
	print "DONE REGULIZING"
	for i in range(img.size[0]):    # for every pixel:
		for j in range(img.size[1]):
			ind= classes_per_pixel[i][j]
			pixels[i,j] = (color_classes[ind][0],color_classes[ind][1],color_classes[ind][2]) # set the colour accordingly
	print color_classes
	img.show()



if __name__=="__main__":
	img = Image.new( 'RGB', (255,255), "black") # create a new black image
	#img.show()
	pixels = img.load() # create the pixel map
	 
	for i in range(img.size[0]):    # for every pixel:
	    for j in range(img.size[1]):
	        pixels[i,j] = (100, i, j) # set the colour accordingly
	 
	#img.show()
	img= Image.open("elvis.jpg")
	img.show()
	regulizer(img)