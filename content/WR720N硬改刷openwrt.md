Title: WR720N硬改刷openwrt
Date: 2022-02-07 15:43:39


## 需要准备的工具：

1. WR720N v3
2. W25Q1238FVSSIG 16M闪存
3. H5DU5162ETR-E3C 64M路由内存
4. 电烙铁
5. 热风枪
6. 土豪金XTW100编程器
7. 网线一根
8. 可以插网线的电脑一台


## 流程

1. 网线连接路由后，打开 192.168.1.253，记录Mac地址，后面会用到
2. 选择4M的openwrt固件升级
3. ssh连接路由备份art
4. 16M闪存用XTW100编程器刷入breed
5. 16M闪存更换到路由
6. 64M内存更换到路由
7. 启动后打开192.168.1.1，进入breed
8. 刷入16M的openwrt固件
9. 刷入备份的art文件
10. 修改Mac地址
11. 重启路由5分钟后灯常亮打开192.168.1.1为openwrt后台

## 固件

1. 安装docker
2. 安装ubuntu容器`docker pull ubuntu:20.04`
3. 查看容器id `docker ps` 
4. 进入容器 `docker exec -it 容器id  /bin/bash`
5. 修改镜像 https://developer.aliyun.com/mirror/ubuntu?spm=a2c6h.13651102.0.0.3e221b11ZrkuE2
```
echo 'deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse' > /etc/apt/sources.list
```
    
6. `apt-get update`
7. `apt-get install git`
8. `apt-get -y install build-essential asciidoc binutils bzip2 gawk gettext git libncurses5-dev libz-dev patch python3.5 python2.7 unzip zlib1g-dev lib32gcc1 libc6-dev-i386 subversion flex uglifyjs git-core gcc-multilib p7zip p7zip-full msmtp libssl-dev texinfo libglib2.0-dev xmlto qemu-utils upx libelf-dev autoconf automake libtool autopoint device-tree-compiler g++-multilib antlr3 gperf wget curl swig rsync`
9. `git clone https://github.com/coolsnowwolf/openwrt.git`
10. export FORCE_UNSAFE_CONFIGURE=1
11. 


常见问题

1. 无法更新订阅
	执行 chown 755 /etc/config/s*
	
	https://github.com/coolsnowwolf/lede/commit/af803f2569bbbaac88d001890a8a7646abf0ce0d#comments
	
	https://github.com/maxlicheng/luci-app-ssr-plus

