import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
# python detector.py --model D:\Users\Aakash\Documents\Programming\Python\Projects\TheTrashCycle\AakashStuff\TACO\detector\models\logs\ --dataset D:\Users\Aakash\Documents\Programming\Python\Projects\TheTrashCycle\AakashStuff\TACO\data --round 0 --class_map D:\Users\Aakash\Documents\Programming\Python\Projects\TheTrashCycle\AakashStuff\TACO\detector\taco_config\map_1.csv test
# python detector.py --model mask_rcnn_taco_0100.h5 --dataset D:\Users\Aakash\Documents\Programming\Python\Projects\TheTrashCycle\AakashStuff\TACO\data --round 0 --class_map D:\Users\Aakash\Documents\Programming\Python\Projects\TheTrashCycle\AakashStuff\TACO\detector\taco_config\map_1.csv test