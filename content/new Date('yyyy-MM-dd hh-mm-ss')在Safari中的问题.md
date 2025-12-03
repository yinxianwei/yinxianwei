Title: new Date('yyyy-MM-dd hh:mm:ss')在Safari中的问题
Date: 2019-09-04 14:18:19


如：`new Date('2019-09-04 09:00:41')` 得到的是 `Invalid Date`

使用 `new Date('2019/09/04 09:00:41')` 是正常的


MDN: [a simplification of the ISO 8601 calendar date extended format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#Date_Time_String_Format)

> The standard string representation of a date time string is a simplification of the ISO 8601 calendar date extended format (see Date Time String Format section in the ECMAScript specification for more details). For example, "2011-10-10" (date-only form), "2011-10-10T14:48:00" (date-time form), or "2011-10-10T14:48:00.000+09:00" (date-time form with milliseconds and time zone) can be passed and will be parsed. When the time zone offset is absent, date-only forms are interpreted as a UTC time and date-time forms are interpreted as local time.


