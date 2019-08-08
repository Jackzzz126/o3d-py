#!/usr/bin/env python
# -*- coding:utf-8 -*-

#**********************************
# show image/depth/pcd of given dir
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

    pinhole_camera_intrinsic = o3d.io.read_pinhole_camera_intrinsic(
            "./TestData/camera_kinect3.json")

    root_dir = base_dir + sys.argv[1] + "/"
    color_dir = root_dir + 'image/'
    depth_dir = root_dir + 'depth/'
    color_files = list_all_files(color_dir)
    depth_files = list_all_files(depth_dir)
    if len(color_files) == 0 or len(depth_files) == 0:
        print("Can't find file")
        sys.exit(0)

    print(color_files[0])
    print(depth_files[0])
    color_img = o3d.io.read_image(color_files[0])
    depth_img = o3d.io.read_image(depth_files[0])
#    t = cv2.imread(depth_files[0], -1);
#    cv2.imwrite("d.png", t);
#    depth_img = o3d.io.read_image("d.png")

    rgbd_img = o3d.geometry.create_rgbd_image_from_color_and_depth(
            color_img, depth_img)

    pcd = o3d.geometry.create_point_cloud_from_rgbd_image(
        rgbd_img, pinhole_camera_intrinsic)

    print(color_img)
    print(depth_img)
    print(rgbd_img)
    print(pcd)
    o3d.visualization.draw_geometries([color_img], "Open3D", 800, 600, 800, 400)
    o3d.visualization.draw_geometries([depth_img], "Open3D", 800, 600, 800, 400)
    o3d.visualization.draw_geometries([pcd], "Open3D", 800, 600, 800, 400)

