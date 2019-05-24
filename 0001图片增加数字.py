from PIL import Image,ImageDraw,ImageFont,ImageColor
def add_num(im):
    #创建一个draw对象
    draw = ImageDraw.Draw(im)
    #设置字体和大小
    myfont = ImageFont.truetype(r'C:\Windows\Fonts\SIMYOU.TTF',size=50)
    #设置颜色
    fillcolor = ImageColor.colormap.get('black')
    #设置文本和在图片上哪里画
    draw.text((im.size[0]-200,0), '9', fill=fillcolor, font=myfont)
    #保存
    im.save('test_af.jpg','jpeg')
    return 
if __name__ == '__main__':
    im = Image.open(r'F:\eclipse workspace\TestPython\MOOC\test_be.jpg')
    add_num(im)
    print('执行完毕~~~~~')
