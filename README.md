"Этот проект использует Tesseract OCR для извлечения текста из сканированных PDF."
## Пошаговая инструкция:
1. Установите зависимости: pip install -r requirements.txt
2. Также необходимо установить сам Tesseract OCR:
    Windows: Скачать Tesseract - https://github.com/UB-Mannheim/tesseract/wiki
3. Установка Tesseract OCR на Windows
Скачать установщик
Перейдите на официальный репозиторий и скачайте последнюю версию:
👉 Tesseract OCR for Windows
Выберите tesseract-ocr-w64-setup-<версия>.exe.

Установить Tesseract

Запустите скачанный .exe файл.

На этапе выбора компонентов добавьте галочку на "Additional script data" и "Training data" (если хотите больше языков).

Обратите внимание на путь установки (по умолчанию: C:\Program Files\Tesseract-OCR).

Добавить Tesseract в переменные среды (если необходимо)

Откройте Пуск → найдите "Переменные среды".

В разделе "Системные переменные" найдите Path, нажмите Изменить.

Нажмите Создать и добавьте путь к tesseract.exe, 
C:\Program Files\Tesseract-OCR
Проверить установку
Откройте командную строку (cmd) и введите:
tesseract -v
Если все установлено правильно, появится версия Tesseract.

Установка русского языка
Если он не установился автоматически, скачайте русские языковые файлы (rus.traineddata) https://github.com/tesseract-ocr/tessdata/blob/main/rus.traineddata и поместите их в папку:
C:\Program Files\Tesseract-OCR\tessdata

4. Запустите проект: python pdf_text.py

