import pytesseract
from PIL import Image

img = Image.open('project2_Recognizing_text_from_picture/ip10k5zk.png') #dla obrazku
# img = Image.open('project2_Recognizing_text_from_picture/eng_text.png') #dla tekstu

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Hladkyi Dmytro\Desktop/IT Oprogromowanie/Python_Projects/tesseract/tesseract.exe'

file_name = img.filename
file_name = file_name.split(".")[0]

custom_config = r'--oem 3 --psm 13' # dla obrazku
# custom_config = r'--oem 3 --psm 6' # dla tekstu

text = pytesseract.image_to_string(img, config=custom_config)
print(text)

with open('project2_Recognizing_text_from_picture/image1.txt', 'w') as text_file: # dla obrazku
    text_file.write(text)# dla obrazku

# with open(f'{file_name}.txt', 'w') as text_file: #dla tekstu
#     text_file.write(text) #dla tekstu
    


# Set Tesseract to only run a subset of layout analysis and assume a certain form of image. The options for N are:
# 0 = Orientation and script detection (OSD) only.
# 1 = Automatic page segmentation with OSD.
# 2 = Automatic page segmentation, but no OSD, or OCR.
# 3 = Fully automatic page segmentation, but no OSD. (Default)
# 4 = Assume a single column of text of variable sizes.
# 5 = Assume a single uniform block of vertically aligned text.
# 6 = Assume a single uniform block of text.
# 7 = Treat the image as a single text line.
# 8 = Treat the image as a single word.
# 9 = Treat the image as a single word in a circle.
# 10 = Treat the image as a single character.