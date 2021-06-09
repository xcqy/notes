```
# 安装gnome桌面
sudo apt install ubuntu-gnome-desktop

# 启动gnome桌面服务，并确保它在启动时运行。
sudo systemctl start gdm
sudo systemctl enable gdm

# ubuntu server可能没有wifi驱动
# 需要手动安装
wget http://downloads.fars-robotics.net/wifi-drivers/install-wifi
sudo mv install-wifi /usr/bin/
sudo install-wifi -h
sudo reboot
```

