import cv2

alg = "./imp_files/haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

img = cv2.imread("images/group.jpg", 0)
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # print(len(faces))
    
    for x, y, w, h in faces:
        top_left = (x,y)
        bottom_right = (x+w, y+h)
        cv2.rectangle(frame, (top_left), (bottom_right), (255,255,255), 4)

    cv2.imshow("frame", frame) 
    
    if cv2.waitKey(1)==ord("q"):
        break
    
cv2.destroyAllWindows()
