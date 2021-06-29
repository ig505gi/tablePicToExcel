#-*- coding: UTF-8 -*- 
# 1.爬虫把图片爬下来
# 2.用ocr识别图片 pytesseract OR https://github.com/JaidedAI/EasyOCR
# 2.1 截取关键部分
# 2.2 去水印
# 2.3 变高清
# 2.4 增加对比度
# 2.5 根据横线特征旋转 https://stackoverflow.com/questions/53854066/pythonhow-to-rotate-an-image-so-that-a-feature-becomes-vertical python rotate picture to make a line horizontal 
# 2.6 水平和垂直投影，找到每一个表格 https://zhuanlan.zhihu.com/p/30391661 
# 2.7 ocr
# 2.8 组合成excel
# https://github.com/wei1111/Tess4JDemo

# pytesseract
import requests
from PIL import Image, ImageEnhance
import pytesseract

filename = './imgs/3.jpeg'
# 2.3 变高清
r = requests.post(
    "https://api.deepai.org/api/waifu2x",
    files={
        'image': open(filename, 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())

im = Image.open(filename)
# 2.1 截取关键部分
# 北京中医药大学
times = 1.6
cropped = im.crop((150 * times, 823 * times, (150 + 190) * times, (823 + 40) * times)) # (left, upper, right, lower)
# cropped = im.crop((150, 823 - 57, 150 + 190, 823 + 40 - 57))
im = cropped

# 2.2 去水印


# 2.4 增加对比度
im = ImageEnhance.Contrast(im).enhance(5.0)
im = ImageEnhance.Sharpness(im).enhance(2.0)

# ocr识别
# print(pytesseract.get_languages(config=''))
print(pytesseract.image_to_string(im, lang='chi_sim'))
im.show()


# easyocr
# import easyocr
# reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
# result = reader.readtext('./imgs/3.jpeg')
# print(result)