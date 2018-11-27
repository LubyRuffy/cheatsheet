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
ALTER TABLE <table> MODIFY COLUMN <column> integer NOT NULL DEFAULT 0;
```



# 任务场景


# 常见问题