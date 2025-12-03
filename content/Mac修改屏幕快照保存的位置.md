Title: Mac修改屏幕快照保存的位置
Date: 2018-07-04 15:18:26


```
$ defaults write com.apple.screencapture location <path>
$ killall SystemUIServer
```