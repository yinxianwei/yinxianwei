Title: Git误删分支恢复方法
Date: 2019-07-04 10:02:49


不小心删除本地分支和远程分支，使用如下方法恢复代码

1. git log -a 找到提交的commit id
2. git branch recover_branch fc4b7dca5e424207c6307118fda69215ec842555
3. git checkout recover_branch
