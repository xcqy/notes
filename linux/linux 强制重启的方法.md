# linux 强制重启的方法

### 1、reboot -f 
### 2、reboot -nf
### 3、magic SysRq key 方法
```
[root@localhost ~] # echo 1 > /proc/sys/kernel/sysrq
[root@localhost ~] # echo b > /proc/sysrq-trigger
```

```
sudo sh -c "echo 1 > /proc/sys/kernel/sysrq"
sudo sh -c "echo 1 > /proc/sysrq-trigger"
```



