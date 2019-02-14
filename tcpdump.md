# 基础知识

## 表达式


# 任务场景
## 抓取syn报文
```bash
$ tcpdump -n -i en0 'tcp[tcpflags] = tcp-syn'
```

## 抓取syn+ack报文
```bash
$ tcpdump -n -i en0 'tcp[tcpflags] & tcp-syn != 0 and tcp[tcpflags] & tcp-ack != 0'
```

## 抓取http的GET报文
"GET "的十六进制是47455420
```bash
$ tcpdump -n -i en0 'tcp[(tcp[12]>>2):4] = 0x47455420'
```
这里要注意：12的偏移是eth默认情况，如果涉及到其他的的网络类型，需要适当的进行修改。





# 常见问题
