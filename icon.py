
"""
Author：Robin·QI
Notes：将图片转换为ico格式
"""
 
# PythonMargick包可以到Unofficial Windows Binaries for Python Extension Packages下载
import pythonmagick as pm
 
img = pm.Image('favicon.png')
# 这里要设置一下尺寸，不然会报ico尺寸异常错误
img.sample('128x128')
img.write('favicon.ico')