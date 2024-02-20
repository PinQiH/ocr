import pytesseract
from PIL import Image
import os
from dotenv import load_dotenv

# 從 .env 文件中加載環境變數
load_dotenv()

# 讀取環境變數
tesseract_cmd = os.getenv("TESSERACT_CMD")

# 設置 Tesseract 執行文件的路徑
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd # 將路徑替換為你的實際路徑

image = Image.open('captcha.png')
result = pytesseract.image_to_string(image)
print(result)