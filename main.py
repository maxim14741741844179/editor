#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QFileDialog
import os
from PIL import Image, ImageOps, ImageFilter
from PyQt5.QtGui import QPixmap

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.image = None
        self.dir = None
        self.save_dir = 'Modified/'
    def LoadImage(self, filename):
        self.filename = filename
        self.dir = workdir
        image_path = os.path.join(self.dir, self.filename)
        self.image = Image.open(image_path)
    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width = Label.width()
        label_height = Label.height()
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        Label.setPixmap(scaled_pixmap)
        Label.setVisible(True)
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if  not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def do_bw(self):
        if ListWidget.selectedItems():
            self.image = ImageOps.grayscale(self.image)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите на кнопку папка и вибирите картинку')
            error_win.exec()
    def do_left(self):
        if ListWidget.selectedItems():
            self.image = self.image.rotate(90)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите на кнопку папка и вибирите картинку')
            error_win.exec()
    def do_right(self):
        if ListWidget.selectedItems():
            self.image = self.image.rotate(-90)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите на кнопку папка и вибирите картинку')
            error_win.exec()
    def do_mirror(self):
        if ListWidget.selectedItems():
            self.image = ImageOps.mirror(self.image)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите на кнопку папка и вибирите картинку')
            error_win.exec()
    def do_sharpen(self):
        if ListWidget.selectedItems():
            try:
                self.image = self.image.filter(ImageFilter.SHARPEN)
                self.saveImage()
                image_path = os.path.join(self.dir, self.save_dir, self.filename)
                self.showImage(image_path)
            except:
                error_win = QMessageBox()
            error_win.setText('я задолбался')
            error_win.exec()
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите на кнопку папка и вибирите картинку')
            error_win.exec()
    def do_blur(self):
        if ListWidget.selectedItems():
            self.image = self.image.filter(ImageFilter.BLUR)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите на кнопку папка и вибирите картинку')
            error_win.exec()
    def do_detail(self):
        if ListWidget.selectedItems():
            self.image = self.image.filter(ImageFilter.DETAIL)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите на кнопку папка и вибирите картинку')
            error_win.exec()
    def do_edge_enhance(self):
        if ListWidget.selectedItems():
            self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите на кнопку папка и вибирите картинку')
            error_win.exec()


workimage = ImageProcessor()

def showChosenImage():
    if ListWidget.currentRow() >= 0:
        filename = ListWidget.currentItem().text()
        workimage.LoadImage(filename)
        image_path = os.path.join(workimage.dir, filename)
        workimage.showImage(image_path)

workdir = ''

def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()   

def filter(files, extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result

def showFilenamesList():
    chooseWorkDir()
    extensions = ['.jpg', '.jpeg', '.png', '.gif']
    files = os.listdir(workdir)
    files = filter(files, extensions)
    ListWidget.clear()
    ListWidget.addItems(files)

app = QApplication([])
win = QWidget()
win.setWindowTitle('Easy Editor')
win.resize(700, 500)

ListWidget = QListWidget()
Label = QLabel('картинка')
PushButton1 = QPushButton('Папка')
PushButton2 = QPushButton('Лево')
PushButton3 = QPushButton('Право')
PushButton4 = QPushButton('Зеркало')
PushButton5 = QPushButton('Резкость')
PushButton6 = QPushButton('Ч/Б')
PushButton7 = QPushButton('блюр')
PushButton8 = QPushButton('детализация')
PushButton9 = QPushButton('чёткость')
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
v1.addWidget(PushButton1)
v1.addWidget(ListWidget)
v2.addWidget(Label)
h2.addWidget(PushButton2)
h2.addWidget(PushButton3)
h2.addWidget(PushButton4)
h2.addWidget(PushButton5)
h2.addWidget(PushButton6)
h2.addWidget(PushButton7)
h2.addWidget(PushButton8)
h2.addWidget(PushButton9)
v2.addLayout(h2)
h1.addLayout(v1)
h1.addLayout(v2)
win.setLayout(h1)

PushButton1.clicked.connect(showFilenamesList)
PushButton2.clicked.connect(workimage.do_left)
PushButton3.clicked.connect(workimage.do_right)
PushButton4.clicked.connect(workimage.do_mirror)
PushButton5.clicked.connect(workimage.do_sharpen)
PushButton6.clicked.connect(workimage.do_bw)
PushButton7.clicked.connect(workimage.do_blur)
PushButton8.clicked.connect(workimage.do_detail)
PushButton9.clicked.connect(workimage.do_edge_enhance)
ListWidget.currentRowChanged.connect(showChosenImage)

win.show()
app.exec()