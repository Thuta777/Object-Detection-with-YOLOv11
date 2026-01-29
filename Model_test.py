import cv2
from ultralytics import YOLO

model = YOLO("C:/Users/thuta/Downloads/Uni/Senior Project/Image Model/runs/detect/train8/weights/best.pt")
model.to("cuda")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.25, device=0, imgsz=640, stream=True)

    for r in results:
        frame = r.plot()

    cv2.imshow("YOLOv11 Demo", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cap.release()
cv2.destroyAllWindows()