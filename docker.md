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

* 启动容器：
```
docker start <name>
```

* 接入运行中的容器：
```
docker attach <name>
```

* 停止容器：
```
docker stop <name>
```

* 删除容器（每次run一下都会生成一个新的容器）：
docker ps -a | grep elastic | awk '{print $1}' | xargs docker rm

* 查看网络配置：
docker network ls

* 删除网络：
docker network rm atsdockers_mynet

* 查看容器配置：
docker inspect <name>

* 查看单个容器网络信息：

* 容器间网络互通：
通过docker compose来实现，links命令即可

* 容器的内存分配：
通过docker compose来实现，mem_limit命令即可

* 查看容器的资源占用情况：
docker stats

* 重命名
docker rename hello_world2 hi_world

# 任务场景
* 太占磁盘空间，需要删除
* 删除所有未命名的镜像：
```
docker images -a | grep '<none>' | awk '{print $3}' | xargs -n 1 docker rmi
```

# 常见问题