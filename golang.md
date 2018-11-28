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

### 同步的方式
* channel
* sync库
原子操作：
```golang	
import "sync/atomic"
var ops uint64
for i := 0; i < 50; i++ {
    go func() {
        atomic.AddUint64(&ops, 1)
    }
}
opsFinal := atomic.LoadUint64(&ops)
fmt.Println("ops:", opsFinal)
```
互斥操作：
```golang	
import "sync/atomic"
var mutex = &sync.Mutex{}
total := 0
for r := 0; r < 100; r++ {
	go func() {
		for {
			mutex.Lock()
			total += rand.Intn(5)
			mutex.Unlock()
			time.Sleep(time.Millisecond)
		}
	}()
}
time.Sleep(time.Second)
fmt.Println(total)
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
// 在close(jobs)后且消息都已经处理完，more为false
```

可以通过range遍历：
```golang
queue := make(chan string, 2)
for elem := range channel_queue {
}
```

可以完成线程池的功能：
```golang
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        fmt.Println("worker", id, "started  job", j)
        time.Sleep(time.Second)
        fmt.Println("worker", id, "finished job", j)
        results <- j * 2
    }
}
jobs := make(chan int, 100)
results := make(chan int, 100)
for w := 1; w <= 3; w++ {
    go worker(w, jobs, results)
}
for j := 1; j <= 5; j++ {
    jobs <- j
}
close(jobs)
for a := 1; a <= 5; a++ {
    <-results
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

## timer和ticker
都是通过定时返回channel消息，区别在于timer是一次性的，ticker是周期性的。
```golang
timer1 := time.NewTimer(2 * time.Second)
<-timer1.C
ticker := time.NewTicker(500 * time.Millisecond)
for t := range ticker.C {
    fmt.Println("Tick at", t)
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

## panic
直接报错退出：panic("a problem")

## time时间操作
```golang
p := fmt.Println
// We'll start by getting the current time.
now := time.Now()
p(now) //=> 2012-10-31 15:50:13.793654 +0000 UTC
// You can build a `time` struct by providing the
// year, month, day, etc. Times are always associated
// with a `Location`, i.e. time zone.
then := time.Date(
2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
p(then) //=> 2009-11-17 20:34:58.651387237 +0000 UTC
// You can extract the various components of the time
// value as expected.
p(then.Year()) //2009
p(then.Month()) //November
p(then.Day())    //17
p(then.Hour())    //20
p(then.Minute())    //34
p(then.Second())    //58
p(then.Nanosecond())    //651387237
p(then.Location()) //UTC
// The Monday-Sunday `Weekday` is also available.
p(then.Weekday())    //Tuesday
// These methods compare two times, testing if the
// first occurs before, after, or at the same time
// as the second, respectively.
p(then.Before(now))    //true
p(then.After(now))    //false
p(then.Equal(now))    //false

// The `Sub` methods returns a `Duration` representing
// the interval between two times.
diff := now.Sub(then)
p(diff) //25891h15m15.142266763s
// We can compute the length of the duration in
// various units.
p(diff.Hours()) //25891.25420618521
p(diff.Minutes()) //1.5534752523711128e+06
p(diff.Seconds()) //9.320851514226677e+07
p(diff.Nanoseconds()) //93208515142266763
// You can use `Add` to advance a time by a given
// duration, or with a `-` to move backwards by a
// duration.
p(then.Add(diff)) //2012-10-31 15:50:13.793654 +0000 UTC
p(then.Add(-diff)) //2006-12-05 01:19:43.509120474 +0000 UTC
```
### 固定格式
```golang
fmt.Println(time.Now().Format("2006-01-02 15:04:05")) #=> 2009-11-10 23:00:00
```
预定义的一些格式如下：
```golang
const (
        ANSIC       = "Mon Jan _2 15:04:05 2006"
        UnixDate    = "Mon Jan _2 15:04:05 MST 2006"
        RubyDate    = "Mon Jan 02 15:04:05 -0700 2006"
        RFC822      = "02 Jan 06 15:04 MST"
        RFC822Z     = "02 Jan 06 15:04 -0700" // RFC822 with numeric zone
        RFC850      = "Monday, 02-Jan-06 15:04:05 MST"
        RFC1123     = "Mon, 02 Jan 2006 15:04:05 MST"
        RFC1123Z    = "Mon, 02 Jan 2006 15:04:05 -0700" // RFC1123 with numeric zone
        RFC3339     = "2006-01-02T15:04:05Z07:00"
        RFC3339Nano = "2006-01-02T15:04:05.999999999Z07:00"
        Kitchen     = "3:04PM"
        // Handy time stamps.
        Stamp      = "Jan _2 15:04:05"
        StampMilli = "Jan _2 15:04:05.000"
        StampMicro = "Jan _2 15:04:05.000000"
        StampNano  = "Jan _2 15:04:05.000000000"
)
```

### 正则表达式
```golang
match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
fmt.Println(match) //true
r, _ := regexp.Compile("p([a-z]+)ch")
fmt.Println(r.MatchString("peach")) //true
fmt.Println(r.FindString("peach punch")) //peach
fmt.Println(r.FindStringIndex("peach punch")) //[0 5]
fmt.Println(r.FindStringSubmatch("peach punch")) //[peach ea]
fmt.Println(r.FindStringSubmatchIndex("peach punch")) //[0 5 1 3]
fmt.Println(r.FindAllString("peach punch pinch", -1)) //[peach punch pinch]
fmt.Println(r.FindAllStringSubmatchIndex("peach punch pinch", -1)) //[[0 5 1 3] [6 11 7 9] [12 17 13 15]]
fmt.Println(r.FindAllString("peach punch pinch", 2)) //[peach punch]
fmt.Println(r.Match([]byte("peach"))) //true
r = regexp.MustCompile("p([a-z]+)ch")
fmt.Println(r)  //p([a-z]+)ch
fmt.Println(r.ReplaceAllString("a peach", "<fruit>")) //a <fruit>
in := []byte("a peach")
out := r.ReplaceAllFunc(in, bytes.ToUpper) 
fmt.Println(string(out)) //a PEACH
```

### 字符串操作
```golang
import s "strings"
var p = fmt.Println
p("Contains:  ", s.Contains("test", "es")) // true
p("Count:     ", s.Count("test", "t")) //2
p("HasPrefix: ", s.HasPrefix("test", "te")) //true
p("HasSuffix: ", s.HasSuffix("test", "st")) //true
p("Index:     ", s.Index("test", "e")) //1
p("Join:      ", s.Join([]string{"a", "b"}, "-")) //a-b
p("Repeat:    ", s.Repeat("a", 5)) //aaaaa
p("Replace:   ", s.Replace("foo", "o", "0", -1)) //f00
p("Replace:   ", s.Replace("foo", "o", "0", 1)) //f0o
p("Split:     ", s.Split("a-b-c-d-e", "-")) //[a b c d e]
p("ToLower:   ", s.ToLower("TEST")) //test
p("ToUpper:   ", s.ToUpper("test")) //TEST
p()
p("Len: ", len("hello")) // 5
p("Char:", "hello"[1]) // 101
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

* 启动tour演练场
```bash
go get golang.org/x/tour #会自动生成tour程序，执行即可
`go env GOPATH`/bin/tour
```

* goroutines如何控制数量？

* 有没有类似于其他语言中的collection函数？

```golang
// Index returns the first index of the target string `t`, or
// -1 if no match is found.
func Index(vs []string, t string) int {
    for i, v := range vs {
        if v == t {
            return i
        }
    }
    return -1
}
// Include returns `true` if the target string t is in the
// slice.
func Include(vs []string, t string) bool {
    return Index(vs, t) >= 0
}
// Any returns `true` if one of the strings in the slice
// satisfies the predicate `f`.
func Any(vs []string, f func(string) bool) bool {
    for _, v := range vs {
        if f(v) {
            return true
        }
    }
    return false
}
// All returns `true` if all of the strings in the slice
// satisfy the predicate `f`.
func All(vs []string, f func(string) bool) bool {
    for _, v := range vs {
        if !f(v) {
            return false
        }
    }
    return true
}
// Filter returns a new slice containing all strings in the
// slice that satisfy the predicate `f`.
func Filter(vs []string, f func(string) bool) []string {
    vsf := make([]string, 0)
    for _, v := range vs {
        if f(v) {
            vsf = append(vsf, v)
        }
    }
    return vsf
}
// Map returns a new slice containing the results of applying
// the function `f` to each string in the original slice.
func Map(vs []string, f func(string) string) []string {
    vsm := make([]string, len(vs))
    for i, v := range vs {
        vsm[i] = f(v)
    }
    return vsm
}
func main() {
    // Here we try out our various collection functions.
    var strs = []string{"peach", "apple", "pear", "plum"}
    fmt.Println(Index(strs, "pear")) //2
    fmt.Println(Include(strs, "grape")) //false
    fmt.Println(Any(strs, func(v string) bool {
        return strings.HasPrefix(v, "p")
    })) //true
    fmt.Println(All(strs, func(v string) bool {
        return strings.HasPrefix(v, "p")
    })) //false
    fmt.Println(Filter(strs, func(v string) bool {
        return strings.Contains(v, "e")
    })) //[peach apple pear]
    fmt.Println(Map(strs, strings.ToUpper)) //[PEACH APPLE PEAR PLUM]

}
```

* 如何处理信号？
```golang
sigs := make(chan os.Signal, 1)
done := make(chan bool, 1)
signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)
go func() {
    sig := <-sigs
    fmt.Println(sig)
    done <- true
}()
fmt.Println("awaiting signal")
<-done
fmt.Println("exiting")
```

* 如何调用外部程序并且实时获取输出？


# 常见问题

* array和slice，数组与切片的区别是什么？

数组是值类型，把一个数组赋予给另一个数组时是发生值拷贝，而切片是指针类型，拷贝的是指针。slice通常通过make创建。

```golang
var a1 []int //无长度定义，是Slice
var a2 [5]int //无长度定义，是Slice
fmt.Println(a1, len(a1), cap(a1)) // [] 0 0
fmt.Println(a2, len(a2), cap(a2)) // [0 0 0 0 0] 5 5
```
