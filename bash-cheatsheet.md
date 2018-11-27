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
echo {A,B}.js
{A,B}	Same as A B
{A,B}.js	Same as A.js B.js
{1..5}	Same as 1 2 3 4 5
```

## 参数

## 循环

## 函数

## 条件
完整参考：http://man7.org/linux/man-pages/man1/test.1.html

### 运算判断
```
字符串
[ STRING = STRING ]	等于
[ STRING != STRING ]	不等于
[ -z STRING ]	空字符
[ -n STRING ]	非空字符

数字
[ NUM -eq NUM ]	等于
[ NUM -ne NUM ]	不等于
[ NUM -lt NUM ]	小于Less than
[ NUM -le NUM ]	小于等于Less than or equal
[ NUM -gt NUM ]	大于Greater than
[ NUM -ge NUM ]	大于等于Greater than or equal

其他
[[ STRING =~ STRING ]]	正则Regexp 需要两个中括号
(( NUM < NUM ))	Numeric conditions
[ -o noclobber ]	If OPTIONNAME is enabled
[ ! EXPR ]	Not
[ X ] && [ Y ]	And
[ X ] || [ Y ]	Or
```

### 文件判断
```
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