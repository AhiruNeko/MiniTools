# ImgSpider
自制小工具

下载：https://github.com/Dylan-wg/ImgSpider/blob/main/dist/spd.exe

### 安装
将spd.exe所在文件夹的路径加入系统环境变量。

### 使用说明
1. ```spd download [url]``` 从给定URL爬取图片。其中包含canvas形式图片，并且会将.webp格式自动转换为.jpg。该功能对于某些网站未必适用，较为局限。
2. ```spd convert [dir] [extention1] [extention2]``` 将给定路径dir下所有后缀为extention1的文件变为后缀为extention2的文件。
3. ```spd open``` 打开下载文件夹。位置位于与spd.exe同一文件夹内的downloads文件夹内。
4. ```spd toJPG [filename]``` 将名为filename的png图片文件重新编码成jpg格式。当filename为"."时将转化路径下的所有png文件。
5. ```spd rename [name format] [var] [from] [to]``` 将路径下拓展名与name format相同的文件重命名，其中var是name format中(不含拓展名)需要迭代的变量，from为var迭代的起始值，to为终止值，当from和to中有字母时将采用ASCII进行迭代。其中to可以为"inf"，此时将对所有文件重命名。
   - 例如：指令```spd rename file_x.txt x 0 5```会将路径下的6个txt文件重命名为file_0.txt, file_1.txt ... file_5.txt
