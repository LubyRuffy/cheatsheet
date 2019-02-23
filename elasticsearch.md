# 基础知识

# 任务场景
* 如何对ES6进行监控？以前的bigdesk不能用了？
- https://github.com/lenolee16/bigdesk

```bash
git clone https://github.com/lenolee16/bigdesk
cd bigdesk/_site
# 随便启动一个服务器
python -m SimpleHTTPServer
```

- 也可以用cerebro：
```bash
docker run -d -p 9000:9000 --name cerebro yannart/cerebro:latest
open http://127.0.0.1:9000/
```

# 常见问题