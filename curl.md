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
- 代理不支持dns解析
```bash
curl https://58.250.137.36 -H "Host: qq.com" -k
curl http://127.0.0.1 -H "Authorization: Token 1234"
curl -H"Host: ip.bmh.im" http://34.216.19.233/h -x http://181.177.20.67:80 
```

## 自定义dns解析
跟上面绑定host头一样的效果，这里我们不用修改host头，不用修改hosts文件，直接：
```bash
curl https://ip.bmh.im --resolve ip.bmh.im:443:127.0.0.1
```
这个与直接host头有一个很大的不同，绑定host头请求https的时候，tls握手是没有域名的，而这种方式则在tls握手的时候就带上去了。

## 结合jq使用不显示中间的进度提示
结合其他命令行比如jq会显示中间的提示：
```
curl http://127.0.0.1 | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   243  100   243    0     0   6004      0 --:--:-- --:--:-- --:--:--  6075
{
}
```
使用-s参数：
```
curl -s http://127.0.0.1 | jq
{
}
```

## 有无办法让"curl -F"发出去的filename包含../，而不要normalize它？
```
curl -F "file=@test.png;filename=../test.png"
```

## 请求路径带有两个点符号`..`
默认是不可以的，带上`--path-as-is`参数就可以了：
```shell
curl http://127.0.0.1:11245/../../../abc -vv  --path-as-is
* processing: http://127.0.0.1:11245/../../../abc
*   Trying 127.0.0.1:11245...
* Connected to 127.0.0.1 (127.0.0.1) port 11245
> GET /../../../abc HTTP/1.1
> Host: 127.0.0.1:11245
> User-Agent: curl/8.2.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Sat, 09 Mar 2024 15:45:53 GMT
< Content-Length: 29
< Content-Type: text/plain; charset=utf-8
<
* Connection #0 to host 127.0.0.1 left intact
Exact match for /../../../abc%
```


# 常见问题
