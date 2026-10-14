!pip install ultralytics opencv-python matplotlib -q
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.7/46.7 kB 1.3 MB/s eta 0:00:00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 12.8 MB/s eta 0:00:00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.2/53.2 kB 1.7 MB/s eta 0:00:00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 88.7/88.7 kB 7.6 MB/s eta 0:00:00
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
model = YOLO("yolo11n.pt")
!wget -q https://ultralytics.com/images/bus.jpg -O bus.jpg
img = cv2.imread("bus.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,7))
plt.imshow(img)
plt.axis("off")
plt.show()
!pip install ultralytics opencv-python matplotlib -q
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
model = YOLO("yolo11n.pt")
!wget -q https://ultralytics.com/images/bus.jpg -O bus.jpg
results = model("bus.jpg")
result_img = results[0].plot()
plt.figure(figsize=(10,7))
plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
print("Detected Objects:")
for box in results[0].boxes:
cls = int(box.cls[0])
conf = float(box.conf[0])
print(model.names[cls], round(conf, 2))
cv2.imwrite("detected_objects.jpg", result_img)
print("Result saved as detected_objects.jpg")
for box in results[0].boxes:
cls = int(box.cls[0])
conf = float(box.conf[0])
print(model.names[cls], round(conf, 2))
v2.imwrite("detected_objects.jpg", result_img)
print("Detection result saved successfully.")
!pip install ultralytics opencv-python matplotlib -q
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
model = YOLO("yolo11n.pt")
!wget -q https://ultralytics.com/images/bus.jpg -O bus.jpg
results = model("bus.jpg")
result_img = results[0].plot()
plt.figure(figsize=(10,7))
plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
for box in results[0].boxes:
cls = int(box.cls[0])
conf = float(box.conf[0])
print(model.names[cls], round(conf, 2))
cv2.imwrite("detected_objects.jpg", result_img)
