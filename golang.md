# 基础知识

* defer
defer 在声明时不会立即执行，而是在函数 return 后，再按照 FILO （先进后出）的原则依次执行每一个 defer. 
defer一般用于异常处理、释放资源、清理数据、记录日志等。这有点像面向对象语言的析构函数，优雅又简洁，是 Golang 的亮点之一。
defer 还有一个重要的特性，就是即便函数抛出了异常，也会被执行的。 这样就不会因程序出现了错误，而导致资源不会释放了。

# 任务场景
* 定义回调函数

```golang
type HookFunction func(ip string) bool
```

# 常见问题