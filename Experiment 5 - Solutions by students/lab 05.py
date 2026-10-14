import cv2 import numpy as np import
matplotlib.pyplot as plt
from skimage.feature import hog from skimage
import exposure
filename = "my_pic01.png" img =
cv2.imread(filename)
filename = "my_pic01.png" img =
cv2.imread(filename)
# Convert BGR to RGB img_rgb = cv2.cvtColor(img,
cv2.COLOR_BGR2RGB)
# Convert to grayscale gray = cv2.cvtColor(img,
cv2.COLOR_BGR2GRAY)
print("Image loaded successfully!") print("Image shape:",
img.shape)
plt.figure(figsize=(6, 4))
plt.imshow(img_rgb) plt.title("Original
Image") plt.axis("off") plt.show()
# Create SIFT detector sift =
cv2.SIFT_create()
# Detect keypoints and compute descriptors keypoints, descriptors =
sift.detectAndCompute(gray, None)
print("Number of keypoints:", len(keypoints)) print("Descriptor shape:",
descriptors.shape)
# Create SIFT detector sift =
cv2.SIFT_create()
# Detect keypoints keypoints, descriptors = sift.detectAndCompute(gray, None)
print("Number of keypoints:", len(keypoints)
# Draw SIFT keypoints on image
sift_image = cv2.drawKeypoints( img_rgb,
keypoints,
None,
flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
) plt.figure(figsize=(8, 6))
plt.imshow(sift_image) plt.title("SIFT
Keypoints") plt.axis("off") plt.show()
# HOG parameters orientations = 9
pixels_per_cell = (8, 8)
cells_per_block = (2, 2)
# Extract HOG features hog_features,
hog_image = hog( gray,
orientations=orientations,
pixels_per_cell=pixels_per_cell,
cells_per_block=cells_per_block,
block_norm='L2-Hys', visualize=True
)
print("HOG feature length:", len(hog_features))
# Improve HOG visualization hog_image_rescaled =
exposure.rescale_intensity( hog_image, in_range=(0, 10)
) plt.figure(figsize=(8, 6))
plt.imshow(hog_image_rescaled, cmap='gray') plt.title("HOG
Descriptor Visualization") plt.axis("off") plt.show()
print("========== SIFT ==========") print("Number of Keypoints:",
len(keypoints)) print("Descriptor Dimension:", descriptors.shape[1])
print("\n========== HOG ==========")
print("Number of HOG Features:", len(hog_features))
print("Orientations:", orientations) print("Pixels per Cell:",
pixels_per_cell) print("Cells per Block:", cells_per_block)
# Create second similar image img2 = cv2.resize(img_rgb, None,
fx=0.8, fy=0.8) gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
sift2 = cv2.SIFT_create()
keypoints2, descriptors2 = sift2.detectAndCompute(gray2, None)
print("Image 1 keypoints:", len(keypoints)) print("Image 2 keypoints:",
len(keypoints2))
# Match SIFT descriptors bf =
cv2.BFMatcher()
matches = bf.knnMatch(descriptors, descriptors2, k=2) good_matches = []
for m, n in matches:
if m.distance < 0.75 * n.distance: good_matches.append(m)
print("Total matches:", len(matches)) print("Good matches:",
len(good_matches))
# Create a second similar image img2 =
cv2.resize( img_rgb, None, fx=0.8, fy=0.8
) gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
# Create SIFT detector sift2 =
cv2.SIFT_create()
# Detect keypoints and descriptors keypoints2, descriptors2 =
sift2.detectAndCompute(gray2, None) print("Image 1 keypoints:", len(keypoints))
print("Image 2 keypoints:", len(keypoints2))
# Create BFMatcher bf =
cv2.BFMatcher()
# KNN matching matches = bf.knnMatch(descriptors, descriptors2, k=2)
# Apply Lowe's ratio test good_matches = []
for m, n in matches:
if m.distance < 0.75 * n.distance: good_matches.append(m)
print("Total matches:", len(matches)) print("Good matches:",
len(good_matches))
# Draw good matches match_image =
cv2.drawMatches( img_rgb, keypoints,
img2, keypoints2, good_matches[:50],
None,
flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
) plt.figure(figsize=(14, 7))
plt.imshow(match_image) plt.title("SIFT
Image Matching") plt.axis("off") plt.show()
print("========== EVALUATION ==========")
print("\nSIFT:")
print("- Detects local keypoints")
print("- Provides 128-dimensional descriptors") print("- Robust to scale and
rotation changes")
print("- Useful for image matching and object recognition")
print("\nHOG:")
print("- Represents image using gradient orientations")
print("- Captures shape and edge information") print("- Computationally
simpler than SIFT")
print("- Useful for object detection and shape analysis")plt.figure(figsize=(14, 10))
# Original plt.subplot(2, 3, 1)
plt.imshow(img_rgb) plt.title("Original
Image") plt.axis("off")
# Grayscale plt.subplot(2, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale") plt.axis("off")
# SIFT plt.subplot(2, 3, 3)
plt.imshow(sift_image) plt.title("SIFT
Keypoints") plt.axis("off")
# HOG plt.subplot(2, 3, 4)
plt.imshow(hog_image_rescaled, cmap="gray") plt.title("HOG
Features") plt.axis("off")
# Second image
plt.subplot(2, 3, 5)
plt.imshow(img2)
plt.title("Similar Image")
plt.axis("off")
# Matches plt.subplot(2, 3, 6)
plt.imshow(match_image)
plt.title("SIFT Matching")
plt.axis("off")
plt.tight_layout() plt.show()