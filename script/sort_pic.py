#!/usr/bin/env python
# -*- coding:utf-8 -*-

#******************************************************
# sort pics by name and move to diff dir
#******************************************************

import cv2
import numpy as np
import os

def list_all_depth_files(rootdir):
    _files = []
    list = os.listdir(rootdir)
    for i in range(0,len(list)):
        file_name = list[i];
        path = os.path.join(rootdir,list[i])
        #if os.path.isdir(path):
        #   _files.extend(list_all_files(path))
        if os.path.isfile(path) and file_name[0:5] == "Depth":
            _files.append(path)
    _files.sort()
    return _files

def list_all_rgb_files(rootdir):
    _files = []
    list = os.listdir(rootdir)
    for i in range(0,len(list)):
        file_name = list[i];
        path = os.path.join(rootdir,list[i])
        #if os.path.isdir(path):
        #   _files.extend(list_all_files(path))
        if os.path.isfile(path) and file_name[0:5] == "Color":
            _files.append(path)
    _files.sort()
    return _files

def trans_depth_file(filePath, num):
    depth_img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    if depth_img is None:
        return
    path = "./out/depth/depth{:0>5d}.png".format(num)
    print(path)
    cv2.imwrite(path, depth_img)

def trans_rgb_file(filePath, num):
    rgb_img = cv2.imread(filePath, cv2.IMREAD_COLOR)
    if rgb_img is None:
        return
    path = "./out/image/image{:0>5d}.png".format(num)
    print(path)
    cv2.imwrite(path, rgb_img)

if __name__ == "__main__":
    files = list_all_depth_files('./pic/')
    for i in range(0, len(files)):
        trans_depth_file(files[i], i)
    files = list_all_rgb_files('./pic/')
    for i in range(0, len(files)):
        trans_rgb_file(files[i], i)

