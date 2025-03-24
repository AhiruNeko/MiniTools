# ImgSpider
自制小工具

下载：https://github.com/Dylan-wg/ImgSpider/blob/main/dist/ImgSpider.zip

### 安装
解压ImgSpeder.zip，将spd.exe所在文件夹的路径加入系统环境变量。

### 使用说明
1. ```spd download [url]``` 从给定URL爬取图片。其中包含canvas形式图片，并且会将.webp格式自动转换为.jpg。该功能对于某些网站未必适用，较为局限。
2. ```spd convert [dir] [extention1] [extention2]``` 将给定路径dir下所有后缀为extention1的文件变为后缀为extention2的文件。
3. ```spd open``` 打开下载文件夹。位置位于与spd.exe同一文件夹内的downloads文件夹内。
