# coding=utf-8

import urllib

import re
#
# def getHtml(url):
#
#     page = urllib.urlopen(url)
#
#     html = page.read()
#
#     return html
#
# def getImg(html):
#
#     reg = r'src="(.+?\.jpg)"'
#
#     imgre = re.compile(reg)
#
#     imglist = re.findall(imgre,html)
#
#     x = 0
#
#     for imgurl in imglist:
#
#         urllib.urlretrieve(imgurl,'/home/jean/workspace/ROCHE/grab/%s.jpg' % x)
#
#         x += 1
#
#
#
# print urllib.urlretrieve('http://cytomine-core/api/userannotation/45867/crop.png', '../grab/thumb.jpg')
#
# print urllib.urlretrieve('https://imgsa.baidu.com/forum/pic/item/b145d688d43f8794d3f1538adb1b0ef41bd53a03.jpg', '../grab/123.jpg')

# html = getHtml("https://tieba.baidu.com/")
#
# print getImg(html)

# print 'over'

#
# import cv2
#
# import numpy as np
#
# import os
#
# import re
#
# idc_path = '../other/IDCdemo/1000/'
#
# filelist = os.listdir(idc_path)
#
# image = np.zeros((23 * 32, 41 * 32, 3), np.uint8)
#
# for filename in filelist:
#
#     patch = cv2.imread(idc_path + filename)
#
#     height, width, dim = patch.shape
#
#     coor = re.findall(r"\d+\.?\d*", filename)
#
#     ox, oy = int(coor[2]), int(coor[3])
#
#     y, x = (ox - 1) * height, (oy - 1) * width
#
#     image[x: x + height, y: y + width] = patch
#
# cv2.imshow('merge', image)
# # cv2.waitKey()
# cv2.imwrite('../other/IDCdemo/res.bmp', image)
#
# # -----------------------------------------------
#
# idc_path = '../other/IDCdemo/1000p/'
#
# filelist = os.listdir(idc_path)
#
# image0 = np.zeros((23 * 32, 41 * 32, 3), np.uint8)
#
# for filename in filelist:
#
#     if filename[-8: -4] != 'lass':
#
#         continue
#
#     patch = cv2.imread(idc_path + filename)
#
#     height, width, dim = patch.shape
#
#     coor = re.findall(r"\d+\.?\d*", filename)
#
#     ox, oy = int(coor[2]), int(coor[3])
#
#     y, x = (ox - 1) * height, (oy - 1) * width
#
#     image0[x: x + height, y: y + width] = patch
#
# cv2.imshow('merge0', image0)
# cv2.waitKey()
# cv2.imwrite('../other/IDCdemo/res0.bmp', image0)




