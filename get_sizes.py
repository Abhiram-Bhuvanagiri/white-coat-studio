import subprocess
import struct
import io

def get_jpeg_size_from_bytes(data):
    try:
        f = io.BytesIO(data)
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

def get_old_size(path):
    res = subprocess.run(['git', 'show', f'HEAD:{path}'], capture_output=True)
    if res.returncode == 0:
        return get_jpeg_size_from_bytes(res.stdout)
    return "Not found"

print("about-1:", get_old_size('assets/images/about-page/about-1.jpg'))
print("about-2:", get_old_size('assets/images/about-page/about-2.jpg'))
print("commitment:", get_old_size('assets/images/about-page/commitment.jpg'))
