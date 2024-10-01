from ultralytics import YOLO
import cv2 
model = YOLO('running_yolo/Yolo_weights/yolov8n.pt')
results = model('Images/img3.jpg', show=True)

cv2.waitKey(0)
