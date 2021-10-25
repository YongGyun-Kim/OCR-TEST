import pytesseract
from PIL import Image


# pytesseract pillow pymupdf
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# import fitz
# doc = fitz.open("aa.pdf")
# page = doc.load_page(1)
# mat = fitz.Matrix(2,2)
# pix = page.get_pixmap(matrix = mat)
# output = "aa.png"
# pix.save(output)

image = Image.open("tt.png")
result = pytesseract.image_to_string(image)
print(result)