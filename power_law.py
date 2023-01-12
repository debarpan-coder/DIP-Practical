from histogram import histogramPlotting
import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import pow
# img=np.array([[4,5,7,4],[2,2,5,3],[6,5,1,6]],np.uint8)
img=cv2.imread("butterfly.jpg",0)
histogramPlotting(img)
lawImg=img.copy()
n=len(format(np.max(img),'b'))
l=2**n
# print(img)
c=1   #constant
g=.6 #gamma
PowerLaw=lambda r:round(c*(pow(r,g)))
for i in range(len(img)):
    for j in range(len(img[0])):
        s=PowerLaw(img[i][j])
        if s>=l-1:
            s=l-1
        lawImg[i][j]=s 
# print(lawImg)
histogramPlotting(lawImg)
mergedImg=np.concatenate((img,lawImg),axis=1)
cv2.imshow(f"Original vs Power Law Transform for c={c} and g={g}",mergedImg)
cv2.waitKey(0)