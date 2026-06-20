import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa_cipher import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối các nút với hàm xử lý, sử dụng tên đúng từ file rsa_cipher.py
        self.ui.btn_gen_key.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Success", data.get("message", "Keys generated"))
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plaintext.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_ciphertext.setPlainText(data.get("encrypted_message", ""))
                QMessageBox.information(self, "Success", "Encrypted Successfully")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txt_ciphertext.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plaintext.setPlainText(data.get("decrypted_message", ""))
                QMessageBox.information(self, "Success", "Decrypted Successfully")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_info.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setPlainText(data.get("signature", ""))
                QMessageBox.information(self, "Success", "Signed Successfully")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data.get("is_verified"):
                    QMessageBox.information(self, "Result", "Verified Successfully")
                else:
                    QMessageBox.warning(self, "Result", "Verified Fail")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())