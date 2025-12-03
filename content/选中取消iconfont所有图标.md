Title: 选中取消iconfont所有图标
Date: 2019-03-14 13:31

# 选中/取消iconfont所有图标

打开控制台，粘贴下面代码，回车

```

var ls = document.getElementsByClassName('icon-cover-freeze');
var mClick = function(index) {
    if (index == ls.length) return;
    ls[index].firstElementChild.click();
    setTimeout(() => {
        mClick(index + 1);
    }, 5);
};
mClick(0);

```

