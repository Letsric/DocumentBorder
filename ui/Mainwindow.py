# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(783, 554)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.previewFrame = QFrame(self.frame)
        self.previewFrame.setObjectName(u"previewFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.previewFrame.sizePolicy().hasHeightForWidth())
        self.previewFrame.setSizePolicy(sizePolicy1)
        self.previewFrame.setMinimumSize(QSize(300, 400))
        self.previewFrame.setFrameShape(QFrame.StyledPanel)
        self.previewFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.previewFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.previewFrame)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, 9, 9)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.A5button = QPushButton(self.frame_5)
        self.A5button.setObjectName(u"A5button")
        self.A5button.setCheckable(True)
        self.A5button.setAutoDefault(False)
        self.A5button.setFlat(False)

        self.horizontalLayout_2.addWidget(self.A5button)

        self.A4button = QPushButton(self.frame_5)
        self.A4button.setObjectName(u"A4button")
        self.A4button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.A4button)

        self.A3button = QPushButton(self.frame_5)
        self.A3button.setObjectName(u"A3button")
        self.A3button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.A3button)

        self.USletterButton = QPushButton(self.frame_5)
        self.USletterButton.setObjectName(u"USletterButton")
        self.USletterButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.USletterButton)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 60))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalOrientationButton = QPushButton(self.frame_12)
        self.verticalOrientationButton.setObjectName(u"verticalOrientationButton")
        self.verticalOrientationButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.verticalOrientationButton)

        self.horizontalOrientationButton = QPushButton(self.frame_12)
        self.horizontalOrientationButton.setObjectName(u"horizontalOrientationButton")
        self.horizontalOrientationButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.horizontalOrientationButton)


        self.verticalLayout_8.addWidget(self.frame_12)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.imagePathField = QPlainTextEdit(self.frame_6)
        self.imagePathField.setObjectName(u"imagePathField")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(4)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.imagePathField.sizePolicy().hasHeightForWidth())
        self.imagePathField.setSizePolicy(sizePolicy4)
        self.imagePathField.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.imagePathField.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.imagePathField.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.imagePathField.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.imagePathField)

        self.browseButton = QPushButton(self.frame_6)
        self.browseButton.setObjectName(u"browseButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.browseButton)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 60))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.imageSizeSlider = QSlider(self.frame_7)
        self.imageSizeSlider.setObjectName(u"imageSizeSlider")
        self.imageSizeSlider.setMinimum(1)
        self.imageSizeSlider.setMaximum(1000)
        self.imageSizeSlider.setValue(500)
        self.imageSizeSlider.setSliderPosition(500)
        self.imageSizeSlider.setTracking(True)
        self.imageSizeSlider.setOrientation(Qt.Horizontal)
        self.imageSizeSlider.setInvertedAppearance(False)
        self.imageSizeSlider.setInvertedControls(False)

        self.verticalLayout_5.addWidget(self.imageSizeSlider)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.numberOfImagesVerticalSlider = QSlider(self.frame_9)
        self.numberOfImagesVerticalSlider.setObjectName(u"numberOfImagesVerticalSlider")
        self.numberOfImagesVerticalSlider.setMinimum(2)
        self.numberOfImagesVerticalSlider.setMaximum(20)
        self.numberOfImagesVerticalSlider.setPageStep(2)
        self.numberOfImagesVerticalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.numberOfImagesVerticalSlider, 1, 1, 1, 1)

        self.numberOfImagesHorizontalSlider = QSlider(self.frame_9)
        self.numberOfImagesHorizontalSlider.setObjectName(u"numberOfImagesHorizontalSlider")
        self.numberOfImagesHorizontalSlider.setMinimum(2)
        self.numberOfImagesHorizontalSlider.setMaximum(20)
        self.numberOfImagesHorizontalSlider.setPageStep(2)
        self.numberOfImagesHorizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.numberOfImagesHorizontalSlider, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.numberOfImagesHorizontalLabel = QLabel(self.frame_9)
        self.numberOfImagesHorizontalLabel.setObjectName(u"numberOfImagesHorizontalLabel")

        self.gridLayout.addWidget(self.numberOfImagesHorizontalLabel, 0, 2, 1, 1)

        self.numberOfImagesVerticalLabel = QLabel(self.frame_9)
        self.numberOfImagesVerticalLabel.setObjectName(u"numberOfImagesVerticalLabel")

        self.gridLayout.addWidget(self.numberOfImagesVerticalLabel, 1, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        self.frame_10 = QFrame(self.centralwidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 30))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.previewButton = QPushButton(self.frame_10)
        self.previewButton.setObjectName(u"previewButton")
        self.previewButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.previewButton)

        self.exportButton = QPushButton(self.frame_10)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.exportButton)


        self.verticalLayout.addWidget(self.frame_10)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.A5button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; text-decoration: underline;\">Document Border</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Papierformat</span></p></body></html>", None))
        self.A5button.setText(QCoreApplication.translate("MainWindow", u"A5", None))
        self.A4button.setText(QCoreApplication.translate("MainWindow", u"A4", None))
        self.A3button.setText(QCoreApplication.translate("MainWindow", u"A3", None))
        self.USletterButton.setText(QCoreApplication.translate("MainWindow", u"US Letter", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Ausrichtung</span></p></body></html>", None))
        self.verticalOrientationButton.setText(QCoreApplication.translate("MainWindow", u"Hochvormat", None))
        self.horizontalOrientationButton.setText(QCoreApplication.translate("MainWindow", u"Querformat", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Bild f\u00fcr den Rand</span></p></body></html>", None))
        self.imagePathField.setPlainText("")
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Bildgr\u00f6\u00dfe</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Anzahl der Bilder</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Horizontal</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Vertikal</span></p></body></html>", None))
        self.numberOfImagesHorizontalLabel.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.numberOfImagesVerticalLabel.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.previewButton.setText(QCoreApplication.translate("MainWindow", u"Vorschau", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Exportieren", None))
    # retranslateUi

