# flask
[官方文档](https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application)


## flask 安装

```
pip install flask
```


## flask最小demo

- 复制以下代码到`hellp.py`

	```
	from flask import Flask		# 导入模块

	app = Flask(__name__)		# 创建一个实例，参数`__name__`在用python直接执行该文件时__name__ == "__main__", 在被其他文件导入时 __name__ 等于该文件名

	@app.route("/")		# flask装饰器实现的路由
	def index():		# 该函数返回浏览器显示的信息，默认类型为html
		return "<p>Hello, World!</p>"

	if __name__ == "__main__":
		app.run()
	```

- 可以直接用编辑器运行，也可以输入以下命令运行：

	- `flask run`
	- `python -m flask run`
	- 运行前需要配置环境变量

		- bash
			```
			export FLASK_APP=hello
			flask run
			```
		- cmd
			```
			set FLASK_APP=hello
			flask run
			```
		- powershell
			```
			$env:FLASK_APP = "hello"
			flask run
			```

- 然后浏览器输入以下地址就可以看到你做好的网站
	```
	http://127.0.0.1:5000/
	```

- 注意事项

	文件或者目录名不要叫`flask`或`Flask`，避免命名冲突，否则包导不进来

## Debug Mode

`flask run`命令可以做的不仅仅是启动开发服务器。通过启用调试模式，如果代码发生更改，服务器将自动重新加载，如果请求期间发生错误，服务器将在浏览器中显示交互式调试器。

开启调试模式有两种方式：
- 在代码中
	```
	app.run(debug=True)
	```
- 通过修改环境变量(不常用)

	- bash
		```
		export FLASK_ENV=development
		flask run
		```
	- cmd
		```
		set FLASK_ENV=development
		flask run
		```
	- powershell
		```
		$env:FLASK_ENV = "development"
		flask run
		```