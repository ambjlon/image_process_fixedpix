# image_process_fixedpix
使用Python图像处理库处理图像, 像素不变调整大小.  
使用示例  
python run.py '/path/to/a.jpg'  '/path/to/b5.jpg' '5'  
三个参数分别是 源图像 目的图像 质量系数(越大质量越高, 从1到100)

运行次脚本之前需要python安装PIL库. PIL又依赖libjpeg libpng.
以后大多情况在mac os上使用此脚本, 现在以mac os安装PIL为例给出安装过程:

1. 使用brew install libjpeg libpng  
2. 下载[PIL](http://effbot.org/media/downloads/PIL-1.1.7.tar.gz)  
3. 解压进入目录后执行:

    + sudo python setup.py build  
    + python setup.py install  
