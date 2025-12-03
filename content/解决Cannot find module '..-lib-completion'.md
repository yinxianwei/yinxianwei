Title: 解决Cannot find module '../lib/completion'
Date: 2017-10-20 11:01:45

```json
// package.json
{
    "scripts": {
        "build": "gulp build"
    }
}
```

<!-- more -->

错误：

```
Error: Cannot find module '../lib/completion'
    at Function.Module._resolveFilename (module.js:469:15)
    at Function.Module._load (module.js:417:25)
    at Module.require (module.js:497:17)
    at require (internal/module.js:20:19)
    at Object.<anonymous> (/staticDisk/repository/jenkins/saas/node_modules/.bin/gulp:13:18)
    at Module._compile (module.js:570:32)
    at Object.Module._extensions..js (module.js:579:10)
    at Module.load (module.js:487:32)
    at tryModuleLoad (module.js:446:12)
    at Function.Module._load (module.js:438:3)
```

修改为：

```json
// package.json
{
    "scripts": {
        "build": "node ./node_modules/gulp/bin/gulp build"
    }
}
```

