from PIL import Image, ImageDraw, ImageFont
import pandas as pd
form = pd.read_excel("E:/name.xlsx")
name_list = form['NAME'].to_list()
for i in name_list:
    im = Image.open(r'template12.jpg')
    d = ImageDraw.Draw(im)
    location = (242,260)
    text_color = (0,0,0)
    font = ImageFont.truetype("C:/Users/Madhushree/MLSJN.TTF", 40)
    d.text(location, i, fill = text_color, font = font)
    im.save("E:\certificate_\certificate_" + i + ".pdf")