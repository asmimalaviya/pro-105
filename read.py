import cv2 
vid=cv2.VideoCapture(0)
if (vid.isOpened ()==False) :
    print("unable to read the video")

height =int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width =int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps= int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

while(True):
    ret,frame=vid.read()
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1)== 32:
        break
vid.release()