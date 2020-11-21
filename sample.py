from laowangImage import laowangImage

class ft_send_image_stu_attend:
    pic_path='/work/'
    pic_bg='bg.png'

    text = '''　　扒拉扒拉扒拉吧把'''

    def run(self):
        
        data=[{
            'class_name':'朗文英语S4（中外联教）（3）',
            'weekday':'周五 17:50-20:20',
            'stu_name':'阎萧萌,韩佳昕',
        }]

        for dat in data:
            image = laowangImage()
            image.load_image(self.pic_bg, self.pic_path)

            #设置字体
            font=self.set_font(image)

            #各位家长
            image.add_font('各位家长:', (45, 75), color='#FFFFFF', font=font['H2'], stroke_width=1)

            #说明
            self.set_content(self.text,image,font)

            #写班级名称
            image.add_font(dat['class_name'],(40,335),color='#FEFEFE',font=font['H1'],stroke_width=1)

            #写班级编号
            image.add_font(dat['weekday'],(77,397),color='#1B4AE2',font=font['H2'])

            #插入学员姓名
            self.set_stu(dat['stu_name'],image,font)

            # o=image.save_on_memory()

            image.show()

    


    def set_content(self,text,image,font):
        x=21
        new_text=''
        for i,t in enumerate(text,1):
            if i%x==0:
                t=f'{t}\n'
            new_text+=t
        image.add_font(new_text, (45, 134), color='#FFFFFF', font=font['H2'],spacing=10)
        return


    def set_stu(self,stu,image,font):
        x=xx=74
        yy=554

        fix_x=167
        fix_y=76

        col_num=4
        stu=stu.split(',')
        i=0
        for name in stu:
            name=f'{name[0]}　{name[-1]}' if len(name)==2 else name
            i+=1
            image.add_font(name,(xx,yy),color='#3B3A38',font=font['H2'])
            xx+=fix_x
            if i==col_num:
                i=0
                xx=x
                yy+=fix_y
        return


    def set_font(self,image):
        result={}
        result['H1']=image.set_font('msyh.ttc',self.pic_path,42)
        result['H2']=image.set_font('msyh.ttc',self.pic_path,32)
        return result
