Title: Google Chrome 控制台
Date: 2020-12-04 14:54:21


## console

#### console.log(object [, object, ...])
#### console.info(object [, object, ...])
#### console.error(object [, object, ...])

```js
var str = 'hello world';
console.log('--->>>%s', str);
```
<!-- more -->

常用格式代码：

| 说明符 | 输出 |
| --- | --- |
| %s |   将值格式化为字符串 |
| %i 或 %d | 将值格式化为整型 |
| %f |   将值格式化为浮点值 |
| %o |   将值格式化为可扩展 DOM 元素。如同在 Elements 面板中显示的一样 |
| %O |   将值格式化为可扩展 JavaScript 对象 |
| %c |   将 CSS 样式规则应用到第二个参数指定的输出字符串 |
#### console.table(object [, columns])
将元素属性按表格结构打印出来
#### console.assert(expression, object)

```js
console.assert(a > b, 'error');
```

#### console.time(label)
#### console.timeEnd(label)
代码执行时间

```js
console.time('time');
console.timeEnd('time');
time: 0.001953125ms;
```

## copy

copy命令，可复制变量到剪切板

```js
copy(str);
```
## 选择元素

检查元素控制台`$0`即为该元素

## 事件监听

```js
// 事件监听
monitorEvents($0, 'mouse');
// 取消事件监听
unmonitorEvents($0);
```


## contenteditable

```js
// 网页body内容可编辑
document.body.contentEditable = true;
```



