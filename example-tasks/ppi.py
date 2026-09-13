import math

print(" --- CALCULATING PPI --- ")
screen_size = float(input("Enter screen size: "))
h_res = int(input("Enter horizontal Resolution: "))
v_res = int(input("Enter vertical Resolution: "))

dp = math.sqrt(h_res ** 2 + v_res **2)
print(f"Diagonal Pixel Count is: {dp:.2f} px")

ppi = int(dp/screen_size)

print(f"The display renders approximately {ppi} pixels per linear inch.")
