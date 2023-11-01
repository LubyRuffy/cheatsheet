# 基础知识

## 基础表达式
基础表达式（Basic filters)是 jq 提供的基本过滤器，用来访问 JSON 对象中的属性，主要有以下几种：

- '.' 符号。单独的一个'.'符号用来表示对作为表达式输入的整个 JSON 对象的引用。
- JSON 对象操作。jq 提供两种基本表达式用来访问 JSON 对象的属性：'.<attributename>'和'.<attributename>?'。正常情况下，这两个表达式的行为相同：都是访问对象属性，如果 JSON 对象不包含指定的属性则返回 null。区别在于，当输入不是 JSON 对象或数组时，第一个表达式会抛出异常。第二个表达式无任何输出。
- 数组操作。jq 提供三种基础表达式来操作数组：
  - 迭代器操作('.[]'). 该表达式的输入可以是数组或者 JSON 对象。输出的是基于数组元素或者 JSON 对象属性值的 iterator。
  - 访问特定元素的操作('.[index]'或'.[attributename]')。用来访问数组元素或者 JSON 对象的属性值。输出是单个值
  - 数组切片操作('.[startindex:endindex]')，其行为类似于 python 语  言中数组切片操作。
- 表达式操作(','和 '|')。表达式操作是用来关联多个基础表达式。其中逗号表示对同一个输入应用多个表达式。管道符表示将前一个表达式的输出用作后一个表达式的输入。当前一个表达式产生的结果是迭代器时，会将迭代器中的每一个值用作后一个表达式的输入从而形成新的表达式。例如'.[]|.+1', 在这个表达式中，第一个子表达式'.[]'在输入数组上构建迭代器，第二个子表达式则在迭代器的每个元素上加 1。

## 内置运算支持
jq 内部支持的数据类型有：数字，字符串，数组和对象(object)。并且在这些数据类型的基础上, jq 提供了一些基本的操作符来实现一些基本的运算和数据操作。列举如下：

- 数学运算。对于数字类型，jq 实现了基本的加减乘除(/)和求余(%)运算。对于除法运算，jq 最多支持 16 位小数。
- 字符串操作。jq 提供字符串的连接操作(运算符为'+'，例如："tom "+"jerry"结果为"tom jerry")，字符串的复制操作(例如：'a'*3 结果为'aaa')，以及字符串分割操作(将字符串按照指定的分割符分成数组，例如"sas"/"s"的结果为["","a",""]，而"sas"/"a"的结果为["s","s"]。
- 数组操作。jq 提供两种数组运算：并集('+')运算，结果数组中包含参与运算的数组的所有元素。差集运算('-')，例如：有数组 a,b, a-b 的结果为所有在 a 中且不包含在 b 中的元素组成的数组。
- 对象操作。jq 实现了两个 JSON 对象的合并操作(merge)。当两个参与运算的对象包含相同的属性时则保留运算符右侧对象的属性值。有两种合并运算符：'+'和'*'。所不同的是，运算符'+'只做顶层属性的合并，运算符'*'则是递归合并。例如：有对象 a={"a":{"b":1}}, b={"a":{"c":2}}，a+b 的结果为{"a":{"c":2}}，而 a*b 的结果为{"a":{"b":1,"c":2}}
- 比较操作：jq 内部支持的比较操作符有==, !=,>,>=,<=和<。其中，'=='的规则和 javascript 中的恒等('===')类似，只有两个操作数的类型和值均相同时其结果才是 true。
- 逻辑运算符: and/or/not。在 jq 逻辑运算中，除了 false 和 null 外，其余的任何值都等同于 true。
- 默认操作符('//'), 表达式'a//b'表示当表达式 a 的值不是 false 或 null 时，a//b 等于 a，否则等于 b。

## 基础操作
* 格式化高亮展示
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

* 返回数组的值
```bash
$ echo -ne '{"a":[1,2]}' | jq '.a[0]'
1
```

# 任务场景
## 如何列出所有的属性名称（key）?
```bash
$ echo -ne '{"a":1, "b":2, "c":{"c1":[11,22,33], "c2":[123,456,789]}}' | jq 'keys'
[
  "a",
  "b",
  "c"
]
```
这里看到只针对顶级的进行处理，如果想打印子对象的keys，可以这样：
```bash
$ echo -ne '{"a":1, "b":2, "c":{"c1":[11,22,33], "c2":[123,456,789]}}' | jq '.c | keys'
[
  "c1",
  "c2"
]
```

## 如何组合显示多个key对应的value？
```json
{
  "a": 1,
  "b": 2,
  "c": {
    "c1": [
      11, 22, 33
    ],
    "c2": [
      123, 456, 789
    ]
  }
}
```
```bash
$ jq '.c | "\(.c1[0]):\(.c2[0])"'
"11:123"
```

直接拼凑就行了：
```bash
echo -ne '{"a":"1", "b":"2"}' | jq '.a + " " + .b'
"1 2"
# 可以结合 --raw-output使用
```

## 整型int转换成字符串string
```bash
echo -ne '{"a":"1", "b":"2"}' | jq '(.a|tostring) + " " + (.b|tostring)'  --raw-output
```

## 处理数据并导出文件
```bash
$ jq ".key1" < file.json > out.txt
```

## 输出的字符串如何不要双引号
```bash
$ echo '{"a":"1234"}' | jq ".a" --raw-output
```

## 如何打印某个属性的字符长度
```bash
$ echo '{"a":"1234"}' | jq ".a | length"
4
```

## 如何打印属性以及长度
```bash
$ echo '{"a":"1234"}' | jq ".a, (.a | length)"
"1234"
4
```

## 如何根据值的长度过滤
```bash
$ echo -e '{"a":"1234"}\n{"a":"1"}' | jq "select((.a | length)>3) | .a"
"1234"
```

## 如何最小（minimum）格式化输出
-c 参数
```bash
$ echo -e '{"a":"1234",\n   "b":     1}' | jq -c
{"a":"1234","b":1}
```

## 打印object所有属性field的长度
```bash
$ echo '{"a":"1234"}' | jq ". | length"
1
```

## 根据某个属性的值过滤父节点的名称
```bash
$ echo '{"lxdns.com":{"name":"网宿 CDN","link":"https://cn.chinacache.com/"},"cloudflare.net":{"name":"Cloudflare","link":"https://www.cloudflare.com"}}' | jq 'keys[] as $k | select(.[$k].name=="网宿 CDN") | $k'
"lxdns.com"
```
  
## 排除存在某个字段的项，再显示特定字段
```bash
echo -e '{"a":1}\n{"a":2,"error":"yes"}\n{"a":3}' | jq '. | select(.error == null) | .a' 
1
3
```
  
## 如何打印tab等字符
```bash
echo -ne '{"a":"1", "b":"2"}' | jq 'join("\t")' --raw-output
echo -ne '{"a":"1", "b":"2"}' | jq '.a + "\t" + .b' --raw-output
1	2
```  
  
## 根据字段做条件筛选
```bash
echo -ne '{"a":"1", "level":"1"}\n{"a":"2", "level":"2"}\n{"a":"3", "level":"3"}' | jq 'select((.level|tonumber)==2) | .a'
"2"
```  
也可以多条查询
```bash
echo -ne '{"a":"1", "level":"1"}\n{"a":"2", "level":"2"}\n{"a":"3", "level":"3"}' | jq 'select((.level|tonumber)==1 or (.level|tonumber)==3) | .a'
"1"
"3"
```
  
## 根据值是否包含子字符串进行过滤显示
```bash
echo -ne '{"a":"123"}\n{"a":"234"}\n{"a":"345"}' | jq 'select(.a|contains("2"))' -c
{"a":"123"}
{"a":"234"}
```

## 不包含
在select里面用not就好了：
```bash
echo -ne '{"a":"123"}\n{"a":"234"}\n{"a":"345"}' | jq 'select(.a | contains("2") | not )' -c
{"a":"345"}
```
  
## 把整个文件根据某个字段的值进行排序
```bash
echo -ne '{"a":"234"}\n{"a":"123"}\n{"a":"345"}' | jq -s -c 'sort_by(.a)[]'
{"a":"123"}
{"a":"234"}
{"a":"345"}
```
  
## 获取数组中元素的field字段值
```bash
echo -ne '[{"a":1},{"a":2}]' | jq '.[].a'
1
2
```
  
## 取两个数组的交集
```bash
echo '{"a":[1,2,3,4],"b":[2,4,6,8,10]}' | jq '.a[] as $x | .b[] | select($x == .)' -c
2
4
```
  
## 如何合并多行的字段？
```
echo -n '{"a":1}\n{"b":2}' | jq -s -c 'reduce .[] as $item({}; .+$item)'
{"a":1,"b":2}
```
  
## 根据某个字段进行聚合
```
❯ echo '{"ip":"1.1.1.1","a":1}\n{"ip":"1.1.1.1","b":2}\n{"ip":"2.2.2.2","c":3}' | jq -s 'group_by(.ip)'
[
  [
    {
      "ip": "1.1.1.1",
      "a": 1
    },
    {
      "ip": "1.1.1.1",
      "b": 2
    }
  ],
  [
    {
      "ip": "2.2.2.2",
      "c": 3
    }
  ]
]
  
echo '{"ip":"1.1.1.1","a":1}\n{"ip":"1.1.1.1","b":2}\n{"ip":"2.2.2.2","c":3}' | jq -s -c 'group_by(.ip)| map({ ip: (.[0].ip), fields: [.[]|del(.ip)] }) | .[]'
{"ip":"1.1.1.1","fields":[{"a":1},{"b":2}]}
{"ip":"2.2.2.2","fields":[{"c":3}]}
  
echo '{"ip":"1.1.1.1","a":1}\n{"ip":"1.1.1.1","b":2}\n{"ip":"2.2.2.2","c":3}' | jq -s -c 'group_by(.ip)| map({ ip: (.[0].ip) } + ([.[]|del(.ip)] | reduce .[] as $item({}; .+$item)) ) | .[]'  
{"ip":"1.1.1.1","a":1,"b":2}
{"ip":"2.2.2.2","c":3}
```

## 如何删除/保留一个字段
```
# 保留一个字段 
echo '{"ip":"1.1.1.1","a":1}' | jq -c '{ip}'
{"ip":"1.1.1.1"}
# 保留多个字段 
echo '{"ip":"1.1.1.1","a":1}' | jq -c '{ip,a}'
{"ip":"1.1.1.1","a":1}
  
# 删除一个字段  
echo '{"ip":"1.1.1.1","a":1}' | jq -c 'del(.a)'
{"ip":"1.1.1.1"}
# 删除多个字段  
echo '{"ip":"1.1.1.1","a":1}' | jq -c 'del(.a,.ip)'
{}
```  
  
## 如何打印key中带有dot点的值？
用引号括起来：
```
echo '{"a.b":1}' | jq '."a.b"'
1
```  
  
## 如何转换为csv？
```
echo -n '{"a":"1","b":"2","c":"3"}\n{"a":"4","b":"5","c":"6"}' | jq --slurp --compact-output --raw-output '(map(keys) | add | unique) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv'
"a","b","c"
"1","2","3"
"4","5","6"
```  
  
## 如何重命名key？
用引号括起来：
```
echo '{"a":1}' | jq -c '{"b":."a"}'
{"b":1}
```  
  
## 替换某个数组类型的值？
```
echo '{"a":1,"b":[["ip","os","updated_at"],["1.1.1.1","","2021-03-24 18:55:22"],["2.2.2.2","","2021-03-24 18:55:22"]]}' | jq --compact-output '. | .+{b:(reduce .b[1:][] as $item([]; .+[$item[0]]) )}'
{"a":1,"b":["1.1.1.1","2.2.2.2"]}
```  
  
## 如何找出不同项
```
echo '{"a1":[1,2,3,4],"a2":[3,4,5]}' | jq -c '.a1more=.a1-.a2, .a2more=.a2-.a1, .a1a2eq=(.a1-(.a1-.a2))'
{"a1":[1,2,3,4],"a2":[3,4,5],"a1more":[1,2]}
{"a1":[1,2,3,4],"a2":[3,4,5],"a2more":[5]}
{"a1":[1,2,3,4],"a2":[3,4,5],"a1a2eq":[3,4]}
```  

## 如何自定义多参数的函数？
好像不能，不过可以变通的用一个数组或者object来实现效果：
```
echo '{"a1":[1,2,3,4],"a2":[3,4,5]}' | jq -c 'def fun(a):a[0],a[1]; fun([.a1,.a2])'
[1,2,3,4]
[3,4,5]
```
  
## 如何根据key来修改value？甚至是直接修改key？
```
echo '{"a1":[1,2,3,4],"a2":[3,4,5]}' | jq -c 'with_entries(.value=1)'
{"a1":1,"a2":1}
  
echo '{"a1":[1,2,3,4],"a2":[3,4,5]}' | jq -c 'with_entries(.key=(if .key=="a1" then "b" else .key end ))'
{"b":[1,2,3,4],"a2":[3,4,5]}
```
 
## 如何根据条件来提取数据？
```
echo '{"a":[["1.1.1.1:80",80,"1.1.1.1"],["a.com:443",443,"2.2.2.2"]]}' | jq '.a | reduce .[] as $item ([]; if ($item[0] | contains($item[2]) | not) then .+=[$item[0]] else . end)'
[
  "a.com:443"
]
```
 
## 如何提取一个url中的host？
```
echo '["1.1.1.1","1.1.1.1:81","http://1.1.1.1:82","https://1.1.1.1:83","[fe80::8407:ad05:f6be:90ad]", "https://[fe80::8407:ad05:f6be:90ad]:8443"]' | jq 'def extracthost(host): host|split("://")|last|(if (.|contains("]")) then .|split("]")[0:-1]|join("")+"]" else split(":")|first end); reduce .[] as $item ([]; .+=[extracthost($item)])'
[
  "1.1.1.1",
  "1.1.1.1",
  "1.1.1.1",
  "1.1.1.1",
  "[fe80::8407:ad05:f6be:90ad]",
  "[fe80::8407:ad05:f6be:90ad]"
]
```

## 如何实时输出到管道
默认情况下jq是有buffer的，如果想要实时，可以用--unbuffered参数：
```
fofa random --fixUrl --size 100 --fields host --sleep 1 | jq -r .host --unbuffered | go run ./main.go
```

## 根据对象的数组中的某个字段进行排序
```
echo '{
  "aggregations": {
    "query_strings": {
      "buckets": [
        {
          "key": "aaa",
          "user_id_count": {
            "value": 1
          }
        },
        {
          "key": "bbb",
          "user_id_count": {
            "value": 2
          }
        }
      ]
    }
  }
}' | jq '.aggregations.query_strings.buckets | sort_by(.user_id_count.value)'
```
  
  
# 常见问题
  
## 如何方便的调试jq语法？
- https://jqplay.org/ 支持多行
- https://jqterm.com/
