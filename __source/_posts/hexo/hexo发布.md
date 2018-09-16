title: "hexo搭建记录"
date: 2016-08-01 20:33:53
tags: hexo
---

#### HEXO

Hexo是一个开源的静态博客生成器，特别的干净，阅读体验非常好。

过去用过一段时间写一些记录，这次拾起来竟然忘记相关的操作，于是把这次搭建博客的过程记录下来。

这是本人搭建的博客：www.xiangry.com

#### 配置环境


1. 安装Git:
 	打算使用githua托管的随笔文件，所以给服务器安装`Git`。
 	
2. 安装hexo:
	hexo是使用`node.js`开发的，所以需要安装`node`。`node`自带包管理器`nmp`(node package manager),可以方便的对node包进行安装、卸载、更新、查看、搜索、发布等。

	```
	sudo yum install nodejs
	```


	安装`hexo`用到了上面的`npm`工具：
	
	```
	npm install -g hexo  		# -g是安装到全局
	```
	
3. 安装Nginx:
	Nginx是一款Web服务器/反向代理服务器及电子邮件代理服务器，在这里选择使用ngixn做为博客的服务器。
	
	```
	yum install nginx
	```
	
4. 安装locate:
	locate是一个搜索工具，可以方便的搜做本地问文件。
	
	```
	yum install mlocate
	updatedb 					# 生成数据库，可以忽略指定目录，详情RTFM
	locate default.conf 		# 查找一个名字叫default.conf文件位置
	```
	
5. 安装forever:
	`forever`官方说明：*一个用来持续（或者说永远）运行一个给定脚本的简单的命令行工具*。可以看做是一个nodejs的守护进程，能够启动、停止或重启node app 应用。在此我们可以使们关掉命令行工具后仍然启动hexo服务。
	
	```
	npm install -g forever
	# forever start app.js   # 简单的启动一个应用。 具体STFW
	```
	
	
如此这些步骤，基本环境就算是完成了。

#### Hexo 生成博客

hexo常用使用的命令:

	```
	hexo init 					# 初始化一个hexo工作目录
	hexo new 'blog name'		# 生成一个新的博客文件：markdown文件
	hexo g 						# 根据配置和markdown文件生成静态网页文件
	hexo s						# 在本地起一个服务器127.0.0.0:4000可以预览，
	hexo s -p 8080				# 指定端口
	```

#### Hexo 发布

这次使用的方式是根据基础的想法：使用`hexo s`在本地起服务，然后使用nginx监听80端口定向到4000端口

1. nginx配置：
	nginx相关的应用还不是很了解，参考了一些网上的文章配置修改nginx的default.conf文件，配置如下：
	
	```
	server {
    	listen       80 default_server;  		                                    # 监听80端口
    	server_name  xiangry.com, www.xiangry.com;                                 # 监听域名
    	
    	location / {
        	proxy_pass              http://127.0.0.1:4000/;                        # 反向代理
        	proxy_redirect          off;                                           # 禁止所有的proxy_redirect
        	proxy_set_header        X-Real-Ip       $remote_addr;                  # 代理服务器ip头
       		proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
    	}
    }

	
	```

2. forever配置：
	在hexo工作目录下建立app.js文件，内容：
	
	```
	var spawn=require('child_process').spawn;
	free=spawn('hexo',['server','-p 4000']);

	free.stdout.on('data',function(data){
        console.log('standard output:\n' + data);
	});

	free.stderr.on('data',function(data){
        console.log('standard error output:\n' + data);
	});

	free.on('exit',function(code,signal){
        console.log('child process exit, exit:' + code);
	});

	```
	
3. 启动：

	```
	forever start -a -l forever.log -o out.log -e err.log app.js
	```
	
#### 总结

	本人对nginx和nodejs不熟悉，相关用法需要在日后继续学习。





