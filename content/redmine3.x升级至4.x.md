Title: redmine3.x升级至4.x
Date: 2022-03-02 10:10:31



1. 下载最新版 https://www.redmine.org/releases/redmine-4.2.3.tar.gz
2. 解压 tar zxvf redmine-4.2.3.tar.gz
3. 复制3.x的files至redmine-4.2.3
4. 3.x数据库备份  https://www.redmine.org/projects/redmine/wiki/RedmineBackupRestore
5. 新建数据库 redmine4
6. 恢复3.x的数据至数据库redmine4
7. 使用rvm或rbenv升级ruby至2.7.0
8. gem install bundle
9. bundle install --without development test
10. [可选] bundle install --without development test rmagick
11. [可选] bundle exec rake generate_secret_token
12. bundle exec rake db:migrate RAILS_ENV=production
13. 下载4.x对应的插件放到plugins内
14. bundle exec rake redmine:plugins:migrate RAILS_ENV=production
15. 启动
 