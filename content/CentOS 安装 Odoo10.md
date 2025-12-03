Title: CentOS 安装 Odoo10
Date: 2022-01-24 15:15:52



## postgresql

<!-- https://blog.csdn.net/S2T11Enterprise/article/details/109775056 -->

1. 根据系统生成命令 https://www.postgresql.org/download/linux/redhat/
2. sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
3. 禁用内置psql `sudo dnf -qy module disable postgresql`
4. 安装psql `sudo yum install -y postgresql10-server`
5. 安装contrib `sudo yum install postgresql10-contrib -y`
6. 初始化 `sudo /usr/pgsql-10/bin/postgresql-10-setup initdb`
7. 开机启动 `sudo systemctl enable postgresql-10`
8. `sudo systemctl start postgresql-10`
9. 切换用户 `su - postgres`
10. `psql`
11. 修改默认密码 `alter user postgres with password 'postgres'`
12. 创建用户 `create user xianwei with password 'password';`
13. 创建odoo数据库 `create database odoo owner xianwei;`
14. 授权数据库 `grant all privileges on database odoo to xianwei;`
15. ALTER USER xianwei WITH CREATEDB;
16. 重启 systemctl restart postgresql-10



## python2.x

1. yum install python2



## odoo10

1. git clone https://gitee.com/mirrors/odoo.git --depth 1 --branch 10.0 --single-branch odoo10
2. sudo yum install libxml2-devel libxslt-devel python2-devel openldap-devel libffi-devel gcc
3. cd odoo10
4. pip2 install -r requirements.txt
5. curl -fsSL https://rpm.nodesource.com/setup_16.x | sudo bash -
6. 修改 /etc/yum.repos.d/nodesource-*.repo 文件，将其中的所有 rpm.nodesource.com 替换为 mirrors.ustc.edu.cn/nodesource/rpm 
7. sudo yum install -y nodejs
8. npm config set registry https://registry.npm.taobao.org
9. sudo npm install -g less@3.0.4 less-plugin-clean-css
10. vim odoo.config
11. vim /etc/systemd/system/odoo.service




```
#修改pip镜像 ~.pip/pip.config
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
```

```
#odoo.config
[options]
db_host = localhost
db_port = 5432
addons_path = addons
db_user = xianwei
db_password = password
dbfilter = odoo
db_name = odoo
addons_path = /usr/local/app/odoo/addons
```


```
#/etc/systemd/system/odoo.service
[Unit]
Description=Odoo
After=postgresql-10.service

[Service]
Type=simple
User=xianwei
Group=xianwei
ExecStart=/usr/bin/python2 /usr/local/app/odoo/odoo-bin -c /usr/local/app/odoo/odoo.conf

[Install]
WantedBy=multi-user.target
```



## 问题

1. OptionBinding with id "failovermethod" does not exist
    `sudo sed -iBAK '/^failovermethod=/d' /etc/yum.repos.d/*.repo`
2. centos添加用户
    1. adduser xianwei
    2. chmod -v u+w /etc/sudoers
    3. vim /etc/sudoers
    4. xianwei ALL=(ALL)       ALL
    5. chmod -v u-w /etc/sudoers
3. 忘记psql密码
    1. 修改/var/lib/pgsql/10/data/pg_hba.conf的local为trust
4. 远程访问
    1. 修改/var/lib/pgsql/10/data/postgresql.conf文件中的listen_addresses为*
    2. /var/lib/pgsql/10/data/pg_hba.conf添加
    ```
    host    all             xianwei             0.0.0.0/0               md5
    ```