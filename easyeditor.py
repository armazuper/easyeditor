import os 
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
QPushButton, QLabel, QFileDialog, QListWidget)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image


app = QApplication([])
window = QWidget()
window.resize(700, 500)
window.setWindowTitle('Easy Editor')

image_label = QLabel("Картинка")
button_directory = QPushButton("Папка")
button_left = QPushButton("Влево")
button_right = QPushButton("Вправо")
button_mirror = QPushButton("Зеркало")
button_sharp = QPushButton("Резкость")
button_nw = QPushButton("Ч\Б")
file_list = QListWidget()

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(button_directory)
col1.addWidget(file_list)
col2.addWidget(image_label)
row_buttons = QHBoxLayout()
row_buttons.addWidget(button_left)
row_buttons.addWidget(button_right)
row_buttons.addWidget(button_mirror)
row_buttons.addWidget(button_sharp)
row_buttons.addWidget(button_nw)
col2.addLayout(row_buttons)

row.addLayout(col1)
row.addLayout(col2)
window.setLayout(row)
window.show()

work_directory = ""

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def choose_directory():
    global work_directory
    work_directory = QFileDialog.getExistingDirectory()


def showfilelist():
    extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', ".webp"]
    choose_directory()
    filenames = filter(os.listdir(work_directory), extensions)
    file_list.clear()
    for filename in filenames:
        file_list.addItem(filename)

button_directory.clicked.connect(showfilelist)

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.filename = None
        self.dir = None
        self.save_dir = "Modded/"

    def load_image(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def showImage(self,path):
        image_label.hide()
        pixmapimage = QPixmap(path)
        w, h = image_label.width(), image_label.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        image_label.setPixmap(pixmapimage)
        image_label.show()

    def do_blackwhite(self):
        if self.image == self.image.convert("L"):
            self.saveImage()
            image_path = os.path.join(self.save_dir, self.filename)
            self.showImage(image_path)

    def saveImage(self):
        path = os.path.join(self.save_dir, self.filename)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(self.save_dir)
        image_path = os.path.join(self.dir, self.filename)
        self.image.save(image_path)
    
        




def showChosenImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        workimage.load_image(work_directory, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

workimage = ImageProcessor()
file_list.currentRowChanged.connect(showChosenImage)
button_nw.clicked.connect(workimage.do_blackwhite)






app.exec()



