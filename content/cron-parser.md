Title: cron-parser
Date: 2018-08-15 14:23:57


Github: [cron-parser](https://github.com/harrisiirak/cron-parser)

```
*    *    *    *    *    *
┬    ┬    ┬    ┬    ┬    ┬
│    │    │    │    │    |
│    │    │    │    │    └ day of week (0 - 7) (0 or 7 is Sun)
│    │    │    │    └───── month (1 - 12)
│    │    │    └────────── day of month (1 - 31)
│    │    └─────────────── hour (0 - 23)
│    └──────────────────── minute (0 - 59)
└───────────────────────── second (0 - 59, optional)
```

1. 每10秒执行: `*/10 * * * * *`
2. 每周一10点执行: 0 0 10 ? * 1
3. 每月1号10点执行: 0 0 10 1 * ?

暂时不支持：`L`、`W`、`#`