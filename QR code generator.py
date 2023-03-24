# install needed libraries (pip)
# create a function that collects a text and convert into QR code
# save the QR code as an image
# run the function


import qrcode

def generate_qrcode(url,any_number):
    data = url + "\n" + any_number  # concatenate the URL and phone number
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 5,
    )

    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "Black",back_color = "white")
    img.save("qrimage01.png")

any_number = input("enter any_number: ")
url = input("enter your url: ")
generate_qrcode(url,any_number)
