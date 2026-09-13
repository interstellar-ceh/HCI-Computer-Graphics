from pathlib import Path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
image_path = Path(__file__).with_name("spiderman.png")
img = np.array(Image.open(image_path).convert("RGB"))

# Step factor
N = 8

# Downsample using NumPy striding
downsampled = img[::N, ::N, :]

# Re-expand using np.repeat()
expanded = np.repeat(downsampled, N, axis=0)
expanded = np.repeat(expanded, N, axis=1)

# Crop to original dimensions
expanded = expanded[:img.shape[0], :img.shape[1], :]

# Calculate dimension reduction
height_reduction = (1 - downsampled.shape[0] / img.shape[0]) * 100
width_reduction = (1 - downsampled.shape[1] / img.shape[1]) * 100

# Calculate memory savings
memory_reduction = (1 - downsampled.nbytes / img.nbytes) * 100

# Print downsampling analysis
print("--- DOWNSAMPLING ANALYSIS (N = 8) ---")
print("Original Shape :", img.shape, "| Memory:", f"{img.nbytes:,}", "bytes")
print("Downsampled Shape :", downsampled.shape, "| Memory:", f"{downsampled.nbytes:,}", "bytes")
print("Re-expanded Shape :", expanded.shape, "| Visual: Blocky Pixelation")
print("Dimension Reduction: {:.2f}% reduction per axis".format(
    (height_reduction + width_reduction) / 2
))
print("Memory Savings : {:.2f}% data reduction".format(memory_reduction))

# Display images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(downsampled)
plt.title("Downsampled (N=8)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(expanded)
plt.title("Pixelated Image")
plt.axis("off")

plt.tight_layout()
plt.show()
