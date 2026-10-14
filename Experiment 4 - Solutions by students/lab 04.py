import cv2 import numpy as np import
matplotlib.pyplot as plt
# Load grayscale image image = cv2.imread("my_pic01.png",
cv2.IMREAD_GRAYSCALE)
# Display original image plt.imshow(image,
cmap="gray") plt.title("Original Image")
plt.axis("off") plt.show()
# Compute Discrete Fourier Transform dft =
np.fft.fft2(image) print("DFT computed successfully")
# Shift zero-frequency component to the center dft_shift =
np.fft.fftshift(dft)
print("Frequency spectrum shifted successfully")
# Calculate magnitude spectrum magnitude_spectrum = 20 *
np.log(np.abs(dft_shift) + 1)
# Display spectrum plt.imshow(magnitude_spectrum,
cmap="gray") plt.title("Magnitude Spectrum")
plt.axis("off") plt.show()
rows, cols = image.shape crow, ccol = rows // 2,
cols // 2
# Create mask mask_low = np.zeros((rows, cols), np.uint8)
# Keep low frequencies around center radius = 50 cv2.circle(mask_low,
(ccol, crow), radius, 1, -1)
# Apply Low-Pass Filter low_pass = dft_shift *
mask_low
# Create High-Pass mask mask_high = np.ones((rows, cols),
np.uint8)
# Remove low frequencies from center radius = 50 cv2.circle(mask_high,
(ccol, crow), radius, 0, -1)
# Apply High-Pass Filter high_pass = dft_shift *
mask_high
# Low-pass inverse transform low_pass_shift =
np.fft.ifftshift(low_pass) low_pass_image =
np.fft.ifft2(low_pass_shift) low_pass_image =
np.abs(low_pass_image)
# High-pass inverse transform high_pass_shift =
np.fft.ifftshift(high_pass) high_pass_image =
np.fft.ifft2(high_pass_shift) high_pass_image =
np.abs(high_pass_image)
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1) plt.imshow(image, cmap="gray")
plt.title("Original Image") plt.axis("off")
plt.subplot(2, 2, 2)
plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("Frequency Spectrum") plt.axis("off")
plt.subplot(2, 2, 3)
plt.imshow(low_pass_image, cmap="gray") plt.title("Low-Pass
Filtered") plt.axis("off")
plt.subplot(2, 2, 4)
plt.imshow(high_pass_image, cmap="gray") plt.title("High-Pass Filtered")
plt.axis("off")
plt.tight_layout() plt.show()
print("""1. Original image contains both low-frequency and high-frequency components.
2. Low-pass filtering removes high-frequency components, resulting in a smoother image and
reducing noise.
3. High-pass filtering removes low-frequency components and highlights edges and fine details.
4. The frequency spectrum shows the distribution of frequency
components in the image. """)