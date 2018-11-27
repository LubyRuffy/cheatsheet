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
docker run —name test123 <image>
docker run —it --rm <image> #运行后删除（在临时生成文件时很有用，比如编译）
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

* 在容器执行命令：
```
docker exec -it app_web_1 tail -f logs/development.log
docker exec -it app_web_1 bash
```


* 启动容器：
```
docker start <name>
```

* 查看容器配置：
```
docker inspect <name>
```

* 接入运行中的容器：
```
docker attach <name>
```

* 停止容器：
```
docker stop <name>
```

* 查看网络配置：
```
docker network ls
```

* 删除网络：
```
docker network rm <network_id>
```

* 查看容器的资源占用情况：
```
docker stats
```

* 重命名
```
docker rename hello_world2 hi_world
```

# 任务场景
* 太占磁盘空间，需要删除
* 删除所有未命名的镜像：
```
docker images -a | grep '<none>' | awk '{print $3}' | xargs -n 1 docker rmi
```

# 常见问题
* run和create有什么区别？

* export/import 与 save和load有什么区别？

* stop和kill有什么区别？

kill直接发送SIGKILL（默认）信号，stop先尝试发送SIGTERM信号（优雅地方式），等待一段时间过后再发送SIGKILL信号。所以默认都用stop，除非是想要强制关闭。

＊ run运行后的容器如何修改环境变量？
docker inspect bmhproxy 查看容器的目录，比如/var/lib/docker/containers/7803bd0b55fcc47dc37fa5acfa00ef3b225ace4b9a3a634e998447d343e61037/
MAC在~/Library/Containers/