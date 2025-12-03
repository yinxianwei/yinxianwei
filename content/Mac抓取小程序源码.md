Title: Mac抓取小程序源码
Date: 2020-12-28 09:59:34


1. 安装安卓模拟器 https://mumu.163.com/
2. 模拟器设置-开启ROOT权限
3. 安装微信 https://weixin.qq.com/download
4. 安装 RE文件管理器
5. 登录微信，点击想要抓取小程序（小程序会闪退）
6. 打开 RE文件管理器，路径：/data/data/com.tencent.mm/MicroMsg/32位字符路径/appbrand/pkg/
7. 长按文件夹压缩，压缩后通过微信发送
8. 下载反编译工具：https://github.com/qwerty472123/wxappUnpacker
9. 执行命令：npm i
10. node wuWxapkg.js xxx..wxapkg