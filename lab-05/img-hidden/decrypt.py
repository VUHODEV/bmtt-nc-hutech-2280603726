import sys
from PIL import Image

def extract_text_from_image(encoded_image):
    """Giải mã văn bản từ ảnh"""
    img = Image.open(encoded_image)
    binary_text = ''
    
    pixels = list(img.getdata())
    for pixel in pixels:
        for color in pixel[:3]:  # Chỉ lấy RGB
            binary_text += str(color & 1)

    binary_chars = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    secret_text = ''

    for binary_char in binary_chars:
        if binary_char == '00000000':  # Dấu hiệu kết thúc
            break
        secret_text += chr(int(binary_char, 2))
    
    print(f"🔍 Văn bản ẩn: {secret_text}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Cách dùng: python decrypt.py <encoded_image>")
        sys.exit(1)

    encoded_image = sys.argv[1]
    extract_text_from_image(encoded_image)
