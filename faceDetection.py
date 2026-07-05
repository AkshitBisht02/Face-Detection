import cv2
#face cascade object
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#stop webcam
webcam=cv2.VideoCapture(0)

while True:
    _,img=webcam.read() # returns two variables, first is a boolean value and second is the image
    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert the image to grayscale
    faces=face_cascade.detectMultiScale(gray,1.7,4) # detect faces in the image

    for(x,y,w,h) in faces: # for each face detected
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4) # draw a rectangle around the face
    cv2.imshow("Face Detection",img) # display the image in a window
    
    key=cv2.waitKey(10) # wait for a key press for 10   millisecond
    if(key==27): # if the key pressed is 'Esc' key
        break
webcam.release() # release the webcam
cv2.destroyAllWindows() # destroy all windows





