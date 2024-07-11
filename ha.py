def main():
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
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    print("Starting main loop. Press 'q' to quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        mask = create_mask(frame, lower_blue, upper_blue)
        output = apply_cloak_effect(frame, mask, background)
        cv2.imshow('Cloak Effect', output)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()