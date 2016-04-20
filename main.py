# -*- coding: utf-8 -*-

from html_to_jsx_converter import html_to_jsx
from css_prefixer import css_prefix
from move_images import move_resource
from shutil import rmtree
import os

file_list = raw_input('파일명을 입력하세요: ').split()
rmtree('./result')
os.mkdir('./result')

html_to_jsx(file_list)
css_prefix(file_list)
move_resource()