#!/usr/bin/env python
# -*- coding:utf-8 -*-

#**********************************
# create & show pcd from depth
#**********************************

import open3d as o3d
import numpy as np
import sys
import os
import cv2

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Provide a depth file")
        sys.exit(0)

    depth_img = o3d.io.read_image(sys.argv[1])
    camera = o3d.camera.PinholeCameraIntrinsic();
    pcd = o3d.geometry.create_point_cloud_from_depth_image(depth_img, camera)

    print(pcd)
    o3d.visualization.draw_geometries([pcd], "Open3D", 800, 600, 800, 400)

