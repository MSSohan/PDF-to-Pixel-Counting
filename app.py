# import module
from pdf2image import convert_from_path
import cv2
import numpy as np

total_number_of_white_pix=0
total_number_of_black_pix=0
images = convert_from_path('Lab 1.pdf',500,poppler_path=r'C:\Program Files\Release-22.04.0-0\poppler-22.04.0\Library\bin')
for i, image in enumerate(images):
    fname = 'image'+str(i)+'.jpg'
    image.save(fname,"PNG")
    img = cv2.imread(fname)
    # counting the number of pixels
    number_of_white_pixi = np.sum(img == 255)
    number_of_black_pixi = np.sum(img == 0)
    total_number_of_white_pix += number_of_white_pixi
    total_number_of_black_pix += number_of_black_pixi
    print('Number of black pixels:', number_of_white_pixi)
    print('Number of black pixels:', number_of_black_pixi)
print("Total Number of black pixels:",total_number_of_white_pix)
print("Total Number of black pixels:",total_number_of_black_pix)