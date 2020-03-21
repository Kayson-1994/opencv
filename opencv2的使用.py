#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# Copyright (c) 2012-2019
#
# @Time  : 2020/3/22
# @Author: ShenKai
# @File  : opencv2的使用.py
# @Software: PyCharm

import cv2
import image_processing


# 鼠标事件
global img
global point1, point2
global g_rect


def on_mouse(event, x, y, flags, param):
    global img, point1, point2, g_rect
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击,则在原图打点
        print("1-EVENT_LBUTTONDOWN")
        point1 = (x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0), 5)
        cv2.imshow('image', img2)

    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳，画框
        print("2-EVENT_FLAG_LBUTTON")
        cv2.rectangle(img2, point1, (x, y), (255, 0, 0), thickness=2)
        cv2.imshow('image', img2)

    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放，显示
        print("3-EVENT_LBUTTONUP")
        # 打上起始坐标
        xy = "(%d, %d)" % (point1[0], point1[1])
        cv2.putText(img2, xy, (point1[0], point1[1]), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (255, 255, 255), thickness=1)

        # 打上结束坐标
        xy = "(%d, %d)" % (x, y)
        cv2.putText(img2, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (255, 255, 255), thickness=1)

        # 画框
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), thickness=2)
        cv2.imshow('image', img2)


def get_image_roi(rgb_image):
    '''
    获得用户ROI区域的rect=[x,y,w,h]
    :param rgb_image:
    :return:
    '''
    bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
    global img
    img = bgr_image
    cv2.namedWindow('image')
    while True:
        cv2.setMouseCallback('image', on_mouse)
        # cv2.startWindowThread()  # 加在这个位置
        cv2.imshow('image', img)
        key = cv2.waitKey(0)
        if key == 13 or key == 32:  # 按空格和回车键退出
            break
    cv2.destroyAllWindows()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


if __name__ == '__main__':
    orig_image = image_processing.read_image("1.jpg")
    resize_image = image_processing.resize_image(orig_image, resize_height=300, resize_width=None)
    get_image_roi(resize_image)
