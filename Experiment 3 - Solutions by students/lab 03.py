import cv2 import numpy as np import
matplotlib.pyplot as plt
# Load image image =
cv2.imread("my_pic01.png")
# Convert BGR to RGB for displaying image_rgb = cv2.cvtColor(image,
cv2.COLOR_BGR2RGB)
# Display original image
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off") plt.show()
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB)) plt.title("Gaussian Blur")
plt.axis("off") plt.show()
median = cv2.medianBlur(image, 5)
plt.imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB)) plt.title("Median Filter")
plt.axis("off") plt.show()
average = cv2.blur(image, (5, 5))
plt.imshow(cv2.cvtColor(average, cv2.COLOR_BGR2RGB)) plt.title("Average Filter")
plt.axis("off") plt.show()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) laplacian =
cv2.Laplacian(gray, cv2.CV_64F)
plt.imshow(np.abs(laplacian), cmap="gray") plt.title("Laplacian Filter")
plt.axis("off") plt.show()
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3) sobel_y = cv2.Sobel(gray,
cv2.CV_64F, 0, 1, ksize=3)
plt.imshow(np.abs(sobel_x), cmap="gray") plt.title("Sobel Horizontal")
plt.axis("off") plt.show()
plt.imshow(np.abs(sobel_y), cmap="gray") plt.title("Sobel Vertical")
plt.axis("off") plt.show()
plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1) plt.imshow(image_rgb)
plt.title("Original") plt.axis("off")
plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
plt.title("Gaussian") plt.axis("off")
plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB))
plt.title("Median") plt.axis("off")
plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(average, cv2.COLOR_BGR2RGB))
plt.title("Average") plt.axis("off")
plt.subplot(2, 3, 5)
plt.imshow(np.abs(laplacian), cmap="gray")
plt.title("Laplacian") plt.axis("off")
plt.subplot(2, 3, 6)
plt.imshow(np.abs(sobel_x), cmap="gray")
plt.title("Sobel") plt.axis("off")
plt.tight_layout()
plt.show()
print("""Gaussian Filter: Reduces noise and produces smooth results while preserving important structures.
Median Filter: Effective for removing salt-and-pepper noise and preserves edges comparatively well.
Average Filter:
Provides simple smoothing but may blur edges.
Laplacian Filter:
Enhances edges and fine details.
Sobel Filter:
Detects edges in horizontal and vertical directions.""")