import Image
import math
import random
import sys

skin_tones= []

def parse_skin_tones(skinFile):
  global skin_tones
  with open(skinFile) as f: 
    for line in f:
      if len(line)>1:
        skin_value= [int(elem) for elem in line.split(",")]
        skin_tones += [skin_value]

def norm(a,b):
	s=0
	for i in range(len(a)):
		s += math.pow(a[i]-b[i],2)
	return math.sqrt(s)

def closest_match(pix):
	return min(skin_tones, key=lambda x:norm(x,pix))

def regulizer(img):
	global color_classes, colors_in_class
	pixels = img.load() # create the pixel map
	for i in range(img.size[0]):    # for every pixel:
	    for j in range(img.size[1]):
	        pixels[i,j] = tuple(closest_match(pixels[i,j])) # set the colour accordingly
	img.show()

if __name__=="__main__":
	global thresh, compute_freq
	#img = Image.new( 'RGB', (255,255), "black") # create a new black image
	#img.show()
	#pixels = img.load() # create the pixel map
	#for i in range(img.size[0]):    # for every pixel:
	#    for j in range(img.size[1]):
	#        pixels[i,j] = (100, i, j) # set the colour accordingly
	#img.show()
	parse_skin_tones("skin_tone_rgb_csv")
	img= Image.open("elvis.jpg")
	img.show()
	regulizer(img)
	#img.save("elvis2","bmp")