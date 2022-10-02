import cv2
import pytesseract as tesseract
import time
#tesseract.pytesseract.tesseract_cmd = "/usr/local/lib/python3.9/dist-packages"
'''
img = cv2.imread("literatura.jpg")
#texto = tesseract.image_to_string(img, lang='por', nice = 1, timeout=1000000)

print(img)
cv2.imshow('Result', img)
time.sleep(60*60)
'''
img = cv2.imread("literatura.jpg")
#img = cv2.resize(img, (1080, 1080))
print(tesseract.image_to_string(img, lang='por'))
cv2.imshow('Result', img)
cv2.waitKey(0)
#time.sleep(60)
