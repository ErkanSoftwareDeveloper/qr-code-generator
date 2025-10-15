import io  # dosya ve bellek işlemleri için
import sys  # sistem işlemleri için
import webbrowser  # web tarayıcısını açmak için
from urllib.parse import urlparse  # URL ayrıştırma için

import qrcode  # QR kodu oluşturmak için
from PIL import Image, ImageTk  # Görüntü işlemleri için
import tkinter as tk  # GUI oluşturmak için
from tkinter import ttk, messagebox, filedialog, colorchooser  # Tkinter bileşenleri

# ---------------
# Pencere olustur
# ---------------

Desktop = tk.Tk()  # Ana pencere
Desktop.title("QR Link Generator")  # Pencere başlığı
Desktop.geometry("400x550")  # Pencere boyutu

# ---------------
# label yazi ekleme
# ---------------

# Label oluştur
lbl = ttk.Label(Desktop, text="Give the url to create a QR code")
lbl.pack(pady=10)  # Label ekle ve üstten boşluk bırak

# ---------------
# Entry kutusu ekleme
# ---------------

entry = ttk.Entry(Desktop, width=40)  # Entry kutusu oluştur
entry.pack(pady=5)  # Entry kutusu ekle ve üstten boşluk bırak

# ---------------
# Buton ekleme
# ---------------


def save_qr():
    global pil_img  # Görüntü değişkenini global yap
    try:
        foulder_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[
                                                    # Kaydetme diyalog kutusunu aç
                                                    ("PNG files", "*.png")])
        if foulder_path and pil_img:
            pil_img.save(foulder_path)  # Görüntüyü belirtilen yola kaydet
    except Exception:  # Hata durumunda
        pass  # Hata durumunda işlem yapma


def buton_click():
    global tk_img, pil_img  # Görüntü değişkenlerini global yap
    text = entry.get().strip()  # Entry kutusundaki metni al ve boşlukları temizle
    if not text:
        return  # Metin boşsa işlem yapma

    # QR kod nesnesi oluştur
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(text)  # Metni QR koda ekle
    qr.make(fit=True)  # QR kodu oluştur
    pil_img = qr.make_image(fill_color="black", back_color="white").convert(
        "RGB")  # QR kod görüntüsünü oluştur

    pil_img = pil_img.resize((300, 300))  # Görüntüyü yeniden boyutlandır

    # ---------------
    # Ttkinerda göstermek icin dönüstür
    # ---------------

    tk_img = ImageTk.PhotoImage(pil_img)  # PIL görüntüsünü Tkinter görünt
    canvas.delete("all")  # Önceki görüntüyü temizle
    canvas.create_image(150, 150, image=tk_img)  # canvas ortasina ciz

# ---------------
# Buton oluşturma
# ---------------


btn = ttk.Button(Desktop, text="Create QR Code",
                 command=buton_click)  # Buton oluştur
btn.pack(pady=10)  # Buton ekle ve üstten boşluk bırak

btn_save = ttk.Button(Desktop, text="Save as PNG", command=save_qr)
btn_save.pack(pady=10)  # Buton ekle ve üstten boşluk bırak


# ---------------
# Canvas ekle (önizleme)
# ---------------

canvas = tk.Canvas(Desktop, width=300, height=300, bg="#eee")  # Canvas oluştur
canvas.pack(pady=20)  # Canvas ekle ve üstten boşluk bırak

# ---------------
# pencereyi calistir
# ---------------
Desktop.mainloop()  # Ana döngüyü başlat
