import cv2


ref_images = [
    #("Hemabh", cv2.imread(r"C:\Users\Hemab\OneDrive\Pictures\Camera Roll\WIN_20231220_19_45_29_Pro.jpg")),
    #("Blackberry box", cv2.imread(r"C:\Users\Hemab\OneDrive\Pictures\Camera Roll\WIN_20231220_20_05_32_Pro.jpg")),
    ("Preksha", cv2.imread(r"C:\Users\Hemab\OneDrive\Pictures\Camera Roll\WIN_20240103_22_07_36_Pro.jpg"))
    
]


cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()

    
    for ref_image_name, ref_image in ref_images:
        result = cv2.matchTemplate(frame, ref_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.5:  
            print("I see:", ref_image_name)
            LookupError(object.__basicsize__)

            
            x, y = max_loc
            w, h = ref_image.shape[1], ref_image.shape[0]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  


    cv2.imshow("Camera", frame)


    if cv2.waitKey(1) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
