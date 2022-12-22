import os
import cv2

path =  "C:/Users/MARCO ANTONIO/Documents/Python/Projeto105/Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        
        print(file_name)
        
        images.append(file_name)
        
count = len(images)

frame = cv2.imread(images[0])
h,w,channels = frame.shape
size = (h,w)
print(size)


out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0,8,size)      

for i in range(0,count-1):
    frame = cv2.imread(images[i])
    out.write(frame)   
print('concluido')    
