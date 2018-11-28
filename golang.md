# 基础知识

* 变量
```golang
var a int //声明一个int类型的变量
var b struct { //声明一个结构体
    name string
}
var a = 8 //声明变量的同时赋值，编译器自动推导其数据类型
var a int = 8 //声明变量的同时赋值
var { //批量声明变量，简洁
    a int
    b string
}
```
我们看到有此两种方式：
    1. var name [type] = value
    如果不书写 type ,则在编译时会根据value自动推导其类型。
    2. name := value

* for循环
```golang
for i := 7; i <= 9; i++ {
    fmt.Println(i)
}
// 死循环
for {
}
// range便利
nums := []int{2, 3, 4}
```

* defer
    
defer 在声明时不会立即执行，而是在函数 return 后，再按照 FILO （先进后出）的原则依次执行每一个 defer。defer一般用于异常处理、释放资源、清理数据、记录日志等。
defer 还有一个重要的特性，就是即便函数抛出了异常，也会被执行的。 这样就不会因程序出现了错误，而导致资源不会释放了。
defer执行顺序为先进后出:
```golang
func b() { for i := 0; i < 4; i++ { defer fmt.Print(i) } }
```
我们可以看到依次输出了3210

* x.(type)
```golang
func MyPrintf(args ...interface{}) {  
    for _, arg := range args {  
        switch arg.(type) {  
            case int:  
                fmt.Println(arg, "is an int value.")  
            case string:  
                fmt.Println(arg, "is a string value.")  
            default:  
                fmt.Println(arg, "is an unknown type.")  
        }  
    }  
} 
```


# 任务场景
* 定义回调函数

```golang
type HookFunction func(ip string) bool
```

* 获取当前文件路径：os.Args[0]

* 如何拼接路径："path/filepath” : filepath.Join("a", "b", "c”)  
 
* 如何获取当前工作目录：os.Getwd

* 字符串如何转换为hex形式？
```golang
import "encoding/hex"
hex.EncodeToString(data)
```

* 定时程序
```golang
        ticker := time.NewTicker(time.Second * interval_second )
        go func() {
            for t := range ticker.C {
                log.Println("Tick at", t)
            }
        }()
```



# 常见问题