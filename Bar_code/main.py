from barcode import EAN13
from barcode.writer import ImageWriter

with open(r'barcode.png', 'wb') as f:
    EAN13('1234567890987', writer = ImageWriter()).write(f)