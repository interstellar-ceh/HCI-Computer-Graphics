import numpy as np

img = np.zeros((300,400,3), dtype=np.uint8)
img[0:150, 0:200] = [255, 0, 0] # Top left
img[0:150, 200:400] = [0, 255, 0] # Top right

img[150:300, 0:200] = [0, 0, 255] # Bottom left
img[150:300, 200:400] = [255, 255, 255] # Bottom right

print("Program initialization (No file input required — synthetic matrix generation)")

print("--- SYNTHETIC MATRIX METRICS ---")
print("Array Shape (H, W, C) : ", img.shape)
print("Data Type : ", img.dtype)
print(f"Total Elements :  {img.size:,} values")

kb = img.nbytes / 1024
print(f"Memory Footprint : {img.nbytes:,} bytes ({kb:.2f} KB)")
