from captcha.image import ImageCaptcha
import string
import random

#CONFIGURE IMG
img = ImageCaptcha(width=300, height=100)

#RANDOM TEXT OF CAPTCHA
text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

#GENERATE THE IMG WITH CAPTCHA
data = img.generate(text)

#SAVE THE IMG
img.write(text, 'captcha.jpg')

print(f'Captcha text: {text}')