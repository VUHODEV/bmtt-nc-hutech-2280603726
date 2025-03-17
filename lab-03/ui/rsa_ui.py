import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import requests

# Thêm đường dẫn tới thư mục chứa UI
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from rsa import Ui_MainWindow

class RSAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối các nút với hàm xử lý
        self.ui.btn_gen_keys.clicked.connect(self.generate_keys)
        self.ui.btn_encrypt.clicked.connect(self.encrypt)
        self.ui.btn_decrypt.clicked.connect(self.decrypt)
        self.ui.btn_sign.clicked.connect(self.sign)
        self.ui.btn_verify.clicked.connect(self.verify)

    def generate_keys(self):
        try:
            response = requests.get('http://127.0.0.1:5000/api/rsa/generate_keys')
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Keys generated successfully!")
            else:
                QMessageBox.warning(self, "Error", "Failed to generate keys")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def encrypt(self):
        try:
            data = {
                "message": self.ui.txt_plain_text.toPlainText(),
                "key_type": "public"
            }
            response = requests.post('http://127.0.0.1:5000/api/rsa/encrypt', json=data)
            if response.status_code == 200:
                self.ui.txt_cipher_text.setPlainText(response.json()["encrypted_message"])
                QMessageBox.information(self, "Success", "Message encrypted successfully!")
            else:
                QMessageBox.warning(self, "Error", "Failed to encrypt message")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def decrypt(self):
        try:
            data = {
                "ciphertext": self.ui.txt_cipher_text.toPlainText(),
                "key_type": "private"
            }
            response = requests.post('http://127.0.0.1:5000/api/rsa/decrypt', json=data)
            if response.status_code == 200:
                self.ui.txt_plain_text.setPlainText(response.json()["decrypted_message"])
                QMessageBox.information(self, "Success", "Message decrypted successfully!")
            else:
                QMessageBox.warning(self, "Error", "Failed to decrypt message")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def sign(self):
        try:
            data = {
                "message": self.ui.txt_info.toPlainText()
            }
            response = requests.post('http://127.0.0.1:5000/api/rsa/sign', json=data)
            if response.status_code == 200:
                self.ui.txt_sign.setPlainText(response.json()["signature"])
                QMessageBox.information(self, "Success", "Message signed successfully!")
            else:
                QMessageBox.warning(self, "Error", "Failed to sign message")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def verify(self):
        try:
            data = {
                "message": self.ui.txt_info.toPlainText(),
                "signature": self.ui.txt_sign.toPlainText()
            }
            response = requests.post('http://127.0.0.1:5000/api/rsa/verify', json=data)
            if response.status_code == 200:
                is_verified = response.json()["is_verified"]
                if is_verified:
                    QMessageBox.information(self, "Success", "Signature is valid!")
                else:
                    QMessageBox.warning(self, "Warning", "Signature is invalid!")
            else:
                QMessageBox.warning(self, "Error", "Failed to verify signature")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

def main():
    app = QApplication(sys.argv)
    window = RSAWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 