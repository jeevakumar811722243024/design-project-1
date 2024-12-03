

# Garbage Classifier for Waste Management

This project is an image classification system that classifies garbage into specific categories (e.g., recyclable, hazardous, food, or residual waste) and suggests the appropriate bin for disposal. The system uses a webcam to capture images, a pre-trained TensorFlow model for classification, and OpenCV for visualization.

---

## Features  
- **Real-Time Classification**: Uses a webcam to capture real-time video frames.  
- **Waste Categories**: Identifies the type of waste and assigns it to a specific category.  
  - **Categories**: Recyclable, Hazardous, Food, Residual.  
- **Bin Suggestions**: Displays the appropriate bin for each waste category.  
- **User-Friendly Interface**: Overlays classification results and visuals on a custom background image.

---

## Requirements  

Ensure you have the following installed before running the project:

### Software and Libraries:  
1. **Python**: Version 3.10 or higher.  
2. **TensorFlow**: Version 2.18.0.  
3. **OpenCV**: Version 4.10.0.  
4. **cvzone**: A utility for computer vision tasks.  

### Hardware:  
1. A webcam (internal or external).  
2. A computer capable of running Python and TensorFlow.  

### Additional Files:  
1. **Pre-trained TensorFlow Model**:  
   - `keras_model.h5`: The trained model for waste classification.  
   - `labels.txt`: A text file containing class labels for the model.  
2. **Resources Folder**:  
   - `Waste/`: Contains images of different types of waste.  
   - `Bins/`: Contains images of different bins.  
   - `arrow.png`: Visual cue for bin suggestions.  
   - `background.png`: Custom background for the interface.

---

## Folder Structure  

```plaintext
Resources/
│
├── Model/
│   ├── keras_model.h5    # Pre-trained classification model.
│   └── labels.txt         # Class labels for the model.
│
├── Waste/
│   └── [Waste images...]  # PNG images representing various waste items.
│
├── Bins/
│   └── [Bin images...]    # PNG images of corresponding bins.
│
├── arrow.png              # Arrow image for bin indication.
└── background.png         # Background image for the display interface.
```

---

## Installation  

Follow these steps to set up the project on your local system:

1. Clone the repository or download the project folder:
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```
2. Install the required libraries:
   ```bash
   pip install tensorflow==2.18.0 opencv-python==4.10.0 cvzone
   ```
3. Ensure the **Resources** folder is in the same directory as your Python script.  

---

## How to Run  

1. Connect your webcam to the computer.  
2. Open the terminal in the project directory.  
3. Run the Python script:
   ```bash
   python app.py
   ```
4. The program will start capturing real-time video from the webcam.  
5. Place an object in front of the camera to classify it. The system will:  
   - Display the waste item on the screen.  
   - Show the suggested bin for disposal.  

---

## Troubleshooting  

### **Camera Issues**:
- If you see `Camera index out of range` or similar errors:
  1. Ensure your webcam is connected and not in use by another application.  
  2. Try changing the camera index in the code:
     ```python
     cap = cv2.VideoCapture(0)  # Change 0 to 1 or 2 if necessary.
     ```

### **Model Issues**:
- If the model does not classify the object:
  1. Ensure `keras_model.h5` and `labels.txt` are present in the `Resources/Model` folder.  
  2. Verify that the model and label files match the categories in `classDic`.

### **Library Errors**:
- If you encounter errors related to TensorFlow or OpenCV:
  - Reinstall the libraries:
    ```bash
    pip install tensorflow==2.18.0 opencv-python==4.10.0
    ```

---

## Future Enhancements  

- Improve classification accuracy by retraining the model with more data.  
- Add a GUI to make the system more user-friendly.  
- Extend the waste categories for broader use cases.  
- Enable voice feedback for bin suggestions.  

---

## Credits  

- **Libraries Used**: TensorFlow, OpenCV, cvzone.  
- **Model Training**: Pre-trained MobileNetV2 model used for waste classification.  

---

## License  

This project is licensed under the [MIT License](LICENSE).  

--- 
