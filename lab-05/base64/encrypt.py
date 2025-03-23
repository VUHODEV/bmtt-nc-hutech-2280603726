import base64

def encode_base64(text: str) -> str:
    """Mã hóa chuỗi bằng Base64"""
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def encode_file(input_file: str):
    """Mã hóa nội dung file bằng Base64 và lưu vào data.txt"""
    with open(input_file, "rb") as file:
        encoded_data = base64.b64encode(file.read())

    with open("data.txt", "wb") as file:
        file.write(encoded_data)

if __name__ == "__main__":
    choice = input("Bạn muốn mã hóa (1) chuỗi hay (2) file? Chọn 1 hoặc 2: ")
    
    if choice == "1":
        text = input("Nhập chuỗi cần mã hóa: ")
        encoded_text = encode_base64(text)
        
        # Lưu vào file data.txt
        with open("data.txt", "w") as file:
            file.write(encoded_text)

        print("Chuỗi Base64:", encoded_text)
        print("Đã lưu vào file: data.txt")

    elif choice == "2":
        input_file = input("Nhập đường dẫn file cần mã hóa: ")
        encode_file(input_file)
        print("File đã được mã hóa và lưu vào: data.txt")
    
    else:
        print("Lựa chọn không hợp lệ!")
