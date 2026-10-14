import cv2 import numpy as np import
matplotlib.pyplot as plt cap =
cv2.VideoCapture(0)
if not cap.isOpened():
print("Error: Camera not opened") else:
print("Camera opened successfully")
cap = cv2.VideoCapture(0)
ret1, frame1 = cap.read() ret2, frame2 = cap.read() if not ret1 or not ret2 or frame1 is
None or frame2 is None:
print("Camera frames could not be read. Check camera connection and permissions.") else:
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY) gray2 =
cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
cv2.imshow("Frame 1", gray1) cv2.imshow("Frame 2", gray2)
cv2.waitKey(0)
cap.release() cv2.destroyAllWindows()
import cv2 import numpy as np cap
= cv2.VideoCapture(0)
ret, old_frame = cap.read() old_gray = cv2.cvtColor(old_frame,
cv2.COLOR_BGR2GRAY)
# Feature points select karna p0 =
cv2.goodFeaturesToTrack( old_gray,
maxCorners=100, qualityLevel=0.3,
minDistance=7
)
ret, frame = cap.read() frame_gray = cv2.cvtColor(frame,
cv2.COLOR_BGR2GRAY)
# Lucas-Kanade Optical Flow p1, status, error =
cv2.calcOpticalFlowPyrLK( old_gray, frame_gray, p0,
None
)
print("Original points:") print(p0)
print("New points:") print(p1)
cap.release()
import cv2 import numpy as np cap =
cv2.VideoCapture(0) ret, old_frame =
cap.read() if not ret or old_frame is None:
cap.release()
raise RuntimeError("Camera frame could not be read. Check camera connection and permissions.")
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack( old_gray,
maxCorners=100, qualityLevel=0.3,
minDistance=7
)
if p0 is None:
cap.release()
raise RuntimeError("No trackable features found in the first camera frame.") while True:
ret, frame = cap.read()
if not ret or frame is None:
break
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
p1, status, error = cv2.calcOpticalFlowPyrLK( old_gray, gray, p0,
None
)
if p1 is not None and status is not None:
good_new = p1[status == 1] good_old = p0[status == 1]
for new, old in zip(good_new, good_old):
x1, y1 = new.ravel() x2, y2 =
old.ravel()
x1, y1 = int(x1), int(y1) x2, y2 = int(x2),
int(y2)
cv2.arrowedLine( frame,
(x2, y2),
(x1, y1),
(0, 255, 0),
2
)
if len(good_new) == 0:
break
p0 = good_new.reshape(-1, 1, 2)
old_gray = gray.copy()
cv2.imshow("Motion Vectors", frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
break
cap.release() cv2.destroyAllWindows()
import cv2
cap = cv2.VideoCapture(0)
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
flow = cv2.calcOpticalFlowFarneback( old_gray,
gray, None,
0.5,
3,
15,
3,
5,
1.2,
0
)
print("Dense Optical Flow calculated") print("Flow shape:",
flow.shape) cap.release()
import cv2 import numpy as np cap
= cv2.VideoCapture(0)
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY) while True: ret,
frame = cap.read() if not ret:
break
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY
# Farneback flow = cv2.calcOpticalFlowFarneback(
old_gray, gray, None,
0.5,
3,
15,
3,
5,
1.2,
0
)
magnitude, angle = cv2.cartToPolar( flow[..., 0],
flow[..., 1]
) hsv = np.zeros_like(frame) hsv[..., 1]
= 255
# Direction hsv[..., 0] = angle * 180 / np.pi / 2
# Magnitude hsv[..., 2] = cv2.normalize(
magnitude, None,
0,
255,
cv2.NORM_MINMAX
)
output = cv2.cvtColor( hsv,
cv2.COLOR_HSV2BGR
cv2.imshow(
"Farneback Dense Optical Flow",
output
) old_gray = gray.copy()
if cv2.waitKey(1) & 0xFF == ord('q'):
break
cap.release() cv2.destroyAllWindows()
import cv2 import
time
cap = cv2.VideoCapture(0)
ret, frame1 = cap.read() ret, frame2 =
cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY) gray2 =
cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
# Lucas-Kanade start =
time.time()
p0 = cv2.goodFeaturesToTrack( gray1,
maxCorners=100, qualityLevel=0.3,
minDistance=7
)
p1, status, error = cv2.calcOpticalFlowPyrLK( gray1, gray2, p0,
None
)
lk_time = time.time() - start
# Farneback start =
time.time()
flow = cv2.calcOpticalFlowFarneback( gray1, gray2,
None,
0.5,
3,
15,
3,
5,
1.2,
0
) farneback_time = time.time() - start
print("Lucas-Kanade Time:", lk_time) print("Farneback
Time:", farneback_time) cap.release()
import cv2
cap = cv2.VideoCapture(0) while True:
ret, frame = cap.read() if not ret:
break
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Brightness check brightness =
gray.mean()
print("Average Brightness:", brightness) cv2.imshow("Video",
frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
break
cap.release() cv2.destroyAllWindows()
import cv2
cap = cv2.VideoCapture(0) tracker =
cv2.TrackerCSRT_create() ret, frame = cap.read()
# Object select karo bbox =
cv2.selectROI( "Select Object",
frame,
False
) tracker.init(frame, bbox) while True:
ret, frame = cap.read() if not ret:
break
success, bbox = tracker.update(frame)
if success:
x, y, w, h = map(int, bbox)
cv2.rectangle( frame,
(x, y),
(x + w, y + h),
(0, 255, 0),
2
)
cv2.putText( frame,
"Object Tracking",
(x, y - 10),
cv2.FONT_HERSHEY_SIMPLEX,
0.7,
(0, 255, 0),
2
)
cv2.imshow(
"Surveillance / Object Tracking",
frame
)
if cv2.waitKey(1) & 0xFF == ord('q'):
break
cap.release() cv2.destroyAllWindows()
print("OBSERVATIONS")
print("-----------------------------")
print("1. Lucas-Kanade performs sparse optical flow.")
print("2. It tracks selected feature points.") print("3. Farneback performs dense optical flow.")
print("4. Farneback estimates motion across the image.") print("5. Object speed affects
optical-flow accuracy.") print("6. Lighting changes can affect motion estimation.") print("7.
Camera movement produces additional motion.") print("8. Optical flow is useful for tracking
and surveillance.")