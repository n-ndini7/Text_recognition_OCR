#Script to read text from images and write into a text file 
#module imports
from pytesseract import image_to_string
from PIL import Image
import pytesseract

#Read image from which text needs to be extracted
im = Image.open(r'D:\APAC AM Team prtc asgnmnts\Text_Reading_python\sample_img.png')
#print(im)

pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')

#extracting text from sample image
text = pytesseract.image_to_string(im)
#print(text)

#writing to the file
file2 = open('result_file.txt', 'w')
file2.write(text)
file2.close()

