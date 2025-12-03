Title: Mac使用U盘安装系统
Date: 2020-10-02 17:43:11


<p style="color: #F44336;">注意备份将要安装系统的电脑内容</p>

官网教程：https://support.apple.com/zh-cn/HT201372

- U盘抹掉格式为：`Mac OS 扩展（日志式）` 重命名为：`UM`
- 下载镜像[High.Sierra.dmg](http://www.pc6.com/mac/484081.html)并打开
- 打开终端并输入：

<!-- more -->

```
sudo /Volumes/Install\ macOS\ High\ Sierra/Install\ macOS\ High\ Sierra.app/Contents/Resources/createinstallmedia --volume /Volumes/UM --applicationpath /Volumes/Install\ macOS\ High\ Sierra/Install\ macOS\ High\ Sierra.app --nointeraction
```

- 等待

```
Erasing Disk: 0%... 10%... 20%... 30%...100%...
Copying installer files to disk...
Copy complete.
Making disk bootable...
Copying boot files...
Copy complete.
Done.
```
-  重启按住option键
-  选择制作的U盘启动
- 打开磁盘工具抹掉系统盘
- 开始安装
- 出现`不能验证`问题时，打开实用工具-终端，输入`date 032208102015.20`回车即可

老款可能需要下载支持文件：[https://support.apple.com/zh-cn/HT205016](https://support.apple.com/zh-cn/HT205016)

