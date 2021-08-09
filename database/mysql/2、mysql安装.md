# 安装MySQL

## 一、下载MySQL社区版
- 下载地址：[https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
- 直接下载dmg文件
- 会跳转到注册页面，不用注册，直接点击下方的 `No thanks, just start my download.`
- 下载后双击dmg安装，会弹出一个.pkg文件再双击
- 一直点击继续就好
- 安装成功后会弹出一个对话框，告诉我们生成了一个root账户的临时密码。请注意保存，否则重设密码会比较麻烦。


## 二、启动MySQL
- 打开系统偏好设置，会发现多了一个MySQL图标，点击它，会进入MySQL的设置界面
- 安装之后，默认MySQL的状态是`stopped`，关闭的，需要点击 `Start MySQL Server` 按钮来启动它，启动之后，状态会变成`running`。下方还有一个复选框按钮，可以设置是否在系统启动的时候自动启动MySQL，默认是勾选的，建议取消，节省开机时间。


## 三、终端连接MySQL
- 打开终端，为Path路径附加MySQL的bin目录
	```
	PATH="$PATH":/usr/local/mysql/bin
	```
- 然后通过以下命令登陆MySQL **（密码就是前面自动生成的临时密码）**
	```
	mysql -u root -p
	```
- 登陆成功，但是运行命令的时候会报错，提示我们需要重设密码。
	```
	mysql> show databases;
	ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.
	mysql>
	```
- 修改密码，新密码为`root`
	```
	set PASSWORD =PASSWORD('root');
	```


## 四、忘记密码
- 点击系统偏好设置->最下边点MySQL，在弹出页面中，关闭服务
- 进入终端输入
	```
	cd /usr/local/mysql/bin/
	```
- 回车后 登录管理员权限
	```
	sudo su
	```
- 回车后输入以下命令来禁止mysql验证功能
	```
	./mysqld_safe --skip-grant-tables &
	```
- 回车后mysql会自动重启（偏好设置中mysql的状态会变成running）
- 输入命令
	```
	./mysql -p
	```
- 回车后，输入命令
	```
	FLUSH PRIVILEGES
	```
- 回车后，输入命令修改密码！
	```
	SET PASSWORD FOR 'root'@'localhost' = PASSWORD('你的新密码');
	```
- 或者使用下面这个更改密码
	```
	update mysql.user set authentication_string=password('root') where user='root' and Host ='localhost';
	```