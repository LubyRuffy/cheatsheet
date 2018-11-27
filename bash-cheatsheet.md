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
echo 'Hi $NAME'  #=> Hi $NAME
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
### 基础判断

### 文件判断

# 任务场景

# 常见问题