# -*- coding: utf-8 -*-

# written by Soo. 16.03.18.
# style fix needed

from time import strftime, localtime
import re
import os

def html_to_jsx(file_list):
    os.mkdir('./result/jsx')
    for file in file_list:
        origin = open('./airbridge/' + file + '.html', 'r')
        dest = open('./result/jsx/' + file + '.jsx', 'w')

        dest.write(
            '/* ===============================================\n' +
            strftime('%y.%m.%d.', localtime()) + (' Written by Soo Kim\n'
                                                  '\n'
                                                  'TODO\n'
                                                  '-Must\n'
                                                  '-More\n'
                                                  '=================================================*/\n'
                                                  '\n'
                                                  'import React, {Component} from \'react\'\n'
                                                  '\n'
                                                  'class ' + file.title() + ' extends Component {\n'
                                                  '  render () {\n'
                                                  '    return (\n'
                                                  '      <div id=')
        )
        dest.write("'" + file + "_page'" + ">\n")

        line_list = origin.readlines()
        cnt = 0
        body_start = None
        body_end = 0
        for line in line_list:
            if '<body>' in line:
                body_start = cnt
            if '</body>' in line:
                body_end = cnt
            cnt += 1

        body_line_list = line_list[body_start+1:body_end]

        fixed_line_list = []
        for line in body_line_list:
            # fit indent
            new_line = '    ' + line
            # replace " with '
            new_line = new_line.replace('"', "'")
            # class to className
            new_line = new_line.replace(' class=', ' className=')

            # style fix
            # new_line = new_line.replace
            # frameborder
            new_line = new_line.replace(' frameborder=', ' frameBorder=')

            new_line = new_line.replace(' panelButtonTargetId=', ' data-panelbuttontargetid=')
            new_line = re.sub(r'\smaxViewPort=(\d+)', r' data-maxviewport={\1}', new_line)
            new_line = re.sub(r'\sminViewPort=(\d+)', r' data-minviewport={\1}', new_line)

            new_line = new_line.replace(' externalClose=', ' data-externalclose=').replace(' JQueryShowDuration=', ' data-jqueryshowduration=').replace(' JQueryShowAnimation=', ' data-jqueryshowanimation=')

            new_line = re.sub(r"(<img)(\s+)(className='[\w\s]+')(\s+)(src='.+')(>)", r'\1\2\3\4\5/>', new_line)

            fixed_line_list.append(new_line)

        for line in fixed_line_list:
            dest.write(line)

        dest.write(
            '      </div>\n'
            '    )\n'
            '  }\n'
            '})\n'
            ''
        )

        origin.close()
        dest.close()