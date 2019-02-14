# 基础知识
涉及sed，awk，curl，wget等基础命令。

## 工具推荐表
| 工具名称      | 描述 |
| ----------- | ------------------    |
| jq          | 最好用的json文件处理工具  |

## jq使用说明
* 格式化展示
```bash
echo -ne '{"a":1, "b":2}' | jq
# 相当于
echo -ne '{"a":1, "b":2}' | jq '.'
```
```json
{
 "a": 1,
 "b": 2
}
```
 

# 任务场景
* 根据进程名称列出PID
```bash
pgrep <pro>
```
或者
```bash
ps aux | grep <pro>
```

* 如何获取运行程序的目录？
```bash
pwdx <PID>
```
或者
```bash
ls -l /proc/<PID>/cwd
```


# 常见问题