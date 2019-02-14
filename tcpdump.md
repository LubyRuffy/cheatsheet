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
```bash
$ tcpdump -n -i en0 'tcp[tcpflags] & tcp-syn != 0 and tcp[tcpflags] & tcp-ack != 0'
```






# 常见问题
