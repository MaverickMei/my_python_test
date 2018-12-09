#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from PIL import Image
import

#读入图片PIL.ImageOps
image = Image.open(r'C:\Users\mcc\Desktop\hyxd.jpg')

#反转颜色
inverted_image = PIL.ImageOps.invert(image)

#保存图片
inverted_image.save(r'C:\Users\mcc\Desktop\new_hyxd.jpg')