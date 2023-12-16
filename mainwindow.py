# Form implementation generated from reading ui file '.\UI\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 881)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color: #F0F0F0;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: #333333;\n"
"  border: none;\n"
"  border-radius: 6px;\n"
"  color: #cccccc;\n"
"  font-size: 14px;\n"
"  font-weight: 500;\n"
"  line-height: 20px;\n"
"  list-style: none;\n"
"  padding: 4px 12px;\n"
"  height:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(51, 51, 51, 0.5);\n"
"     text-decoration: none;\n"
"}\n"
"QPushButton:focus{\n"
"     outline: 1px transparent;\n"
"}\n"
"QLabel{\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"}\n"
"QGroupBox{\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    padding:30px 0px 0px 0px;\n"
"    border:none;\n"
"}\n"
"QLineEdit{\n"
"    border:none;\n"
"    padding:4px 10px;\n"
"    border-radius: 3px;\n"
"}\n"
"QListWidget{\n"
"    border:none;\n"
"    border-radius: 3px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QScrollArea{\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.controlFrame = QtWidgets.QFrame(parent=self.frame)
        self.controlFrame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.controlFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.controlFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.controlFrame.setObjectName("controlFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.controlFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(parent=self.controlFrame)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.stopBtn = QtWidgets.QPushButton(parent=self.controlFrame)
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout_2.addWidget(self.stopBtn)
        self.inOutCB = QtWidgets.QComboBox(parent=self.controlFrame)
        self.inOutCB.setObjectName("inOutCB")
        self.horizontalLayout_2.addWidget(self.inOutCB)
        self.componentModeCB = QtWidgets.QComboBox(parent=self.controlFrame)
        self.componentModeCB.setObjectName("componentModeCB")
        self.horizontalLayout_2.addWidget(self.componentModeCB)
        self.channelCB = QtWidgets.QComboBox(parent=self.controlFrame)
        self.channelCB.setObjectName("channelCB")
        self.horizontalLayout_2.addWidget(self.channelCB)
        self.convertBtn = QtWidgets.QPushButton(parent=self.controlFrame)
        self.convertBtn.setObjectName("convertBtn")
        self.horizontalLayout_2.addWidget(self.convertBtn)
        self.verticalLayout.addWidget(self.controlFrame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.imageOneWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.imageOneWidget.setMinimumSize(QtCore.QSize(0, 320))
        self.imageOneWidget.setMaximumSize(QtCore.QSize(320, 320))
        self.imageOneWidget.setStyleSheet("QWidget{\n"
"    border:1px solid;\n"
"}")
        self.imageOneWidget.setObjectName("imageOneWidget")
        self.horizontalLayout_4.addWidget(self.imageOneWidget)
        self.imageOneComponentWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.imageOneComponentWidget.setMinimumSize(QtCore.QSize(0, 320))
        self.imageOneComponentWidget.setMaximumSize(QtCore.QSize(320, 320))
        self.imageOneComponentWidget.setStyleSheet("QWidget{\n"
"    border:1px solid;\n"
"}")
        self.imageOneComponentWidget.setObjectName("imageOneComponentWidget")
        self.horizontalLayout_4.addWidget(self.imageOneComponentWidget)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.componentOneCB = QtWidgets.QComboBox(parent=self.frame_3)
        self.componentOneCB.setObjectName("componentOneCB")
        self.horizontalLayout_5.addWidget(self.componentOneCB)
        self.componentOneRatioSlider = QtWidgets.QSlider(parent=self.frame_3)
        self.componentOneRatioSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.componentOneRatioSlider.setObjectName("componentOneRatioSlider")
        self.horizontalLayout_5.addWidget(self.componentOneRatioSlider)
        self.componentOneRatioLabel = QtWidgets.QLabel(parent=self.frame_3)
        self.componentOneRatioLabel.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.componentOneRatioLabel.setFont(font)
        self.componentOneRatioLabel.setObjectName("componentOneRatioLabel")
        self.horizontalLayout_5.addWidget(self.componentOneRatioLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.imageThreeWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.imageThreeWidget.setMinimumSize(QtCore.QSize(0, 320))
        self.imageThreeWidget.setMaximumSize(QtCore.QSize(320, 320))
        self.imageThreeWidget.setStyleSheet("QWidget{\n"
"    border:1px solid;\n"
"}")
        self.imageThreeWidget.setObjectName("imageThreeWidget")
        self.horizontalLayout_8.addWidget(self.imageThreeWidget)
        self.imageThreeComponentWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.imageThreeComponentWidget.setMinimumSize(QtCore.QSize(0, 320))
        self.imageThreeComponentWidget.setMaximumSize(QtCore.QSize(320, 320))
        self.imageThreeComponentWidget.setStyleSheet("QWidget{\n"
"    border:1px solid;\n"
"}")
        self.imageThreeComponentWidget.setObjectName("imageThreeComponentWidget")
        self.horizontalLayout_8.addWidget(self.imageThreeComponentWidget)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.componentThreeCB = QtWidgets.QComboBox(parent=self.frame_3)
        self.componentThreeCB.setObjectName("componentThreeCB")
        self.horizontalLayout_9.addWidget(self.componentThreeCB)
        self.componentThreeRatioSlider = QtWidgets.QSlider(parent=self.frame_3)
        self.componentThreeRatioSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.componentThreeRatioSlider.setObjectName("componentThreeRatioSlider")
        self.horizontalLayout_9.addWidget(self.componentThreeRatioSlider)
        self.componentThreeRatioLabel = QtWidgets.QLabel(parent=self.frame_3)
        self.componentThreeRatioLabel.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.componentThreeRatioLabel.setFont(font)
        self.componentThreeRatioLabel.setObjectName("componentThreeRatioLabel")
        self.horizontalLayout_9.addWidget(self.componentThreeRatioLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.imageTwoWidget = QtWidgets.QWidget(parent=self.frame_4)
        self.imageTwoWidget.setMinimumSize(QtCore.QSize(0, 320))
        self.imageTwoWidget.setMaximumSize(QtCore.QSize(320, 320))
        self.imageTwoWidget.setStyleSheet("QWidget{\n"
"    border:1px solid;\n"
"}")
        self.imageTwoWidget.setObjectName("imageTwoWidget")
        self.horizontalLayout_6.addWidget(self.imageTwoWidget)
        self.imageTwoComponentWidget = QtWidgets.QWidget(parent=self.frame_4)
        self.imageTwoComponentWidget.setMinimumSize(QtCore.QSize(0, 320))
        self.imageTwoComponentWidget.setMaximumSize(QtCore.QSize(320, 320))
        self.imageTwoComponentWidget.setStyleSheet("QWidget{\n"
"    border:1px solid;\n"
"}")
        self.imageTwoComponentWidget.setObjectName("imageTwoComponentWidget")
        self.horizontalLayout_6.addWidget(self.imageTwoComponentWidget)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.componentTwoCB = QtWidgets.QComboBox(parent=self.frame_4)
        self.componentTwoCB.setObjectName("componentTwoCB")
        self.horizontalLayout_7.addWidget(self.componentTwoCB)
        self.componentTwoRatioSlider = QtWidgets.QSlider(parent=self.frame_4)
        self.componentTwoRatioSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.componentTwoRatioSlider.setObjectName("componentTwoRatioSlider")
        self.horizontalLayout_7.addWidget(self.componentTwoRatioSlider)
        self.componentTwoRatioLabel = QtWidgets.QLabel(parent=self.frame_4)
        self.componentTwoRatioLabel.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.componentTwoRatioLabel.setFont(font)
        self.componentTwoRatioLabel.setObjectName("componentTwoRatioLabel")
        self.horizontalLayout_7.addWidget(self.componentTwoRatioLabel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_10.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.imageFourWidget = QtWidgets.QWidget(parent=self.frame_4)
        self.imageFourWidget.setMinimumSize(QtCore.QSize(0, 320))
        self.imageFourWidget.setMaximumSize(QtCore.QSize(320, 320))
        self.imageFourWidget.setStyleSheet("QWidget{\n"
"    border:1px solid;\n"
"}")
        self.imageFourWidget.setObjectName("imageFourWidget")
        self.horizontalLayout_10.addWidget(self.imageFourWidget)
        self.imageFourComponentWidget = QtWidgets.QWidget(parent=self.frame_4)
        self.imageFourComponentWidget.setMinimumSize(QtCore.QSize(0, 320))
        self.imageFourComponentWidget.setMaximumSize(QtCore.QSize(320, 320))
        self.imageFourComponentWidget.setStyleSheet("QWidget{\n"
"    border:1px solid;\n"
"}")
        self.imageFourComponentWidget.setObjectName("imageFourComponentWidget")
        self.horizontalLayout_10.addWidget(self.imageFourComponentWidget)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.componentFourCB = QtWidgets.QComboBox(parent=self.frame_4)
        self.componentFourCB.setObjectName("componentFourCB")
        self.horizontalLayout_11.addWidget(self.componentFourCB)
        self.componentFourRatioSlider = QtWidgets.QSlider(parent=self.frame_4)
        self.componentFourRatioSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.componentFourRatioSlider.setObjectName("componentFourRatioSlider")
        self.horizontalLayout_11.addWidget(self.componentFourRatioSlider)
        self.componentFourRatioLabel = QtWidgets.QLabel(parent=self.frame_4)
        self.componentFourRatioLabel.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.componentFourRatioLabel.setFont(font)
        self.componentFourRatioLabel.setObjectName("componentFourRatioLabel")
        self.horizontalLayout_11.addWidget(self.componentFourRatioLabel)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(450, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.outputOneLabel = QtWidgets.QLabel(parent=self.frame_2)
        self.outputOneLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.outputOneLabel.setObjectName("outputOneLabel")
        self.verticalLayout_2.addWidget(self.outputOneLabel)
        self.outputOneWidget = QtWidgets.QWidget(parent=self.frame_2)
        self.outputOneWidget.setMinimumSize(QtCore.QSize(0, 360))
        self.outputOneWidget.setStyleSheet("QWidget{\n"
"    border:1px solid;\n"
"}")
        self.outputOneWidget.setObjectName("outputOneWidget")
        self.verticalLayout_2.addWidget(self.outputOneWidget)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.outputTwoLabel = QtWidgets.QLabel(parent=self.frame_2)
        self.outputTwoLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.outputTwoLabel.setObjectName("outputTwoLabel")
        self.verticalLayout_3.addWidget(self.outputTwoLabel)
        self.outputTwoWidget = QtWidgets.QWidget(parent=self.frame_2)
        self.outputTwoWidget.setMinimumSize(QtCore.QSize(0, 360))
        self.outputTwoWidget.setStyleSheet("QWidget{\n"
"    border:1px solid;\n"
"}\n"
"")
        self.outputTwoWidget.setObjectName("outputTwoWidget")
        self.verticalLayout_3.addWidget(self.outputTwoWidget)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.convertBtn.setText(_translate("MainWindow", "Convert"))
        self.componentOneRatioLabel.setText(_translate("MainWindow", "0%"))
        self.componentThreeRatioLabel.setText(_translate("MainWindow", "0%"))
        self.componentTwoRatioLabel.setText(_translate("MainWindow", "0%"))
        self.componentFourRatioLabel.setText(_translate("MainWindow", "0%"))
        self.outputOneLabel.setText(_translate("MainWindow", "Output 1"))
        self.outputTwoLabel.setText(_translate("MainWindow", "Output 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
