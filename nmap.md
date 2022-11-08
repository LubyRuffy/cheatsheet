# 基础知识

## 参数说明
### 端口扫描技术
端口扫描技术分为SYN，UDP，CONNECT，ACK，FIN，NULL，XMAS，IDEL扫描等等。。但是考虑到通用性的问题（很多技术以来于目标系统，绝大部分用不上），最常用的是CONNECT，SYN，UDP扫描

| 参数 | 说明 | 示例 |
| -- | -- | -- |
| -sS | TCP SYN方式 | nmap -sS 192.168.1.1 |
| -sT | TCP 全连接方式 | nmap -sT 192.168.1.1 |
|   -sU  |     UDP端口扫描     | nmap -sU 192.168.1.1 |
|   -sA  |   TCP ACK方式  | nmap -sA 192.168.1.1 |

### 主机发现
| 参数 |        说明        |          示例          |
| -- | -- | -- |
|   -Pn  |         只做端口扫描.         | nmap -Pn 192.168.1.1 |
|   -sn  |       制作主机发现.      | nmap -sn 192.168.1.1 |
|   -PR  | 本地的ARP网络扫描. | nmap -PR 192.168.1.1 |
|   -n   |     禁用 DNS 解析.     |  nmap -n 192.168.1.1 |

### 端口的分组
| 参数 |        说明        |          示例          |
| -- | -- | -- |
|   -p   |    端口或者端口范围.    | nmap -p 22-80 192.168.1.1 |
|   -p-  |      扫描所有端口.      |    nmap -p- 192.168.1.1   |
|   -F   | 快速端口扫描. (top 100) |    nmap -F 192.168.1.1    |

### 服务和版本的发现
默认情况下只做端口扫描，不做协议识别（显示出来的协议是根据端口号来推测的，非真实判断）。

| 参数 |        说明        |          示例          |
| -- | -- | -- |
|   -sV  | 识别服务的版本. | nmap -sV 192.168.1.1 |
|   -A   |      识别操作系统,版本, 执行脚本script扫描以及traceroute.      |  nmap -A 192.168.1.1 |
|   -O  | 通过TCP/IP协议来判断操作系统. | nmap -sV 192.168.1.1 |

### 时间和性能
| 参数 |        说明        |          示例          |
| -- | -- | -- |
|   -T0  |       Paranoid IDS evasion.      | nmap -T0 192.168.1.1 |
|   -T1  |        Sneaky IDS evasion.       | nmap -T1 192.168.1.1 |
|   -T2  |        Polite IDS evasion. (requires less bandwidth)       | nmap -T2 192.168.1.1 |
|   -T3  |   Normal IDS evasion. (default)  | nmap -T3 192.168.1.1 |
|   -T4  |      Aggressive speed scan.(requires fast network)      | nmap -T4 192.168.1.1 |
|   -T5  |        Insane speed scan.(requires massive network speed)        | nmap -T5 192.168.1.1 |

### NSE脚本
| 参数 |        说明        |          示例          |
| -- | -- | -- |
|       -sC       |  Default script scan.  | nmap -sC 192.168.1.1 |
| --script banner | 执行特定的脚本.(这里是banner举例) | nmap --script banner 192.168.1.1 |
# 任务场景

### 扫描网段最常用的语句
```bash
nmap -sV -sS 10.10.10.0/24
```
默认端口列表，获取服务信息。-sS和-sU需要root权限。

### 全端口扫描
```bash
nmap -p 1–65535 1.1.1.1
```

### PING网段
```bash
nmap -sP 10.0.0.0/24
```

### 扫描单个TCP端口
```bash
nmap -p 80 1.1.1.1
```
这种是默认的TCP Connect扫描方式。

### SYN方式扫描
```bash
nmap -sS -p 80 1.1.1.1
```

### 扫描单个UDP端口
```bash
nmap -p U:161 1.1.1.1
```

### 不启用PING直接做端口扫描
```bash
nmap -P0 1.1.1.1
```

### 扫描返回banner信息
```bash
nmap --script banner 1.1.1.1
```
```
PORT     STATE SERVICE
22/tcp   open  ssh
|_banner: SSH-2.0-OpenSSH_7.4
```

### 扫描多个IP
```bash
nmap 1.1.1.1 2.2.2.2
nmap 1.1.1.0/24
```

### 查看网卡列表
```bash
nmap --iflist
```

### 使用指定网卡进行扫描
```bash
nmap -e eth0 127.0.0.1
```

# 常见问题
