```
#查看是否已存在swap file
sudo swapon -s

#如果已存在需要先禁用
sudo swapoff /swapfile

#修改swap 空间的大小为1G
sudo dd if=/dev/zero of=/swapfile bs=1M count=1024

#设置文件为“swap file”类型
sudo mkswap /swapfile

#启用swapfile
sudo swapon /swapfile
```