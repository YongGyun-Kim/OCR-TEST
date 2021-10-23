import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

a = Image.open("tt.png")
result = pytesseract.image_to_string(a)
print(result)