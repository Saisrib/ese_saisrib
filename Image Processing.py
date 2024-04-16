import streamlit as st
from PIL import Image
from PIL import ImageOps
from PIL import ImageEnhance
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image1.jpg')
cv.imshow(img)

#resize image
resized_img = cv2.resize(img, (400, 400))
cv.imshow( resized_img)

gray_image = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
cv.imshow( gray_image)

#image cropping 
x, y, w, h = 0, 0, 200, 200
region_of_interest = gray_image[y:y+h, x:x+w]
cv.imshow(region_of_interest)

img_cw_90 = cv2.rotate(region_of_interest, cv2.ROTATE_90_CLOCKWISE)
cv2_imshow(img_cw_90)

plt.figure(figsize=(20, 20))

# Original Image
plt.subplot(231),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)),plt.axis('off'),plt.title('Original Image', size=10)

# Resized Image
plt.subplot(232),plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)),plt.axis('off'),plt.title('Resized Image (400x400)', size=10)

# gray image
plt.subplot(233),plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY),cmap='gray'),plt.axis('off'),plt.title('gray Image', size=10)

# cropping gray image
plt.subplot(234),plt.imshow(region_of_interest, cmap='gray'),plt.axis('off'),plt.title('Cropped Image (200x200)')

# 45 deg rotated cropped gray imge
plt.subplot(235),plt.imshow(rotated_image1, cmap='gray'),plt.axis('off'),plt.title('rotated image 45 deg')

# blurred image
plt.subplot(236),plt.imshow(Gaussian, cmap='gray'),plt.axis('off'),plt.title('blurred image')

# Save the combined figure
plt.savefig('output_image.jpg') # plt.savefig('combined_figure.png', bbox_inches='tight', pad_inches=0.1)