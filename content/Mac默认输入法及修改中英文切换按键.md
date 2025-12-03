Title: Mac默认输入法及修改中英文切换按键
Date: 2020-05-12 15:59:51


1. 删除默认英文输入法
    1. 关闭SIP
    2. 打开`~/Library/Preferences/com.apple.HIToolbox.plist`文件,删除ABC相关内容后重启
     ![-w800](media/15706071952409/15706076184375.jpg)
2. 修改中文输入入法为shift切换中英文
    1. 使用[https://github.com/Eronana/scimex](https://github.com/Eronana/scimex)插件修改(需重启)
    2. 可以修改 `scimex/blob/master/src/injlib/injlib.m`文件的`NSEventModifierFlagShift`为其他按键:  [https://developer.apple.com/documentation/appkit/nseventmodifierflags?language=objc](https://developer.apple.com/documentation/appkit/nseventmodifierflags?language=objc)

    