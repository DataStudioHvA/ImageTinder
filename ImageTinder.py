import cv2
import glob
import os
import ctypes

image_list=[]
filename_list = []

os.chdir('C:/Users/pc/Desktop/ImageTinder/images/')

for filename in glob.glob("*.jpg"):
    img = cv2.imread(filename)
    imS = cv2.resize(img, (960, 540))
    image_list.append(img)
    filename_list.append(filename)
    written = False
    while written == False:
        cv2.imshow('image', imS)
        key = cv2.waitKey(0)
        char_key = chr(key%256)
        path = char_key  + '/' + str(filename)
        if os.path.isdir(char_key):
            cv2.imwrite(path, img)
            written = True
        else:
            ctypes.windll.user32.MessageBoxW(0, "path does not exist", "Error", 1)
    
    cv2.destroyAllWindows()





