# 基础知识
* 列出本地镜像：
docker images

* 运行镜像：
    - docker run -itd <image>
    - docker run -itd -v <local>:<container> <image>
    - docker run -p 127.0.0.1:9200:9200 <image> <cmd>
    - docker —name test123 <image>

*

# 任务场景
* 太占磁盘空间，需要删除

# 常见问题