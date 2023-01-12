import os
import time
try:
    import cv2
except:
    os.system('cmd /c " pip install opencv-contrib-python"')
print('cv2 is ready for use')    
try:
    import numpy
except:
    os.system('cmd /c " pip install numpy"')
print('numpy is ready for use')    
try:
    import matplotlib
except:
    os.system('cmd /c " pip install matplotlib"')
print('matplotlib is ready for use')
time.sleep(3)
exit(0)
