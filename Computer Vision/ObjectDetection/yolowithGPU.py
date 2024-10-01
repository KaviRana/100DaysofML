"""Changing settings and making YOLO run on the GPU rather on the CPU
1. pip install torch torchvision torchaudio
2. What is mps = MPS (Metal Performance Shaders) is a framework provided by Apple 
for GPU-accelerated computing on Mac devices.

"""
import torch
from ultralytics import YOLO
import cv2
import cvzone
import math 

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model = YOLO('/Users/kavi/Desktop/College/computer vision/obj_detection/YOLO/Yolo_weights/yolov8l.pt').to(device)

cap = cv2.VideoCapture("/Users/kavi/Desktop/College/computer vision/obj_detection/Videos/bottle-detection.mp4")

coco_classes = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat',
    'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat',
    'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
    'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair',
    'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
    'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
    ]


while True:
    success, img = cap.read()
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes: 
            
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1,y1,x2,y2)
            w,h = x2-x1,y2-y1
            
            cvzone.cornerRect(img, (x1,y1,w,h),colorR=(255,0,255))

            
            conf = math.ceil((box.conf[0]*100))/100
            print(conf)
            cls = int(box.cls[0])
            cvzone.putTextRect(img,f'{coco_classes[cls]} {conf}',(max(0,x1),max(35,y1)), scale=1, thickness=1)




    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(f"Using device: {device}")
