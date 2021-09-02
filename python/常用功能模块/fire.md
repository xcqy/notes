# fire 介绍

`fire`是 `python`中用于生成命令行界面( Command Line Interfaces,CLIs)的工具,不需要做任何额外的工作,只需要从主模 块中调用`fire.Fire()`,它会自动将你的代码转化为CLI,`Fire()`的参数可以是任何的 `python`对象

# 安装
```
pip install fire
```

# 用法

- 单个函数

    新建文件test_fire.py

    ```
    import fire

    def add(a, b):
        return a + b

    if __name__ == "__main__":
        fire.Fire(add)
    ```
    命令行执行：
    ```
    python test_fire.py 1 2     # 文件后面接传入函数的参数
    # 或者 python test_fire.py --a 1 --b 2
    ```
    输出：
    ```
    3
    ```

- 多个函数

    ```
    import fire

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    if __name__ == "__main__":
        fire.Fire()     # 注意这里没接参数
    ```
    命令行执行：
    ```
    # 文件名后接方法名再接参数
    python fire_test.py add 1 1 
    # 输出 2
    python fire_test.py sub 1 1
    # 输出 0
    ```

- 传入类

    ```
    import fire
    class Calculator(object):

        def add(self, a, b):
            return a + b

        def sub(self, a, b):
            return a - b

    if __name__ == "__main__":
        fire.Fire(Calculator)     # 这里传入类Calculator
    ```
    命令行执行：
    ```
    # 文件名后接方法名再接参数
    python fire_test.py add 1 1
    # 输出 2
    python fire_test.py sub 1 1
    # 输出 0
    ```