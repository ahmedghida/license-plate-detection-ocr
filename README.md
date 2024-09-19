# License Plate Detection and OCR

This project aims to detect license plates from images using a custom-trained YOLOv8 model and extract text from the detected plates using EasyOCR. The solution is wrapped in a user-friendly web application built with Streamlit, allowing users to upload images, detect license plates, and perform OCR in a streamlined process.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model)
- [OCR](#ocr)
- [Web Application](#web-application)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)

## Project Overview

The main objective of this project is to provide an automated system for detecting vehicle license plates and extracting their corresponding text using deep learning and optical character recognition (OCR). It combines object detection with YOLOv8 and OCR with EasyOCR.

### Tech Stack:
- **YOLOv8** for license plate detection.
- **EasyOCR** for text extraction from the plates.
- **Streamlit** for the web-based user interface.

## Features

- Upload an image (.jpg or .png) via the web interface.
- Detect and highlight license plates using the custom-trained YOLOv8 model.
- Perform OCR on the detected license plates to extract text.
- Display the original and processed images side-by-side in the web app.
- Easy-to-use interface with customizable features.


## Video Demonstration

To see how to run this project locally, you can watch the following video:

<video width="365" height="480" controls>
  <source src="media/video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>





## Installation

To get started with this project, follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/your-repo/license-plate-detection-ocr.git
cd license-plate-detection-ocr

```

### 2. Create a virtual environment and activate it:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

```

## 3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Download the YOLOv8 model

Download your custom-trained YOLOv8 model weights file called `LPD.pt` and place it in the `models` folder.


## Usage
Once all dependencies are installed and the YOLOv8 model is ready, you can run the Streamlit web app:

```bash
streamlit run app.py
```

### Using the Web App

- **Upload an Image**: Select a .jpg or .png file containing a vehicle.
- **Submit the Image**: Click on the "Submit" button to detect the license plate and extract the text.
- **View Results**: The original and processed images are displayed side-by-side, with detected license plates and the extracted text highlighted.


## Dataset

The dataset used to train the YOLOv8 model was sourced from the Kaggle car plate detection dataset. It contains images of vehicles with annotated license plates for object detection training. You can download the dataset from the [Kaggle car plate detection dataset](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection).

## Model

### License Plate Detection

The project uses a YOLOv8 model trained on the custom Kaggle dataset to detect license plates in images. YOLO (You Only Look Once) is an efficient, real-time object detection algorithm that performs well on small objects like license plates.

### OCR

For extracting text from detected license plates, EasyOCR is used. It is a lightweight and easy-to-use OCR library that supports multiple languages, ensuring that the license plate text is accurately identified and extracted.

## Web Application

The web application is built using Streamlit, allowing users to upload an image, detect license plates, and extract text in a simple and user-friendly interface. The detection and OCR processes are encapsulated in the `DetectionOCR` class in the `utils.py` file.

### Files

- **app.py**: The main Streamlit app file for running the web application.
- **utils.py**: Contains the `DetectionOCR` class responsible for detection and OCR processing.

## Future Improvements

Possible improvements to this project include:

- Support for video input (real-time detection and OCR).
- Enhancement of OCR accuracy for different types of license plates (international formats).
- Deployment on cloud platforms (e.g., AWS, Heroku) for broader access.
- Extending the model to support other license plate detection tasks like blurred plates.

## Contributors

We welcome contributions to enhance this project. If you'd like to contribute, please follow the standard open-source contribution guidelines.

