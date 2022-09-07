gorm是golang语言中常用的数据库框架，ORM是指Object-relational mapping也就是对象关系映射。

# 基础知识
直接阅读：https://gorm.io/zh_CN/

# 任务场景

## 如何定义关联关系
有A表和B表，再有一个AB表来表示A和B多对多的绑定关系。
```
type A struct {
	gorm.Model
}

type B struct {
	gorm.Model
}

type AB struct {
	gorm.Model
  AID  int `gorm:"primaryKey"`
  BID int `gorm:"primaryKey"`
  A      A `gorm:"foreignKey:AID"`
  B      B `gorm:"foreignKey:AID"`
}
```


# 常见问题
