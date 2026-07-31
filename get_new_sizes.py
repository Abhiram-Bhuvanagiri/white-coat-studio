import struct
import io
import os

def get_jpeg_size(file_path):
    if not os.path.exists(file_path): return "File not found"
    try:
        with open(file_path, 'rb') as f:
            f.read(2)
            while True:
                marker_data = f.read(2)
                if not marker_data: break
                marker, = struct.unpack(">H", marker_data)
                if marker == 0xFFD8:
                    continue
                elif marker == 0xFFC0 or marker == 0xFFC2:
                    f.read(3)
                    h, w = struct.unpack(">HH", f.read(4))
                    return w, h
                else:
                    length, = struct.unpack(">H", f.read(2))
                    f.read(length - 2)
    except Exception as e:
        return str(e)
    return None

images = [
    "services.jpg", "adv-1.jpg", "adv-2.jpg", "discovery.jpg", 
    "design.jpg", "launch.jpg", "data-driven-opt.jpg", "market.jpg"
]

for img in images:
    path = f'assets/images/Services/{img}'
    print(f"{img}: {get_jpeg_size(path)}")
