# opencv
opencv2的使用

***
这个对输入图片，画矩形框并标识出首、尾坐标，该程序被测试过，能正常运行。程序使用的图片和视频，都在根目录下文件内。

Setup安装
1. 安装cv2模块
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
```


## 开发环境
- Python 3.6.1
- OpenCV 3.2.0
- PyCharm 2018.3

## 怎样翻墙？使用Google搜索引擎，观看YouTube视频教程
- shadowsocks
  - 方便，随地随时翻墙
  - 手机使用4G信号上网，也可以。
  - 强烈推荐！
  - 购物国外服务器，搭建也很容易
  - 参考 https://isweic.com/build-shadowsocks-python-server/
  - pip install shadowsocks
  - 运行
    - shell窗口运行
      - ssserver -p 8388 -k password -m aes-256-cfb
      - 8388是端口号，password是密码，aes-256-cfb是加密类型，通过Ctrl+C结束
    - 后台运行
      - ssserver -p 8388 -k password -m aes-256-cfb --user nobody -d start
    - 结束后台运行
      - ssserver -d stop
    - 检查运行日志
      - less /var/log/shadowsocks.log
