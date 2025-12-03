Title: google push-notifications
Date: 2020-11-09 18:14:39


按照教程添加前端

https://developers.google.com/web/fundamentals/codelabs/push-notifications?hl=zh-cn


后端服务使用web-push

需要审核key:

https://console.firebase.google.com/project/test-22de3/settings/cloudmessaging/web:Mzg2N2Q4MzgtNmY5MS00YTAzLTkzYTItMDc2NTczZWJkYmE2?hl=zh-cn

服务端需要能正常访问google api




index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>push</title>
    <link href="https://unpkg.com/ant-design-vue@1.6.4/dist/antd.min.css"rel="stylesheet">
</head>

<body>
    <script src="https://cdn.jsdelivr.net/npm/vue"></script>
    <script src="https://unpkg.com/ant-design-vue@1.6.4/dist/antd.min.js"></script>
    <div id="app">
        <div style="padding: 40px;">
            <a-switch :checked="checked"
                      @change="onChange"
                      :loading="loading"></a-switch> 开启推送

            <pre v-if="subscription"
                 style="max-width: 800px;white-space: pre-wrap;background-color: #EEEEEE;padding: 16px;word-break: break-all;overflow: inherit;margin-top: 15px;">
                {{subscription}}
            </div>
        </div>
    </div>
    <script>
        const applicationServerPublicKey = 'BLkKIpmYE9jtuWVRQ6Ov8ypgYTDzxfq2i8rzj0AguQrXj1Qf-htthf9_o0ThaJWvpO9MogVjas7ENFHgFzfvMpI';

        new Vue({
            el: '#app',
            data() {
                return {
                    loading: false,
                    checked: false,
                    supported: false,
                    subscription: '',
                    swRegistration: undefined
                };
            },
            mounted() {
                this.support();
                this.regist();
            },
            methods: {
                onChange() {
                    this.loading = true;
                    if (this.checked) {

                    } else {
                        const applicationServerKey = this.urlB64ToUint8Array(applicationServerPublicKey);
                        this.swRegistration.pushManager
                            .subscribe({
                                userVisibleOnly: true,
                                applicationServerKey: applicationServerKey
                            })
                            .then(subscription => {
                                this.$message.success('开启成功');
                                this.subscription = JSON.stringify(subscription);
                                this.loading = false;
                                this.checked = true;
                            }, err => {
                                this.$message.error(err);
                                this.loading = false;
                            });
                    }
                },
                // 判断是否支持消息推送
                support() {
                    if ('serviceWorker' in navigator && 'PushManager' in window) {
                        this.supported = true;
                    } else {
                        this.supported = true;
                    }
                },
                regist() {
                    navigator.serviceWorker
                        .register('sw.js')
                        .then(swReg => {
                            console.log('Service Worker is registered', swReg);
                            this.swRegistration = swReg;
                            this.getSubscription();
                        }, err => {
                            console.error('Service Worker Error', err);
                        });
                },
                getSubscription() {
                    this.swRegistration.pushManager.getSubscription().then(subscription => {
                        if (subscription) {
                                console.log(subscription);
                            this.subscription = JSON.stringify(subscription);
                            this.checked = true;
                        }
                    }, err => { });
                },
                urlB64ToUint8Array(base64String) {
                    const padding = '='.repeat((4 - (base64String.length % 4)) % 4);
                    const base64 = (base64String + padding).replace(/\-/g, '+').replace(/_/g, '/');

                    const rawData = window.atob(base64);
                    const outputArray = new Uint8Array(rawData.length);

                    for (let i = 0; i < rawData.length; ++i) {
                        outputArray[i] = rawData.charCodeAt(i);
                    }
                    return outputArray;
                }
            }
        });
    </script>
</body>

</html>
```


// sw.js

```js
/*
 *
 *  Push Notifications codelab
 *  Copyright 2015 Google Inc. All rights reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License
 *
 */

/* eslint-env browser, serviceworker, es6 */

'use strict';

self.addEventListener('push', function (event) {
    console.log('[Service Worker] Push Received.');
    console.log(`[Service Worker] Push had this data: "${event.data.text()}"`);

    const title = 'Push Codelab';
    const options = {
        body: 'Yay it works.',
        icon: 'images/icon.png',
        badge: 'images/badge.png'
    };

    event.waitUntil(self.registration.showNotification(title, options));
});

```

服务端 main.js

```js
const webpush = require('web-push');

const pushSubscription = {
    endpoint:
        'https://fcm.googleapis.com/fcm/send/d3FnYYAEL8c:APA91bFM5XKXi50PfFaP14R4GQ4NQ89ZZfZuY2YdS_nT3HNS1oavF66AOTuFwWA3JEs00MafFynUY3TGqXs8VebpyIpCqFD8y72nIrlc3Ge_QLVwNzcRIKz412872ncgBIitTbly99fz',
    keys: { p256dh: 'BEA3VFLE-Q6rp2qYrABzn6fRjiYzaSGq5gTVGFlemTuD7WVHRX9zjbivdUEjiSLldP4WnpVYVLjl-BxqSpJGr7I', auth: '7PzGHHVMZMh7g39f3S1vNg' }
};

const vapidKeys = {
    privateKey: '3AtAfoXtsVOs2UjNZ-_JVZYnbfzxrjO4M0r9SZ2mw00',
    publicKey: 'BLkKIpmYE9jtuWVRQ6Ov8ypgYTDzxfq2i8rzj0AguQrXj1Qf-htthf9_o0ThaJWvpO9MogVjas7ENFHgFzfvMpI'
};

webpush.setGCMAPIKey('< FCM KEY >');

webpush.setVapidDetails('mailto:web-push-book@gauntface.com', vapidKeys.publicKey, vapidKeys.privateKey);

webpush.sendNotification(pushSubscription, 'The text of the notification').then(
    res => {
        console.log('success');
    },
    err => {
        console.log(err);
    }
);
```