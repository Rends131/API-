#!usr/bin/env python
# -*- coding:utf-8 -*-
import os

base_url=os.path.dirname(os.path.dirname(__file__))

# print(os.path.join(base_url,'data','login.yaml'))

def filePath(fileDir='data',fileName='login.yaml'):
	"""

	:param fileDir:目录
	:param fileName:文件的名称
	:return:
	"""
	return os.path.join(
		os.path.dirname(os.path.dirname(__file__)),fileDir,fileName
	)

# print(filePath())
# print(filePath('common','public'))
# print(filePath(fileDir='',fileName='Readme.md'))