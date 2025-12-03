Title: nginx 配置https
Date: 2018-11-01 11:00:28


`update: 2018-08-20`

已支持泛域名申请：[https://certbot.eff.org/](https://certbot.eff.org/)

> Trying to get a wildcard certificate? Please use the dropdown menus below to get instructions specific to your system, and read those instructions carefully.

---

```
$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install python-certbot-nginx 
```

```
$ service nginx stop
$ certbot certonly --standalone --email your@email.com -d yourdomain.com
```

安装参考：[[https://www.cnblogs.com/SzeCheng/p/8075799.html](https://www.cnblogs.com/SzeCheng/p/8075799.html)]([https://www.cnblogs.com/SzeCheng/p/8075799.html](https://www.cnblogs.com/SzeCheng/p/8075799.html))
证书三个月需要续签一次，使用`crontab`每个月检查一次，自动续期
`0 0 1 * * certbot renew -q --pre-hook "service nginx stop" --post-hook "service nginx start"`




