import analysis
import cv2

cv2.namedWindow("video")
print("Opening capture device")
vc = cv2.VideoCapture(0)
analyser = analysis.BlobAnalysis()


if vc.isOpened(): # try to get the first frame
    print("Try first capture")
    rval, frame = vc.read()
else:
    rval = False


print("Going into loop")
while rval:
    rval, frame = vc.read()
    analyser.analyse(frame)
    print(analyser.keypoint_tuples())
    im_with_keypoints = analyser.overlay_image(frame)
    cv2.imshow("video", im_with_keypoints)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break



vc.release()
cv2.destroyWindow("video")