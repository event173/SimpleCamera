import cv2

def main():
    # Open a connection to the webcam (0 is the default camera)
    cap = cv2.VideoCapture(0)
    
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    # Loop to continuously get frames from the webcam
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Check if frame is read correctly
        if not ret:
            print("Error: Could not read frame.")
            break
        
        # Display the resulting frame
        cv2.imshow('Webcam Feed', frame)
        
        # Press 'q' on the keyboard to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # When everything is done, release the capture and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
