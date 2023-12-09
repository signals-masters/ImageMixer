from math import comb
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

modes = ['Real', 'Imaginary', 'Magnitude', 'Phase']

class MainWindow(QMainWindow, Ui_MainWindow):
    image = None
    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setupUi(self)
        self.oriImage = None
        self.gallery = Gallery.Gallery()
        self.totalOfComponents = 100
        self.remainderOfComponents = 100
        self.currentSumOfComponents = 0

        # Browsing Images
        self.imageWidgets = [self.imageOneWidget, self.imageTwoWidget, self.imageThreeWidget, self.imageFourWidget]
        self.transWidgets = [self.imageOneComponentWidget, self.imageTwoComponentWidget, self.imageThreeComponentWidget, self.imageFourComponentWidget]
        self.componentSliders = [self.componentOneRatioSlider, self.componentTwoRatioSlider, self.componentThreeRatioSlider, self.componentFourRatioSlider]
        self.componentValueLabels = [self.componentOneRatioLabel, self.componentTwoRatioLabel, self.componentThreeRatioLabel, self.componentFourRatioLabel]
        self.sliderValues = [0, 0, 0, 0]
        self.imageModesCombobox = [self.imageOneModeSelect, self.imageTwoModeSelect, self.imageThreeModeSelect, self.imageFourModeSelect]
        self.realRadioButtons = [self.componentOneRealRadio, self.componentTwoRealRadio, self.componentThreeRealRadio, self.componentFourRealRadio]

        self.imaginaryRadioButtons = [self.componentOneImaginaryRadio, self.componentTwoImaginaryRadio, self.componentThreeImaginaryRadio, self.componentFourImaginaryRadio]
        self.magnitudeRadioButtons = [self.componentOneMagnitudeRadio, self.componentTwoMagnitudeRadio, self.componentThreeMagnitudeRadio, self.componentFourMagnitudeRadio]
        self.phaseRadioButtons = [self.componentOnePhaseRadio, self.componentTwoPhaseRadio, self.componentThreePhaseRadio, self.componentFourPhaseRadio]
        self.radioButtons = [self.realRadioButtons, self.imaginaryRadioButtons, self.magnitudeRadioButtons, self.phaseRadioButtons]
        self.componentsImagesSelect = [self.componentOneImageSelect, self.componentTwoImageSelect, self.componentThreeImageSelect, self.componentFourImageSelect]

        self.componentsTypes = ['', '', '', '']
        self.componentsIds = [0, 0, 0, 0]
        self.currentOutput = 0

        self.mixerModeSelect.currentIndexChanged.connect(self.handleMixerModeChange)

        for i, widget in enumerate(self.imageWidgets):
            layout = QHBoxLayout()
            widget.setLayout(layout)
            widget.mouseDoubleClickEvent = lambda event, i=i: self.handleUploadImage(event, i)
        
        for i, widget in enumerate(self.transWidgets):
            layout = QHBoxLayout()
            widget.setLayout(layout)

        for i, combobox in enumerate(self.componentsImagesSelect):
            combobox.currentIndexChanged.connect(lambda index, i=i: self.handleImageChange(index, i))            
        
        for i, slider in enumerate(self.componentSliders):
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setEnabled(False)
            # slider.valueChanged.connect(lambda value, i=i: self.handleComponentSlider(value, i))

        self.convertButton.clicked.connect(self.handleConvertBtn)

        for i, combobox in enumerate(self.imageModesCombobox):
            combobox.clear()
            for mode in modes:
                combobox.addItem(mode)
            combobox.setEnabled(False)
            combobox.currentIndexChanged.connect(lambda index, i=i: self.handleImageModeChange(index, i))

        for index, radioButtons in enumerate(self.radioButtons):
            for i, radioButton in enumerate(radioButtons):
                if index > 1:
                    radioButton.setEnabled(False)
                radioButton.toggled.connect(lambda checked, i=i, index=index: self.handleRadioButton(checked, i, index))
        
        for i , slider in enumerate(self.componentSliders):
            slider.valueChanged.connect(lambda value, i=i: self.handleSlider(value, i))


        # Cropping
        # self.firstPushBtn.clicked.connect(lambda: self.handleCropBtn('./imgs/1.png'))
        # self.secondPushBtn.clicked.connect(lambda: self.handleCropBtn('./imgs/1.png'))
        # self.thirdPushBtn.clicked.connect(lambda: self.handleCropBtn('./imgs/1.png'))
        # self.fourthPushBtn.clicked.connect(lambda: self.handleCropBtn('./imgs/1.png'))

    def handleImageChange(self, index, i):
        print(index)
        print(i)
        self.componentsIds[i] = index
        print(self.componentsIds)

    def handleMixerModeChange(self, index):
        for slider in self.componentSliders:
            slider.setEnabled(False)
            slider.setValue(0)

        if index == 0:
            for radioButtons in self.radioButtons[0:2]:
                for radioButton in radioButtons:
                    radioButton.setEnabled(True)
                    radioButton.setCheckable(True)

            for radioButtons in self.radioButtons[2:]:
                for radioButton in radioButtons:
                    radioButton.setEnabled(False)
                    radioButton.setCheckable(False)
        else:
            for radioButtons in self.radioButtons[2:]:
                for radioButton in radioButtons:
                    radioButton.setEnabled(True)
                    radioButton.setCheckable(True)

            for radioButtons in self.radioButtons[0:2]:
                for radioButton in radioButtons:
                    radioButton.setEnabled(False)
                    radioButton.setCheckable(False)
        self.componentsTypes = ['', '', '', '']

    def handleRadioButton(self, checked, index, mode):
        if checked:
            self.componentSliders[index].setEnabled(True)
            self.componentsTypes[index] = modes[mode].lower()
        else:
            self.componentSliders[index].setEnabled(False)
            self.componentsTypes[index] = ''

    def handleUploadImage(self, event, index):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.handleBrowseImage(index)
    
    # Sliders Function
    def sumSlidersValues(self):
        return sum(self.sliderValues)
    
    def handleSlider(self, value, index):
        # logging.info(f'handleSlider: value: {value} , Index: {index}')
        # logging.info(f'handleSlider: Sliders Values: {self.sliderValues}')
        # logging.info(f'handleSlider: Current: {self.currentSumOfComponents}')
        # logging.info(f'handleSlider: Total: {self.totalOfComponents}')
        # logging.info(f'handleSlider: Remainder: {self.remainderOfComponents}')
        # logging.info('-------------------------------------------------------------')
        if self.currentSumOfComponents - self.sliderValues[index] + value <= self.totalOfComponents:
            self.sliderValues[index] = value
            self.currentSumOfComponents = self.sumSlidersValues()
            self.remainderOfComponents = self.totalOfComponents - self.currentSumOfComponents
            self.componentValueLabels[index].setText(str(value) + "%")
            self.componentSliders[index].setValue(value)
        else:
            self.sliderValues[index] += self.remainderOfComponents
            self.currentSumOfComponents = self.sumSlidersValues()
            self.remainderOfComponents = self.totalOfComponents - self.currentSumOfComponents
            self.componentValueLabels[index].setText(str(self.sliderValues[index]) + "%")
        
        # logging.info(f'handleSlider: Sliders Values: {self.sliderValues}')
        # logging.info(f'handleSlider: Current: {self.currentSumOfComponents}')
        # logging.info(f'handleSlider: Total: {self.totalOfComponents}')
        # logging.info(f'handleSlider: Remainder: {self.remainderOfComponents}')
        # logging.info('===============================================================')


    def handleImageModeChange(self, index, i):
        mode = modes[index]

        image = self.gallery.get_gallery()[i]

        layout = self.transWidgets[i].layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if mode == 'Magnitude':
            graph = pg.image(image.get_mag())
            self.transWidgets[i].layout().addWidget(graph)
        elif mode == 'Phase':
            graph = pg.image(image.get_phase())
            self.transWidgets[i].layout().addWidget(graph)
        elif mode == 'Real':
            graph = pg.image(image.get_real())
            self.transWidgets[i].layout().addWidget(graph)
        elif mode == 'Imaginary':
            graph = pg.image(image.get_imaginary())
            self.transWidgets[i].layout().addWidget(graph)

    def handleBrowseImage(self, index):
        img = QFileDialog.getOpenFileName(
            self, "Open file", ".\\", "Image files (*.jpg *.png)"
        )
        if img:
            image = Image.Image()
            imagePath = img[0].strip().split("/")[-1]
            image.load_img(imagePath, show=True)
            image.compute_fourier_transform()
            graph = pg.image(image.get_img())
            widget1 = self.imageWidgets[index]
            widget2 = self.transWidgets[index]
            
            layout = widget1.layout()
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            widget1.layout().addWidget(graph)
            
            layout2 = widget2.layout()
            while layout2.count():
                child = layout2.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            magGraph = pg.image(image.get_mag())
            widget2.layout().addWidget(magGraph)

            self.imageModesCombobox[index].setEnabled(True)
            self.imageModesCombobox[index].setCurrentIndex(0)
            # TODO: Add the image to gallery
            self.gallery.add_image(image, index)

            # TODO: Call reshape_all with a list of images in gallery
            Image.Image.reshape_all(self.gallery.get_gallery().values())

    def handleConvertBtn(self):
        currentMixer = Mixer.Mixer(0.5, 0.5, 1, 0, self.componentsIds[0], self.componentsIds[1], self.componentsIds[2], self.componentsIds[3], self.componentsTypes[0], self.componentsTypes[1], self.componentsTypes[2], self.componentsTypes[3])
        output = currentMixer.inverse_fft(self.gallery.get_gallery()).T
        
        print(output)
        layout = QHBoxLayout()
        self.outputOneWidget.setLayout(layout)
        currentOutput = pg.image(output)
        print(currentOutput)
        self.outputOneWidget.layout().addWidget(currentOutput)


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
                # TODO: get x, y, width, height and call crop_imgs

                # Remove those later
                cv2.imwrite("cropped.png", roi)
                # Close the window
                # Keep this
                cv2.destroyAllWindows()

                # TODO: show the cropped image in the image widget

    # def handleComponentSlider(self, value, index):
    #     # Disable the event
    #     totalValue = sum(self.sliderValues)
    #     self.componentValueLabels[index].setText(str(value) + "%")
    #     self.sliderValues[index] = value

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
    

        
