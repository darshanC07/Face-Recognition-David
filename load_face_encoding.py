import face_recognition
import os
import json
import numpy
import cv2

known_faces_dict = {}

def load_new_face_encoding():
    global new_faces_list, json_file, known_faces_dict
    for image in new_faces_list:
        name = image
        img = cv2.imread(f"./known_faces/{image}")
        rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # img = face_recognition.load_image_file(f"./known_faces/{image}")
        face_location = face_recognition.face_locations(rgb_img)
        # print(face_location)
        img_encoding = numpy.array(face_recognition.face_encodings(rgb_img,face_location)[0])
        known_faces_dict[name] = img_encoding.tolist()
        
def load_known_face_encoding_dict():
    for image in (os.listdir("./known_faces/")):
        name = image
        img = cv2.imread(f"./known_faces/{image}")
        rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # img = face_recognition.load_image_file(f"./known_faces/{image}")
        face_location = face_recognition.face_locations(rgb_img)
        img_encoding = numpy.array(face_recognition.face_encodings(rgb_img,face_location)[0])
        known_faces_dict[name] = img_encoding.tolist()
    # return known_faces_dict

def known_faces_json_creater():       
    global json_file, known_faces_dict
    json_file.seek(0)
    json.dump(known_faces_dict,json_file)
        
load_known_face_encoding_dict()
       
json_file = open("./known_face_encoding.json","r+")
json_data = json.load(json_file)

# json_dict = json.loads(json_data)
old_known_names_list = list(json_data.keys())
old_known_names_list = map(lambda img: img+".png", old_known_names_list )


known_faces_data = os.listdir("./known_faces/")
# new_known_names_list = list(map(lambda i: i.split(".")[0], known_faces_data))

diff = list(set(known_faces_data)-set(old_known_names_list))
new_faces_list = []
for new_face in diff:
    for face in known_faces_data:
        if new_face not in face:
            new_faces_list.append(face)


load_new_face_encoding() 
known_faces_json_creater()    





    
