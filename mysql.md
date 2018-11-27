# 基础知识
* 创建/删除数据库
```sql
CREATE DATABASE <database>
CREATE DATABASE <database> CHARACTER SET utf8
DROP DATABASE <database>
ALTER DATABASE <database> CHARACTER SET utf8
CREATE DATABASE <database> DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

* 创建帐号：
```sql
grant all privileges on <database>.* to <user>@'%' identified by '<password>';
flush privileges;
```

* 修改列的默认值：
```sql
ALTER TABLE <table> MODIFY COLUMN <column> integer NOT NULL DEFAULT 0;
```

* 查询select
```sql
SELECT * FROM table
SELECT * FROM table1, table2, ...
SELECT field1, field2, ... FROM table1, table2, ...
SELECT ... FROM ... WHERE condition
SELECT ... FROM ... WHERE condition GROUPBY field
SELECT ... FROM ... WHERE condition GROUPBY field HAVING condition2
SELECT ... FROM ... WHERE condition ORDER BY field1, field2
SELECT ... FROM ... WHERE condition ORDER BY field1, field2 DESC
SELECT ... FROM ... WHERE condition LIMIT 10
SELECT DISTINCT field1 FROM ...
SELECT DISTINCT field1, field2 FROM ...
```

* 查询select-join
```sql
SELECT ... FROM t1 JOIN t2 ON t1.id1 = t2.id2 WHERE condition
SELECT ... FROM t1 LEFT JOIN t2 ON t1.id1 = t2.id2 WHERE condition
SELECT ... FROM t1 JOIN (t2 JOIN t3 ON ...) ON ...
```

* 查询条件
```sql
field1 = value1
field1 <> value1
field1 LIKE 'value _ %'
field1 IS NULL
field1 IS NOT NULL
field1 IS IN (value1, value2)
field1 IS NOT IN (value1, value2)
condition1 AND condition2
condition1 OR condition2
```

* 插入
```sql
INSERT INTO table1 (field1, field2, ...) VALUES (value1, value2, ...)
```

* 删除
```sql
DELETE FROM table1 / TRUNCATE table1
DELETE FROM table1 WHERE condition
DELETE FROM table1, table2 FROM table1, table2 WHERE table1.id1 =
table2.id2 AND condition
```

* 更新
```sql
DELETE FROM table1 / TRUNCATE table1
DELETE FROM table1 WHERE condition
DELETE FROM table1, table2 FROM table1, table2 WHERE table1.id1 =
table2.id2 AND condition
```


# 任务场景


# 常见问题