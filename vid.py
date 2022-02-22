import cv2
from gui import App

def main():
   vid = cv2.VideoCapture(0)
   gui = App()
   detail = 19
   zoom = 1

   while(True):
      _, img = vid.read()
      width = int(img.shape[0] * (zoom / 100))
      height = int(img.shape[1] * (zoom / 100))
      img_scaled = cv2.resize(img, (height, width))
      gray = cv2.cvtColor(img_scaled, cv2.COLOR_BGR2GRAY)
      edges = cv2.Canny(gray,detail,detail+50, apertureSize = 3)
      img = cv2.resize(img, (height, width), interpolation = cv2.INTER_AREA)

      cv2.imshow("linesEdges (Original)", edges)
      cv2.imshow("Original Video", img)
      detail = gui.get_detail()
      zoom = gui.get_scale()
      if cv2.waitKey(1) == 27:
         break


if __name__ == "__main__":
   main()