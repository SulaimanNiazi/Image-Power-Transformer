import cv2
import matplotlib.pylab as plt
from skimage import img_as_float
import os
import random

def transform(imgPath, title=''):
    img=cv2.imread(imgPath)
    if (title == 'inverse'):        
        (thresh, binary) = cv2.threshold(img,  90,  255, cv2.THRESH_BINARY)
        binary1 = 255 - binary        
        plt.figure(figsize=(10, 8))     
        plt.subplot(121), plt.imshow(binary), plt.title('Binary',  size=10)    
        plt.subplot(122), plt.imshow(binary1), plt.title('Invert',  size=10)    
        plt.show()
    else: 
        im = img_as_float(img)        
        gamma = 2
        im2 = im ** gamma       
        plt.figure(figsize=(10, 8))        
        plt.subplot(121), plt.imshow(im), plt.title('image', size=10)       
        plt.subplot(122), plt.imshow(im2), plt.title('Power', size=10)    
        plt.show() 

def imagePathCheck(imagePath):
    return imagePath.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))

def getRandomImage(path):
    if path=="":
        path="."
    try:
        files = os.listdir(path)
        images = [file for file in files if imagePathCheck(file)]
        if not images:
            print("No images found in the specified folder.")
            return None
        return random.choice(images)
    except Exception as e:
        print(f"An error occurred while selecting image randomly: {e}")
        return None

def main():    
    imgFile=input("Enter path to an image: ")
    if not imagePathCheck(imgFile):
        print("You did not enter an image, so a random image will be selected from the given directory.\n")
        imgFile=getRandomImage(imgFile)
    transform(imgFile,title='power')

if __name__=='__main__':
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
    main()