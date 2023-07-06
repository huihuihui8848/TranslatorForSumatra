import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self, text):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 无边框窗口，始终在最前面

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)  # 设置边界的间距

        self.label = QLabel(self)
        self.label.setText(text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel { background-color: white; }")

        layout.addWidget(self.label)

        self.adjustSize()
        self.setFixedWidth(300)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.close()


def show_window_with_text(text):
    app = QApplication(sys.argv)
    window = MyWindow(text)
    window.show()
    app.exec()
