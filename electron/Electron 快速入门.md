# Electron 快速入门

## 依赖
在开发之前，需要安装[Node.js](https://nodejs.org/en/download/), 建议最新的LTS版(长期支持版)。
检查版本
```
node -v
npm -v
```
**注意** 因为 Electron 将 Node.js 嵌入到其二进制文件中，你应用运行时的 Node.js 版本与你系统中运行的 Node.js 版本无关。

## 使用脚手架创建应用程序
Electron 应用程序遵循与其他 Node.js 项目相同的结构。 首先创建一个文件夹并初始化 npm 包。
```
mkdir my-electron-app 
cd my-electron-app 
npm init
```
`npm init`命令会在项目中生成一个`package.json`,内容如下：
```
{
  "name": "my-electron-app",
  "version": "1.0.0",
  "description": "Hello World!",
  "main": "main.js",
  "author": "xxx",
  "license": "MIT"
}

# 注意：入口文件必须是main.js
```


然后，将`electron`包安装到应用的开发依赖中，[安装指南](https://www.electronjs.org/docs/tutorial/installation)
```
npm install --save-dev electron

# 安装时遇到的问题大多数是网络问题
# 多试几次就好了，或者科学上网
```

最后，您希望能够执行`Electron` 如下所示，在您的 `package.json`配置文件中的`scripts`字段下增加一条`start`命令：
```
{
  "scripts": {
    "start": "electron ."
  }
}
```

运行程序

```
npm start
```

