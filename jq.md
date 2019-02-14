# 基础知识

* 格式化展示
```bash
$ echo -ne '{"a":1, "b":2}' | jq
# 相当于
$ echo -ne '{"a":1, "b":2}' | jq '.'
```
```json
{
 "a": 1,
 "b": 2
}
```

* 返回某一个字段的值
```bash
$ echo -ne '{"a":1, "b":2}' | jq '.a'
1
```

# 任务场景
* 如何组合显示多个key对应的value？
```bash
$ jq '.fields | "\(.ip[0]):\(.port[0])"'
```

# 常见问题