#!/usr/bin/python

import sys
from blog_util import *

def help_menu():
    print('''
        arg1: md dir. For instance, md/ref/python/pandas
    ''')

def check_arg():
    print(len(sys.argv))
    sys.exit(0)
    if len(sys.argv)==1:
        help_menu()
        sys.exit(0)

def main():
    check_arg()
    check_html_directory()
    create_html_files(get_all_markdown_files(get_md_path()))
    mv_image_files()

if __name__ == "__main__":
    main()


