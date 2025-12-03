Title: 安卓 position: absolute; position: fixed;和键盘冲突的问题
Date: 2018-12-27 16:29:40


### 解决方式一

修改为relative或static

### 解决方式二

设置absolute时固定父元素高度（px）

### 解决方式三

弹出键盘时隐藏内容

```css
@media (max-height: 500px) {
    .class {
        display: none;
    }
}
```