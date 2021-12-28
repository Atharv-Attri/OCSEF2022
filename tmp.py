from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import numpy as np
# Opens a image in RGB mode
img = cv2.imread("eye.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)

scale_percent = 7.5 # percent of original size
width = int(img.shape[0] * scale_percent / 100)
height = int(img.shape[1] * scale_percent / 100)
dim = (width, height)
capture = cv2.VideoCapture(1)

while(True):
      
    # Frame obtain / convert logic
      
   if cv2.waitKey(1) == 27:
      break
   ret, img = capture.read()
   ogimg = img
   imgS = cv2.resize(img, (560, 240))
   gray = cv2.cvtColor(imgS, cv2.COLOR_BGR2GRAY)
   edges = cv2.Canny(gray, 75, 150)
   img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
   im_matrix = img

   
   edgesS = cv2.resize(edges, (64,32))                    # Resize image
   edgesS = cv2.resize(edges, (200,100))                    # Resize image



   imgS = cv2.resize(img, (960, 540))                    # Resize image

   lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)
   try:
      for line in lines:
         x1, y1, x2, y2 = line[0]
         cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)
   except TypeError:
      pass
   
   cv2.imshow("linesEdges (Scaled for Viewing)", edges)
   cv2.imshow("linesEdges (Original)", edgesS)
   try:
      cv2.imshow("Original Video", cv2.resize(ogimg,(500,500)))
      pass
   except Exception as e:
      print(e)

   #cv2.imshow("linesDetected (Scaled For Viewing)", imgS)



