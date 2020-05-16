# text recognition
#import cv2
import pytesseract
from PIL import Image

# read image
def test_detect():
    im = cv2.imread('./floor_sign.png')

    # configurations
    config = ('-l eng --oem 1 --psm 3')

    # pytessercat
    text = pytesseract.image_to_string(im, config=config)

    # print text
    text = text.split('\n')
    text

# text detection
def contours_text(orig, img, contours):
    for cnt in contours: 
        x, y, w, h = cv2.boundingRect(cnt) 

        # Drawing a rectangle on copied image 
        rect = cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 255, 255), 2) 
        
        cv2.imshow('cnt',rect)
        cv2.waitKey()

        # Cropping the text block for giving input to OCR 
        cropped = orig[y:y + h, x:x + w] 

        # Apply OCR on the cropped image 
        config = ('-l eng --oem 1 --psm 3')
        text = pytesseract.image_to_string(cropped, config=config) 

        print(text)