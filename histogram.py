import cv2
import numpy as np
import matplotlib.pyplot as plt
def histogramPlotting(image):
    l=2**len(format(np.max(image),'b'))
    intensity=np.array(range(l))
    frequency=np.zeros(l)
    for i in range(len(image)):
        for j in range(len(image[0])):
            frequency[image[i][j]]+=1
    plt.plot(intensity,frequency,marker='o')
    plt.xlabel("Gray Level")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()
if __name__=='__main__':
    # img=np.array([[4,5,7,4],[2,2,5,3],[6,5,1,6]],np.uint8)
    # img=np.array([[5,4,7],[1,2,3],[6,4,7]],np.uint8)
    img=cv2.imread('butterfly.jpg',0)
    histogramPlotting(img)
    
