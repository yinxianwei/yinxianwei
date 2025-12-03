Title: 关于通过document.styleSheets修改样式规则
Date: 2018-07-19 15:49:25



```js
var innerText = '';
function changeTheme() {
    try {
        var colors = JSON.parse(
            window.localStorage.getItem(window.localStorage.getItem('ROLE_ID') + '__theme')
        );
    } catch (error) { }
    if (!colors) {
        return;
    }
    var keys = ['background', 'background-color', 'color', 'border-color'];
    
    var styleSheet = document.styleSheets[0].href ? document.styleSheets[0] : document.styleSheets[1];
    for (var index = 0; index < styleSheet.rules.length; index++) {
        var rule = styleSheet.rules[index];
        if (rule.style) {
            Object.keys(colors).forEach(function(key) {
                keys.forEach(function(styleKey) {
                    var sc = rule.style.getPropertyValue(styleKey).replace(key, colors[key]);
                    if (sc) {
                        rule.style.setProperty(styleKey, sc, rule.style.getPropertyPriority(styleKey))
                    }
                });
            });
        }
    }
}
changeTheme();

```