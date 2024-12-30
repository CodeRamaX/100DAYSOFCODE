import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def create_collage(folder_path):
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
    if not image_files:
        return None

    images = [Image.open(os.path.join(folder_path, file)) for file in image_files]

    # Resize images to a uniform size
    width, height = 100, 100
    resized_images = [img.resize((width, height)) for img in images]

    # Determine collage size
    cols = 5
    rows = (len(resized_images) + cols - 1) // cols
    collage_width = cols * width
    collage_height = rows * height

    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))

    for index, img in enumerate(resized_images):
        x = (index % cols) * width
        y = (index // cols) * height
        collage.paste(img, (x, y))

    return collage

def open_folder():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    collage = create_collage(folder_path)
    if collage:
        collage.thumbnail((600, 600))
        collage_tk = ImageTk.PhotoImage(collage)
        canvas.config(width=collage_tk.width(), height=collage_tk.height())
        canvas.create_image(0, 0, anchor=tk.NW, image=collage_tk)
        canvas.image = collage_tk
    else:
        canvas.delete("all")
        canvas.create_text(150, 150, text="No images found in the folder", fill="red")

# Create the main window
root = tk.Tk()
root.title("Image Collage Viewer")

# Create a button to select folder
button = tk.Button(root, text="Select Folder", command=open_folder)
button.pack()

# Create a canvas to display the collage
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

root.mainloop()
