# 基础知识
* 创建/删除数据库
```sql
CREATE DATABASE dbNameYouWant
CREATE DATABASE dbNameYouWant CHARACTER SET utf8
DROP DATABASE dbNameYouWant
ALTER DATABASE dbNameYouWant CHARACTER SET utf8
```

# 任务场景
* 创建数据库：
```sql
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

# 常见问题