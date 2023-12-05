from PyQt6 import QtCore , QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow , QLabel , QFileDialog , QWidget
from mainwindow import Ui_MainWindow
import os
import Gallery , Image , Mixer



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setupUi(self)
        # self.galary = Gallery()
        self.setupSlidersRanges(0, 100)
        # self.setupBrowseImage()
        self.firstComponentSlider_2.valueChanged.connect(self.handleFirstComponentSlider)
        self.secondComponentSlider.valueChanged.connect(self.handleSecondComponentSlider)
        self.thirdComponentSlider.valueChanged.connect(self.handleThirdComponentSlider)
        self.fourthComponentSlider.valueChanged.connect(self.handleFourthComponentSlider)
        self.imgWidget.mouseDoubleClickEvent = self.handleImgWidgetDoubleClicke
        self.imgWidget_2.mouseDoubleClickEvent = self.handleImgWidget2DoubleClicke
        self.imgWidget_3.mouseDoubleClickEvent = self.handleImgWidget3DoubleClicke
        self.imgWidget_4.mouseDoubleClickEvent = self.handleImgWidget4DoubleClicke


    # Handlers
    def handleImgWidgetDoubleClicke(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.handleBrowseImage(self.imgWidget)

    def handleImgWidget2DoubleClicke(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.handleBrowseImage(self.imgWidget_2)
    
    def handleImgWidget3DoubleClicke(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.handleBrowseImage(self.imgWidget_3)
    
    def handleImgWidget4DoubleClicke(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.handleBrowseImage(self.imgWidget_4)


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
        

    # Functions
    def handleBrowseImage(self, widget:QWidget):
        img = QFileDialog.getOpenFileName(
            self, "Open file", ".\\", "Image files (*.jpg *.png)"
        )
        if img:
            image = Image()
            

        
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
    

        
