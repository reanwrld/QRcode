
# QR Code Generator (Python Project)

This project generates QR codes for personal links using Python.

## 📌 Description

The script creates QR codes for:
- GitHub profile
- LinkedIn profile

Each link is converted into a QR image and saved as a `.png` file.

---

## 🛠️ Technologies Used

- Python
- qrcode library
- PIL (Pillow) via qrcode dependency

---

## 📂 Files in this project

- `app.py` → Main Python script that generates QR codes  
- `github_qr.png` → QR code for GitHub profile  
- `linkedin_qr.png` → QR code for LinkedIn profile  

---

## 🚀 How it works

The script:
1. Stores links in a dictionary
2. Loops through each link
3. Generates a QR code using the `qrcode` library
4. Saves each QR code as an image file

---

## 💻 Code Overview

```python
import qrcode 

links = {
    "github": "https://github.com/reanwrld",
    "linkedin": "https://www.linkedin.com/in/reyan-h-724314350/"
}

for name, url in links.items():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H, 
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    filename = f"{name}_qr.png"
    img.save(filename)
    print(f"Generated: {filename}")
