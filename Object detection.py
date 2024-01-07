import cv2


ref_images = [
    ("Object_Name", cv2.imread(r"Location")),
    ("Object_Name", cv2.imread(r"Location")),
    ("Object_Name", cv2.imread(r"Location"))
    #add "r" only when you are using local location
    
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
