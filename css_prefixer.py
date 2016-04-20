# -*- coding: utf-8 -*-
import os

# written by Soo. 16.03.18.
def css_prefix(file_list):
    os.mkdir('./result/css')
    for file in file_list:
        media_flag = False
        origin = open('./airbridge/resource/css/pages/' + file + '.css', 'r')
        dest = open('./result/css/' + file + '.css', 'w')

        line_list = origin.readlines()
        for line in line_list:
            if media_flag:
                # in @media
                if line == '}\n':
                    media_flag = False
                    dest.write(line)
                else:
                    dest.write('  #' + file + '_page ' + line[2:])
            else:
                # not in @media
                if line.split()[0] == '@media':
                    media_flag = True
                    dest.write(line)
                else:
                    dest.write('#' + file + '_page ' + line)

        origin.close()
        dest.close()