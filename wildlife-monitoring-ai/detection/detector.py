import cv2
import torch
from ultralytics import YOLO

class WildlifeDetector:
    def __init__(self, model_path='yolov9c.pt', confidence=0.5):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame):
        results = self.model(frame)
        detections = []
        for result in results:
            for box in result.boxes:
                if box.conf >= self.confidence:
                    detections.append({
                        "bbox": box.xyxy.tolist(),
                        "label": box.cls,
                        "confidence": float(box.conf)
                    })
        return detections