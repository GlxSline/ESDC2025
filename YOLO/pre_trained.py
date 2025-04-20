from ultralytics import YOLO

a1 = YOLO('yolov8n.pt')

a1('1.mp4', show=True,save = True)

