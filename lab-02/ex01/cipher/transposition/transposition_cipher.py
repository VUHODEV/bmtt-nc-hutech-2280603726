class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ""
        # Duyệt qua từng cột trong bảng mã hóa
        for col in range(key):
            pointer = col
            # Thêm ký tự vào văn bản mã hóa từ cột hiện tại
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        decrypted_text = [''] * key
        row, col = 0, 0
        # Duyệt qua từng ký tự trong văn bản mã hóa
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            # Khi đạt đến cuối cột, chuyển sang hàng tiếp theo
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1
        return ''.join(decrypted_text)