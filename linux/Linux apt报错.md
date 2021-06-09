# Linux遇到的问题

### apt报错 ：
- Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution)

  按照提示来执行：

  ```
  sudo apt --fix-broken install
  ```
  又报错:
  
  ```
  rocess: Resource temporarily unavailable
  ```
  
  解决：
  
  ```
  $ sudo fuser /var/cache/debconf/config.dat
  /var/cache/debconf/config.dat: 4503
  
  $ ps aux | grep 4503
  root 4503 0.0 0.8 10816 9088 ? S 08:39 0:00 /usr/bin/perl -w /usr/share/debconf/frontend /usr/sbin/update-grub
  
  $ sudo kill 4503
  
  After killing the process (4503 in this case) and running update-manager again, the upgrade can be completed successfully.
  ```
  
- 
     ```
     Errors were encountered while processing:
     grub-pc
     grub-efi-amd64-signed
     gdm3
     E: Sub-process /usr/bin/dpkg returned an error code (1)
     ```
     ```
     cd /var/lib/dpkg
     sudo mv info info.bak (或用cp)
     sudo mkdir info
     sudo apt-get update
     sudo apt-get -f install  grub-pc gdm3 grub-efi-amd64-signed
     sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info.bak
     sudo rm -rf /var/lib/dpkg/info
     sudo mv /var/lib/dpkg/info.bak /var/lib/dpkg/info
     ```
