import face_recognition
import cv2
from simple_facerec import SimpleFacerec
import os

sfr = SimpleFacerec()
sfr.load_encoding_images("./stored_faces/")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    face_location, face_name = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_location, face_name):
        # print(face_loc)
        y1, x2, y2, x1 = face_loc[0],face_loc[1],face_loc[2],face_loc[3]
        cv2.putText(frame, name, (x1, y1-10), cv2.FONT_HERSHEY_PLAIN,1,(0))
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0),4)
        
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()






















# img = cv2.imread('./images/trial_messi.jpg')
# rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_encoding = face_recognition.face_encodings(rgb_img)[0]

# files = os.listdir("./known_faces")

# for images in files:
#     image = cv2.imread(f'./known_faces/{images}')
#     rgb_img2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     img2_encoding = face_recognition.face_encodings(rgb_img2)[0]

#     result = face_recognition.compare_faces([img_encoding], img2_encoding)
#     print(result)
    
    
