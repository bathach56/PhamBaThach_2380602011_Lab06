import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.railfence_ui import Ui_MainWindow
from railfence_cipher import RailFenceCipher


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.cipher = RailFenceCipher()

        self.ui.btnEncrypt.clicked.connect(self.encrypt)
        self.ui.btnDecrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        text = self.ui.txtInput.toPlainText()
        rails = int(self.ui.txtRails.toPlainText())

        result = self.cipher.rail_fence_encrypt(text, rails)
        self.ui.txtOutput.setPlainText(result)

    def decrypt(self):
        text = self.ui.txtInput.toPlainText()
        rails = int(self.ui.txtRails.toPlainText())

        result = self.cipher.rail_fence_decrypt(text, rails)
        self.ui.txtOutput.setPlainText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
