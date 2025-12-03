Title: Git Commit Msg
Date: 2018-09-06 18:10:51


```
<type>(<scope>): <subject>

<body>

<footer>
```


Example

```
fix(middleware): ensure Range headers adhere more closely to RFC 2616

Add one new dependency, use `range-parser` (Express dependency) to compute
range. It is more well-tested in the wild.

Fixes #2310
```

<!-- more -->

Allowed <type> values:

- feat 针对用户来时的新功能
- fix 针对用户来说的bug修复
- docs 文档更新
- style 代码格式化，添加分号对代码没有影响的提交
- refactor 代码重构，如变更一个变量名
- test 测试代码修改
- chore 更新注释等
- ci 配置更新

Example <scope> values:

- init
- runner
- watcher
- config
- web-server
- proxy

Message body:

- 修改内容说明

Message footer:

- 关闭的问题如：
    Closes #123, #442
    Fixes #422


参考： http://karma-runner.github.io/2.0/dev/git-commit-msg.html