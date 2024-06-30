import cv2
import numpy as np
import ultralytics
from ultralytics import YOLO

class VehicleDetector:

    def __init__(self):
        # Load Network
        self.model = YOLO("yolov8n.pt")

        # Allow classes containing Vehicles only
        self.classes_allowed = [2, 3, 5, 6, 7]
        #2=car, 3=motorcycle, 5=bus, 6=train, 7=truck

    def detect_vehicles(self, img):
      
        # Detect Objects
        vehicles_boxes = []
        results = self.model(img, save=True)
        result = results[0].boxes
        
        xyxy = result.xyxy.tolist()
        class_ids = result.cls.tolist()
        confidence = result.conf.tolist()
        
        for box, class_id, confidence in zip(xyxy, class_ids, confidence):
            if confidence < 0.3:
                # Skip detection with low confidence
                continue
            if class_id in self.classes_allowed:
                vehicles_boxes.append(box)

        return vehicles_boxes



