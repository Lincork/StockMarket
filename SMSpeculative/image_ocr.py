
from PIL import Image
import pytesseract
import pandas as pd


# 打开图像文件
image_path = '/Users/xnzi/StockMarket/SMSpeculative/WechatIMG638.jpg'
img = Image.open(image_path)

# 设置语言
language = 'chi_sim'

# 使用 pytesseract 进行文字识别
text = pytesseract.image_to_string(img, lang=language)

# 打印识别结果
print("识别的文字：")
print(text)

# 将文本按行分割并去除空行
lines = [line.strip() for line in text.split('\n') if line.strip()]

# 将每行文本按逗号分隔，创建二维列表
data = [line.split(',') for line in lines]

# 创建 Pandas DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# 打印 DataFrame
print("Pandas DataFrame:")
print(df)



