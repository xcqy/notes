# linux基本命令

### ls
- ls -a  	  # 全部文件，包含隐藏文件
- ls -l   	  # 长数据列出，包含文件的属性和权限等等
- ls -al 	  # 等于上面两个相加

### cd
- cd 或 cd ~		# 切换到home目录
- cd ..  		        # 回到上一级
- cd /  		         # 回到根目录

### pwd		#显示当前目录

- pwd -P 	# 显示出确实的路径，而非使用链接（link）路径

    ```
    # 单纯显示出目前的工作目录
    [root@xxx ~]# pwd
    /root

    # 如果是链接,要显示真实地址,可以使用 -P参数
    [root@xxx /]# cd bin
    [root@xxx bin]# pwd -P
    /usr/bin
    ```

### mkdir	# 创建新目录
mkdir [-mp] 目录名称
- -m : 配置文件权限
	
	```
  [root@xxx home]# mkdir -m 711 test2
	[root@xxx home]# ls -l
	drwxr-xr-x 2 root root 4096 Mar 12 21:55 test
	drwxr-xr-x 3 root root 4096 Mar 12 21:56 test1
	drwx--x--x 2 root root 4096 Mar 12 21:58 test2
	```
	
- -p : 创建递归目录

  ```
  # 创建多层级目录
  mkdir test1/test2/test3/test4
  mkdir: cannot create directory ‘test1/test2/test3/test4’:
  No such file or directory
  # <== 没办法直接创建此目录啊!
  # 加了这个 -p 的选项,可以自行帮你创建多层目录!
  mkdir -p test1/test2/test3/test4
  ```

### rmdir 	# 删除空目录

### cp 		# 复制文件或目录
- 语法：
	```
	cp [-adfilprsu] 来源档(source) 目标档(destination)
	cp [options] source1 source2 source3 .... directory
	```

- 选项与参数：
    - -a : 相当於 -pdr 的意思,至於 pdr 请参考下列说明;(常用)
    - -p : 连同文件的属性一起复制过去,而非使用默认属性(备份常用);
    - -d : 若来源档为连结档的属性(link file),则复制连结档属性而非文件本身;
    - -r : 递归持续复制,用於目录的复制行为;(常用)
    - -f : 为强制(force)的意思,若目标文件已经存在且无法开启,则移除后再尝试一次;
    - -i : 若目标档(destination)已经存在时,在覆盖时会先询问动作的进行(常用)
    - -l : 进行硬式连结(hard link)的连结档创建,而非复制文件本身。
    - -s : 复制成为符号连结档 (symbolic link),亦即『捷径』文件;
    - -u : 若 destination 比 source 旧才升级 destination !

### rm 	 	# 移除文件或目录
- 语法
	```
	rm [-fir] 文件或目录
	```
- 选项与参数
	- -f : force强制删除，忽略不存在的文件，不会出现警告信息 
	- -i : 互动模式，在删除前会询问使用者是否确认删除
	- -r : 递归删除，删除整个文件夹的内容

### mv		# 移动文件与目录，或修改名称
- 语法：
	```
	mv [-fiu] source destination
	mv [options] source1 source2 source3 .... directory
	```
- 选项与参数：
	- -f : force强制，如果目标文件已存在，不会询问直接覆盖
	- -i : 若目标文件存在，会询问是否覆盖
	- -u : 若目标文件已存在，且source比较新，才会update

### find		#查找文件
- 语法：
	```
	find path -option [-print] [-exec -ok |xargs |grep] [command {} \;]
	```
- 选项与参数：

	- path : 要查找的目录路径
	- print : 表示将结果输出到标准输出
	- exec ：对匹配的文件执行该参数所给出的shell命令。形式为command {} \;，注意{}与\;之间有空格 
	- ok ：与exec作用相同。区别在于在执行命令之前会给出提示，确认是否执行
	- |xargs ：与exec作用相同，起惩戒