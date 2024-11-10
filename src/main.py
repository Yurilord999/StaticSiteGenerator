from textnode import *
from htmlnode import *
from markdown_converter import *
from markdown_blocks import *
import os.path
import shutil


def main():
    public_path = "/home/yurilord/workspace/github.com/Yurilord999/static_site_generator/public"
    static_path = "/home/yurilord/workspace/github.com/Yurilord999/static_site_generator/static"
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    static_dir = os.listdir(static_path)
    copy_files(static_dir, static_path, public_path)
    print("done")

def copy_files(dir, static_path, public_path):
    for file in dir:
        if os.path.isfile(os.path.join(static_path, file)):
            shutil.copy(os.path.join(static_path, file), os.path.join(public_path, file))
        else:
            public_subfolder_path = os.path.join(public_path, file)
            static_subfolder_path = os.path.join(static_path, file)
            os.mkdir(public_subfolder_path)
            subfolder_dir = os.listdir(static_subfolder_path)
            copy_files(subfolder_dir, static_subfolder_path, public_subfolder_path)
     
    

main()
