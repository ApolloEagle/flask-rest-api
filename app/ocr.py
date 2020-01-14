try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def read_file(file):
    output = pytesseract.image_to_string(Image.open(file))
    return output