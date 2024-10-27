import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QFileDialog
from PyQt5.QtGui import QPixmap

class PictureViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Extrapicturary")
        
        # Image properties
        self.image = None
        self.image_path = ""
        self.zoom_level = 100
        
        # UI elements
        self.label = QLabel(self)
        self.setCentralWidget(self.label)
        
        self.status_label = QLabel(self)
        self.statusBar().addWidget(self.status_label)
        
        self.menu = self.menuBar()
        
        self.file_menu = self.menu.addMenu("File")
        self.open_action = QAction("Open", self)
        self.open_action.triggered.connect(self.open_image)
        self.file_menu.addAction(self.open_action)
        
        self.zoom_menu = self.menu.addMenu("Zoom")
        self.zoom_in_action = QAction("Zoom In", self)
        self.zoom_in_action.triggered.connect(self.zoom_in)
        self.zoom_menu.addAction(self.zoom_in_action)
        self.zoom_out_action = QAction("Zoom Out", self)
        self.zoom_out_action.triggered.connect(self.zoom_out)
        self.zoom_menu.addAction(self.zoom_out_action)
        
    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.gif)")
        if file_path:
            self.image_path = file_path
            self.image = QPixmap(file_path)
            self.show_image()
    
    def show_image(self):
        if self.image:
            # Calculate zoomed dimensions
            width = int(self.image.width() * self.zoom_level / 100)
            height = int(self.image.height() * self.zoom_level / 100)

            # Resize image
            resized_image = self.image.scaled(width, height)

            # Update label with the new image
            self.label.setPixmap(resized_image)

            # Update status label with image size
            self.status_label.setText(f"Image Size: {width}x{height}")

            self.resize(width, height)
    
    def zoom_in(self):
        if self.zoom_level < 200:
            self.zoom_level += 10
            self.show_image()
    
    def zoom_out(self):
        if self.zoom_level > 20:
            self.zoom_level -= 10
            self.show_image()

# Create the application instance
app = QApplication(sys.argv)

# Create the picture viewer instance
viewer = PictureViewer()

# Show the main window
viewer.show()

# Run the application event loop
sys.exit(app.exec_())