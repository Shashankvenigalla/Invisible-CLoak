import cv2
import numpy as np
import time

def create_background(cap, num_frames=30):
    print("Capturing Background. Please move out of frame.")
    backgrounds = []
    for i in range(num_frames):
        ret, frame = cap.read()
        if ret:
            backgrounds.append(frame)
        else:
            print(f"Warning; Could not read frame {i+1}/{num_frames}")
        time.sleep(0.1)
    if backgrounds:
        return np.median(backgrounds, axis=0).astype(np.uint8)
    else:
        raise ValueError("Could not capture any frame for background")

def create_mask(frame, lower_color, upper_color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=4)
    return mask

def apply_cloak_effect(frame, mask, background):
    mask_inv = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    bg = cv2.bitwise_and(background, background, mask=mask)
    return cv2.add(fg, bg)
def colors():
    return input()
def colorselection(color):
    if color=="B":
        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])
        return lower_blue,upper_blue
    elif color=='b':
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([30, 30, 30])
        return lower_black,upper_black
    elif color=="w":
        lower_white = np.array([245, 245, 245])
        upper_white = np.array([255, 255, 255])
        return lower_white,upper_white
    elif color=="R":
        lower_red = np.array([0, 0, 120])
        upper_red = np.array([10, 10, 255])
        return lower_red,upper_red
    elif color=="Y":
        lower_yellow = np.array([120, 150, 0])
        upper_yellow = np.array([255, 255, 150])
        return lower_red,upper_red
    else:
        print("Enter the Correct input")
def main():
    print("Enter wich color do u want?")
    print("Select 'B' for BLue \n 'b' for black\n 'w' for white\n 'R' for Red\n 'Y' for Yellow" )
    color=colors()
    print("OpenCV version:", cv2.__version__)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    try:
        background = create_background(cap)
    except ValueError as e:
        print(f"Error: {e}")
        cap.release()
        return
    lower,upper=colorselection(color)
    
    print("Starting main loop. Press 'q' to quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        mask = create_mask(frame, lower, upper)
        output = apply_cloak_effect(frame, mask, background)
        cv2.imshow('Cloak Effect', output)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()