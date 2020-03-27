try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def binarize_image():
    col = Image.open("../../test/outs/mark.png")
    gray = col.convert('L')
    bw = gray.point(lambda x: 0 if x<145 else 255, '1')
    bw.save("test/result_bw1.png")

#binarize_image()
print(ocr_core('../../test/outs/result_bw1.png'))