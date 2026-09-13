print(" --- Video Throughput Example Problem --- ")
h_res = int(input("Enter horizontal resolution: "))
v_res = int(input("Enter vertical resolution: "))
bits = int(input("Enter bits: "))
fps = int(input("Enter frames per second (FPS): "))

print("\n --- SOLUTION --- ")
frame_size = (h_res * v_res * bits)
print(f"Frame Size in bits: {frame_size:,} bits/frame")

bitrate = (frame_size * fps)
print(f"Bitrate: {bitrate:,} bits/sec")

throughput = bitrate / 10 **9 
print(f"Throughput: {throughput:.2f} Gbps") 
