import cv2
import matplotlib.pylab as plt
from skimage import img_as_float

def transform(img, title=''):
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

def main():    
    img_file=input("Enter path to an image: ")
    if img_file=="":
        img_file="*.{jpg,png}"
    img = (cv2.imread(img_file))
    transform(img, title='power')

if __name__=='__main__':
    main()