Title: yarn puppeteer错误
Date: 2018-09-05 18:50:32



error /app/node_modules/puppeteer: Command failed.
Exit code: 1
Command: node install.js
Arguments:
Directory: /app/node_modules/puppeteer
Output:
ERROR: Failed to download Chromium r579032! Set "PUPPETEER_SKIP_CHROMIUM_DOWNLOAD" env variable to skip download.
{ Error: connect ETIMEDOUT 216.58.221.240:443
    at Object._errnoException (util.js:992:11)
    at _exceptionWithHostPort (util.js:1014:20)
    at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1186:14)
  code: 'ETIMEDOUT',
  errno: 'ETIMEDOUT',
  syscall: 'connect',

解决办法：

`export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true && yarn install`
