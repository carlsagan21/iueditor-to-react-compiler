# -*- coding: utf-8 -*-

# written by Soo. 16.03.18.

media_flag = False
origin = open('class.scss', 'r')
dest = open('class2.scss', 'w')

line_list = origin.readlines()
for line in line_list:
    if line == '\n':
        dest.write('\n')
    else:
        if media_flag:
            # in @media
            if line == '}\n':
                media_flag = False
                dest.write(line)
            else:
                if line[2] == '.':
                    if '.dashboard-style-wrapper' in line[:26]:
                        dest.write(line)
                    else:
                        dest.write('  .dashboard-style-wrapper ' + line[2:])
                else:
                    dest.write(line)
        else:
            # not in @media
            if line.split()[0] == '@media':
                media_flag = True
                dest.write(line)
            else:
                if line[0] == '.':
                    if '.dashboard-style-wrapper' in line[:24]:
                        dest.write(line)
                    else:
                        dest.write('.dashboard-style-wrapper ' + line)
                else:
                    dest.write(line)

origin.close()
dest.close()