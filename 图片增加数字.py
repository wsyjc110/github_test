from PIL import Image,ImageDraw,ImageFont,ImageColor
def add_num(im):
    draw = ImageDraw.Draw(im)
    myfont = ImageFont.truetype(r'C:\Windows\Fonts\SIMYOU.TTF',size=50)
    fillcolor = ImageColor.colormap.get('black')
    draw.text((im.size[0]-200,0), '9', fill=fillcolor, font=myfont)
    im.save('test_af.jpg','jpeg')
    return 0
if __name__ == '__main__':
    im = Image.open(r'F:\eclipse workspace\TestPython\MOOC\test_be.jpg')
    add_num(im)
    print('执行完毕~~~~~')