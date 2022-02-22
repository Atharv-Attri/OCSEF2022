
import cv2
from gui import App

def main():
   img = cv2.imread("pedestrian.jpg")
   gui = App()
   value = 19
   scale = 1
   ogimg = img

   while(True):
      if cv2.waitKey(1) == 27:
         break
      img = ogimg
      width = int(ogimg.shape[0] * (scale / 100))
      height = int(ogimg.shape[1] * (scale / 100))
      imgS = cv2.resize(img, (height, width))
      gray = cv2.cvtColor(imgS, cv2.COLOR_BGR2GRAY)
      edges = cv2.Canny(gray,value,value+50, apertureSize = 3)
      img = cv2.resize(img, (height, width), interpolation = cv2.INTER_AREA)

      
      cv2.imshow("linesEdges (Original)", edges)
      cv2.imshow("Original Video", img)
      value = gui.get_detail()
      scale = gui.get_scale()


if __name__ == "__main__":
   main()