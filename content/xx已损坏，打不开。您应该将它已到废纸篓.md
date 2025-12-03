Title: xx已损坏，打不开。您应该将它已到废纸篓
Date: 2022-3-3 20:54

1. 打开终端
2. 输入 `sudo spctl --master-disable`
3. 输入系统密码(终端不会显示输入的密码)，输入完成直接回车
4. 打开系统偏好设置-安全性与隐私-任何来源
5. sudo xattr -rd com.apple.quarantine /Applications/xxx.app
