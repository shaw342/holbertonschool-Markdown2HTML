#!/usr/bin/python3
""" this is my function"""
import sys
import os.path

path = "/" + sys.argv[1]

check_file = os.path.isfile(path)

if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

if sys.argv[1].split("."):
    print("true")

if check_file == False:
    print("Missing README.md")
