#!/usr/bin/env python
# -*- coding:utf-8 -*-

#**********************************
# show info of given depth file
#**********************************

import sys
import cv2

if __name__ == "__main__":
	if(len(sys.argv) != 2):
		print("Must provide a file to show")
		sys.exit(0)

	print(sys.argv[1])
	depth_img = cv2.imread(sys.argv[1], -1)#-1 unchanged
	print("shape:	", depth_img.shape)
	print("min/max:", depth_img.min(), depth_img.max())
	print("dtype:	", depth_img.dtype)

