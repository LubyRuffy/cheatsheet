# curl

# 基础知识
## -v参数
用于打印更多调试信息，包括http header和证书cert等信息。

# 任务场景

## 同步显示http响应头
```bash
curl http://baidu.com -i
```

## 同步打印http请求和响应头
```bash
curl http://baidu.com -v
```

## 查看https证书信息
```bash
curl https://qq.com -k -v
```

## 请求自签名证书的网站
请求自签名的证书默认会提示错误：```curl: (60) SSL certificate problem: self signed certificate```
```bash
curl https://127.0.0.1 -k
```

## 自定义header请求
一些场景，比如：
- 需要绑定host，否则提示```curl: (60) SSL: no alternative certificate subject name matches target host name '58.250.137.36'```；
- 需要指定认证信息
```bash
curl https://58.250.137.36 -H "Host: qq.com" -k
curl http://127.0.0.1 -H "Authorization: Token 1234"
```

# 常见问题
