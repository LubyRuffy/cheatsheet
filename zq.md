# 基础知识

## zq是什么
是jq的替代品，同样用于处理多行的json，可以通过预置的特性完成丰富的数据操作。

## 为什么要用zq
性能高，且能够内嵌到golang语言中。

## operator和function有什么区别？
operator是不带括号的，function是带括号的调用。比如cut a，以及flattern(a)。

<table>
  <tr>
    <td>操作符</td><td>功能说明</td><td>示例</td><td>备注</td>
  </tr>
  
<tr>
<td>assert</td>
<td>断言，成功或者返回错误</td>
<td>
     
```bash
> echo {a:1} | zq -z 'assert a > 0' - 
{a:1} 
> echo {a:-1} | zq -z 'assert a > 0' - 
error({message:"assertion failed",expr:"a > 0",on:{a:-1}})   
```
    
</td>
<td>跟where不同的就是是否报错</td>
</tr>
  
  
<tr>
<td>combine</td>
<td>合并不同的来源到一份数据</td>
<td>
     
```bash
echo '1 2' | zq -z 'fork (=>pass =>pass) ' -
1
2
1
2  
```
    
</td>
<td>fork是什么？pass是什么？参看fork
如何构造不同的数据来源？大约是from，后续需要确认。</td>
</tr>
  
  
<tr>
<td>cut</td>
<td>只保留选定的几个字段</td>
<td>
     
```bash
echo '{a:1,b:2,c:3}' | zq -z 'cut a,c' -
{a:1,c:3}
```
    
</td>
<td></td>
</tr>
  
  
<tr>
<td>drop</td>
<td>删除特定的字段</td>
<td>
     
```bash
echo '1 {a:1,b:2,c:3}' | zq -z 'drop a,b' -
1 {c:3}
```
    
</td>
<td></td>
</tr>
  
</table>

# 任务场景

## 如何进行格式转换
```bash
echo '{"port":81}' | zq -j 'cast(port,<string>)' -
"81"
echo '{"port":81}' | zq -j 'put port:=cast(port,<string>)' -
{"port":"81"}
echo '{"ip":"1.1.1.1","port":81}' | zq -j 'put c:="socks5://"+ip+":"+cast(port,<string>)' -
{"ip":"1.1.1.1","port":81,"c":"socks5://1.1.1.1:81"}
```

## 字符串可以用双引号也可以用单引号
```bash
echo '{"port":81}' | zq -j "put port:='a'" -
{"port":"a"}
echo '{"port":81}' | zq -j 'put port:="a"' -
{"port":"a"}
```
  
## 如何解析一个json字符串的值展开为json的object？
```
echo '{"msg":"{\"code\":200}"}' | zq -j 'msg:=parse_zson(msg)' -
{"msg":{"code":200}}
```

## 如何提取字段数组有内容的行？
```
❯ echo '{"a":null}\n{"a":[1,2]}' | zq -j 'a' -
{"a":null}
{"a":[1,2]}
❯ echo '{"a":null}\n{"a":[1,2]}' | zq -j 'len(a)>0' -
{"a":[1,2]}
```

## 如何替换一个数组中的元素，比如执行trim函数。
```
echo '{"b":1, "a":[" 1 ", "2 ", " 3"]}' | zq -j 'over a with b => (trim(this) | collect(this) | yield {b,collect}) | rename host:=collect' -
{"b":1,"host":["1","2","3"]}
```

## 如何选出没有字段的行？
```
echo '{a:1}{b:2}{a:3}' | zq -j 'not a' -
{"b":2}
```

## 如何替换字符串
```
echo '{"a":"b","c":"d"}' |  zq -j 'a:=replace(a, "b", "1")' -
{"a":"1","c":"d"}
```

## 如何取数组中间的一项内容？
```
echo '{"Sheet1":[["IP","域名"],["1.1.1.1","a.com"]],"Sheet2":[null,["Hello world."]]}' | zq -j 'over Sheet1 | this[0]' -
"IP"
"1.1.1.1"
```

## 保留原始内容，先处理其中的一个数据字段，再进行整合
```
echo '{"Sheet1":[["IP","域名"],["1.1.1.1","a.com"],["2.2.2.2","b.com"]],"Sheet2":[null,["Hello world."]]}' | zq -j 'yield {...this, ip:collect(over Sheet1 | flatten(this[0]))[0][1:]}' -
{"Sheet1":[["IP","域名"],["1.1.1.1","a.com"],["2.2.2.2","b.com"]],"Sheet2":[null,["Hello world."]],"ip":["1.1.1.1","2.2.2.2"]}
```

## 数组如何删除其中一个元素
```
echo "[1,2,3]" | zq -j 'this[1:]' -
[2,3]
```

## 如何取所有的key
```
❯ echo '{"a":1,"b":2}' | jq keys -c
["a","b"]
❯ echo '{"a":1,"b":2}' | zq -j 'fields(this)' -
[["a"],["b"]]
zq -j 'fields(this) | over this | this[0] | collect(this) | yield collect' -
["a","b"]
```

## 如何过滤key，比如排除开头为点符号.
```
echo '{".a":"1","b":2,"c":3}' | zq -j 'over this | key[0][0:1] != "."' -
{"key":["b"],"value":2}
{"key":["c"],"value":3}
```
  
# 常见问题
  
## yield到底有什么用？
如果不带yield，那么取的是完整的结构，带了yield就会以新的表达式来返回，比如：
```
❯ echo '{"a":[" 1 ", "2 ", " 3"]}' | zq -j 'a' -
{"a":[" 1 ","2 "," 3"]}
❯ echo '{"a":[" 1 ", "2 ", " 3"]}' | zq -j 'yield a' -
[" 1 ","2 "," 3"]
```
