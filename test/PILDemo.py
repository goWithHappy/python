from  PIL import Image,ImageFilter
#测试PIL
# im=Image.open('./picture/1.jpg')
# w,h=im.size
# #输出图像的格式
# print('the picture size is:%s,%s'%(w,h))
# #对图像进行操作
# im.thumbnail((w/5,h/5))
# print('Resize image to:%s,%s'%(w/2,h/2))
# #把缩放的图形用jpeg格式来进行保存
# im.save('thumbnail.jpg','jpeg')
#实现模糊效果
Im=Image.open('./picture/2.jpg')
im2 = Im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
