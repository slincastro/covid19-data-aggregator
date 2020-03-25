try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


def binarize_image():
    col = Image.open("../../test/mark.png")
    gray = col.convert('L')
    bw = gray.point(lambda x: 0 if x<145 else 255, '1')
    bw.save("test/result_bw1.png")

#binarize_image()
print(ocr_core('../../test/result_bw1.png'))