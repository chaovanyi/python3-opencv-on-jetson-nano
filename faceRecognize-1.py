import face_recognition
import cv2
print(cv2.__version__)

#load image and find face location
image = face_recognition.load_image_file('file path')
face_location = face_recognition.face_location(image)
print(face_locations) #it will show the corner of the first face and the second face.

#converting the color space
image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR) #because python use BGR and the image is RGB

for (row1,col1,row2,col2) in face_locations:
  cv2.rectangle(image,(col1,row1),(col2,row2),(0,0,255),2)

cv2.imshow('myWindow'.image)
cv2.moveWindow('myWindow',0,0)


if cv2.waitKey(0) == ord('q'):
  break
cv2.destroyAllWindow()
