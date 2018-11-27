# 基础知识
* 变量
```
NAME="John"
echo $NAME
echo "$NAME"
echo "${NAME}!"
```

* 字符串引号
```
NAME="John"
echo "Hi $NAME"  #=> Hi John
echo 'Hi $NAME'  #=> Hi $NAME
```

* 函数
```
get_name() {
  echo "John"
}
echo "You are $(get_name)"
```

* 条件执行
```
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