import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QMouseEvent
from PyQt6 import QtCore

from Image import Image

class ImageDisplayApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create labels and set image paths
        self.x = None
        self.y = None
        image_path1 = "./moza1.png"
        image_path2 = "./moza2.png"

        self.label1 = QLabel(self)
        self.image = Image()
        self.image.load_img(image_path1)
        output_path1 = self.image.save_img()
        
        label2 = QLabel(self)
        self.image2 = Image()
        self.image2.load_img(image_path2)
        output_path2 = self.image2.save_img()
        # Set images to labels
        self.set_image(self.label1, output_path1)
        self.set_image(label2, output_path2)

        # Set red background color for labels
        self.label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: red;")

        # Create a vertical layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label1)
        layout.addWidget(label2)
        layout.setAlignment(self.label1, QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(label2, QtCore.Qt.AlignmentFlag.AlignCenter)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Image Display App")
        self.setGeometry(100, 100, 800, 600)

        # Variable to track mouse movement
        self.mouse_pressed = False

    def set_image(self, label, image_path):
        # Set image to the label
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def mousePressEvent(self, event: QMouseEvent):
        if (
            event.button() == QtCore.Qt.MouseButton.LeftButton
            and self.label1.geometry().contains(event.pos())
        ):
            self.mouse_pressed = True
            self.track_mouse_position(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.mouse_pressed:
            self.track_mouse_position(event)

    def track_mouse_position(self, event: QMouseEvent):
        # Track mouse position when clicking and holding on label1
        crrX, crrY = event.pos().x(), event.pos().y()
        # print(f"Mouse Position: ({crrX}, {crrY})")
        if self.x is None:
            self.x = crrX
            self.y = crrY
        else:
            if crrX - self.x > 5:
                print("Right")
            elif crrX - self.x < -5:
                print("Left")
            self.x = crrX
            if crrY - self.y > 5:
                print("Down")
            elif crrY - self.y < -5:
                print("Up")
            self.y = crrY
        # print(f"Mouse Position: ({self.x}, {self.y})")
        
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.mouse_pressed = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageDisplayApp()
    window.show()
    sys.exit(app.exec())
