'''
1.下载王者荣耀高清壁纸图片
2.将不同人物的图片分别保存到临时文件夹
3.将不同人物的图片打包压缩证zip文件
4.移动图片到picture文件夹
'''

import requests
from urllib import parse
from urllib import request
import os
import tempfile
import zipfile
import shutil

# 存放无法下载的链接
un_download = []
