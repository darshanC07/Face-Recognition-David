import cv2
import face_recognition 
import os
import numpy as np
import matplotlib.pyplot as plt

known_faces_dict = {}

def load_known_face_encoding_dict():
    global known_faces_dict
    for image in (os.listdir("./stored_faces/")):
        name = image.split(".")[0]
        img = face_recognition.load_image_file(f"./stored_faces/{image}")
        img_encoding = face_recognition.face_encodings(img)[0]
        known_faces_dict[name] = img_encoding

load_known_face_encoding_dict()

# img = cv2.imread("./images/group.jpg")
# rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# face_location = face_recognition.face_locations(rgb_img)
# face_encodings = face_recognition.face_encodings(rgb_img,face_location)

# print((face_location))
# plt.imshow(rgb_img)
# plt.show()
# print(known_faces_dict.values())

# for i,face_encoding in enumerate(face_encodings):

#     y1, x2, y2, x1 = face_location[i]
#     # top_left = (face_loc[3],face_loc[0])
#     # bottom_right = (face_loc[1],face_loc[3])
    
#     matches = face_recognition.compare_faces(list(known_faces_dict.values()),face_encoding)
#     face_distance = face_recognition.face_distance(list(known_faces_dict.values()),face_encoding)
    
#     best_match = np.argmin(face_distance)
    
#     if(matches[best_match]):
#         try:
#             name = list(known_faces_dict.keys())[best_match]
#         except:
#             name = "unknown"
#     else:
#         name = "unknown"
        
#     cv2.rectangle(img, (x1,y1),(x2,y2),(255,255,255),3)
#     cv2.putText(img, name,(x1+10, y1+20),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),1)
        
# cv2.imshow("frame",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    face_location = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame,face_location)
    
    for i,face_encoding in enumerate(face_encodings):

        y1, x2, y2, x1 = face_location[i]
        # top_left = (face_loc[3],face_loc[0])
        # bottom_right = (face_loc[1],face_loc[3])
    
        matches = face_recognition.compare_faces(list(known_faces_dict.values()),face_encoding)
        face_distance = face_recognition.face_distance(list(known_faces_dict.values()),face_encoding)
        
        best_match = np.argmin(face_distance)
        
        if(matches[best_match]):
            try:
                name = list(known_faces_dict.keys())[best_match]
            except:
                name = "unknown"
        else:
            name = "unknown"
            
        cv2.rectangle(frame, (x1,y1),(x2,y2),(255,255,255),3)
        cv2.putText(frame, name,(x1+10, y1+20),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),1)
            
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord("q"):
        break
    

cv2.destroyAllWindows()
