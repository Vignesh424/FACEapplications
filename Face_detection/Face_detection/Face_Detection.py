import cv2
import argparse
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,
help="Path to the image saved")
ap.add_argument("-c","--cascade",
default="haarcascade_frontalface_default.xml",
help="Path to the detector haar cascade ")
args = vars(ap.parse_args())
image=cv2.imread(args["image"])
#convert to gray scale
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#detector initialize
detector=cv2.CascadeClassifier(args["cascade"])
rects = detector.detectMultiScale(gray, scaleFactor=1.3,
minNeighbors=10, minSize=(75, 75))
#loop over
for (i ,(x,y,w,h)) in enumerate(rects):
    # draw rectangle
    cv2.rectangle(image,(x, y),(x + w,y + h),(0, 0, 255), 2)
    # write in the image
    cv2.putText(image,"Face* {}".format(i + 1),(x, y-10),
    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
# Show Detected Faces
cv2.imshow("Faces",image)
cv2.waitKey(0)

