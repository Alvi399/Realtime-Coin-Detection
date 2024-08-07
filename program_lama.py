import cv2
import numpy as np

img = cv2.imread('./IDR_1000_Koin.JPG',0)
blur = cv2.GaussianBlur(img,(11,11),0)
edges = cv2.Canny(blur,40,150)
dilated = cv2.dilate(edges,(1,1),iterations = 2)

(cnt, _) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Terdapat {} koin dalam gambar".format(len(cnt)))

cv2.imshow("koin", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()



