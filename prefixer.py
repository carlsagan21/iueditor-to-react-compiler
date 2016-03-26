# -*- coding: utf-8 -*-

# written by Soo. 16.03.18.
def css_prefixer(file_list):
    for file in file_list:
        media_flag = False
        origin = open('./airbridge/resource/css/pages/' + file + '.css', 'r')
        dest = open('./result/' + file + '.scss', 'w')

        line_list = origin.readlines()
        for line in line_list:
            if media_flag:
                # in @media
                if line == '}\n':
                    media_flag = False
                    dest.write(line)
                else:
                    dest.write('  #home_page ' + line[2:])
            else:
                # not in @media
                if line.split()[0] == '@media':
                    media_flag = True
                    dest.write(line)
                else:
                    dest.write('#home_page ' + line)

        origin.close()
        dest.close()