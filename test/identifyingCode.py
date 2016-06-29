#progrem：
#       用来生成验证码
#生成随机字母
import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter

def rndChar():
    return chr(random.randint(65,90))
#生成随机颜色1
def randColer():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#生成随机颜色2：
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
#设置图片的宽和高
width=240
height=60
image=Image.new('RGB',(width,height),(255,255,255))
#创建font对象
font=ImageFont.truetype('./Font/Arial.ttf',36)
#创建Draw对象
draw=ImageDraw.Draw(image)
#对背景使用四个元素进行填充
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=randColer())
#输出文字
for t in  range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#对图像进行模糊处理image=image.filter(ImageFilter.BLUR)
image.save('./AimPicture/randCode.jpg','jpeg')
