from PIL import Image
import pytesseract
from io import BytesIO
import base64

pytesseract.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'


def read_file(file):
    file = Image.open(BytesIO(base64.b64decode(file)))
    updatefile = file.convert('1')
    output = pytesseract.image_to_string(updatefile)
    return output