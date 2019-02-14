# 基础知识
tcpdump完成抓包工作，基础命令为
```text
tcpdump [options] [expression]
```

## 表达式expression

tcpdump的表达式由一个或多个"单元"组成，每个单元一般包含ID的修饰符和一个ID(数字或名称)。有三种修饰符：

1. type：指定ID的类型。
可以给定的值有host/net/port/portrange。例如"host foo"，"net 128.3"，"port 20"，"portrange 6000-6008"。默认的type为host。
2. dir：指定ID的方向。
可以给定的值包括src/dst/src or dst/src and dst，默认为src or dst。例如，"src foo"表示源主机为foo的数据包，"dst net 128.3"表示目标网络为128.3的数据包，"src or dst port 22"表示源或目的端口为22的数据包。
3. proto：通过给定协议限定匹配的数据包类型。
常用的协议有tcp/udp/arp/ip/ether/icmp等，若未给定协议类型，则匹配所有可能的类型。例如"tcp port 21"，"udp portrange 7000-7009"。

### 说明
* 一个基本的**表达式单元**格式为"proto dir type ID"。
* **表达式单元**之间可以使用操作符" and / && / or / || / not / ! "进行连接
* 使用括号"()"可以改变表达式的优先级

## 一些参考
- [完整的filter表达式参考](http://www.tcpdump.org/manpages/pcap-filter.7.html)
- [50 tcpdump Examples for Security and Networking Professionals](https://danielmiessler.com/study/tcpdump/)


# 任务场景

## 最常用的命令
用hexdump的形式显示抓取的报文
```bash
$ tcpdump -ns0 -X
10:45:19.930473 IP 123.58.182.251.443 > 10.10.10.43.50055: Flags [.], ack 223, win 14, options [nop,nop,TS val 2204598484 ecr 739145925], length 0
	0x0000:  a45e 60bf 4415 00f0 7e28 db01 0800 4500  .^`.D...~(....E.
	0x0010:  0034 49fa 4000 3706 b35f 7b3a b6fb 0a0a  .4I.@.7.._{:....
	0x0020:  0a2b 01bb c387 e682 c929 fdd7 43cd 8010  .+.......)..C...
	0x0030:  000e d0a0 0000 0101 080a 8367 80d4 2c0e  ...........g..,.
	0x0040:  78c5                                     x.
```

如果只抓取的是文本，可以用A参数
```bash
$ tcpdump -ns0 -A 
,....H1.GET /img/5.png HTTP/1.1
Host: 10.10.10.150:50081
Accept: image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)
Accept-Language: zh-cn
Accept-Encoding: gzip, deflate
Connection: keep-alive
```

## 查看网口
```bash
$ tcpdump -D
```

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
