import sys
from PIL import Image

def text_to_bin(text):
    """Chuyển văn bản thành chuỗi nhị phân"""
    return ''.join(format(ord(char), '08b') for char in text) + '00000000'  # Dấu hiệu kết thúc (NULL byte)

def hide_text_in_image(input_image, output_image, secret_text):
    """Ẩn văn bản vào ảnh bằng kỹ thuật LSB"""
    img = Image.open(input_image).convert("RGB")  # Chắc chắn ảnh là RGB
    binary_text = text_to_bin(secret_text)

    pixels = list(img.getdata())
    new_pixels = []
    data_index = 0

    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Chỉ chỉnh sửa R, G, B
            if data_index < len(binary_text):
                new_pixel[i] = (new_pixel[i] & 0xFE) | int(binary_text[data_index])  # Chỉnh sửa bit cuối
                data_index += 1
        new_pixels.append(tuple(new_pixel))

    # Nếu dữ liệu quá dài để nhúng vào ảnh
    if data_index >= len(binary_text):
        img.putdata(new_pixels)
        img.save(output_image)
        print(f"✅ Văn bản đã được ẩn vào ảnh và lưu tại {output_image}")
    else:
        print("❌ Ảnh không đủ không gian để giấu dữ liệu!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❌ Cách dùng: python encrypt.py <input_image> <text>")
        sys.exit(1)

    input_image = sys.argv[1]
    secret_text = sys.argv[2]
    output_image = "encoded_image.png"

    hide_text_in_image(input_image, output_image, secret_text)
