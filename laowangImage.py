from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class laowangImage:
    Image = None
    Draw = None

    # 创建一个白色画布
    def new_image(self, width=400, height=400, mode='RGBA', color=(255, 255, 255)):
        self.Image = Image.new(mode=mode, size=(width, height), color=color)

        self.Draw = ImageDraw.Draw(self.Image)
        return

    # 打开一个现有的图片
    def load_image(self, filename, filepath=''):
        fp = os.path.join(filepath, filename)
        self.Image = Image.open(fp)

        self.Draw = ImageDraw.Draw(self.Image)
        return

    # 展示图片
    def show(self):
        if self.Image:
            self.Image.show()
        else:
            print('请先new_image或者load_image')

    # 保存图片
    def save(self, filename, filepath=''):
        if self.Image:
            fp = os.path.join(filepath, filename)
            self.Image.save(fp)
        else:
            print('请先new_image或者load_image')

    # 保存为文件流
    def save_on_memory(self, formater='PNG'):
        img = io.BytesIO()
        self.Image.save(img, format=formater)
        output = img.getvalue()
        return output

    # 添加一条线
    def add_line(self, start=(0, 0), end=(255, 255), color=(0, 0, 0), width=1):
        '''

        :param start: 起点坐标
        :param end: 终点坐标
        :param color: 颜色
        :param width: 宽度
        :return:
        '''
        self.Draw.line(start + end, fill=color, width=width)
        return

    #画一个矩形
    def add_square(self,start=(0, 0), end=(255, 255),bg_color=(255,255,255),out_line_color=(0,0,0),out_line_width=1):
        self.Draw.rectangle(start+end,fill=bg_color,outline=out_line_color,width=out_line_width)
        return

    #画一个弧线
    def add_bow_line(self, start=(0, 0), end=(255, 255),start_angle=0,end_angle=90, color=(0, 0, 0), width=1):
        self.Draw.arc(start+end,start_angle,end_angle,fill=color,width=width)
        return

    #画一个弦
    def add_chord(self,start=(0, 0), end=(255, 255),start_angle=0,end_angle=90,bg_color=(255,255,255),out_line_color=(0,0,0),out_line_width=1):
        self.Draw.chord(start+end,start_angle,end_angle,fill=bg_color,outline=out_line_color,width=out_line_width)
        return

    #画一个饼
    def add_pie_slice(self,start=(0, 0), end=(255, 255),start_angle=0,end_angle=90,bg_color=(255,255,255),out_line_color=(0,0,0),out_line_width=1):
        self.Draw.pieslice(start+end,start_angle,end_angle,fill=bg_color,outline=out_line_color,width=out_line_width)
        return

    #画一个园
    def add_circle(self,start=(0, 0), end=(255, 255),bg_color=(255,255,255),out_line_color=(0,0,0),out_line_width=1):
        self.Draw.ellipse(start+end,fill=bg_color,outline=out_line_color,width=out_line_width)
        return

    #绘制多边形
    def add_polygon(self,xy=(0,0,255,0,255,255),bg_color=(255,255,255),out_line_color=(0,0,0)):
        self.Draw.polygon(xy,fill=bg_color,outline=out_line_color)
        return

    #设置字体
    def set_font(self,file_name,file_path='',size=10):
        fp=os.path.join(file_path,file_name)
        font= ImageFont.truetype(fp,size)
        return font

    #插入字体
    def add_font(self,text,xy=(255,255),color=(0,0,0),font=None,align='left',spacing=4,**kwargs):
        '''
        :param xy: 起始坐标
        :param color: 颜色
        :param font: 字体
        :param align: 对齐
        :param spacing: 间隔
        :param kwargs:
            xy,
            text,
            fill=None,
            font=None,
            anchor=None,
            spacing=4,
            align="left",
            direction=None,
            features=None,
            language=None,
            stroke_width=0,
            stroke_fill=None,
            embedded_color=False,
        :return:
        '''
        self.Draw.text(xy,text=text,fill=color,font=font,align=align,spacing=spacing,**kwargs)
        return

    #插入图片
    def add_image(self,filename,file_path='',xy=(0,0),resize=None):
        img=Image.open(os.path.join(file_path,filename))
        if resize:
            img=img.resize(resize,Image.ANTIALIAS)
        self.Image.paste(img,xy)
        return

    #修改图片大小
    def resize(self,width=None,height=None):
        if width or height:
            size = self.Image.size
            if not height:
                height = width / size[0] * size[1]
            elif not width:
                width = height / size[1] * size[0]

            self.Image=self.Image.resize((int(width),int(height)),Image.ANTIALIAS)

    #裁剪图片
    def crop_image(self,xy=(0,0,100,100)):
        self.Image=self.Image.crop(xy)
        return
