import cv2 # opencv library

def preprocess() :
    # read the image
    image = cv2.imread('opencv_frame_0.png')
    
    # convert the image to grayscale format
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # apply binary thresholding
    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    
    # convert the image to negative format 
    img_not = cv2.bitwise_not(thresh)
    
    # resize the image
    img = cv2.resize(img_not,(28,28))

    img = img.astype('float32')
    return img