# Face Detection using OpenCV

A simple face detection project built with Python and OpenCV. This project captures live video from the webcam and detects human faces using OpenCV's Haar Cascade Classifier, drawing a green bounding box around each detected face.

## Features

* Real-time face detection using a webcam
* Detects multiple faces in a single frame
* Draws bounding boxes around detected faces
* Press **Esc** to exit the application

## Technologies Used

* Python
* OpenCV (cv2)

## Project Structure

```text
Face-Detection/
│── faceDetection.py
│── haarcascade_frontalface_default.xml
│── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AkshitBisht02/Face-Detection.git
```

2. Navigate to the project folder:

```bash
cd Face-Detection
```

3. Install OpenCV:

```bash
pip install opencv-python
```

## How to Run

Run the following command:

```bash
python faceDetection.py
```

A webcam window will open and start detecting faces in real time.

## How It Works

1. Loads the pre-trained Haar Cascade face detection model.
2. Opens the system webcam.
3. Converts each frame to grayscale.
4. Detects faces using the cascade classifier.
5. Draws a green rectangle around every detected face.
6. Closes the application when the **Esc** key is pressed.

## Learning Outcomes

This project helped me understand:

* Capturing live video using OpenCV
* Image preprocessing (grayscale conversion)
* Face detection with Haar Cascades
* Drawing shapes on video frames
* Working with webcam input in Python

## Future Improvements

* Face recognition
* Eye and smile detection
* Face mask detection
* Emotion detection
* Face counting

## Author

**Akshit Bisht**

GitHub: https://github.com/AkshitBisht02
