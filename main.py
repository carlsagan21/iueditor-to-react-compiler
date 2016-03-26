# -*- coding: utf-8 -*-

from jsxcompiler import html_to_jsx
from prefixer import css_prefixer

file_list = raw_input('파일명을 입력하세요: ').split()

html_to_jsx(file_list)
css_prefixer(file_list)