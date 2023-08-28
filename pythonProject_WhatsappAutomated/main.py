import cv2

face_cap=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#ENABLE THE VIDEO-OPENING THE WEBCAM !!
video_cap=cv2.VideoCapture(0)
while True:
    ret , video_data=video_cap.read()
    col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY) #BLAC N WHITE MEIN CHANGE KR RHA CAPTURED
    faces=face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces: #GREEN CLOLOUR KA BOX ISSI KE KARAN BNA HAI
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,225,0),2)
    cv2.imshow("Live_show",video_data)
    if cv2.waitKey(10) == ord("x"):
        break
video_cap.release()

