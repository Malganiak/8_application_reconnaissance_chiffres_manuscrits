import cv2

def capture():
    
    cam = cv2.VideoCapture(0)
    WIDTH = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    HEIGHT = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
   
    img_counter = 0

    while True:
        
        ret, frame = cam.read()
        
        # Create Cropped frame 
        bbox_size = (60, 60)
        center_x = int(WIDTH // 2)
        center_y = int(HEIGHT // 2)
        bbox = [(center_x - bbox_size[0] // 2, center_y - bbox_size[1] // 2),
                (center_x + bbox_size[0] // 2, center_y + bbox_size[1] // 2)]
        img_cropped = frame[bbox[0][1]:bbox[1][1], bbox[0][0]:bbox[1][0]]
        img_gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
        img_gray = cv2.resize(img_gray, (200, 200))

        # Added a white square contour to our cropped frame to help centering   
        bbox_color = (255, 255, 255)
        cv2.rectangle(img_gray, (0, 0), (img_gray.shape[1], img_gray.shape[0]), bbox_color, 25)
        
        # Create Crosshair
        crosshair_length = 20
        color = (255, 0, 0)  # Blue color
        # Crosshair on Main frame 
        cv2.line(frame, (center_x - crosshair_length, center_y), (center_x + crosshair_length, center_y), color, 2)
        cv2.line(frame, (center_x, center_y - crosshair_length), (center_x, center_y + crosshair_length), color, 2)
        # Crosshair on Cropped frame
        cv2.line(img_gray, (img_gray.shape[1] // 2 - crosshair_length, img_gray.shape[0] // 2),
                 (img_gray.shape[1] // 2 + crosshair_length, img_gray.shape[0] // 2), color, 2)
        cv2.line(img_gray, (img_gray.shape[1] // 2, img_gray.shape[0] // 2 - crosshair_length),
                 (img_gray.shape[1] // 2, img_gray.shape[0] // 2 + crosshair_length), color, 2)
        
        if not ret:
            print("failed to grab frame")
            break
        
        # Showing frames
        cv2.imshow("Main frame", frame)
        cv2.imshow("Cropped frame", img_gray)
        
        # Key command
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed for quitting
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed for taking picture
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, img_gray)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()