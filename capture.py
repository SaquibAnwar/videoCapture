import cv2, time

video = cv2.VideoCapture(0)                                                     #for reading video from the camera

a=0

while True:
    a=a+1
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(3)                                                              #opening the camera for 3 secs
    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1)

    if key == ord('q'):                                                         #will break when pressed q from the keyboard
        break

print(a)
video.release()
cv2.destroyAllWindows()
