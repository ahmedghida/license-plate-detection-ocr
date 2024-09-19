import cv2
import numpy as np
from ultralytics import YOLO
import easyocr

class DetectionOCR:
    
    def __init__(self, model_path='models\LPD.pt', lang_list=['en']):
        """
        Initializes the object detection and OCR model.

        Args:
            model_path (str): Path to the YOLO model.
            lang_list (list): List of languages for EasyOCR.
        """
        self.model = YOLO(model_path)
        self.reader = easyocr.Reader(lang_list)

    def detect_objects(self, image):
        """
        Detects all objects in the given image using the YOLO model and returns bounding boxes, 
        class labels, and confidence scores.

        Args:
            image (np.array): Input image for detection.

        Returns:
            list: A list of dictionaries containing 'bbox', 'cls', and 'conf' for detected objects.
        """
        results = self.model.predict(image, verbose=False)
        detections = []

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy.cpu().numpy()[0]
                conf = box.conf.cpu().numpy()[0]
                cls = box.cls.cpu().numpy()[0]

                detections.append([x1, y1, x2, y2, conf, cls])

        return detections

    def extract_plate_text(self, image, detections):
        """
        Crops detected bounding boxes from the image and performs OCR to extract text.

        Args:
            image (np.array): Input image.
            detections (list): List of detected objects with bounding boxes.

        Returns:
            list: Extracted text for each detection.
        """
        texts = []

        for detection in detections:
            x1, y1, x2, y2, _, _ = detection
            cropped_image = image[int(y1):int(y2), int(x1):int(x2)]
            ocr_results = self.reader.readtext(cropped_image)

            for ocr_result in ocr_results:
                _, text, _ = ocr_result
                texts.append(text)

        return texts

    def draw_detections(self, image, detections, texts):
        """
        Draws bounding boxes and OCR results on the image.

        Args:
            image (np.array): Original input image.
            detections (list): List of detected objects with bounding boxes.
            texts (list): Extracted texts for the detected objects.
        """
        for idx, detection in enumerate(detections):
            x1, y1, x2, y2, _, _ = detection
            text = texts[idx]

            # Draw bounding box
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

            # Calculate text size and draw background rectangle for the text
            text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
            text_width, text_height = text_size
            cv2.rectangle(image, (int(x1), int(y1) - text_height - 10),
                          (int(x1) + text_width + 10, int(y1)),
                          (0, 0, 255), -1)

            # Put the text on the image
            cv2.putText(image, text, (int(x1) + 5, int(y1) - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    def detect_and_plot(self, image):
        """
        Detects objects in the image, performs OCR, and draws bounding boxes with OCR text.

        Args:
            image (np.array): Input image.
        """
        detections = self.detect_objects(image)
        texts = self.extract_plate_text(image, detections)
        self.draw_detections(image, detections, texts)
















