# Shadowsocks-flask

本项目基于 Flask 框架，用于管理服务器后台 Shadowsocks 的用户信息，提供用户注册、查询用户账号有效期等功能。



# Installation

创建数据库并导入模型中定义的数据结构

```powershell
python db_create.py
```

数据库已存在，更新模型

```powershell
python db_migrate.py
```

升级数据库的模型版本

```powershell
python db_upgrade.py
```

降级数据库的模型版本

```powershell
python db_downgrade.py
```



# TO DO

- Shadowsocks 账号的自动分配

- 账号有效期截止提醒功能

- 通过微信支付充值

  ​



Changelog
===

- 用户密码加盐哈希处理后存入数据库 password_hash 字段；优化注册、登录界面


- 完成新用户注册、登录、注销功能