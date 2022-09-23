import cv2
import pytesseract as tesseract

#tesseract.pytesseract.tesseract_cmd = "/usr/local/lib/python3.9/dist-packages"

img = cv2.imread("parede.jpg")
texto = tesseract.image_to_string(img, lang='por')

print(texto)

