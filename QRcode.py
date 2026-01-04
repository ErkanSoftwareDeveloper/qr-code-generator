# ---------------------
# --- LIBRARIES ---
# ---------------------
import io  # For file and memory operations (input/output streams)
import sys  # For system-level operations and parameters
import webbrowser  # To open URLs in the default web browser
from urllib.parse import urlparse  # To parse and validate URLs

import qrcode  # Library to generate QR codes
from PIL import Image, ImageTk  # PIL for image manipulation, ImageTk to show images in Tkinter
import tkinter as tk  # Tkinter GUI library
from tkinter import ttk, messagebox, filedialog, colorchooser
# ttk: themed Tkinter widgets
# messagebox: for popup dialogs like info/error
# filedialog: for file open/save dialogs
# colorchooser: for choosing colors (not used here but imported)

# ---------------------
# --- MAIN WINDOW ---
# ---------------------
Desktop = tk.Tk()  # Create main Tkinter window
Desktop.title("QR Link Generator")  # Set window title
Desktop.geometry("400x550")  # Set window size (width x height)

# ---------------------
# --- LABEL ---
# ---------------------
lbl = ttk.Label(Desktop, text="Give the url to create a QR code")  # Create label widget
lbl.pack(pady=10)  # Add label to window and give vertical padding

# ---------------------
# --- ENTRY BOX ---
# ---------------------
entry = ttk.Entry(Desktop, width=40)  # Create entry box for user input
entry.pack(pady=5)  # Add entry box to window with vertical padding

# ---------------------
# --- BUTTON FUNCTIONS ---
# ---------------------

# Function to save QR code image
def save_qr():
    global pil_img  # Use global PIL image variable
    try:
        foulder_path = filedialog.asksaveasfilename(
            defaultextension=".png",  # Default file extension
            filetypes=[("PNG files", "*.png")]  # Allow only PNG files
        )
        if foulder_path and pil_img:  # If a path is selected and image exists
            pil_img.save(foulder_path)  # Save the image to the specified path
    except Exception:  # Catch any exception
        pass  # Do nothing if an error occurs

# Function triggered by "Create QR Code" button
def buton_click():
    global tk_img, pil_img  # Make image variables global so they persist
    text = entry.get().strip()  # Get text from entry box and remove leading/trailing spaces
    if not text:
        return  # If text is empty, do nothing

    # Create QR code object
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(text)  # Add the input text to QR code
    qr.make(fit=True)  # Generate QR code

    pil_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    # Convert QR code to RGB PIL image

    pil_img = pil_img.resize((300, 300))  # Resize image to 300x300 pixels

    # ---------------------
    # --- CONVERT TO TKINTER IMAGE ---
    # ---------------------
    tk_img = ImageTk.PhotoImage(pil_img)  # Convert PIL image to Tkinter-compatible image
    canvas.delete("all")  # Clear previous image on canvas
    canvas.create_image(150, 150, image=tk_img)  # Draw new image at center of canvas

# ---------------------
# --- BUTTONS ---
# ---------------------
btn = ttk.Button(Desktop, text="Create QR Code", command=buton_click)
# Create button to generate QR code, linked to buton_click function
btn.pack(pady=10)  # Add button to window with vertical padding

btn_save = ttk.Button(Desktop, text="Save as PNG", command=save_qr)
# Create button to save QR code, linked to save_qr function
btn_save.pack(pady=10)  # Add button to window with vertical padding

# ---------------------
# --- CANVAS (PREVIEW) ---
# ---------------------
canvas = tk.Canvas(Desktop, width=300, height=300, bg="#eee")  
# Create canvas to display QR code image, 300x300 size, light gray background
canvas.pack(pady=20)  # Add canvas to window with vertical padding

# ---------------------
# --- RUN MAIN LOOP ---
# ---------------------
Desktop.mainloop()  # Start Tkinter event loop to keep the window running
