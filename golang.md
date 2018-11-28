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

* if/else
```golang
if 7%2 == 0 {
    fmt.Println("7 is even")
} else {
    fmt.Println("7 is odd")
}
```

* for循环
```golang
for i := 7; i <= 9; i++ {
    fmt.Println(i)
}
// 死循环
for {
}
// range遍历数组
nums := []int{2, 3, 4}
for _, num := range nums {
}
// range遍历map
kvs := map[string]string{"a": "apple", "b": "banana"}
for k, v := range kvs {
    fmt.Printf("%s -> %s\n", k, v)
}
```

* switch
```golang
switch i {
case 1:
    fmt.Println("one")
case 2:
    fmt.Println("two")
case 3:
    fmt.Println("three")
}
// x.(type)的用法，只在switch配合使用
switch i.(type) {  
    case int:  
        fmt.Println(arg, "is an int value.")  
    case string:  
        fmt.Println(arg, "is a string value.")  
    default:  
        fmt.Println(arg, "is an unknown type.")  
}  
```

* array数组和slices切片
```golang
var a [5]int //存在默认值
a := [5]int{1, 2, 3, 4, 5}
var twoD [2][3]int
//slice与array最大的区别在于：动态增加数据长度只能是slice；也就是说array是固定的数据，slice是可动态扩展的数据
var a []int
a = append(a, 1)
```

* defer

defer 在声明时不会立即执行，而是在函数 return 后，再按照 FILO （先进后出）的原则依次执行每一个 defer。defer一般用于异常处理、释放资源、清理数据、记录日志等。
defer 还有一个重要的特性，就是即便函数抛出了异常，也会被执行的。 这样就不会因程序出现了错误，而导致资源不会释放了。
defer执行顺序为先进后出:
```golang
func b() { for i := 0; i < 4; i++ { defer fmt.Print(i) } }
```
我们可以看到依次输出了3210


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

* 启动tour演练场
```bash
go get golang.org/x/tour
`go env GOPATH`/bin/tour
```

# 常见问题

* array和slice，数组与切片的区别是什么？

数组是值类型，把一个数组赋予给另一个数组时是发生值拷贝，而切片是指针类型，拷贝的是指针。slice通常通过make创建。

```golang
var a1 []int //无长度定义，是Slice
var a2 [5]int //无长度定义，是Slice
fmt.Println(a1, len(a1), cap(a1)) // [] 0 0
fmt.Println(a2, len(a2), cap(a2)) // [0 0 0 0 0] 5 5
```