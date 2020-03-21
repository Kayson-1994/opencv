# opencv
opencv2的使用

***
这个对输入图片，画矩形框并标识出首、尾坐标，该程序被测试过，能正常运行。程序使用的图片和视频，都在根目录下文件内。

## Setup安装
1. 安装cv2模块
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
```


## 开发环境
- Python 3.6.1
- OpenCV 3.2.0
- PyCharm 2018.3

## 新闻News https://opencv.org/news.html
- 中文论坛 http://www.opencv.org.cn/
- OpenCV 3.3发布了
    1. 主要消息是我们将DNN模块从opencv_contrib推广到主存储库，改进和加速了很多。不再需要外部BLAS实现。对于GPU，使用Halide（http://halide-lang.org）进行实验性DNN加速。有关该模块的详细信息可以在我们的wiki中找到：[OpenCV中的深度学习](https://github.com/opencv/opencv/wiki/Deep-Learning-in-OpenCV)。
    2. OpenCV现在可以使用标志ENABLE_CXX11构建为C ++ 11库。添加了C ++ 11程序员的一些很酷的功能。
    3. 由于“动态调度”功能，我们还在OpenCV的默认版本中启用了不少AVX / AVX2和SSE4.x优化。DNN模块还具有一些AVX / AVX2优化。 Intel Media SDK现在可以被我们的videoio模块用来进行硬件加速的视频编码/解码。支持MPEG1 / 2，以及H.264。
    4. 嵌入OpenCV Intel IPP子集已从2015.12升级到2017.2版本，从而在我们的核心和imgproc perf测试中提高了15％的速度。
    5. 716拉请求已经合并，588我们的错误跟踪器中的问题已经关闭，因为OpenCV 3.2。另外，我们通过一些严格的静态分析仪工具运行OpenCV，并修复了检测到的问题。所以OpenCV 3.3应该是非常稳定和可靠的释放。
    6. 有关OpenCV 3.3的更改和新功能的更多详细信息，请访问https://github.com/opencv/opencv/wiki/ChangeLog。
    7. [下载OpenCV 3.3](https://github.com/opencv/opencv/releases/tag/3.3.0)
    7. [安装OpenCV 3.3](http://www.linuxfromscratch.org/blfs/view/cvs/general/opencv.html)
- OpenCV 4.0发布了 https://opencv.org/opencv-4-0-0.html

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
