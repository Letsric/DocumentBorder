# This Python file uses the following encoding: utf-8
import sys

import PIL.Image
from PySide6.QtGui import QResizeEvent, QPixmap, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QMessageBox
from PySide6.QtCore import Qt

from PIL import Image, ImageDraw

from ui.Mainwindow import Ui_MainWindow

paperType = ""
orientation = ""
imagePath = ""
previewPath = "assets/blank.png"
imageSize = 500
numberOfImagesHorizontal = 2
numberOfImagesVertical = 2


class borderPreview(QLabel):
    def __init__(self):
        super(borderPreview, self).__init__()
        self.setAlignment(Qt.AlignCenter)
        self.updatePreview()

    def resizeEvent(self, event: QResizeEvent):
        pixmap = QPixmap(previewPath)
        width = self.width()
        height = self.height()
        self.setPixmap(pixmap.scaled(width, height, Qt.KeepAspectRatio))

    def updatePreview(self):
        pixmap = QPixmap(previewPath)
        width = self.width()
        height = self.height()
        self.setPixmap(pixmap.scaled(width, height, Qt.KeepAspectRatio))


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # My code goes here :)

        self.ui.A3button.clicked.connect(self.A3button)
        self.ui.A4button.clicked.connect(self.A4button)
        self.ui.A5button.clicked.connect(self.A5button)
        self.ui.USletterButton.clicked.connect(self.USletterButton)
        self.ui.horizontalOrientationButton.clicked.connect(self.horizontalOrientationButton)
        self.ui.verticalOrientationButton.clicked.connect(self.verticalOrientationButton)
        self.ui.browseButton.clicked.connect(self.browseButton)
        self.ui.imageSizeSlider.valueChanged.connect(self.imageSizeSliderValueChanged)
        self.ui.numberOfImagesHorizontalSlider.valueChanged.connect(
            self.numberOfImagesHorizontalSliderValueChanged)
        self.ui.numberOfImagesVerticalSlider.valueChanged.connect(
            self.numberOfImagesVertivalSliderValueChanged)
        self.ui.exportButton.clicked.connect(self.exportButton)
        self.preview = borderPreview()
        self.ui.previewFrame.layout().addWidget(self.preview)
        self.ui.previewButton.clicked.connect(self.previewButton)

    def A3button(self):
        global paperType
        self.ui.A3button.setChecked(True)
        self.ui.A4button.setChecked(False)
        self.ui.A5button.setChecked(False)
        self.ui.USletterButton.setChecked(False)
        paperType = "A3"

    def A4button(self):
        global paperType
        self.ui.A3button.setChecked(False)
        self.ui.A4button.setChecked(True)
        self.ui.A5button.setChecked(False)
        self.ui.USletterButton.setChecked(False)
        paperType = "A4"

    def A5button(self):
        global paperType
        self.ui.A3button.setChecked(False)
        self.ui.A4button.setChecked(False)
        self.ui.A5button.setChecked(True)
        self.ui.USletterButton.setChecked(False)
        paperType = "A5"

    def USletterButton(self):
        global paperType
        self.ui.A3button.setChecked(False)
        self.ui.A4button.setChecked(False)
        self.ui.A5button.setChecked(False)
        self.ui.USletterButton.setChecked(True)
        paperType = "USletter"

    def horizontalOrientationButton(self):
        global orientation
        self.ui.verticalOrientationButton.setChecked(False)
        self.ui.horizontalOrientationButton.setChecked(True)
        orientation = "horizontal"

    def verticalOrientationButton(self):
        global orientation
        self.ui.verticalOrientationButton.setChecked(True)
        self.ui.horizontalOrientationButton.setChecked(False)
        orientation = "vertical"

    def browseButton(self):
        global imagePath
        value = QFileDialog.getOpenFileName(self, "Bilddatei auswählen", "", "PNG-Dateien (*.png)")
        self.ui.imagePathField.setPlainText(value[0])
        imagePath = value[0]

    def imageSizeSliderValueChanged(self):
        global imageSize
        imageSize = self.ui.imageSizeSlider.value()

    def numberOfImagesHorizontalSliderValueChanged(self):
        global numberOfImagesHorizontal
        value = self.ui.numberOfImagesHorizontalSlider.value()
        self.ui.numberOfImagesHorizontalLabel.setText(str(value))
        numberOfImagesHorizontal = value

    def numberOfImagesVertivalSliderValueChanged(self):
        global numberOfImagesVertical
        value = self.ui.numberOfImagesVerticalSlider.value()
        self.ui.numberOfImagesVerticalLabel.setText(str(value))
        numberOfImagesVertical = value

    def validateValues(self):
        if paperType == "":
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("Bitte wähle zuerst den Papiertyp!")
            return -1
        elif orientation == "":
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("Bitte wähle zuerst die Papierausrichtung!")
            return -2
        elif imagePath == "":
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("Bitte wähle zuerst die Bilddatei!")
            return -3
        else:
            return 0

    def exportButton(self):
        if self.validateValues() != 0:
            pass

        exportPath = QFileDialog.getSaveFileName(self, "Datei Speichern", "", "PNG_Dateien (*.png)")
        self.previewButton()
        img = PIL.Image.open("temp.png")
        img.save(exportPath[0])

    def previewButton(self):
        global previewPath
        if self.validateValues() != 0:
            pass

        if paperType == "A3":
            if orientation == "vertical":
                img = Image.new("RGB", (3508, 4960), "WHITE")
            if orientation == "horizontal":
                img = Image.new("RGB", (4960, 3508), "WHITE")

        if paperType == "A4":
            if orientation == "vertical":
                img = Image.new("RGB", (2480, 3508), "WHITE")
            if orientation == "horizontal":
                img = Image.new("RGB", (3508, 2480), "WHITE")

        if paperType == "A5":
            if orientation == "vertical":
                img = Image.new("RGB", (1748, 2480), "WHITE")
            if orientation == "horizontal":
                img = Image.new("RGB", (2480, 1748), "WHITE")

        if paperType == "USletter":
            if orientation == "vertical":
                img = Image.new("RGB", (2550, 3300), "WHITE")
            if orientation == "horizontal":
                img = Image.new("RGB", (3300, 2550), "WHITE")

        borderImg = Image.open(imagePath)
        myW = borderImg.width
        myH = borderImg.height
        newW = imageSize
        newH = int((myH / myW) * imageSize)
        resizedBorderImg = borderImg.resize((newW, newH))

        padding = 50  # TODO: Add a slider for padding

        i1 = 0
        i2 = 0
        while i2 != img.width - padding * 2:
            i2 = (img.width - padding * 2) / (numberOfImagesHorizontal - 1) * i1
            t1 = i2 / (img.width - padding * 2) * 100
            t2 = i2 - (newW / 100 * t1)
            img.paste(resizedBorderImg, (int(t2 + padding), padding))
            img.paste(resizedBorderImg, (int(t2 + padding), img.height - newH - padding))
            i1 += 1

        i1 = 0
        i2 = 0
        while i2 != img.height - padding * 2:
            i2 = (img.height - padding * 2) / (numberOfImagesVertical - 1) * i1
            t1 = i2 / (img.height - padding * 2) * 100
            t2 = i2 - (newH / 100 * t1)
            img.paste(resizedBorderImg, (padding, int(t2 + padding)))
            img.paste(resizedBorderImg, (img.width - newW - padding, int(t2 + padding)))
            i1 += 1

        img.save("temp.png")
        previewPath = "temp.png"
        self.preview.updatePreview()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
