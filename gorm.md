gorm是golang语言中常用的数据库框架，ORM是指Object-relational mapping也就是对象关系映射。

# 基础知识
直接阅读：https://gorm.io/zh_CN/

# 任务场景

## 如何定义关联关系
有User表和Proxy表，再有一个UserProxy表来表示User和Proxy多对多的绑定关系。
```golang
func TestGetDB(t *testing.T) {
	type User struct {
		gorm.Model
		Name string
	}

	type Proxy struct {
		gorm.Model
		Name string
	}

	type UserProxy struct {
		gorm.Model
		UserID int  `gorm:"primaryKey"`
		User   User `gorm:"foreignKey:UserID"`

		ProxyID int   `gorm:"primaryKey"`
		Proxy   Proxy `gorm:"foreignKey:ProxyID"`
	}

	// 确保文件生成，并且有表结构
	var err error
	dbfile := filepath.Join(os.TempDir(), time.Now().Format("20060102150405.sqlite"))
	defer os.Remove(dbfile)
	db, err := gorm.Open(sqlite.Open(dbfile), &gorm.Config{Logger: logger.Default.LogMode(logger.Info)})
	assert.Nil(t, err)
	assert.NotNil(t, db)
	err = db.AutoMigrate(&User{}, &Proxy{}, &UserProxy{})
	assert.Nil(t, err)

	err = db.Save(&UserProxy{
		User: User{
			Name: "a",
		},
		Proxy: Proxy{
			Name: "b",
		},
	}).Error
	assert.Nil(t, err)
	var ab1 UserProxy
	err = db.Preload("User").Preload("Proxy").First(&ab1).Error
	assert.Nil(t, err)
	assert.Equal(t, ab1.User.Name, "a")
	assert.Equal(t, ab1.Proxy.Name, "b")
}
```

## 如何定义复合索引（两个关键字的组合是唯一）
使用uniqueIndex关键字，两个字段的索引名称保持一致。拿上面的案例举例：
```golang
// UserProxy 用户对应代理表
type UserProxy struct {
	gorm.Model
	UserID int  `gorm:"primaryKey,uniqueIndex:idx_user_proxy"`
	User   User `gorm:"foreignKey:UserID"`

	ProxyID int   `gorm:"primaryKey,uniqueIndex:idx_user_proxy"`
	Proxy   Proxy `gorm:"foreignKey:ProxyID"`
}
```
对应的sql为：
```sql
CREATE UNIQUE INDEX `idx_user_proxy` ON `user_proxies`(`user_id`,`proxy_id`)
```

## 设置了uniq时，如何冲突时不报错
```sql
// 在冲突时，什么都不做
db.Clauses(clause.OnConflict{DoNothing: true}).Create(&user)
```

# 常见问题
