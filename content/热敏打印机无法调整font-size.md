Title: 热敏打印机无法调整font-size
Date: 2020-12-04 14:57:48



Web前端需要连接热敏打印机打印小票，但是font-size始终无法调小，最终解决见demo：


<!-- more -->

update：2020年12月04日

https://medium.com/@Idan_Co/the-ultimate-print-html-template-with-header-footer-568f415f6d2a

```html
<!DOCTYPE HTML>
<html>

<head>
    <meta name="renderer" content="webkit">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>美问</title>
    <style type="text/css">
    @media screen {
        #printSection {
            display: none;
        }
    }
    @page {
        margin: 0cm;
    }
   @media print {
        body * {
            visibility: hidden;
        }
        #printSection * {
            visibility: visible;
        }
        p {
            font-size: 9pt;
        }
        h4 {
            font-size: 18pt;
        }
    }
    </style>
    <script type="text/javascript">
    function printTest() {
        window.print();
    }

    </script>
</head>

<body>
    <div>
        <div id="printSection">
            <div style="width: 150%;height: 1px;"></div>
            <!-- 如果打印内容宽度过短，则需要添加宽度大于100%的div，否则字体大小设置无效 -->
            <p>打印测试</p>
            <h4>打印测试</h4>
        </div>
        <button onclick="printTest()">打印</button>
    </div>
</body>

</html>

```





