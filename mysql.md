# 基础知识

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
ALTER TABLE vulcallbacks MODIFY COLUMN state integer NOT NULL DEFAULT 0;
```

# 常见问题