import pdfplumber
import pytesseract
from PIL import Image
import io

def extract_text(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text.lower()

    elif filename.endswith((".png", ".jpg", ".jpeg")):
        image = Image.open(file)
        return pytesseract.image_to_string(image).lower()

    return ""
    

def extract_data(text):
    import re
    return {
        "weight": re.findall(r'(\d+[.,]?\d*)\s*(kg)', text),
        "packages": re.findall(r'(\d+)\s*(ctn|carton)', text),
        "total": re.findall(r'(\d+[.,]?\d+)', text)
    }
