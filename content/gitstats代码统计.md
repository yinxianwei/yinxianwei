Title: gitstats代码统计
Date: 2019-01-09 13:18:41


```
brew install gnuplot

git clone https://github.com/hoxu/gitstats.git

python gitstats/gitstats "git路径" "git路径" "生成路径"

如: python gitstats/gitstats -c project_name="name" -c start_date=2017-10-1 "git/code1" "git/code2" out

统计git/code1，git/code2代码，时间从2017-10-1号开始，项目名为name，输出至out目录

```


```json
// 一些参数：
{
	'max_domains': 10,
	'max_ext_length': 10,
	'style': 'gitstats.css',
	'max_authors': 20,
	'authors_top': 5,
	'commit_begin': '',
	'commit_end': 'HEAD',
	'linear_linestats': 1,
	'project_name': '',
	'processes': 8,
	'start_date': '注意格式'
}
```


