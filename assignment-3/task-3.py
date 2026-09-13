# Task 1: Display Pixel Density (PPI/DPI) Calculator

import math

horizontal_res = int(input("Enter horizontal resolution (pixels): "))
vertical_res = int(input("Enter vertical resolution (pixels): "))
diagonal_size = int(input("Enter physical diagonal size (inches): "))

total_pixel = (horizontal_res * vertical_res)
gcd = math.gcd(horizontal_res, vertical_res)
aspect_ratio = f"{horizontal_res // gcd}:{vertical_res // gcd}"

# Calculating diagonal pixels by pythogoras theorem
diagonal_pixels = math.sqrt(horizontal_res**2 + vertical_res**2)

dpi = round(diagonal_pixels/diagonal_size, 2)

print("--- DISPLAY METRICS ANALYSIS ---")
print(f"Total Pixel Count : {total_pixel:,} pixels")
print(f"Aspect Ratio :  {aspect_ratio}")
print("Calculated DPI : ", dpi)

if dpi < 100:
    print("Density Category : Low Density (Standard Monitor)")
elif ( 100 <= dpi <= 200 ):
    print("Density Category : Medium Density (HD Display)")
elif dpi > 200:
    print("Density Category : High Density (Retina / Mobile)")
else:
    print("Invalid DPI")
