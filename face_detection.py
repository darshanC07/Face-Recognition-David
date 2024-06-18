import cv2

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

img = cv2.imread("/trial_img.jpg", 0)
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = haar_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5, minSize=(100,100))

i = 0
for x, y, w, h in faces:
    cropped_img = img[ y:y+h, x:x+w]
    cv2.imwrite(f"stored_face/{i}.jpg",cropped_img)
    i+=1
