from math import comb
import random
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow , QLabel , QFileDialog , QWidget , QVBoxLayout , QHBoxLayout
from mainwindow import Ui_MainWindow
import Gallery , Image , Mixer
from PyQt6.QtCore import QThread, pyqtSignal, QTimer, QRectF
import matplotlib.pyplot as plt
import pyqtgraph as pg
import cv2
import logging

# Logging

logging.basicConfig(filename='mainLog.log', filemode='w',level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


import numpy as np

modes = ['Real', 'Imaginary', 'Magnitude', 'Phase']

class ImageProcessingThread(QThread):
    processingDone = pyqtSignal(object)

    def __init__(self, weights, componentsIds, componentsTypes, gallery, cropMode, currentState):
        QThread.__init__(self)
        self.weights = weights
        self.componentsIds = componentsIds
        self.componentsTypes = componentsTypes
        self.gallery = gallery
        self.cropMode = cropMode
        self.currentState = currentState

    def run(self):
        currentMixer = Mixer.Mixer(*self.weights, *self.componentsIds, *self.componentsTypes)
        coords = [self.currentState['pos'][0], self.currentState['pos'][0] + self.currentState['size'][0], self.currentState['pos'][1], self.currentState['pos'][1] + self.currentState['size'][1]]
        coords = [int(coord) for coord in coords]
        print(coords)
        output = currentMixer.inverse_fft(self.gallery.get_gallery(), self.cropMode, coords).T
        self.processingDone.emit(output)

class CustomViewBox(pg.ViewBox):
    def __init__(self, imageViewComponent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dragStartPos = None
        self.child = imageViewComponent
        self.currentBrightness = 0
        self.currentContrast = 0

    def mouseDragEvent(self, event, axis=None):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            dx, dy = 0, 0
            if self.dragStartPos is not None:
                dx = event.pos().x() - self.dragStartPos.x()
                dy = event.pos().y() - self.dragStartPos.y()
            self.dragStartPos = event.pos()
            if abs(dx) > 2:
                self.currentBrightness += dx
            if abs(dy) > 2:
                self.currentContrast += dy * 0.01
            newImage = np.clip((self.child.originalImage + self.currentBrightness) * (1 + self.currentContrast) , 0, 255.0)
            self.child.setImage(newImage)
            event.accept()  # Accept the event

    def mouseClickEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.dragStartPos = None
            self.currentBrightness = 0
            self.currentContrast = 0
            self.child.setImage(self.child.originalImage)
        
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragStartPos = None
        super(CustomViewBox, self).mouseReleaseEvent(event)

class CustomImageView(pg.ImageView):
    def __init__(self, *args, **kwargs):
        kwargs['view'] = CustomViewBox(imageViewComponent=self)
        super().__init__(*args, **kwargs)
        self.imageItem = self.getImageItem()
        self.originalImage = None
        self.firstTime = True

    def setImage(self, img, *args, **kwargs):
        super().setImage(img, *args, **kwargs)
        self.imageItem = self.getImageItem()
        if (self.firstTime):
            self.firstTime = False
            self.originalImage = self.getImageItem().image  # Store a reference instead of a copy

    def __del__(self):
        self.imageItem = None
        self.originalImage = None
        print("DELETED")

class MainWindow(QMainWindow, Ui_MainWindow):
    image = None
    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setupUi(self)
        # self.oriImage = None
        self.viewWidgets = [None, None, None, None]
        self.freqViewWidgets = [None, None, None, None]
        self.gallery = Gallery.Gallery()
        self.cropping = False
        self.x_start, self.y_start, self.x_end, self.y_end = 0, 0, 0, 0
        self.image = cv2.imread('./imgs/1.png')
        self.oriImage = self.image.copy()
        self.totalOfComponents = 100
        self.remainderOfComponents = 100
        self.currentSumOfComponents = 0
        self.progressBar.setVisible(False)

        # Browsing Images
        self.imageWidgets = [self.imageOneWidget, self.imageTwoWidget, self.imageThreeWidget, self.imageFourWidget]
        self.transWidgets = [self.imageOneComponentWidget, self.imageTwoComponentWidget, self.imageThreeComponentWidget, self.imageFourComponentWidget]
        self.componentSliders = [self.componentOneRatioSlider, self.componentTwoRatioSlider, self.componentThreeRatioSlider, self.componentFourRatioSlider]
        self.componentValueLabels = [self.componentOneRatioLabel, self.componentTwoRatioLabel, self.componentThreeRatioLabel, self.componentFourRatioLabel]
        self.sliderValues = [0, 0, 0, 0]
        self.outputSliderValues = [0, 0, 0, 0]
        self.imageModesCombobox = [self.imageOneModeSelect, self.imageTwoModeSelect, self.imageThreeModeSelect, self.imageFourModeSelect]
        self.rois = [None, None, None, None]
        self.imagePaths = ['', '', '', '']
        self.componentsTypes = ['real', 'real', 'real', 'real']
        self.componentsIds = [0, 0, 0, 0]
        self.outputWidgets = [self.outputOneWidget, self.outputTwoWidget]
        self.currentOutput = 0
        self.outputSelect.currentIndexChanged.connect(self.handleOutputChange)

        self.mixerModeSelect.currentIndexChanged.connect(self.handleMixerModeChange)

        self.leaveCropping = False
        self.currentState = {'pos': (0.000000, 0.000000), 'size': (50.000000, 50.000000), 'angle': 0.0}
        self.cropMode = 0
        self.cropModeSelect.currentIndexChanged.connect(self.handleCropModeChange)

        for i, widget in enumerate(self.imageWidgets):
            layout = QHBoxLayout()
            widget.setLayout(layout)
            widget.mouseDoubleClickEvent = lambda event, i=i: self.handleUploadImage(event, i)

        for i, widget in enumerate(self.outputWidgets):
            layout = QHBoxLayout()
            widget.setLayout(layout)
        
        for i, widget in enumerate(self.transWidgets):
            layout = QHBoxLayout()
            widget.setLayout(layout)

        for i, slider in enumerate(self.componentSliders):
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setEnabled(False)

        self.convertButton.clicked.connect(self.handleConvertBtn)

        for i, combobox in enumerate(self.imageModesCombobox):
            combobox.clear()
            for mode in modes:
                combobox.addItem(mode)
            combobox.setEnabled(False)
            combobox.currentIndexChanged.connect(lambda index, i=i: self.handleImageModeChange(index, i))
            model = combobox.model()
            model.item(2).setEnabled(False)
            model.item(3).setEnabled(False)
        
        for i , slider in enumerate(self.componentSliders):
            slider.valueChanged.connect(lambda value, i=i: self.handleSlider(value, i))

        self.x_start, self.y_start, self.x_end, self.y_end , self.cropping
        self.stopButton.setVisible(False)
        self.stopButton.clicked.connect(self.cancelProgressBar)
        self.stopped = False

    def handleCropModeChange(self, index):
        self.cropMode = index
        for roi in self.rois:
            if roi:
                if index == 0:
                    roi.hide()
                else:
                    roi.show()

    def handleOutputChange(self, index):
        self.currentOutput = index

    def handleMixerModeChange(self, index):
        if index == 0:
            for combobox in self.imageModesCombobox:
                model = combobox.model()
                model.item(0).setEnabled(True)
                model.item(1).setEnabled(True)
                model.item(2).setEnabled(False)
                model.item(3).setEnabled(False)
                combobox.setCurrentIndex(0)
                self.componentsTypes = ['real', 'real', 'real', 'real']
        else:
            for combobox in self.imageModesCombobox:
                model = combobox.model()
                model.item(0).setEnabled(False)
                model.item(1).setEnabled(False)
                model.item(2).setEnabled(True)
                model.item(3).setEnabled(True)
                combobox.setCurrentIndex(2)
                self.componentsTypes = ['magnitude', 'magnitude', 'magnitude', 'magnitude']

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
        self.sliderValues[index] = value
        self.componentValueLabels[index].setText(str(value) + "%")
        self.componentSliders[index].setValue(value)
        currentSumOfComponents = self.sumSlidersValues()
        if currentSumOfComponents > 100:
            self.outputSliderValues = [(value / currentSumOfComponents) * 1 for value in self.sliderValues]
        else:
            self.outputSliderValues = [(value / 100) for value in self.sliderValues]
        # self.outputSliderValues = [(value / 100) for value in self.sliderValues]

    def handleImageModeChange(self, index, i):
        mode = modes[index]
        image = self.gallery.get_gallery()[i]

        graph = self.freqViewWidgets[i]
        if mode == 'Magnitude':
            graph.setImage(image.get_mag())
        elif mode == 'Phase':
            graph.setImage(image.get_phase())
        elif mode == 'Real':
            graph.setImage(image.get_real())
        elif mode == 'Imaginary':
            graph.setImage(image.get_imaginary())

        self.componentsTypes[i] = mode.lower()

    def handleBrowseImage(self, index):
        img = QFileDialog.getOpenFileName(
            self, "Open file", ".\\", "Image files (*.jpg *.png)"
        )
        if img:
            image = Image.Image()
            imagePath = img[0].strip().split("/")[-1]
            image.load_img(imagePath)
            image.compute_fourier_transform()
            self.imageModesCombobox[index].setEnabled(True)
            self.imageModesCombobox[index].setCurrentIndex(0 if self.mixerModeSelect.currentIndex() == 0 else 2)
            # TODO: Add the image to gallery
            self.gallery.add_image(image, index)

            # TODO: Call reshape_all with a list of images in gallery
            Image.Image.reshape_all(self.gallery.get_gallery().values())
            current_images = self.gallery.get_gallery()
            self.componentsIds[index] = index
            self.componentSliders[index].setEnabled(True)
            for i in current_images:
                if self.viewWidgets[i] == None:
                    newGraph = CustomImageView(parent=self.imageWidgets[i])
                    self.viewWidgets[i] = newGraph
                    self.imageWidgets[i].layout().addWidget(self.viewWidgets[i])
                    self.viewWidgets[i].ui.roiBtn.hide()
                    self.viewWidgets[i].ui.menuBtn.hide()
                    self.viewWidgets[i].ui.histogram.hide()
                
                self.viewWidgets[i].setImage(current_images[i].get_img())

                if self.freqViewWidgets[i] == None:
                    realGraph = pg.ImageView()
                    self.freqViewWidgets[i] = realGraph
                    self.transWidgets[i].layout().addWidget(self.freqViewWidgets[i])
                    self.freqViewWidgets[i].ui.roiBtn.hide()
                    self.freqViewWidgets[i].ui.menuBtn.hide()
                    self.freqViewWidgets[i].ui.histogram.hide()
                    self.freqViewWidgets[i].getView().setMouseEnabled(x=False, y=False)

                currentMode = self.componentsTypes[i]
                if currentMode == 'magnitude':
                    self.freqViewWidgets[i].setImage(current_images[i].get_mag())
                elif currentMode == 'phase':
                    self.freqViewWidgets[i].setImage(current_images[i].get_phase())
                elif currentMode == 'real':
                    self.freqViewWidgets[i].setImage(current_images[i].get_real())
                elif currentMode == 'imaginary':
                    self.freqViewWidgets[i].setImage(current_images[i].get_imaginary())

                if self.rois[i] == None:
                    ROI_Maxbounds = QRectF(0, 0, 100, 100)
                    ROI_Maxbounds.adjust(0, 0, self.freqViewWidgets[i].getImageItem().width() - 100, self.freqViewWidgets[i].getImageItem().height() - 100)
                    roi = pg.ROI(pos = self.currentState['pos'], size = self.currentState['size'], hoverPen='b', resizable= True, invertible= True, rotatable= False, maxBounds= ROI_Maxbounds)
                    if self.cropMode == 0:
                        roi.hide()
                    self.rois[i] = roi
                    roi.sigRegionChangeFinished.connect(lambda: self.modify_regions(i))
                    self.freqViewWidgets[i].getView().addItem(roi)

    def handleConvertBtn(self):
        # Show progress bar
        self.progressBar.setVisible(True)
        self.stopButton.setVisible(True)
        self.progressBar.setValue(0)

        # Start a QTimer to periodically update the progress bar value
        self.progressTimer = QTimer()
        self.progressTimer.timeout.connect(self.updateProgressBar)
        self.progressTimer.start(100)  # update every 100 ms

        # Start image processing in a separate thread
        self.stopped = False
        self.thread = ImageProcessingThread(self.outputSliderValues, self.componentsIds, self.componentsTypes, self.gallery, self.cropMode, self.currentState)
        self.thread.processingDone.connect(self.delayShowImage)
        self.thread.start()

    def updateProgressBar(self):
        value = self.progressBar.value()
        if value < 99:
            self.progressBar.setValue(value + random.randint(3, 6))
        else:
            self.progressTimer.stop()

    def delayShowImage(self, output):
        QTimer.singleShot(2000, lambda: self.showImage(output))

    def showImage(self, output):
        if not self.stopped:
            outputWidget = self.outputWidgets[self.currentOutput]
            layout = outputWidget.layout()
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()


            outputImage = pg.image(output)
            outputImage.ui.roiBtn.hide()
            outputImage.ui.menuBtn.hide()
            outputImage.ui.histogram.hide()
            outputWidget.layout().addWidget(outputImage)

        # Hide progress bar
        self.progressTimer.stop()
        self.progressBar.setValue(100)
        QTimer.singleShot(2000, self.hideProgressbar)

    def modify_regions(self, index):
        newState = self.rois[index].getState()
        self.currentState = newState
        for roi in self.rois:
            if roi:
                roi.setState(newState, update = False)
                roi.stateChanged(finish = False)

    def hideProgressbar(self):
        self.progressBar.setVisible(False)
        self.stopButton.setVisible(False)

    def cancelProgressBar(self):
        # Terminate the thread if progress bar is cancelled
        if self.thread.isRunning():
            self.thread.terminate()
        self.progressTimer.stop()
        self.stopped = True
        self.hideProgressbar()

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()