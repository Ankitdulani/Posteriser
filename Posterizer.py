import numpy as np 
import cv2
import poster_fuzz
import logic

#refer: https://arxiv.org/pdf/1802.01009.pdf
class Posteriser:
	def __init__():
		self.fuzz=poster_fuzz()
		self.fuzz.addLogic(0,73,50)  #fuzzy for dark pixel
		self.fuzz.addLogic(127,127,50) #fuzzy for gray pixel
 		self.fuzz.addLogic(255,177,50)	#fuzzy for dark pixels

 	def precomputedTable(self):
 		return np.array([self.fuzz.classify(i) for i in np.arange(0, 256)]).astype("uint8")

	def posterise(self,image):

		#iterate over the image to preserve the image backgroud
		# refer https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#bilateralfilter
		# refer https://www.csie.ntu.edu.tw/~cyy/courses/vfx/10spring/lectures/handouts/lec14_bilateral_4up.pdf
		blur = cv2.bilateralFilter(image,7,75,75)

		lookUp = self.precomputedTable()

		overlay = cv2.LUT(blur, lookUp).astype('uint8')
		return cv2.addWeighted(blur,0.8,overlay,0.2,0)




