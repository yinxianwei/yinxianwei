Title: docker
Date: 2018-06-20 16:07:38


## 访问容器

`docker exec -it <CONTAINER ID> /bin/bash`

## 拷贝容器文件至本地

`docker cp <IMAGE>:<容器路径> <本地路径>`

## 拷贝本地文件至容器

`docker cp <本地文件> <IMAGE>:<容器路径>`


