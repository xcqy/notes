# 安装MySQL

去官网下的安装包都安装失败了，这里选择用`homebrew`安装

- 下载
```
brew install mysql
```

- 启动服务
```
brew services start mysql
```

- 配置,设置密码   #都选`y`
```
mysql_secure_installation
```

- 停止服务
```
brew services stop mysql
```

- 开机自启
```
mysql.server start
mysql.server stop
```

- 连接服务器
```
mysql -u root -p
```

# GUI-TablePlus

TablePlus是我们可以用来与SQLite数据库进行交互的出色GUI(图形)软件。

- 下载链接: 
[https://tableplus.com/](https://tableplus.com/)