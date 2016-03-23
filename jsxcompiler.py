# -*- coding: utf-8 -*-

# written by Soo. 16.03.18.

origin = open('team.html', 'r')
dest = open('../../Bitbucket/airbridge-front-webpack/team_page.jsx', 'w')

dest.write(
    '''/* ===============================================
2016.03.18. Written by Soo Kim

TODO
-Must
-More
=================================================*/

var React = require('react')

module.exports = React.createClass({
  render: function () {
    return (
      <div id='''
)
dest.write("'team_page'" + ">\n")

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
    new_line = new_line.replace(' maxViewPort=', ' data-maxviewport=').replace(' minViewPort=', ' data-minviewport=')
    new_line = new_line.replace(' externalClose=', ' data-externalclose=').replace(' JQueryShowDuration=', ' data-jqueryshowduration=').replace(' JQueryShowAnimation=', ' data-jqueryshowanimation=')

    if '<img ' in new_line:
        new_line = new_line[:-2] + '/>\n'
    fixed_line_list.append(new_line)

for line in fixed_line_list:
    dest.write(line)

dest.write(
    '''      </div>
    )
  }
})
'''
)