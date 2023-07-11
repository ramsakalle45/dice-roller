import tkinter as tk
from PIL import Image, ImageTk
import random

# Create window
window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roller Game")

frame1 = tk.Frame(window, highlightbackground="blue", highlightthickness=2)
frame1.pack(padx=20, pady=20)

# List of dice images
dice = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]


# Function to resize the image to fit within the frame
def resize_image(image_path, frame_width, frame_height):
    image = Image.open(image_path)

    # Calculate the aspect ratio of the image
    aspect_ratio = image.width / image.height

    # Calculate the new width and height based on the frame dimensions and aspect ratio
    if frame_width / aspect_ratio <= frame_height:
        new_width = frame_width
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = frame_height
        new_width = int(new_height * aspect_ratio)

    # Resize the image using the calculated dimensions
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)


# Function to roll the dice
def roll_dice():
    # Select random dice images
    image1_path = random.choice(dice)
    image2_path = random.choice(dice)

    # Resize the images to fit within the frame
    image1 = resize_image(image1_path, 100, 100)
    image2 = resize_image(image2_path, 100, 100)

    # Update the dice images
    label1.configure(image=image1)
    label2.configure(image=image2)

    # Keep a reference to the images to prevent garbage collection
    label1.image = image1
    label2.image = image2


# Create dice labels
label1 = tk.Label(window)
label2 = tk.Label(window)

# label1.place(x=50, y=200)
# label2.place(x=50, y=200)

# Center align the dice labels
label1.place(relx=0.35, rely=0.5, anchor=tk.CENTER)
label2.place(relx=0.65, rely=0.5, anchor=tk.CENTER)

# Roll dice button
button = tk.Button(window, text="Roll Dice", command=roll_dice,
                   borderwidth=3, bg="#7FFFD4",
                   font=("Helvetica", 10, "bold"))
button.place(x=220, y=250)

window.mainloop()
