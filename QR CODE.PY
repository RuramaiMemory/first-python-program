def generate_qr_code(data, filename):
    qr =qr.QRCode(
        version=1,
        box_size=20,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

data = "https://www.example.com"
filename = "example_qr_code.png"
generate_qr_code(data,filename)


 





