import pytesseract
import cv2
from pdf2image import convert_from_path
from PIL import Image
poppler_path=r'C:/Program Files/poppler-0.68.0/bin'

def pdf_imagen(pdf):
    # import module
    pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract'
    pages = convert_from_path(pdf,500,poppler_path)
    for i in range(len(pages)):
        ruta_imagen = 'pdf_leido/page'+ str(i) +'.jpg'
        pages[i].save(ruta_imagen, 'JPEG')
        print('Ruta de la imagen',ruta_imagen)
    print('Termino la conversion')
    return ruta_imagen

def extraerTexto_imagen(palabra,imagen):
    image_path =imagen
    #path_to_tesseract = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    img = Image.open(image_path) 
    #pytesseract.tesseract_cmd = path_to_tesseract 
    text = pytesseract.image_to_string(img) 
    r=text.find(palabra) 
    if r!=-1:
        print('Se encontro')
    else:
        print('No encontro')

def extraer_texto(imagen):
    pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract'
    image = cv2.imread(imagen)
    text=pytesseract.image_to_string(image,lang='spa')
    print('texto: ',text)
