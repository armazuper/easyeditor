import os 
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
QPushButton, QLabel, QFileDialog, QListWidget)

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap
from PIL import Image

from PIL.ImageFilter import(
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE,
    GaussianBlur, UnsharpMask
)

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
button_blur = QPushButton("Размытие")
button_smooth = QPushButton("Сглаживание")
button_detail = QPushButton("Детализация")
button_emboss = QPushButton("Тиснение")
button_gaussian = QPushButton("По Гаусу")
button_contour = QPushButton("Контур")
button_edge_enhance = QPushButton("Усиление ")
button_unsharpmask = QPushButton("Нерезкость")
button_edge_enhance_more = QPushButton("Усиленная резкость")
button_smooth_more = QPushButton("Больше сглаживания")
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

row2_buttons = QHBoxLayout()
row2_buttons.addWidget(button_blur)
row2_buttons.addWidget(button_smooth)
row2_buttons.addWidget(button_detail)
row2_buttons.addWidget(button_emboss)
row2_buttons.addWidget(button_gaussian)

col2.addLayout(row2_buttons)

col2.addLayout(row_buttons)
row3_buttons = QHBoxLayout()
row3_buttons.addWidget
row3_buttons.addWidget(button_contour)
row3_buttons.addWidget(button_edge_enhance)
row3_buttons.addWidget(button_unsharpmask)
row3_buttons.addWidget(button_edge_enhance_more)
row3_buttons.addWidget(button_smooth_more)

col2.addLayout(row3_buttons)

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

class ImageProcessor():
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
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_sharp(self):
        self.image = self.image.convert("RGB")
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(BLUR)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_smooth(self):
        self.image = self.image.filter(SMOOTH)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_detail(self):
        self.image = self.image.filter(DETAIL)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_emboss(self):
        self.image = self.image.filter(EMBOSS)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_gaussian(self):
        self.image = self.image.convert("RGB")
        self.image = self.image.filter(GaussianBlur)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_contour(self):
        self.image = self.image.filter(CONTOUR)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_edge_enhance(self):
        self.image = self.image.filter(EDGE_ENHANCE)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_unsharpmask(self):
        self.image = self.image.filter(UnsharpMask)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_edge_enhance_more(self):
        self.image = self.image.filter(EDGE_ENHANCE_MORE)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)

    def do_smooth_more(self):
        self.image = self.image.filter(SMOOTH_MORE)
        self.saveImage()
        image_path = os.path.join(self.save_dir, self.filename)
        self.showImage(image_path)


    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
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
button_left.clicked.connect(workimage.do_left)
button_right.clicked.connect(workimage.do_right)
button_sharp.clicked.connect(workimage.do_sharp)
button_mirror.clicked.connect(workimage.do_flip)
button_blur.clicked.connect(workimage.do_blur)
button_smooth.clicked.connect(workimage.do_smooth) 
button_detail.clicked.connect(workimage.do_detail)
button_emboss.clicked.connect(workimage.do_emboss)
button_gaussian.clicked.connect(workimage.do_gaussian)
button_contour.clicked.connect(workimage.do_contour)
button_edge_enhance.clicked.connect(workimage.do_edge_enhance)
button_unsharpmask.clicked.connect(workimage.do_unsharpmask)
button_edge_enhance_more.clicked.connect(workimage.do_edge_enhance_more)
button_smooth_more.clicked.connect(workimage.do_smooth_more)
app.exec()



