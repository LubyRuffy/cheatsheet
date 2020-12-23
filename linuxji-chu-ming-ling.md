# 基础知识
涉及sed，awk，curl，wget等基础命令。

## 工具推荐表
| 工具名称      | 描述 |
| ----------- | ------------------    |
| [jq](jq.md)          | 最好用的json文件处理工具  |
| [tcpdump](tcpdump.md) | 最基础的网络抓包分析工具 |
 

# 任务场景
* 根据进程名称列出PID
```bash
pgrep <pro>
```
或者
```bash
ps aux | grep <pro>
```

* 如何获取运行程序的目录？
```bash
pwdx <PID>
```
或者
```bash
ls -l /proc/<PID>/cwd
```

* 添加用户
```bash

```

* hexstring转换为binary，十六进制字符串转换为二进制
```bash
echo "4141" | xxd -r -p
AA

echo "4141" | xxd -r -p | hexdump -C
00000000  41 41                                             |AA|
00000002
```

* 对比两个二进制文件
vimdiff查看完整：
```bash
vimdiff <(xxd id1.ser) <(xxd id2.ser)
```
或者用colordiff
```bash
colordiff <(xxd id1.ser) <(xxd id2.ser)
```

* 全局监控一个文件是否尝试被请求（没有完整路径，没有进程号，只是根据文件名来判断，比如查看一个进程读取文件的目录顺序）
```bash
# 需要安装fatrace，mac上直接使用fs_usage
sudo fatrace | grep libxar
```

# 常见问题
