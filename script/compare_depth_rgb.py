#!/usr/bin/env python
# -*- coding:utf-8 -*-

#**********************************
# compare depth and RGB image
#**********************************

import os
import matplotlib.pyplot as plt
import cv2

def check_image_overlay(color_path, depth_path, is_resize=True, is_overlay=True, is_show=False):
    color_files = os.listdir(color_path)
    for color_name in color_files:
        depth = color_name.replace('Color', 'Depth')
        color_full_path = os.path.join(color_path, color_name)
        depth_full_path = os.path.join(depth_path, depth)
        if is_resize:
            resize_single_img(color_full_path, is_show)
            resize_single_img(depth_full_path, is_show)
        if is_overlay:
            img_color = get_img_from_file(color_full_path)
            img_depth = get_img_from_file(depth_full_path)
            plt.figure(figsize=(12, 12))
            plot_img_dep_weights2save(img_color, img_depth, color_name, is_show)


def get_img_from_file(img_path):
    img = cv2.imread(img_path)
    print(img_path)
    return img[:, :, (2, 1, 0)]


def plot_img_dep_weights2save(img_color, img_depth, color_name, is_show):
    img_color_depth = cv2.addWeighted(img_color, 0.6, img_depth, 0.7, 0)
    plt.subplot(2, 2, 1)
    plt.imshow(img_color)
    plt.subplot(2, 2, 2)
    plt.imshow(img_depth)
    plt.subplot(2, 2, 3)
    plt.imshow(img_color_depth)
    if is_show:
        plt.show()
        plt.clf()
    else:
        plt.savefig(os.path.join(OUTPUT_PATH, color_name.replace('Color', 'Color-Depth')))


def resize_single_img(img_file, is_show):
    print(img_file)
    img = cv2.imread(img_file)
    r = 424 / img.shape[0]
    dim = (int(img.shape[1] * r), 424)
    # r = 640 / img.shape[1]
    # dim = (640, int(img.shape[0] * r))
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    if is_show:
        cv2.imshow('test', resized)
        cv2.imshow('cut', resized[106:746, :, :])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    image_path = os.path.join(OUTPUT_PATH, 'image')
    depth_path = os.path.join(OUTPUT_PATH, 'depth')
    if not os.path.exists(image_path):
        os.mkdir(image_path)
    if not os.path.exists(depth_path):
        os.mkdir(depth_path)
    fname = os.path.basename(img_file)
    if 'Depth' in fname:
        cv2.imwrite(os.path.join(depth_path, fname), resized[:, 121:633, :])
    else:
        cv2.imwrite(os.path.join(image_path, fname), resized[:, 121:633, :])


if __name__ == '__main__':
    OUTPUT_PATH = './outputs'
    if not os.path.exists(OUTPUT_PATH):
        os.mkdir(OUTPUT_PATH)

    color_path = \
            r'./dataset/s3/image'
    depth_path = \
            r'./dataset/s3/depth'
    check_image_overlay(color_path, depth_path, is_resize=False, is_overlay=True, is_show=False)

