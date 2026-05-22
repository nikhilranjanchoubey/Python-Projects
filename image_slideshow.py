from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image Paths
image_paths = [
    r"C:\Users\choub\OneDrive\Pictures\Screenshots\Screenshot 2026-02-27 225907.png",
    r"C:\Users\choub\OneDrive\Pictures\Screenshots\Screenshot 2026-04-13 221601.png",
    r"C:\Users\choub\OneDrive\Pictures\Screenshots\Screenshot (36).png",
    r"C:\Users\choub\OneDrive\Pictures\Screenshots\Screenshot (61).png",
    r"C:\Users\choub\OneDrive\Pictures\Screenshots\Screenshot 2026-04-28 165500.png",
]

# Resize images
image_size = (1080, 1080)

images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(img) for img in images]

# Create cycle iterator
slideshow = cycle(photo_images)

# Label to show images
label = tk.Label(root)
label.pack()

# Function to update image
def update_image():
    photo = next(slideshow)
    label.config(image=photo)
    label.image = photo

    # Call again after 3 seconds
    root.after(3000, update_image)

# Start slideshow
play_button = tk.Button(root, text="Play Slideshow", command=update_image)
play_button.pack()

root.mainloop()