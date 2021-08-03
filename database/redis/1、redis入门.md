# redis 入门

## redis是什么
redis是一个开源的、使用C语言编写的、支持网络交互的、可基于内存也可持久化的Key-Value数据库。

redis的官网地址，非常好记，是redis.io。（特意查了一下，域名后缀io属于国家域名，是british Indian Ocean territory，即英属印度洋领地）

目前，Vmware在资助着redis项目的开发和维护。


## redis的作者
![11](src/author.png)

这位便是redis的作者，他叫Salvatore Sanfilippo，来自意大利的西西里岛，现在居住在卡塔尼亚。目前供职于Pivotal公司。

他使用的网名是antirez，如果你有兴趣，可以去他的博客逛逛，地址是`antirez.com`，当然也可以去follow他的github，地址是[http://github.com/antirez](http://github.com/antirez).


## 谁在使用redis
Blizzard、digg、stackoverflow、github、flickr …


## 安装redis
从[redis.io](redis.io)下载最新版redis-X.Y.Z.tar.gz后解压，然后进入redis-X.Y.Z文件夹后直接make即可，安装非常简单。

make成功后会在src文件夹下产生一些二进制可执行文件，包括redis-server、redis-cli等等：
```
$ find . -type f -executable
./redis-benchmark //用于进行redis性能测试的工具
./redis-check-dump //用于修复出问题的dump.rdb文件
./redis-cli //redis的客户端
./redis-server //redis的服务端
./redis-check-aof //用于修复出问题的AOF文件
./redis-sentinel //用于集群管理
```

## 启动redis
启动redis非常简单，直接./redis-server就可以启动服务端了，还可以用下面的方法指定要加载的配置文件：
```
cd src/
./redis-server ../redis.conf
```
默认情况下，redis-server会以非daemon的方式来运行，且默认服务端口为6379。

有关作者为什么选择6379作为默认端口，还有一段有趣的典故，英语好的同学可以看看作者这篇博文中的解释。


## 使用redis客户端
我们直接看一个例子：
```
// 这样来启动redis客户端
$ ./redis-cli

// 用set指令来设置key、value
127.0.0.1:6379> set name "roc" 
OK

// 来获取name的值
127.0.0.1:6379> get name 
"roc"

// 通过客户端来关闭redis服务端
127.0.0.1:6379> shutdown 
not connected>
```

## redis数据结构 – 简介
```
redis是一种高级的key:value存储系统，其中value支持五种数据类型：

1.字符串（strings）
2.字符串列表（lists）
3.字符串集合（sets）
4.有序字符串集合（sorted sets）
5.哈希（hashes）

而关于key，有几个点要提醒大家：

1.key不要太长，尽量不要超过1024字节，这不仅消耗内存，而且会降低查找的效率；
2.key也不要太短，太短的话，key的可读性会降低；
3.在一个项目中，key最好使用统一的命名模式，例如user:10000:passwd。
```

### redis数据结构 – strings
有人说，如果只使用redis中的字符串类型，且不使用redis的持久化功能，那么，redis就和memcache非常非常的像了。这说明strings类型是一个很基础的数据类型，也是任何存储系统都必备的数据类型。

我们来看一个最简单的例子：
```
set mystr "hello world!" //设置字符串类型
get mystr //读取字符串类型
```
字符串类型的用法就是这么简单，因为是二进制安全的，所以你完全可以把一个图片文件的内容作为字符串来存储。

另外，我们还可以通过字符串类型进行数值操作：
```
127.0.0.1:6379> set mynum "2"
OK
127.0.0.1:6379> get mynum
"2"
127.0.0.1:6379> incr mynum
(integer) 3
127.0.0.1:6379> get mynum
"3"
```
看，在遇到数值操作时，redis会将字符串类型转换成数值。

由于INCR等指令本身就具有原子操作的特性，所以我们完全可以利用redis的INCR、INCRBY、DECR、DECRBY等指令来实现原子计数的效果，假如，在某种场景下有3个客户端同时读取了mynum的值（值为2），然后对其同时进行了加1的操作，那么，最后mynum的值一定是5。不少网站都利用redis的这个特性来实现业务上的统计计数需求。


### redis数据结构 – lists
redis的另一个重要的数据结构叫做lists，翻译成中文叫做“列表”。

首先要明确一点，redis中的lists在底层实现上并不是数组，而是链表，也就是说对于一个具有上百万个元素的lists来说，在头部和尾部插入一个新元素，其时间复杂度是常数级别的，比如用LPUSH在10个元素的lists头部插入新元素，和在上千万元素的lists头部插入新元素的速度应该是相同的。

虽然lists有这样的优势，但同样有其弊端，那就是，链表型lists的元素定位会比较慢，而数组型lists的元素定位就会快得多。

lists的常用操作包括LPUSH、RPUSH、LRANGE等。我们可以用LPUSH在lists的左侧插入一个新元素，用RPUSH在lists的右侧插入一个新元素，用LRANGE命令从lists中指定一个范围来提取元素。我们来看几个例子：
```
//新建一个list叫做mylist，并在列表头部插入元素"1"
127.0.0.1:6379> lpush mylist "1" 
//返回当前mylist中的元素个数
(integer) 1 
//在mylist右侧插入元素"2"
127.0.0.1:6379> rpush mylist "2" 
(integer) 2
//在mylist左侧插入元素"0"
127.0.0.1:6379> lpush mylist "0" 
(integer) 3
//列出mylist中从编号0到编号1的元素
127.0.0.1:6379> lrange mylist 0 1 
1) "0"
2) "1"
//列出mylist中从编号0到倒数第一个元素
127.0.0.1:6379> lrange mylist 0 -1 
1) "0"
2) "1"
3) "2"
```
lists的应用相当广泛，随便举几个例子：

- 我们可以利用lists来实现一个消息队列，而且可以确保先后顺序，不必像MySQL那样还需要通过ORDER BY来进行排序。
- 利用LRANGE还可以很方便的实现分页的功能。
- 在博客系统中，每片博文的评论也可以存入一个单独的list中。


### redis数据结构 – 集合

redis的集合，是一种无序的集合，集合中的元素没有先后顺序。

集合相关的操作也很丰富，如添加新元素、删除已有元素、取交集、取并集、取差集等。我们来看例子：
```
//向集合myset中加入一个新元素"one"
127.0.0.1:6379> sadd myset "one" 
(integer) 1
127.0.0.1:6379> sadd myset "two"
(integer) 1
//列出集合myset中的所有元素
127.0.0.1:6379> smembers myset 
1) "one"
2) "two"
//判断元素1是否在集合myset中，返回1表示存在
127.0.0.1:6379> sismember myset "one" 
(integer) 1
//判断元素3是否在集合myset中，返回0表示不存在
127.0.0.1:6379> sismember myset "three" 
(integer) 0
//新建一个新的集合yourset
127.0.0.1:6379> sadd yourset "1" 
(integer) 1
127.0.0.1:6379> sadd yourset "2"
(integer) 1
127.0.0.1:6379> smembers yourset
1) "1"
2) "2"
//对两个集合求并集
127.0.0.1:6379> sunion myset yourset 
1) "1"
2) "one"
3) "2"
4) "two"
```
对于集合的使用，也有一些常见的方式，比如，QQ有一个社交功能叫做“好友标签”，大家可以给你的好友贴标签，比如“大美女”、“土豪”、“欧巴”等等，这时就可以使用redis的集合来实现，把每一个用户的标签都存储在一个集合之中。


### redis数据结构-有序集合

redis不但提供了无需集合（sets），还很体贴的提供了有序集合（sorted sets）。有序集合中的每个元素都关联一个序号（score），这便是排序的依据。

很多时候，我们都将redis中的有序集合叫做zsets，这是因为在redis中，有序集合相关的操作指令都是以z开头的，比如zrange、zadd、zrevrange、zrangebyscore等等

老规矩，我们来看几个生动的例子：
```
//新增一个有序集合myzset，并加入一个元素baidu.com，给它赋予的序号是1：
127.0.0.1:6379> zadd myzset 1 baidu.com 
(integer) 1
//向myzset中新增一个元素360.com，赋予它的序号是3
127.0.0.1:6379> zadd myzset 3 360.com 
(integer) 1
//向myzset中新增一个元素google.com，赋予它的序号是2
127.0.0.1:6379> zadd myzset 2 google.com 
(integer) 1
//列出myzset的所有元素，同时列出其序号，可以看出myzset已经是有序的了。
127.0.0.1:6379> zrange myzset 0 -1 with scores 
1) "baidu.com"
2) "1"
3) "google.com"
4) "2"
5) "360.com"
6) "3"
//只列出myzset的元素
127.0.0.1:6379> zrange myzset 0 -1 
1) "baidu.com"
2) "google.com"
3) "360.com"
```

### redis数据结构 – 哈希

最后要给大家介绍的是hashes，即哈希。哈希是从redis-2.0.0版本之后才有的数据结构。

hashes存的是字符串和字符串值之间的映射，比如一个用户要存储其全名、姓氏、年龄等等，就很适合使用哈希。

我们来看一个例子：
```
//建立哈希，并赋值
127.0.0.1:6379> HMSET user:001 username antirez password P1pp0 age 34 
OK
//列出哈希的内容
127.0.0.1:6379> HGETALL user:001 
1) "username"
2) "antirez"
3) "password"
4) "P1pp0"
5) "age"
6) "34"
//更改哈希中的某一个值
127.0.0.1:6379> HSET user:001 password 12345 
(integer) 0
//再次列出哈希的内容
127.0.0.1:6379> HGETALL user:001 
1) "username"
2) "antirez"
3) "password"
4) "12345"
5) "age"
6) "34"
```
有关hashes的操作，同样很丰富，需要时，大家可以从[这里](https://redis.io/commands#hash)查询。

