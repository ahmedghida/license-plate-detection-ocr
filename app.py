import streamlit as st
from utils import DetectionOCR
from PIL import Image
import numpy as np
import cv2
import base64

DO = DetectionOCR()

# Inject CSS for background

# Function to convert image to base64
def image_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to your local background image
background_image_path = "background.jpg"  # Replace with your image path
background_image_base64 = image_to_base64(background_image_path)

# Inject CSS for background using base64 image
st.markdown(
    f"""
    <style>
    .main {{
        background-color: #f0f2f6; /* Fallback background color */
        background-image: url("data:image/jpeg;base64,{background_image_base64}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# Inject custom CSS for button styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: rgba(0, 123, 255, 0.3); /* Semi-transparent blue background */
        color: white; /* White text */
        border: none; /* Remove border */
        padding: 10px 20px; /* Padding */
        text-align: center; /* Center text */
        text-decoration: none; /* Remove underline */
        display: inline-block; /* Inline-block for sizing */
        font-size: 16px; /* Font size */
        margin: 4px 2px; /* Margin */
        cursor: pointer; /* Pointer cursor on hover */
        border-radius: 5px; /* Rounded corners */
        transition: background-color 0.3s; /* Smooth transition */
        font-weight: bold; /* Make text bold */
    }
    .stButton>button:hover {
        background-color: rgba(0, 123, 255, 0.5); /* Slightly less transparent on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header('Licence Plate Detection and Text Extraction')

# File uploader restricted to jpg and png files
original_image = st.file_uploader("Choose an image file", type=["jpg", "png"])

# Check if a file is uploaded
if original_image is not None:
    # Load the image using PIL
    image = Image.open(original_image)
    
    # Convert the PIL image to a numpy array for OpenCV/other image processing
    image_np = np.array(image)

    # Button to trigger detection
    btn = st.button(label="Submit")

    if btn:
        # Make a copy of the image to pass into detect_and_plot
        output_image = image_np.copy()

        # Call detection and plotting function
        DO.detect_and_plot(output_image)

        # Convert back to PIL image for displaying in Streamlit
        output_image_pil = Image.fromarray(output_image)

        # Create two columns for side-by-side display
        col1, col2 = st.columns(2)

        with col1:
            st.image(image, caption='Original Image', use_column_width=True)

        with col2:
            st.image(output_image_pil, caption='Processed Image', use_column_width=True)
