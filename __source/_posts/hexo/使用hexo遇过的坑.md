title: 使用hexo遇过的坑
date: 2016-08-08 10:42:03
tags:
---

#### 使用Hexo遇过的问题

由于对部分技术的问题不了解，在使用hexo过程中遇过很多问题，在这里记录下来，加深记忆，理解和日后遇到问题有个参考。再深入就是对每个问题的具体原因做深入学习。

#### 具体问题

###### Error: getaddrinfo ENOTFOUND

执行`hexo s`后报错[error] Error: getaddrinfo ENOTFOUND`。

查看`hexo`的config.js文件，可以使用`locate`查找。我的目录是`/usr/local/lib/node_modules/hexo/lib/loaders/config.js`，打开可以看到默认设置：

```
server_ip: 'localhost',   # 会查找hosts文件配置
```	

于是这个问题的原因是由于`/etc/hosts`文件中没有`127.0.0.1  localhost`这句，它可以让nodejs定位本机服务。过去修改过hosts文件把它注释掉了，所以出现了问题。

问题解决方法：还原`hosts`文件关于localhost的设置或者修改`config.js`文件的这句改为：

```
server_ip: '127.0.0.1',   # 会查找hosts文件配置
```
	
详细问题参考[Error: getaddrinfo ENOTFOUND][1]。

######  HexoError: Port 4000 has been used. Try other port instead.

问题原因是端口被占用，一种解决方式是启用另一个空闲的端口个

```
hexo s -p 4001  # 启用4001端口
```

或者释放掉该端口之后再启用。释放端口参考[netstat 相关用法][2]。

###### 生成的页面没有内容

一般是由于使用的主题模板问题引起的，换一个模板。






[1]:https://github.com/Unitech/pm2/issues/324 "Error: getaddrinfo ENOTFOUND"
[2]:./netstat.md    "netstat 相关的用法"