Title: JS中toFixed的坑
Date: 2020-07-20 14:01:48


重点：toFixed不是四舍五入

MDN: 
> toFixed() 方法使用定点表示法来格式化一个数。

Chrome：

```js
console.log((0.005).toFixed(2)) -> 0.01
console.log((0.015).toFixed(2)) -> 0.01
console.log((0.025).toFixed(2)) -> 0.03
console.log((0.035).toFixed(2)) -> 0.04
console.log((0.045).toFixed(2)) -> 0.04
console.log((0.055).toFixed(2)) -> 0.06
console.log((0.065).toFixed(2)) -> 0.07
console.log((0.075).toFixed(2)) -> 0.07
console.log((0.085).toFixed(2)) -> 0.09
console.log((0.095).toFixed(2)) -> 0.10
```

```js
console.log(Math.round(0.005 * 100, 2) / 100) -> 0.01
console.log(Math.round(0.015 * 100, 2) / 100) -> 0.02
console.log(Math.round(0.025 * 100, 2) / 100) -> 0.03
console.log(Math.round(0.035 * 100, 2) / 100) -> 0.04
console.log(Math.round(0.045 * 100, 2) / 100) -> 0.05
console.log(Math.round(0.055 * 100, 2) / 100) -> 0.06
console.log(Math.round(0.065 * 100, 2) / 100) -> 0.07
console.log(Math.round(0.075 * 100, 2) / 100) -> 0.08
console.log(Math.round(0.085 * 100, 2) / 100) -> 0.09
console.log(Math.round(0.095 * 100, 2) / 100) -> 0.1
```

[为什么(2.55).toFixed(1)等于2.5？](https://zhuanlan.zhihu.com/p/31202697)