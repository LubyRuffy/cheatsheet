# 基础知识
tcpdump完成抓包工作，基础命令为
```text
tcpdump [options] [expression]
```

## 表达式expression
* host

    源或者目标
    ```
    host 192.168.1.1
    ```
    源地址
    ```
    src host 192.168.1.1
    ```
    目标地址
    ```
    dst host 192.168.1.1
    ```


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

## 实时远程tcpdump抓包到本地wireshark显示
很多情况下需要交互分析，用wireshark更方便一点，这时候就可以通过管道实时推送到wireshark，命令如下：
```bash
$ ssh <user>@<ip> tcpdump -U -s0 -w - <filter> | wireshark -k -i -
```



# 常见问题
