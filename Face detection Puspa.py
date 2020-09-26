# importing libraries 
import os 
import cv2  
import numpy as np
import time
from PIL import Image  
  
face_cascade = cv2.CascadeClassifier('C:\\Users\\girip\\Downloads\\opencv-4.3.0\\data\\haarcascades\\haarcascade_frontalface_default.xml')

os.chdir("C:\\Users\\girip\\Downloads\\facedetect")   
path = "C:\\Users\\girip\\Downloads\\facedetect"

saves='.jpg'

for file in os.listdir('.'): 
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
        
        img = cv2.imread(os.path.join(path, file))  
        

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        
        with open('C:\\Users\\girip\\Downloads\\AIvideo\\bg_img.txt') as f:
                datafile = f.readlines()
                for line in datafile:
                    if file in line:
                        cv2.imwrite("C:\\Users\\girip\\Downloads\\facedetectwithframe\\" + file,img)
            

        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
      
            new_pic=(file)
            cv2.imwrite("C:\\Users\\girip\\Downloads\\facedetectwithframe\\" + new_pic,img)

print(os.getcwd())  
  
os.chdir("C:\\Users\\girip\\Downloads\\facedetectwithframe")   
path = "C:\\Users\\girip\\Downloads\\facedetectwithframe"
  
mean_height = 0
mean_width = 0
  
num_of_images = len(os.listdir('.')) 

  
for file in os.listdir('.'): 
    im = Image.open(os.path.join(path, file)) 
    width, height = im.size 
    mean_width += width 
    mean_height += height 
    
mean_width = int(mean_width / num_of_images) 
mean_height = int(mean_height / num_of_images) 
  
saves='.jpg'

    
for file in os.listdir('.'): 
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
      
        im = Image.open(os.path.join(path, file))  
   
      
        width, height = im.size    
        print(width, height) 
  
      
        imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)  
        imResize.save( file, 'JPEG', quality = 95) # setting quality 
       
        print(im.filename.split('\\')[-1], " is resized")  

def generate_video(): 
    image_folder = '.' # make sure to use your folder 
    video_name = 'mygeneratedvideo.avi'
    os.chdir("C:\\Users\\girip\\Downloads\\facedetectwithframe") 
      
    images = [img for img in os.listdir(image_folder) 
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith("png")] 
     
    # Array images should only consider 
    # the image files ignoring others if any 
    print(images)  
  
    frame = cv2.imread(os.path.join(image_folder, images[0])) 
  
    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape   
  
    video = cv2.VideoWriter(video_name, 0, 20, (width, height))  
  
    # Appending the images to the video one by one 
    for image in images:  
        video.write(cv2.imread(os.path.join(image_folder, image)))  
      
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()  
    video.release() 
  
  

generate_video() 