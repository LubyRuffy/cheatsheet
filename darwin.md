# Darwin/MacOS

## 如何查看监听一个端口的程序？
linux 下可以直接使用```netstat -anop```来完成，mac下不行，可以这样：
```
lsof -ni :8088 |grep LISTEN
```
