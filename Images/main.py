from cv2 import cv2
import numpy as np
from PIL import Image

while(True):
	answer = (int(input("#CONVERT TO:\n[1]CARTOON\n[2]BLACK AND WHITE\n[0]EXIT\n")))

	if answer == 0:
		break
	elif answer == 1:	
		#LOAD IMAGE
		img = cv2.imread(r'img.webp')

		#PARAMETERS OF THE GRAY SCALE
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray = cv2.medianBlur(gray, 5)
		edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

		#CARTOON TRANSFORM
		color = cv2.bilateralFilter(img, 9,250, 250)
		cartoon = cv2.bitwise_and(color, color, mask=edges)

		#SHOW IMAGES
		cv2.imshow("Image", img)
		cv2.imshow("Edges", edges)
		cv2.imshow("Cartoon", cartoon)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	else:
		#LOAD IMAGE
		img = Image.open(r'img.webp')

		#CONVERT IMG TO BACK AND WHITE
		img = img.convert('L')

		#SAVE IMG IN BLACK AND WHITE
		img.save(r'black_and__white.webp')
		
		print("\nImg saved!\n")
