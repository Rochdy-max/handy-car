from BotDirective import BotDirective
from IDirectiveInterpretor import IDirectiveInterpretor
import cv2
from cvzone.HandTrackingModule import HandDetector

@IDirectiveInterpretor.register
class HandImageInterpretor:
    def __init__(self, *, display_cap=False, debug=False):
        # Init attributes bounded to parameters
        self.display_cap = display_cap
        self.debug = debug

        # Init video capture
        self.cap = cv2.VideoCapture(0)
        # Set the frame width and height in pixels
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        # Init hand detector
        self.detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

    def get_image(self):
        success, img = self.cap.read()
        if not success:
            print('Impossible to read capture')
        return img

    def interpret(self) -> BotDirective:
        img = self.get_image()

        hands, img = self.detector.findHands(img, draw=True, flipType=True)

        if self.display_cap:
            cv2.imshow("Handy-Car", img)
            cv2.waitKey(1)

        if hands:
            # Information for the first hand detected
            hand1 = hands[0]  # Get the first hand detected
            lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
            bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
            center1 = hand1['center']  # Center coordinates of the first hand
            handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

            # Count the number of fingers up for the first hand
            fingers = self.detector.fingersUp(hand1)
            # Get the count of fingers that are up
            fingersCount = fingers.count(1)
            if self.debug and fingersCount > 0:
                print(f'H1 = {fingersCount}')

            match fingersCount:
                case 0:
                    return BotDirective.NOTHING
                case 1:
                    return BotDirective.GO_FORWARD
                case 2:
                    return BotDirective.GO_BACKWARD
                case 3:
                    return BotDirective.TURN_LEFT
                case 4:
                    return BotDirective.TURN_RIGHT
                case 5:
                    return BotDirective.STOP

            # Calculate distance between specific landmarks on the first hand and draw it on the image
            # length, info, img = self.detector.findDistance(lmList1[8][0:2], lmList1[12][0:2], img, color=(255, 0, 255),
            #                                         scale=10)


"""
# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(2)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# Continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()

    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
        bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
        center1 = hand1['center']  # Center coordinates of the first hand
        handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

        # Count the number of fingers up for the first hand
        fingers1 = detector.fingersUp(hand1)
        print(f'H1 = {fingers1.count(1)}', end=" ")  # Print the count of fingers that are up

        # Calculate distance between specific landmarks on the first hand and draw it on the image
        length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[12][0:2], img, color=(255, 0, 255),
                                                  scale=10)

        # Check if a second hand is detected
        if len(hands) == 2:
            # Information for the second hand
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            center2 = hand2['center']
            handType2 = hand2["type"]

            # Count the number of fingers up for the second hand
            fingers2 = detector.fingersUp(hand2)
            print(f'H2 = {fingers2.count(1)}', end=" ")

            # Calculate distance between the index fingers of both hands and draw it on the image
            length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img, color=(255, 0, 0),
                                                      scale=10)

        print(" ")  # New line for better readability of the printed output

    # Display the image in a window
    cv2.imshow("Image", img)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)
"""
