Title: JwtBearer
Date: 2018-08-21 09:53:49


#### [JWT](https://jwt.io/) Token由以下三部分组成：


- [HEADER:ALGORITHM & TOKEN TYPE](https://tools.ietf.org/html/rfc7519#section-5)

    ```json
     {
      "alg": "HS256",
      "typ": "JWT"
    }
    ```

<!-- more -->

- [PAYLOAD:DATA](https://tools.ietf.org/html/rfc7519#section-4.1)

    ```json
    {
      "sub": "1234567890",
      "name": "John Doe",
      "iat": 1516239022
    }
    ```

- VERIFY SIGNATURE

    ```json
    HMACSHA256(
      base64UrlEncode(header) + "." +
      base64UrlEncode(payload),
      your-256-bit-secret
    )
    ```
    