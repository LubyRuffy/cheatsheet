# 基础知识
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
```
echo "I'm in $(pwd)"
echo "I'm in `pwd`"
```

# 任务场景

# 常见问题