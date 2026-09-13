from pathlib import Path

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
image_path = Path(__file__).with_name("spiderm-converted.png")
img = np.array(Image.open(image_path).convert("RGB"))

# Extract individual channels
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

# Create three separate 3D color arrays
red_only = np.zeros_like(img)
green_only = np.zeros_like(img)
blue_only = np.zeros_like(img)

# Keep only one channel active
red_only[:, :, 0] = red
green_only[:, :, 1] = green
blue_only[:, :, 2] = blue

# Print channel extraction summary
print("--- CHANNEL EXTRACTION SUMMARY ---")
print("Original Image Shape :", img.shape)
print("Red Channel 2D Shape :", red.shape, "| Mean Intensity:", round(np.mean(red), 2))
print("Green Channel 2D Shape:", green.shape, "| Mean Intensity:", round(np.mean(green), 2))
print("Blue Channel 2D Shape :", blue.shape, "| Mean Intensity:", round(np.mean(blue), 2))
print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")

# Create 2x3 subplot
plt.figure(figsize=(12, 8))

# Top row - color isolated images
plt.subplot(2, 3, 1)
plt.imshow(red_only)
plt.title("Red-Only")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(green_only)
plt.title("Green-Only")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(blue_only)
plt.title("Blue-Only")
plt.axis("off")

# Bottom row - grayscale intensity maps
plt.subplot(2, 3, 4)
plt.imshow(red, cmap="gray")
plt.title("Red Intensity")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(green, cmap="gray")
plt.title("Green Intensity")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(blue, cmap="gray")
plt.title("Blue Intensity")
plt.axis("off")

plt.tight_layout()
plt.show()
