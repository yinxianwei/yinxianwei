Title: element-ui + element-theme + vue-cli + postcss-px2rem
Date: 2017-09-29 14:58:12


- element-ui: 1.4.2
- vue-cli: 2.8.2

```js
// utils.j
exports.cssLoaders = function (options) {
    ...
    return {
        css: generateLoaders('postcss', {
            plugins() {
                return [require('postcss-px2rem')({ remUnit: 75 })]
            }
        }),
        ...
    }
}
```

```js
// vue-loader.conf.js
module.exports = {
    ...
    postcss: [require('postcss-px2rem')({ remUnit: 75 })],
    ...
}
```



