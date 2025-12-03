Title: nginx certbot 免费泛域名证书
Date: 2020-12-07 09:58:57



系统: CentOS 7

<!-- more -->

https://certbot.eff.org/lets-encrypt/centosrhel7-nginx

1. ```sudo yum install python2-certbot-dns-cloudflare```
2. ```yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm```
3. ```sudo yum install certbot python2-certbot-nginx```
4. ```sudo yum install python2-certbot-dns-cloudflare```
5. 注册并添加域名: https://dash.cloudflare.com/login
6. 添加路径和文件
    ~/.secrets/certbot/cloudflare.ini
    内容: 
    
    ```
    # Cloudflare API token used by Certbot
    dns_cloudflare_api_token = 你的api token
    ```
1. ```chmod 600 ~/.secrets/certbot/cloudflare.ini```
2. ```certbot certonly --dns-cloudflare --dns-cloudflare-credentials ~/.secrets/certbot/cloudflare.ini -d *.yinxianwei.com --email example@qq.com```
3. nginx配置泛域名解析
    ```
    # /etc/nginx/conf.d/www.conf
    server {
        server_name  ~^(?<subdomain>.+)\.yinxianwei\.com$;
        root   /usr/share/nginx/$subdomain; 
        index  index.html index.htm index.php;
        fastcgi_intercept_errors on;
        error_page  404      = /404.html;
        location / {
                try_files $uri $uri/ =404;
       }
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
        location ~ /\.ht {
            deny  all;
        }
    }
    ```
4. `certbot run -a manual -i nginx -d *.yinxianwei.com`
5. 按照提示域名添加解析
    ```
    记录类型: TXT
    主机记录: _acme-challenge
    记录值: 提示字符串
    ```
6. 选择重定向https
7. 自动更新: 
~~`echo "0 0,12 * * * root python -c 'import random; import time; time.sleep(random.random() * 3600)' && certbot renew -q" | sudo tee -a /etc/crontab > /dev/null`~~
    
    https://github.com/ywdblog/certbot-letencrypt-wildcardcertificates-alydns-au

一个教程: https://www.willh.cn/articles/2018/07/27/1532676216270.html


https://certbot-dns-cloudflare.readthedocs.io/en/stable/