# 基础知识

## 变量
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

## if/else
```golang
if 7%2 == 0 {
    fmt.Println("7 is even")
} else {
    fmt.Println("7 is odd")
}
```

## for循环
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
// range遍历channel
queue := make(chan string, 2)
for elem := range channel_queue {
}
```

## switch
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

## array数组和slices切片
```golang
var a [5]int //存在默认值
a := [5]int{1, 2, 3, 4, 5}
var twoD [2][3]int
//slice与array最大的区别在于：动态增加数据长度只能是slice；也就是说array是固定的数据，slice是可动态扩展的数据
var a []int 也可以
a = append(a, 1)
```

* map
```golang
m := make(map[string]int)
n := map[string]int{"foo": 1, "bar": 2}
```

## func函数
```golang
func plus(a int, b int) int {
}
//如果类型一致，可以一起定义
func plusPlus(a, b, c int) int {
}
//多个返回值
func vals() (int, int) {
    return 3, 7
}
//可变参函数Variadic
func sum(nums ...int) {
}
nums := []int{1, 2, 3, 4}
sum(nums...) //通过...三个点进行展开
```

## Closures闭包
```golang
func intSeq() func() int {
    i := 0
    return func() int {
        i++
        return i
    }
}
```

## 指针

跟C一样，通过*表示，通过&取值的指针。

## 结构
```golang
type person struct {
    name string
    age  int
}
person{"Bob", 20}
person{name: "Alice", age: 30}
//可以直接给结构定义方法methods
func (p *person) myage() int {
    return p.age
}
//直接调用
a:=person{"Bob", 20}
fmt.Println(a.myage())
```

## 接口Interface

类似于C++里面的虚类：
```golang
type geometry interface {
    area() float64
}
type circle struct {
    radius float64
}
func (r rect) area() float64 {
    return r.width * r.height
}
func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}
func measure(g geometry) {  //参数类型为接口类型
    fmt.Println(g.area())
}
```

## Goroutines

简单粗暴的理解类似于线程

```golang	
func f(from string) {
}
go f("goroutine")
go func(msg string) {
    fmt.Println(msg)
}("going")
```

## Channels
```golang
messages := make(chan string)
go func() { messages <- "ping" }()
msg := <-messages
fmt.Println(msg)
```
没有指定buffer的话，会死锁等到有消息可读。
```golang
messages := make(chan string, 2)
messages <- "buffered"
messages <- "channel"
fmt.Println(<-messages)
fmt.Println(<-messages)
```
可以用在等待goroutines完成
```golang
func worker(done chan bool) {
    fmt.Print("working...")
    time.Sleep(time.Second)
    fmt.Println("done")
    done <- true
}
func main() {
    done := make(chan bool, 1)
    go worker(done)
    <-done
}
```

close可以让channel的接收方得到通知。
```golang
j, more := <-jobs
// 在close(jobs)后，more为false
```

可以通过range遍历：
```golang
queue := make(chan string, 2)
for elem := range channel_queue {
}

```

## select消息
有时有多个channels需要监控，可以统一通过select来完成：

```golang
go func() {
    time.Sleep(1 * time.Second)
    c1 <- "one"
}()
go func() {
    time.Sleep(2 * time.Second)
    c2 <- "two"
}()
for i := 0; i < 2; i++ {
    select {
    case msg1 := <-c1:
        fmt.Println("received", msg1)
    case msg2 := <-c2:
        fmt.Println("received", msg2)
    }
}
```

上面是阻塞模式，可以增加default进行非阻塞模式：
```golang
select {
case messages <- msg:
    fmt.Println("sent message", msg)
default:
    fmt.Println("no message sent")
}
```

可以利用select来解决超时跟踪：
```golang
select {
case res := <-c1:
    fmt.Println(res)
case <-time.After(1 * time.Second):
    fmt.Println("timeout 1")
}
```

## defer

defer 在声明时不会立即执行，而是在函数 return 后，再按照 FILO （先进后出）的原则依次执行每一个 defer。defer一般用于异常处理、释放资源、清理数据、记录日志等。
defer 还有一个重要的特性，就是即便函数抛出了异常，也会被执行的。 这样就不会因程序出现了错误，而导致资源不会释放了。
defer执行顺序为先进后出:
```golang
func b() {
    for i := 0; i < 4; i++ {
        defer fmt.Print(i)
    }
}
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
go get golang.org/x/tour #会自动生成tour程序，执行即可
`go env GOPATH`/bin/tour
```

* goroutines如何控制数量？


# 常见问题

* array和slice，数组与切片的区别是什么？

数组是值类型，把一个数组赋予给另一个数组时是发生值拷贝，而切片是指针类型，拷贝的是指针。slice通常通过make创建。

```golang
var a1 []int //无长度定义，是Slice
var a2 [5]int //无长度定义，是Slice
fmt.Println(a1, len(a1), cap(a1)) // [] 0 0
fmt.Println(a2, len(a2), cap(a2)) // [0 0 0 0 0] 5 5
```
