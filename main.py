import cv2
import numpy as np




def single_color_detector():
    # Webcamera no 0 is used to capture the frames
    cap = cv2.VideoCapture(0)

    # This drives the program into an infinite loop.
    while True:
        # Captures the live stream frame-by-frame
        _, frame = cap.read()
        # Converts images from BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([110, 50, 50])
        upper_red = np.array([130, 255, 255])

        # Here we are defining range of bluecolor in HSV
        # This creates a mask of blue coloured
        # objects found in the frame.
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # The bitwise and of the frame and mask is done so
        # that only the blue coloured objects are highlighted
        # and stored in res
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        # This displays the frame, mask
        # and res which we created in 3 separate windows.
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

        # Destroys all of the HighGUI windows.
        # cv2.destroyAllWindows()

        # release the captured frame
        # cap.release()


def mul_color_detector():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Red color
        low_red = np.array([161, 155, 84])
        high_red = np.array([179, 255, 255])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        red = cv2.bitwise_and(frame, frame, mask=red_mask)

        # Blue color
        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

        # Green color
        low_green = np.array([25, 52, 72])
        high_green = np.array([102, 255, 255])
        green_mask = cv2.inRange(hsv_frame, low_green, high_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)

        # Every color except white
        low = np.array([0, 42, 0])
        high = np.array([179, 255, 255])
        mask = cv2.inRange(hsv_frame, low, high)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Frame", frame)
        # cv2.imshow("Red", red)
        # cv2.imshow("Blue", blue)
        # cv2.imshow("Green", green)
        cv2.imshow("Result", result)

        key = cv2.waitKey(1)
        if key == 27:
            break


def img_reader():
    frame = cv2.imread('imshow.png')

    cv2.imshow('sample image', frame)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    cv2.imshow("Blue Color", blue)
    cv2.waitKey(0)  # waits until a key is pressed
    cv2.destroyAllWindows()  # destroys the window showing image


if __name__ == '__main__':
    # single_color_detector()
    # mul_color_detector()
    img_reader()
