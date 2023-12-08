from PyQt6 import QtCore , QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow , QLabel , QFileDialog , QWidget , QVBoxLayout , QHBoxLayout
from mainwindow import Ui_MainWindow
import os
import Gallery , Image , Mixer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QScreen, QPixmap
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pyqtgraph as pg
import cv2
import logging

# Logging

logging.basicConfig(filename='mainLog.log', filemode='w',level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')




x_start, y_start, x_end, y_end = 0, 0, 0, 0
cropping = False

class MainWindow(QMainWindow, Ui_MainWindow):
    image = None
    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setupUi(self)
        self.oriImage = None
        self.galary = Gallery.Gallery()
        self.setupSlidersRanges(0, 100)
    
        # Sliders
        self.firstComponentSlider_2.valueChanged.connect(self.handleFirstComponentSlider)
        self.secondComponentSlider.valueChanged.connect(self.handleSecondComponentSlider)
        self.thirdComponentSlider.valueChanged.connect(self.handleThirdComponentSlider)
        self.fourthComponentSlider.valueChanged.connect(self.handleFourthComponentSlider)


        # Browsing Images
        self.imgWidget.mouseDoubleClickEvent = self.handleImgWidgetDoubleClicke
        self.imgWidget_2.mouseDoubleClickEvent = self.handleImgWidget2DoubleClicke
        self.imgWidget_3.mouseDoubleClickEvent = self.handleImgWidget3DoubleClicke
        self.imgWidget_4.mouseDoubleClickEvent = self.handleImgWidget4DoubleClicke


        # Cropping
        self.firstPushBtn.clicked.connect(lambda: self.handleCropBtn('./imgs/1.png'))
        self.secondPushBtn.clicked.connect(lambda: self.handleCropBtn('./imgs/1.png'))
        self.thirdPushBtn.clicked.connect(lambda: self.handleCropBtn('./imgs/1.png'))
        self.fourthPushBtn.clicked.connect(lambda: self.handleCropBtn('./imgs/1.png'))


    # Handlers
    def handleImgWidgetDoubleClicke(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.handleBrowseImage(self.imgWidget , self.transWidget)

    def handleImgWidget2DoubleClicke(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.handleBrowseImage(self.imgWidget_2)
    
    def handleImgWidget3DoubleClicke(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.handleBrowseImage(self.imgWidget_3)
    
    def handleImgWidget4DoubleClicke(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.handleBrowseImage(self.imgWidget_4)

    def handleBrowseImage(self, widget1:QWidget , widget2 : QWidget):  
        img = QFileDialog.getOpenFileName(
            self, "Open file", ".\\", "Image files (*.jpg *.png)"
        )
        if img:
            image = Image.Image()
            imagePath = img[0].strip().split("/")[-1]
            image.load_img(imagePath, show=True)
            image.compute_fourier_transform()   
            graph = pg.image(image.get_img())
            layout = QHBoxLayout()
            widget1.setLayout(layout)
            widget1.layout().addWidget(graph)
            layout2 = QHBoxLayout()
            widget2.setLayout(layout2)
            # TODO: show the components in the second widget


    def handleCropBtn(self,path):
        image = cv2.imread(path)
        self.oriImage = image.copy()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.mouseCrop)
        i = image.copy()
        if not cropping:
            cv2.imshow("image", image)
        elif cropping:
            cv2.rectangle(i, (self.x_start, self.y_start), (self.x_end, self.y_end), (255, 0, 0), 2)
            cv2.imshow("image", i)
        cv2.waitKey(1)

    def mouseCrop(self, event, x, y, flags, param):
        global x_start, y_start, x_end, y_end , cropping

        if event == cv2.EVENT_LBUTTONDOWN:
            x_start, y_start, x_end, y_end = x, y, x, y
            cropping = True

        elif event == cv2.EVENT_MOUSEMOVE:
            if cropping == True:
                x_end, y_end = x, y

        elif event == cv2.EVENT_LBUTTONUP:
            x_end, y_end = x, y
            cropping = False

            refPoint = [(x_start, y_start), (x_end, y_end)]

            if len(refPoint) == 2:
                roi = self.oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
                # save the cropped image to disk
                cv2.imwrite("cropped.png", roi)
                # Close the window
                cv2.destroyAllWindows()

                # TODO: show the cropped image in the image widget






    def handleFirstComponentSlider(self, value):
        self.firstComponentLabel_2.setText(str(value) + "%")
    
    def handleSecondComponentSlider(self, value):
        self.secondComponentLabel.setText(str(value) + "%")
    
    def handleThirdComponentSlider(self, value):
        self.thirdComponentLabel.setText(str(value) + "%")
    
    def handleFourthComponentSlider(self, value):
        self.fourthComponentLabel.setText(str(value) + "%")

    def handleImageWidgetDoubleClick(self , event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.handleBrowseImage(self.imgWidget)
        
        
    # Setups
    def setupSlidersRanges(self, min, max):
        self.brightnessSlider.setMinimum(min)
        self.brightnessSlider.setMaximum(max)
        self.contrastSlider.setMinimum(min)
        self.contrastSlider.setMaximum(max)
        self.brightnessSlider_2.setMinimum(min)
        self.brightnessSlider_2.setMaximum(max)
        self.contrastSlider_2.setMinimum(min)
        self.contrastSlider_2.setMaximum(max)
        self.brightnessSlider_3.setMinimum(min)
        self.brightnessSlider_3.setMaximum(max)
        self.contrastSlider_3.setMinimum(min)
        self.contrastSlider_3.setMaximum(max)
        self.brightnessSlider_4.setMinimum(min)
        self.brightnessSlider_4.setMaximum(max)
        self.contrastSlider_4.setMinimum(min)
        self.contrastSlider_4.setMaximum(max)
        self.firstComponentSlider_2.setMinimum(min)
        self.firstComponentSlider_2.setMaximum(max)
        self.secondComponentSlider.setMinimum(min)
        self.secondComponentSlider.setMaximum(max)
        self.thirdComponentSlider.setMinimum(min)
        self.thirdComponentSlider.setMaximum(max)
        self.fourthComponentSlider.setMinimum(min)
        self.fourthComponentSlider.setMaximum(max)



def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
    

        
