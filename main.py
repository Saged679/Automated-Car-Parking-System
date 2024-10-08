import numpy as np
import pickle
import cv2
import cvzone

cap = cv2.VideoCapture("f:/My Files/Project/Car Parking System/carPark.mp4")

with open('CarPos', 'rb') as f:
        posList = pickle.load(f)

width, height = 107, 48

def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y : y + height, x : x + width]
        count = cv2.countNonZero(imgCrop)

        if count < 905:
            color = (0, 255, 0)
            thickness = 3
            spaceCounter += 1
        else:
                color = (0, 0, 255)
                thickness = 3

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                        thickness=2, offset=0, colorR=(0, 0, 0, 0))

    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (15, 20), scale=1.5,
                        thickness=2, offset=0, colorR=(0, 0, 0, 0))

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break