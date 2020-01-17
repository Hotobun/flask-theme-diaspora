---
title: MySql
tags:
  - mysql
categories:
  - 基础
date: 2019-12-04 17:51:56
cover: /img/mysql.jpg
---

## 创建数据库
指定urf-8编码  
- `CREATE DATABASE databasename DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci; `

## 删除数据库 
- `drop databases <databasename>;`
- `>>> drop databases pwd;`
 
## 创建数据表
通用语法:
- `CREATE TABLE table_name (column_name column_type);`
```
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,   // int无符号自增
   `runoob_title` VARCHAR(100) NOT NULL,      
   `runoob_author` VARCHAR(40) NOT NULL,      
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

## 删除数据表
- `DROP TABLE tableanme ;`   

## 插入数据
```
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );
```

## 查询数据
```
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]
```
1.查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用WHERE语句来设定查询条件。  
2.SELECT 命令可以读取一条或者多条记录。  
3.你可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有字段数据  
4.你可以使用 WHERE 语句来包含任何条件。  
5.你可以使用 LIMIT 属性来设定返回的记录数。  
6.你可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。  

## 查询去重
```
select distinct 字段名 from table;
```

## concat函数
* 功能：拼接字符 `"1"+"23" = "123"`
```
select concat (字段1,字段2 ) from table;
```

## ifnull函数：
* 功能：判断某字段或表达式是否为null，如果为null 返回指定的值，否则返回原本的值
```
# 如果`hello`列为空则返回0
select ifnull(hello, 0) from employees;
```

## isnull函数
* 功能：判断某字段或表达式是否为null，如果是，则返回1，否则返回0
```
select id, isnull(root) from table;
```

## 条件查询
* where字句
用于筛选符合条件的数据 将不满足条件的行过滤
```
select * from table 
    where id = 1 or data = 'hello' ;
```


|      运算符      |                                               说明                                               |
| :--------------: | :----------------------------------------------------------------------------------------------: |
| BETWEEN...AND... |                                  现在某一区间的值(包含头与结尾)                                  |
|     IN(set)      |                                现在在in列表中的值 例：in(100,200)                                |
|    LIKE通配符    | 模糊查询，Like语句中有两个通配符：% 用来匹配多个字符；例name like "%a"; "_"用来表示任意一个字符; |
|     IS NULL      |                              判断是否为空， is not null; 判断不为空                              |
|     AND(&&)      |                                         多个条件同时成立                                         |
|     OR(\|\|)     |                                       多个条件任意一个成立                                       |
|      not(!)      |                                不成立，例：where not(salary>100);                                |


## 排序查询
ORDER BY 
* 使用ORDER BY 子句排序
  * ASC(ascend) 默认 升序
  * DESC(descend) 降序
```
# 查询名字含有a的行 按mid进行降序排序 显示前20行
select * from table
    where name like "%a%" 
    order by mid desc 
    limit 20;
```

## 分组查询 
```
select 分组函数，分组后的字段
from 表
where 筛选条件
group by 分组的字段
having 分组后的筛选
order by 排序列表
```

## 简易备份与恢复
本机可忽略主机名与端口  
备份：  
`mysqldump -h主机名 -P端口 -u用户名 -p密码 --database 数据库名 > 文件名.sql`  
恢复：  
`mysql -u用户名 -p密码 数据库名 < 文件名.sql ;`  