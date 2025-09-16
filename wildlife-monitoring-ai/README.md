# Wildlife Monitoring & Human-Wildlife Conflict Prevention Using AI

A real-time, multi-sensor, AI-powered app for wildlife monitoring, species classification, and conflict prevention, with live alerts and dashboard.

## Features

- Real-time animal detection using YOLOv5/YOLOv9
- Multi-sensor fusion (camera + audio)
- Species classification using Wildlife Insights API
- Live actions: buzzer, light, visual alerts
- SMS/Email notifications for human-wildlife conflict
- Dashboard for live metrics and analysis
- Modular and extensible codebase

## Quick Start

1. **Clone the repo** and `cd wildlife-monitoring-ai`
2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure `config.yaml`** with your device and API keys.
4. **Run the app:**
   ```bash
   streamlit run app/main.py
   ```

## Hardware Integration

Connect an Arduino or Raspberry Pi Zero to your laptop. Use `hardware/serial_comm.py` for triggering buzzer/light.

## Extending

- Add wildfire detection with a pretrained model.
- Poacher detection and illegal construction: treat as optional, see TODO notes in code.

## References

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [Wildlife Insights API](https://www.wildlifeinsights.org/get-started/upload/share-our-api)