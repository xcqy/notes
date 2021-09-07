# 关于字典的常用用法

## 字典排序
```
dic = {2:333,4:222,3:111}
print(sorted(dic.keys()))   #按照键排序
print(sorted(dic.values())) #按照值排序
print(sorted(dic.items()))  #按照健值排序

[2, 3, 4]
[111, 222, 333]
[(2, 333), (3, 111), (4, 222)]
```

## 字典遍历

- 遍历`key`值
    ```
    a = {'a': '1', 'b': '2', 'c': '3'}
    for key in a:
        print(key+':'+a[key])

    for key in a.keys():
        print(key+':'+a[key])

    # ---------两种方法等价----------------
    a:1
    b:2
    c:3
    ```

- 遍历`value`值
    ```
    for value in a.values():
        print(value)

    # --------输出字典的值——————————
    1
    2
    3
    ```

- 遍历字典项
    ```
    for kv in a.items():
        print(kv)

    # --------以元祖输出字典的键、值——————————
    ('a', '1')
    ('b', '2')
    ('c', '3')
    ```

- 遍历字典健值
    ```
    for key,value in a.items():
        print(key+':'+value)
    

    for (key,value) in a.items():
        print(key+':'+value)

    # ---------两种方法等价----------------
    a:1
    b:2
    c:3
    ```
