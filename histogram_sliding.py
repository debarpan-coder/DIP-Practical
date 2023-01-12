from histogram import histogramPlotting
import cv2
import numpy as np
# img=np.array([[4,5,7,4],[2,2,5,3],[6,5,1,6]],np.uint8)
# print(img)
img=cv2.imread("butterfly.jpg",0)
histogramPlotting(img)
n=len(format(np.max(img),'b'))
l=2**n
slidingImg=img.copy()
offset=80
HisSliding=lambda r: r + offset
for i in range(len(img)):
    for j in range(len(img[0])):
        s=HisSliding(img[i][j])
        if s >= l-1:
            s=l-1
        elif s < 0:
            s=0
        slidingImg[i][j]=s
# print(slidingImg)
histogramPlotting(slidingImg)
mergedImg=np.concatenate((img,slidingImg),axis=1)
cv2.imshow(f"Original vs Histogram Sliding for offset value {offset}",mergedImg)
cv2.waitKey(0)