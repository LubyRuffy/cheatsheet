# 基础知识
mysql作为最基本的关系型数据库，对行业影响深远，也是做开发和安全研究过程中必须学习的知识。

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

* 插入记录
```sql
INSERT INTO table1 (field1, field2, ...) VALUES (value1, value2, ...)
```

* 删除记录
```sql
DELETE FROM table1 / TRUNCATE table1
DELETE FROM table1 WHERE condition
DELETE FROM table1, table2 FROM table1, table2 WHERE table1.id1 =
table2.id2 AND condition
```

* 更新记录
```sql
UPDATE table1 SET field1=new_value1 WHERE condition
UPDATE table1, table2 SET field1=new_value1, field2=new_value2, ... WHERE
table1.id1 = table2.id2 AND condition
```

* 创建表
```sql
CREATE TABLE table (field1 type1, field2 type2, ...)
CREATE TABLE table (field1 type1, field2 type2, ..., INDEX (field))
CREATE TABLE table (field1 type1, field2 type2, ..., PRIMARY KEY (field1))
CREATE TABLE table (field1 type1, field2 type2, ..., PRIMARY KEY (field1,
field2))
CREATE TABLE table1 (fk_field1 type1, field2 type2, ...,
  FOREIGN KEY (fk_field1) REFERENCES table2 (t2_fieldA))
    [ON UPDATE|ON DELETE] [CASCADE|SET NULL]
CREATE TABLE table1 (fk_field1 type1, fk_field2 type2, ...,
 FOREIGN KEY (fk_field1, fk_field2) REFERENCES table2 (t2_fieldA, t2_fieldB))
CREATE TABLE table IF NOT EXISTS (...)
CREATE TEMPORARY TABLE table (...)
```
* 删除表
```sql
DROP TABLE table
DROP TABLE IF EXISTS table
DROP TABLE table1, table2, ...
```

* 修改表
```sql
ALTER TABLE table MODIFY field1 type1
ALTER TABLE table MODIFY field1 type1 NOT NULL ...
ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1
ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1 NOT NULL ...
ALTER TABLE table ALTER field1 SET DEFAULT ...
ALTER TABLE table ALTER field1 DROP DEFAULT
ALTER TABLE table ADD new_name_field1 type1
ALTER TABLE table ADD new_name_field1 type1 FIRST
ALTER TABLE table ADD new_name_field1 type1 AFTER another_field
ALTER TABLE table DROP field1
ALTER TABLE table ADD INDEX (field);
*Change field order*
ALTER TABLE table MODIFY field1 type1 FIRST
ALTER TABLE table MODIFY field1 type1 AFTER another_field
ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1 FIRST
ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1 AFTER
another_field
```
* 主键
```sql
CREATE TABLE table (..., PRIMARY KEY (field1, field2))
CREATE TABLE table (..., FOREIGN KEY (field1, field2) REFERENCES table2
(t2_field1, t2_field2))
```

* 用户权限
```sql
GRANT ALL PRIVILEGES ON base.* TO 'user'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT, DELETE ON base.* TO 'user'@'localhost' IDENTIFIED BY 'password';
REVOKE ALL PRIVILEGES ON base.* FROM 'user'@'host'; -- one permission only
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user'@'host'; -- all permissions
SET PASSWORD = PASSWORD('new_pass')
SET PASSWORD FOR 'user'@'host' = PASSWORD('new_pass')
SET PASSWORD = OLD_PASSWORD('new_pass')
DROP USER 'user'@'host' -- host ‘%’ indicates any host.
```
grant之后记得：flush privileges;

* 数据类型
```
 TINYINT (1o: -217+128) SMALLINT (2o: +-65 000)
 MEDIUMINT (3o: +-16 000 000) INT (4o: +- 2 000 000 000)
 BIGINT (8o: +-9.10^18)

 Precise interval: -(2^(8*N-1)) -> (2^8*N)-1
 /!\ INT(2) = "2 digits displayed" -- NOT "number with 2 digits max"

 FLOAT(M,D) DOUBLE(M,D) FLOAT(D=0->53)
 /!\ 8,3 -> 12345,678 -- NOT 12345678,123!

 TIME (HH:MM) YEAR (AAAA) DATE (AAAA-MM-JJ) DATETIME (AAAA-MM-JJ HH:MM; années 1000->9999)
 TIMESTAMP (like DATETIME, but 1970->2038, compatible with Unix)

 VARCHAR (single-line; explicit size) TEXT (multi-lines; max size=65535) BLOB (binary; max size=65535)
 Variants for TEXT&BLOB: TINY (max=255) MEDIUM (max=~16000) LONG (max=4Go)
 Ex: VARCHAR(32), TINYTEXT, LONGBLOB, MEDIUMTEXT

 ENUM ('value1', 'value2', ...) -- (default NULL, or '' if NOT NULL)
```

# 任务场景


# 常见问题
