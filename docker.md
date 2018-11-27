# 基础知识
* 列出本地镜像：
```
docker images
```

* 获取镜像
```
docker pull <image>
```

* 运行镜像：
```
docker run -itd <image>
docker run -itd -v <local>:<container> <image>
docker run -p 127.0.0.1:9200:9200 <image> <cmd>
docker —name test123 <image>
```

* 删除镜像：
```
docker rmi <image>
```

* 删除tag：
```
docker rmi <image>
```

* 查看运行的容器：
```
docker ps 
docker ps -a #查看创建的所有容器：
```


# 任务场景
* 太占磁盘空间，需要删除

# 常见问题