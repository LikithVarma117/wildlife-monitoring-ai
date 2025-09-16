import streamlit as st
from detection.detector import WildlifeDetector
from detection.species_api import SpeciesClassifier
from hardware.serial_comm import ActionDevice
from notifications.notifier import send_sms, send_email
import cv2
import yaml

st.set_page_config(page_title="Wildlife Monitoring AI", layout="wide")

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

st.title("🐾 Wildlife Monitoring & Human-Wildlife Conflict Prevention")

detector = WildlifeDetector(confidence=config["confidence_threshold"])
species_classifier = SpeciesClassifier(config["wildlife_insights_api_key"])
device = ActionDevice()

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])
if run:
    cap = cv2.VideoCapture(config["camera_index"])
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Camera not found!")
            break

        detections = detector.detect(frame)
        for det in detections:
            # Draw bounding boxes
            x1, y1, x2, y2 = map(int, det['bbox'][0])
            label = det['label']
            conf = det['confidence']
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, f"{label}:{conf:.2f}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

            # If target species, trigger actions
            if label in config["target_species"]:
                if "buzzer" in config["alert_methods"]:
                    device.trigger_buzzer()
                if "light" in config["alert_methods"]:
                    device.trigger_light()
                if "sms" in config["alert_methods"]:
                    send_sms(
                        f"Alert: {label} detected with confidence {conf:.2f}",
                        config["notification"]["sms"]
                    )
                if "email" in config["alert_methods"]:
                    send_email(
                        subject="Wildlife Alert",
                        body=f"{label} detected with confidence {conf:.2f}",
                        config=config["notification"]["email"]
                    )
        FRAME_WINDOW.image(frame, channels='BGR')
    cap.release()