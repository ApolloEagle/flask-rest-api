from PIL import Image
import pytesseract
from io import BytesIO
import base64

pytesseract.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'


def read_file(file):
    output = pytesseract.image_to_string(Image.open(BytesIO(base64.b64decode(file))))
    return output