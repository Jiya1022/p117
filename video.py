import os 
import cv2
path="C:/Users/jiya Agrawal/OneDrive/Desktop/New folder/PRO-C105-Project-Images-main/Images"
images=[]
for file in os.listdir(path):
    name,extension=os.path.splitext(file)

    if extension in['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name=path+"/"+file 
    images.append(file_name)
frame=cv2.imread(images[0])
height,width,layers=frame.shape
size=(width,height)
out=cv2.VideoWriter("project.mp4",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)  
for i in range(0,len(images)):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()
print("Done")    


