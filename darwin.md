# Darwin/MacOS

## 如何查看监听一个端口的程序？
linux 下可以直接使用```netstat -anop```来完成，mac下不行，可以这样：
```shell
lsof -ni :8088 |grep LISTEN
```

## 查看目录占用情况时排除Library目录
```shell
du -lh -d1 -I "Library" ~
```