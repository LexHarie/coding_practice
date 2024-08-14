# Import necessary libraries
from transformers import BeitImageProcessor, BeitForImageClassification
from PIL import Image
import torch
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Function to predict the class of the image
def predict_image_class(image, model, processor, device):
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    return predicted_class_idx

# Function to display the image and its predicted class
def display_prediction(image, prediction, id2label):
    plt.imshow(image)
    plt.title(f"Predicted: {id2label[prediction]}")
    plt.axis('off')
    plt.show()

# Function to capture an image from the camera, crop the region of interest (ROI), and return it
def capture_image_from_camera():
    cap = cv2.VideoCapture(0)  # Open the default camera
    ret, frame = cap.read()  # Read a frame from the camera

    if not ret:
        print("Failed to capture image")
        return None

    # Define the ROI as a small square in the center of the frame
    h, w, _ = frame.shape
    center_x, center_y = w // 2, h // 2
    square_size = min(h, w) // 4  # Define the size of the square
    top_left_x = center_x - square_size // 2
    top_left_y = center_y - square_size // 2
    bottom_right_x = center_x + square_size // 2
    bottom_right_y = center_y + square_size // 2

    # Draw a rectangle (for visualization)
    cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 2)
    cv2.imshow('Capture', frame)

    # Wait for a key press and capture the image inside the ROI
    cv2.waitKey(0)
    roi = frame[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    return Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

# Capture an image from the camera and classify it
def camera_image_classification():
    # Initialize the processor and model
    processor = BeitImageProcessor.from_pretrained('microsoft/beit-large-patch16-224-pt22k-ft22k')
    model = BeitForImageClassification.from_pretrained('microsoft/beit-large-patch16-224-pt22k-ft22k')
    model.eval()
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device)
    
    # Capture image from the camera
    image = capture_image_from_camera()
    
    if image is not None:
        # Predict the class of the captured image
        prediction = predict_image_class(image, model, processor, device)
        predicted_label = model.config.id2label[prediction]
        
        # Display the captured image and its predicted class
        display_prediction(image, prediction, model.config.id2label)

# Run the image classification pipeline for a captured image from the camera
camera_image_classification()
