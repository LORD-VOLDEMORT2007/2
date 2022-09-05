import cv2 , os

img = "images"
arr = []

for i in os.listdir(img):
    name , ext = os.path.splitext(i)

    if ext in [".png" , ".jpg"]:
        file_name = img + "/" + i
        arr.append(file_name)
        

length = len(arr)


vedio = cv2.imread(arr[0])
w , h , channel= vedio.shape

out = cv2.VideoWriter("friends.avi" , cv2.VideoWriter_fourcc(*'DIVX') , 10 , (w , h) )

for i in range(0 , length-1):
    frame = cv2.imread(arr[i])
    out.write(frame)
out.release()