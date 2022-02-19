from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import numpy as np
from gui import App
# Opens a image in RGB mode
img = cv2.imread("tree.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)


#capture = cv2.VideoCapture(0)
gui = App()
value = 19
scale = 1
ogimg = img

while(True):
      
    # Frame obtain / convert logic
   if cv2.waitKey(1) == 27:
      break
   img = ogimg
   #ret, img = capture.read()
   width = int(ogimg.shape[0] * (scale / 100))
   height = int(ogimg.shape[1] * (scale / 100))
   if width < 1:
      width = 1
   if height < 1:
      height = 1
   dim = (width, height)
   print(dim)
   imgS = cv2.resize(img, (height, width))
   gray = cv2.cvtColor(imgS, cv2.COLOR_BGR2GRAY)
   edges = cv2.Canny(gray,value,value+50, apertureSize = 3)
   img = cv2.resize(img, (height, width), interpolation = cv2.INTER_AREA)
   im_matrix = img

   
   edgesS = edges#cv2.resize(edges, (200,100))                    # Resize image



   imgS = img #cv2.resize(img, (960, 540))                    # Resize image

   #lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)
   #try:
   #   for line in lines:
   #      x1, y1, x2, y2 = line[0]
   #      cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)
   #except TypeError:
   #   pass
   
   cv2.imshow("linesEdges (Original)", edgesS)
   try:
      cv2.imshow("Original Video", img)# cv2.resize(ogimg,(500,500))))))
      pass
   except Exception as e:
      print(e)
   value = gui.get_value()
   scale = gui.get_scale()

   #cv2.imshow("linesDetected (Scaled For Viewing)", imgS)



