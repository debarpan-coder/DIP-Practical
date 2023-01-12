from histogram import histogramPlotting
import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import log10 as log
# img=np.array([[4,5,7,4],[2,2,5,3],[6,5,1,6]],np.uint8)
# print(img)
img=cv2.imread('download.jpeg',0)
histogramPlotting(img)
logImg=img.copy()
n=len(format(np.max(img),'b'))
l=2**n
# print(l)
c=120
# c=l/log(1+l)
LogTran=lambda r:round(c*log(1+r))
for i in range(len(img)):
    for j in range(len(img[0])):
        s=LogTran(img[i][j])
        if s >= l-1:
            s=l-1
        logImg[i][j]=s
# print(logImg)
histogramPlotting(logImg)
mergedImg=np.concatenate((img,logImg),axis=1)
cv2.imshow(f"Original vs Log Transform for c={c}",mergedImg)
cv2.waitKey(0)