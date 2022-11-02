import analysis
import cv2
import os

directory = os.path.dirname(__file__)
path = os.path.join(directory, "example_coins.jpg")
im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
ret,thresh = cv2.threshold(im, 110, 255, cv2.THRESH_BINARY)

analyser = analysis.BlobAnalysis()
analyser.analyse(im)
im_with_keypoints = analyser.overlay_image(im)
print(analyser.keypoint_tuples())
cv2.imshow("Detected", im_with_keypoints)
cv2.waitKey(0)