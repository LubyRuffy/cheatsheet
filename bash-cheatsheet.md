# 基础知识

## 背景知识
* 变量
```bash
NAME="John"
echo $NAME
echo "$NAME"
echo "${NAME}!"
```

* 字符串引号
```bash
NAME="John"
echo "Hi $NAME"  #=> Hi John
echo 'Hi $NAME'  #=> Hi $NAME 单引号不做解析
```

* 函数
```bash
get_name() {
  echo "John"
}
echo "You are $(get_name)"
```

* 条件执行
```bash
git commit && git push
git commit || echo "Commit failed"
```

* 执行命令
```bash
echo "I'm in $(pwd)"
echo "I'm in `pwd`"
```

* 条件判断
```bash
if [ -z "$string" ]; then
  echo "String is empty"
elif [ -n "$string" ]; then
  echo "String is not empty"
fi
```

* 花括号展开
```bash
echo {A,B}.js  => A.js B.js
{A,B}	展开就是 A B
{A,B}.js	展开就是 A.js B.js
{1..5}	展开就是 1 2 3 4 5
```

* 注释

```bash
单行注释用#符号

多行注释用冒号空格单引号 : '任意换行'
```

## 参数
```bash
name="John"
echo ${name}
echo ${name/J/j}    #=> "john" (substitution)
echo ${name:0:2}    #=> "Jo" (slicing)
echo ${name::2}     #=> "Jo" (slicing)
echo ${name::-1}    #=> "Joh" (slicing)
echo ${food:-Cake}  #=> $food or "Cake"
length=2
echo ${name:0:length}  #=> "Jo"
```

```bash
STR="/path/to/foo.cpp"
echo ${STR%.cpp}    # /path/to/foo
echo ${STR%.cpp}.o  # /path/to/foo.o

echo ${STR##*.}     # cpp (extension)
echo ${STR##*/}     # foo.cpp (basepath)

echo ${STR#*/}      # path/to/foo.cpp
echo ${STR##*/}     # foo.cpp

echo ${STR/foo/bar} # /path/to/bar.cpp
STR="Hello world"
echo ${STR:6:5}   # "world"
echo ${STR:-5:5}  # "world"
SRC="/path/to/foo.cpp"
BASE=${SRC##*/}   #=> "foo.cpp" (basepath)
DIR=${SRC%$BASE}  #=> "/path/to/" (dirpath)
```

```bash
${FOO%suffix}	删除后缀Remove suffix
${FOO#prefix}	删除前缀Remove prefix
${FOO%%suffix}	Remove long suffix
${FOO##prefix}	Remove long prefix
${FOO/from/to}	Replace first match
${FOO//from/to}	Replace all
${FOO/%from/to}	Replace suffix
${FOO/#from/to}	Replace prefix
```

## 循环
* 基础循环
```bash
for i in /etc/rc.*; do
  echo $i
done
```

* 死循环
```bash
while true; do
  ···
done
```



## 函数

## 条件判断
完整参考：http://man7.org/linux/man-pages/man1/test.1.html

### 运算判断
```bash
# 字符串
[ STRING = STRING ]	等于
[ STRING != STRING ]	不等于
[ -z STRING ]	空字符
[ -n STRING ]	非空字符

# 数字
[ NUM -eq NUM ]	等于
[ NUM -ne NUM ]	不等于
[ NUM -lt NUM ]	小于Less than
[ NUM -le NUM ]	小于等于Less than or equal
[ NUM -gt NUM ]	大于Greater than
[ NUM -ge NUM ]	大于等于Greater than or equal

# 其他
[[ STRING =~ STRING ]]	正则Regexp 需要两个中括号
(( NUM < NUM ))	Numeric conditions
[ -o noclobber ]	If OPTIONNAME is enabled
[ ! EXPR ]	Not
[ X ] && [ Y ]	And
[ X ] || [ Y ]	Or
```

### 文件判断
```bash
[ -e FILE ]	文件存在（包含目录和文件）Exists
[ -r FILE ]	文件可读Readable
[ -h FILE ]	文件时链接Symlink
[ -d FILE ]	目录存在Directory
[ -w FILE ]	文件可写Writable
[ -s FILE ]	文件大小 > 0 bytes
[ -f FILE ]	文件存在（只是文件）File
[ -x FILE ]	文件可执行Executable
[ FILE1 -nt FILE2 ]	1 is more recent than 2
[ FILE1 -ot FILE2 ]	2 is more recent than 1
[ FILE1 -ef FILE2 ]	Same files
```

# 任务场景

# 常见问题
* -e -f -d的区别是什么？
-e是判断文件是否存在，包含-f和-d；-f只判断普通文件存在，-d只判断目录存在

* 条件语句中一个中括号[]与两个中括号[[]]的区别是什么？
区分在于是否进行了单词切分（word splitting），比如如下语句报错：
```bash
x='a b'; [ -s $x ] || echo "0"
bash: [: a: 需要二元表达式
```
换一种方式：
```bash
x='a b'; [[ -s $x ]] || echo "0"
0
```bash
如上等同于：
```bash
x='a b'; [ -s “$x” ] || echo "0"
0
```

* 删除前缀和长前缀有什么区别？
```bash
bash-4.4$ X="abc.123.com";echo ${X%.*}
abc.123
bash-4.4$ X="abc.123.com";echo ${X%%.*}
abc
同样
bash-4.4$ X="abc.123.com";echo ${X##*.}
com
bash-4.4$ X="abc.123.com";echo ${X#*.}
123.com
```