Title: Ubuntu 14.04.5 安装 MySQL 5.7
Date: 2020-05-07 13:46:19


### 安装

下载地址：[https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
- `wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-server_5.7.21-1ubuntu14.04_amd64.deb-bundle.tar`  

<!-- more -->

- `tar -xf mysql-server_5.7.21-1ubuntu14.04_amd64.deb-bundle.tar`
- `sudo apt-get update`
- `sudo apt-get upgrade`
- `apt-get install libaio1`
- `sudo dpkg -i mysql-common_5.7.21-1ubuntu14.04_amd64.deb`
- `sudo dpkg-preconfigure mysql-community-server_5.7.21-1ubuntu14.04_amd64.deb`
- `sudo dpkg -i libmysqlclient20_5.7.21-1ubuntu14.04_amd64.deb`
- `sudo dpkg -i libmysqlclient-dev_5.7.21-1ubuntu14.04_amd64.deb`
- `sudo dpkg -i libmysqld-dev_5.7.21-1ubuntu14.04_amd64.deb`
- `sudo dpkg -i mysql-community-client_5.7.21-1ubuntu14.04_amd64.deb`
- `sudo dpkg -i mysql-client_5.7.21-1ubuntu14.04_amd64.deb`
- `sudo dpkg -i mysql-community-source_5.7.21-1ubuntu14.04_amd64.deb`
- `sudo apt-get -f install`
- `sudo apt-get -f install libmecab2`
- `sudo dpkg -i mysql-community-server_5.7.21-1ubuntu14.04_amd64.deb`
- `sudo dpkg -i mysql-server_5.7.20-1u`
- `sudo dpkg -i mysql-server_5.7.21-1ubuntu14.04_amd64.deb`
- `mysql -u root -p`


### MySQL常用命令
>
进入MySQL: `mysql -u root -p`
启动: `sudo service mysql start`
重启: `sudo  service mysql restart`
关闭: `sudo service mysql stop`

### 远程访问
>
- `vim /etc/mysql/mysql.conf.d/mysqld.cnf`
- 修改`bind-address: 127.0.0.1`为`0.0.0.0`
- 新增可远程访问的用户
- `grant all on *.* to 用户名@'%' identified by '密码' with grant option; `
- `flush privileges;`

### nodejs
> 安装git `sudo apt-get install git`
> 安装nvm `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh |bash`
> `source ~/.bashrc`
> 安装nodejs `nvm install v8.9.4`

### 其他
[https://juejin.im/post/5d07cf13f265da1bd522cfb6](https://juejin.im/post/5d07cf13f265da1bd522cfb6)