from BotDirective import BotDirective
from IDirectiveInterpretor import IDirectiveInterpretor
try:
    import cv2 as cv
    from cvzone.HandTrackingModule import HandDetector
except: print("error import cv2 and cvzone")

@IDirectiveInterpretor.register
class HandImageInterpretor(IDirectiveInterpretor):
    def __init__(self, cap = None, *, display_cap=False, window_name = None, debug=False):
        # Init video capture
        if not cap:
            cap = cv.VideoCapture(0)
        self.cap = cap

        self.display_cap = display_cap # Boolean for displaying captured image or not
        self.debug = debug # Boolean for displaying debug info or not
        # Name of the imshow window
        if not window_name:
            window_name = "Handy-Car"
        self.window_name = window_name
        self.window_closed = False # Boolean for window closing or not (initially False)

        # Init hand detector
        self.detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

    @property
    def cap(self):
        return self._cap

    @cap.setter
    def cap(self, vcap):
        if not vcap.isOpened():
            raise AttributeError("Video capture unavailable")
        self._cap = vcap

    def get_image(self):
        success, img = self.cap.read()
        if not success:
            raise RuntimeError('Impossible to read video capture')
        return img

    def poll_directive(self) -> BotDirective:
        img = self.get_image()

        hands, img = self.detector.findHands(img, draw=True, flipType=True)

        if self.display_cap and not self.window_closed:
            cv.imshow(self.window_name, img)
            cv.waitKey(1)
            if cv.getWindowProperty(self.window_name, cv.WND_PROP_VISIBLE) < 1:
                self.window_closed = True

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
