# -*- coding: utf-8 -*-

# written by Soo. 16.03.18.
media_flag = False
origin = open('home.css', 'r')
dest = open('home.scss', 'w')

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


media_flag = False
origin = open('simplelink.css', 'r')
dest = open('simplelink.scss', 'w')

line_list = origin.readlines()
for line in line_list:
    if media_flag:
        # in @media
        if line == '}\n':
            media_flag = False
            dest.write(line)
        else:
            dest.write('  #simplelink_page ' + line[2:])
    else:
        # not in @media
        if line.split()[0] == '@media':
            media_flag = True
            dest.write(line)
        else:
            dest.write('#simplelink_page ' + line)

origin.close()
dest.close()


media_flag = False
origin = open('team.css', 'r')
dest = open('team.scss', 'w')

line_list = origin.readlines()
for line in line_list:
    if media_flag:
        # in @media
        if line == '}\n':
            media_flag = False
            dest.write(line)
        else:
            dest.write('  #team_page ' + line[2:])
    else:
        # not in @media
        if line.split()[0] == '@media':
            media_flag = True
            dest.write(line)
        else:
            dest.write('#team_page ' + line)

origin.close()
dest.close()