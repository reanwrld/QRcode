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