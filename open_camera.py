import cv2

# open camera
camera = cv2.VideoCapture(0)

# while loop to read the camera image
while True:
    success, img = camera.read()
    # if read success, it'll show the image in a "Video" window
    if success:
        cv2.imshow("Video", img)
    # get the key press, if you pressed "q" key it'll break the while loop
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

# release you camera device and close the OpenCV windows
camera.release()
cv2.destroyAllWindows()