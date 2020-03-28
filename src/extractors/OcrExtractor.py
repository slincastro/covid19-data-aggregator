try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pdf2image import convert_from_path

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

def pdf_to_image():
    pages = convert_from_path('https://www.gestionderiesgos.gob.ec/wp-content/uploads/2020/03/INFOGRAFIA-NACIONALCOVI-19-COE-NACIONAL-26032020-17h00-propuestav2.pdf', 500)
    print("---------------", pages)
    for page in pages:
        page.save('test/outs/out.jpg', 'JPEG')


def binarize_image():
    col = Image.open("../../test/outs/mark.png")
    gray = col.convert('L')
    bw = gray.point(lambda x: 0 if x<145 else 255, '1')
    bw.save("test/outs/result_bw1.png")

#binarize_image()
#print(ocr_core('../../test/outs/result_bw1.png'))

pdf_to_image()