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

# 强制删除
docke rmi -f <image>
```

* 查看运行的容器：
```
docker ps 
docker ps -a #查看创建的所有容器：
```

* 在容器执行命令：
```
docker exec -it <container> tail -f logs/development.log
docker exec -it <container> bash
```

* 挂载磁盘 -v
```
docker exec -it -v <local>:<container> <container> 
```

* 设置环境变量 -e
```
docker exec -it -e a=b <container> 
```

* 启动容器：
```
docker start <container>
```

* 查看容器配置：
```
docker inspect <container>
```

* 接入运行中的容器：
```
docker attach <container>
```

* 停止容器：
```
docker stop <container>
```

* 删除容器：
```
docker rm <container>

# 强制删除
docker rm -f <container>
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
```
docker container prune
docker system prune 
```
* 删除所有未命名的镜像：
```
docker images -a | grep '<none>' | awk '{print $3}' | xargs -n 1 docker rmi
```

* 发布到hub.docker.io
```
docker login 确保登陆成功
docker tag <image> <project>/<image>:lastest
docker push <project>/<image>:lastest

如果是自己的私有仓库，可以：
docker login docker.yousite.com
docker tag <image> docker.yousite.com/<project>/<image>:lastest
docker push docker.yousite.com/<project>/<image>:lastest

```

# 常见问题
* run和create有什么区别？

    docker create命令能够基于镜像创建容器。 该命令执行的效果类似于docker run -d，即创建一个将在系统后台运行的容器。 但是与docker run -d不同的是，docker create创建的容器并未实际启动，还需要执行docker start命令或docker run命令以启动容器。 事实上，docker create命令常用于在启动容器之前进行必要的设置。
    
* export/import 与 save和load有什么区别？
    1. docker save保存的是镜像（image），docker export保存的是容器（container）；
    2. docker load用来载入镜像包，docker import用来载入容器包，但两者都会恢复为镜像；
    3. docker load不能对载入的镜像重命名，而docker import可以为镜像指定新名称。


* stop和kill有什么区别？

    kill直接发送SIGKILL（默认）信号，stop先尝试发送SIGTERM信号（优雅地方式），等待一段时间过后再发送SIGKILL信号。所以默认都用stop，除非是想要强制关闭。

* run运行后的容器如何修改环境变量？

    如下方式仅仅在linux下面有效：
    docker inspect <container> 查看容器的目录，比如/var/lib/docker/containers/7803bd0b55fcc47dc37fa5acfa00ef3b225ace4b9a3a634e998447d343e61037/
