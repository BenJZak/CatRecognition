import cv2

face_cascade=cv2.CascadeClassifier("cat_face.xml")

img=cv2.imread("face1.jpg") #rename to your image

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,scaleFactor=1.01,minNeighbors=5)

for x,y,w,h in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)


cv2.imshow("Cat Face",img)
cv2.waitKey()
