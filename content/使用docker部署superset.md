Title: 使用docker部署superset
Date: 2023-12-13 17:32:44
Tags: BI,superset,docker


```sh
git clone https://github.com/apache/superset.git

cd superset

docker compose up

docker compose -f docker-compose-non-dev.yml pull
docker compose -f docker-compose-non-dev.yml up

open http://localhost:8088
```

> 如何添加superset_config.py文件   
https://github.com/apache/superset/tree/master/docker#readme

```sh
docker cp superset_config.py superset_app:/app/pythonpath
docker restart superset_app
```

## 多语言

```sh
# /app/pythonpath/superset_config.py

# 多语言
LANGUAGES = {
    'en': {'flag': 'us', 'name': 'English'},
    "zh": {"flag": "cn", "name": "Chinese"},
}
```

## 开启sql模板

```sh
# /app/pythonpath/superset_config.py

# sql模版 https://superset.apache.org/docs/installation/sql-templating
FEATURE_FLAGS = {
    'ENABLE_TEMPLATE_PROCESSING': True
}
```

## 仅LDAP登录

> https://medium.com/@ozan/configure-ldap-and-local-user-login-on-superset-69fa4df4ee24


```sh
apt update && apt install libldap2-dev
pip install python-ldap
```

```sh
# /app/pythonpath/superset_config.py

from flask_appbuilder.security.manager import AUTH_DB,AUTH_LDAP

AUTH_TYPE = AUTH_LDAP 
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public" 
AUTH_LDAP_SERVER = "ldaps://server.yourdomain.com:636"
AUTH_LDAP_USE_TLS = False
AUTH_LDAP_BIND_USER = "CN=Surname\, Name,OU=ouSystemAccounts,DC=yourdomain,DC=com"
AUTH_LDAP_BIND_PASSWORD = "password"
AUTH_LDAP_SEARCH = "DC=your_domain,DC=com,DC=tr"
AUTH_LDAP_UID_FIELD = "sAMAccountName"
AUTH_LDAP_ALLOW_SELF_SIGNED=True
AUTH_LDAP_APPEND_DOMAIN=False
AUTH_LDAP_FIRSTNAME_FIELD="givenName"
AUTH_LDAP_LASTNAME_FIELD="sn"
AUTH_LDAP_USE_TLS=False
AUTH_USER_REGISTRATION=True
```

## 同时LDAP和本地登录

```sh
# /app/pythonpath/custom_security_manager.py

from superset.security import SupersetSecurityManager
from flask_appbuilder.security.views import AuthLDAPView
from flask_appbuilder.security.views import expose
from flask import g, redirect, flash
from flask_appbuilder.security.forms import LoginForm_db
from flask_login import login_user
from flask_appbuilder._compat import as_unicode

class AuthLocalAndLDAPView(AuthLDAPView):
    @expose("/login/", methods=["GET", "POST"])
    def login(self):
        if g.user is not None and g.user.is_authenticated:
            return redirect(self.appbuilder.get_url_for_index)
        form = LoginForm_db()
        if form.validate_on_submit():
            user = self.appbuilder.sm.auth_user_ldap(
                form.username.data, form.password.data
            )
            if not user:
                user = self.appbuilder.sm.auth_user_db(
                    form.username.data, form.password.data
                )
            if user:
                login_user(user, remember=False)
                return redirect(self.appbuilder.get_url_for_index)
            else:
                flash(as_unicode(self.invalid_login_message), "warning")
                return redirect(self.appbuilder.get_url_for_login)
        return self.render_template(
            self.login_template, title=self.title, form=form, appbuilder=self.appbuilder
        )


class CustomSecurityManager(SupersetSecurityManager):
    authldapview = AuthLocalAndLDAPView
    def __init__(self, appbuilder):
        super(CustomSecurityManager, self).__init__(appbuilder)
```

```sh
# /app/pythonpath/superset_config.py

import os
from superset.security import SupersetSecurityManager
from flask_appbuilder.security.manager import AUTH_DB,AUTH_LDAP
from custom_security_manager import CustomSecurityManager

AUTH_TYPE = AUTH_LDAP 
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public" 
AUTH_LDAP_SERVER = "ldaps://server.yourdomain.com:636"
AUTH_LDAP_USE_TLS = False
AUTH_LDAP_BIND_USER = "CN=Surname\, Name,OU=ouSystemAccounts,DC=yourdomain,DC=com"
AUTH_LDAP_BIND_PASSWORD = "password"
AUTH_LDAP_SEARCH = "DC=your_domain,DC=com,DC=tr"
AUTH_LDAP_UID_FIELD = "sAMAccountName"
AUTH_LDAP_ALLOW_SELF_SIGNED=True
AUTH_LDAP_APPEND_DOMAIN=False
AUTH_LDAP_FIRSTNAME_FIELD="givenName"
AUTH_LDAP_LASTNAME_FIELD="sn"
AUTH_LDAP_USE_TLS=False
AUTH_USER_REGISTRATION=True

CUSTOM_SECURITY_MANAGER = CustomSecurityManager
```

## rest api 登录


```sh
# /app/pythonpath/superset_config.py

AUTH_API_LOGIN_ALLOW_MULTIPLE_PROVIDERS = True
```