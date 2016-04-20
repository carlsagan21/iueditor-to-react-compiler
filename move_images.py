import os
import shutil

def move_resource():
    src = './airbridge/resource/project'
    src_files = os.listdir(src)
    os.mkdir('./result/resource')
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        shutil.copyfile(full_file_name, os.path.join('./result/resource/', file_name))