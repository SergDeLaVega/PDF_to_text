import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# Укажи полный путь к Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_scanned_pdf(pdf_path):
    doc = fitz.open("00.pdf")
    full_text = ""

    for page_num in range(len(doc)):
        # Извлекаем изображение со страницы
        for img_index, img in enumerate(doc[page_num].get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            img = Image.open(io.BytesIO(image_bytes))

            # Распознаем текст с изображения
            text = pytesseract.image_to_string(img, lang="rus") # Укажите нужные языки
            full_text += f"\n--- Page {page_num + 1} ---\n{text}"

    return full_text

# Пример использования
pdf_path = "scan.pdf"
text = extract_text_from_scanned_pdf(pdf_path)

# Сохраняем результат в текстовый файл
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Текст успешно сохранён в output.txt!")
