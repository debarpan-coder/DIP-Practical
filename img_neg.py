from histogram import histogramPlotting
import cv2
import numpy as np
import matplotlib.pyplot as plt
# img=np.array([[4,5,7,4],[2,2,5,3],[6,5,1,6]],np.uint8)
img=cv2.imread('image.jpeg',1)
cv2.imshow("Original",img)
histogramPlotting(img)
n=len(format(np.max(img),'b'))
l=2**n
# print(img,n,l)
negImg=l-1-img
cv2.imshow("Negative",negImg)
histogramPlotting(negImg)
# print(negImg)
cv2.waitKey(0)