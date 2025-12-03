Title: CommonJS和AMD/CMD
Date: 2018-08-29 17:06:25


CommonJS根据JS的表现制定规范：
> {模块引用(require)} {模块定义(exports)} {模块标识(module)}

NodeJS遵循了CommonJS规范，写法如下：

```js
// foo.js

module.exports = function(x) {
    console.log(x);
};
```

```js
// index.js

let foo = require('./foo')
foo(1);
```

<!-- more -->

CommonJS主要为了JS在后端制定的规范，但并不适用与前端，因为代码在是通过网络加载，所以AMD（异步模块定义）出现：

> define(['dep1','dep2'],function(dep1,dep2){...});


RequireJS实现了AMD规范，写法如下：

```js
// foo.js

define(function() {
    return function(x) {
        console.log(x);
    };
});
```

```js
// index.js

define(['foo'], function(foo) {
    foo(2);
});
```

CMD （通用模块定义）写法更加直观：


> // 所有模块都通过 define 来定义
> define(function(require, exports, module) {
> 
>   // 通过 require 引入依赖
>   var $ = require('jquery');
>   var Spinning = require('./spinning');
> 
>   // 通过 exports 对外提供接口
>   exports.doSomething = ...
> 
>   // 或者通过 module.exports 提供整个接口
>   module.exports = ...
> });

```js
// foo.js

define(function(require, exports, module) {
  module.exports = function(x) {
      console.log(x);
  }
});
```

```js
// index.js

define(function(require, exports, module) {
    var foo = require('foo');
    foo(3);
});
```
