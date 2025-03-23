import base64

def decode_base64(encoded_text: str) -> str:
    """Giải mã Base64 về chuỗi gốc"""
    decoded_bytes = base64.b64decode(encoded_text)
    return decoded_bytes.decode("utf-8")

def decode_file(input_file: str, output_file: str):
    """Giải mã nội dung file Base64 về dữ liệu gốc"""
    with open(input_file, "rb") as file:
        decoded_data = base64.b64decode(file.read())

    with open(output_file, "wb") as file:
        file.write(decoded_data)

if __name__ == "__main__":
    choice = input("Bạn muốn giải mã click (1): ")

    if choice == "1":
        # Đọc chuỗi từ data.txt
        try:
            with open("data.txt", "r") as file:
                encoded_text = file.read().strip()

            decoded_text = decode_base64(encoded_text)
            print("Chuỗi gốc:", decoded_text)
        except Exception:
            print("Lỗi: Không thể giải mã hoặc file data.txt trống!")

    elif choice == "2":
        output_file = input("Nhập đường dẫn file output: ")
        try:
            decode_file("data.txt", output_file)
            print(f"File đã được giải mã và lưu tại: {output_file}")
        except Exception:
            print("Lỗi: Không thể giải mã file!")

    else:
        print("Lựa chọn không hợp lệ!")
