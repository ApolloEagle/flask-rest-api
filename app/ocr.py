from PIL import Image
import pytesseract
import tesseract
from io import BytesIO
import base64


def read_file(file):
    output = pytesseract.image_to_string(Image.open(BytesIO(base64.b64decode(file))))
    return output