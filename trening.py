from ultralytics import YOLO

# Wariant A: Lekki (High FPS)
model_a = YOLO("yolov8n.pt")
model_a.train(
    data="VisDrone.yaml",
    epochs=10,
    imgsz=640,
    fraction=0.2,
    name="wariant_A_yolov8n"
)

# Wariant B: Precyzyjny (High mAP)
model_b = YOLO("yolo11n.pt")
model_b.train(
    data="VisDrone.yaml",
    epochs=10,
    imgsz=640,
    fraction=0.2,
    name="wariant_B_yolo11n"
)