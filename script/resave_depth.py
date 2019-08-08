#!/usr/bin/env python
# -*- coding:utf-8 -*-

#**********************************
# read & resave depth image by cv2 of given dir
#**********************************

import open3d as o3d
import numpy as np
import sys
import os
import cv2

def list_all_files(rootdir):
    _files = []
    list = os.listdir(rootdir)
    for i in range(0,len(list)):
        file_name = list[i]
        path = os.path.join(rootdir,list[i])
        #if os.path.isdir(path):
        #   _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    _files.sort()
    return _files

if __name__ == "__main__":
    base_dir = "./dataset/"
    if(len(sys.argv) != 2):
        print("Must provide dir to show")
        sys.exit(0)

    root_dir = base_dir + sys.argv[1] + "/"
    depth_dir = root_dir + 'depth/'
    depth_files = list_all_files(depth_dir)
    for i in range(0, len(depth_files)):
        file_name = depth_files[i][-14:-4]
        print(file_name)
        dimg = cv2.imread(depth_files[i], -1);
        cv2.imwrite(root_dir + "depth2/" + file_name + ".png", dimg);


