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






# 常见问题
