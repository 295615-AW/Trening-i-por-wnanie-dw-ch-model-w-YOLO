from ultralytics import YOLO

model_a = YOLO("runs/detect/wariant_A_yolov8n/weights/best.pt")
model_b = YOLO("runs/detect/wariant_B_yolo11n/weights/best.pt")

model_a.predict(source="p4.jpg", save=True, conf=0.25)
model_b.predict(source="p4.jpg", save=True, conf=0.25)
# model_a.predict(source="photo2.png", save=True, conf=0.25)
# model_b.predict(source="photo2.png", save=True, conf=0.25)