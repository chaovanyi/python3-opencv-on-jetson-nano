import cv2
import face_recognition
print(cv2.__version__)

donFace = face_recognition.load_image_file('image path')




if cv2.waitKey(1) == ord('q'):
  break
cv2.destroyAllWindow()
