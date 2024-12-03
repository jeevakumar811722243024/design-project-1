import os
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

# Try accessing the camera
cap = cv2.VideoCapture(0)  # Changed to 0 for default camera

if not cap.isOpened():
    raise RuntimeError("Error: Cannot access the camera. Check if the camera is connected and working.")

# Load model and labels
classifier = Classifier('Resources/Model/keras_model.h5', 'Resources/Model/labels.txt')
imgArrow = cv2.imread('Resources/arrow.png', cv2.IMREAD_UNCHANGED)
classIDBin = 0

# Import all the waste images
imgWasteList = []
pathFolderWaste = "Resources/Waste"
pathList = os.listdir(pathFolderWaste)
for path in pathList:
    imgWasteList.append(cv2.imread(os.path.join(pathFolderWaste, path), cv2.IMREAD_UNCHANGED))

# Import all the bin images
imgBinsList = []
pathFolderBins = "Resources/Bins"
pathList = os.listdir(pathFolderBins)
for path in pathList:
    imgBinsList.append(cv2.imread(os.path.join(pathFolderBins, path), cv2.IMREAD_UNCHANGED))

# Class to bin mapping
classDic = {0: None,
            1: 0,
            2: 0,
            3: 3,
            4: 3,
            5: 1,
            6: 1,
            7: 2,
            8: 2}

while True:
    # Read frame from the camera
    ret, img = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    imgResize = cv2.resize(img, (454, 340))  # Resize for display

    # Background image for displaying the results
    imgBackground = cv2.imread('Resources/background.png')

    # Get prediction from the classifier
    prediction = classifier.getPrediction(img)
    classID = prediction[1]
    
    print(f"Predicted class ID: {classID}")
    
    # If we have a valid class prediction (not 'None')
    if classID != 0:
        # Overlay the appropriate waste image and arrow on the background
        imgBackground = cvzone.overlayPNG(imgBackground, imgWasteList[classID - 1], (909, 127))
        imgBackground = cvzone.overlayPNG(imgBackground, imgArrow, (978, 320))

        # Get corresponding bin based on the class ID
        classIDBin = classDic.get(classID, 0)

    # Overlay the bin image on the background
    imgBackground = cvzone.overlayPNG(imgBackground, imgBinsList[classIDBin], (895, 374))

    # Overlay the resized camera image
    imgBackground[148:148 + 340, 159:159 + 454] = imgResize

    # Display the resulting frame
    cv2.imshow("Output", imgBackground)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
