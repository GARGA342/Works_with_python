import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

#CREATE QRCODE
qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 4)

qr.add_data('https://github.com/GARGA342/')
qr.make(fit = True)

img = qr.make_image(fill_color='black', back_color='white').convert('RGB')
img.save("qrcode.png")

#READ QRCODE
read = decode(Image.open('qrcode.png'))
print(read[0].data)