import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class PictureViewer:
    def __init__(self, root):
        self.root = root
        root.title("Extrapicturary")
        
        # Image properties
        self.image = None
        self.image_path = ""
        self.zoom_level = 100
        
        # UI elements
        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.status_label = tk.Label(root, text="Image Size: ")
        self.status_label.pack(side=tk.BOTTOM)
        
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_image)
        
        self.zoom_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Zoom", menu=self.zoom_menu)
        self.zoom_menu.add_command(label="Zoom In", command=self.zoom_in)
        self.zoom_menu.add_command(label="Zoom Out", command=self.zoom_out)
        
    def open_image(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif"),("I don't work", "*blablablablablablablabladoyouhavealongenoughscreentoviewthis?blablablaitoldyouthisdoesntworkyaknow!blablablablagotorelgoshop.github.ioandviewmorestufflikethisemailethan.mslam@gmail.comandtellhimyoufoundthiseastereggblablablaremembertoscreenshotthisandshowittoyourfriendssotheywoulddownloadourdumbapps!")])
        if file_path:
            self.image_path = file_path
            self.image = Image.open(file_path)
            self.show_image()
    
    def show_image(self):
        if self.image:
            # Calculate zoomed dimensions
            width = int(self.image.width * self.zoom_level / 100)
            height = int(self.image.height * self.zoom_level / 100)

            # Resize image
            resized_image = self.image.resize((width, height), Image.ANTIALIAS)

            # Convert image to Tkinter-compatible format
            self.tk_image = ImageTk.PhotoImage(resized_image)  # Use self.tk_image

            # Update canvas with the new image
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)  # Use self.tk_image
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

            # Update status label with image size
            self.status_label.config(text="Image Size: {}x{}".format(width, height))

            self.root.geometry("{}x{}".format(width, height))
    
    def zoom_in(self):
        if self.zoom_level < 200:
            self.zoom_level += 10
            self.show_image()
    
    def zoom_out(self):
        if self.zoom_level > 20:
            self.zoom_level -= 10
            self.show_image()

# Create the main window
root = tk.Tk()

# Create the picture viewer instance
viewer = PictureViewer(root)

# Run the application
root.mainloop()