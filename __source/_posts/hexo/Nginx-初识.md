title: Nginx 初识
date: 2016-08-03 23:07:30
tags: hexo
---

#### 结识
    
搭建本博客使用的就是本款强大的可扩展的`Nginx`web/proxy服务器。在了记录一下nginx相关的信息方便后面查找使用，加深一下自己对nginx的理解，毕竟作为自己不经常使用。

Nginx的安装步骤就不在这里提了，毕竟网上优秀的文章很多，在这里主要记一下相关的使用方法。
参考[Nginx的介绍和使用][1]

#### 使用


nginx启动、重启、关闭

```

	# 启动
	nginx    

	# 关闭
	ps -ef | grep nginx   	# 查询nginx主进程号
	kill -QUIT 进程号      	# 从容停止
	kill -TERM 进程号 		# 快速停止
	kill -9 进程号  			# 强制停止
	# 如果ngixn.conf配置了pid文件路径，如果没有，则在logs目录下
	kill -信号类型 '/usr/local/nginx/logs/nginx.pid'

	# 重启 更改配置后需要重启
	kill -HUD 主进程号或进程号文件路径  # 方法1
	nginx -s reload   

```

#### Nginx配置

nginx的配置文件是一个纯文本文件，它一般位于Nginx安装目录下，整个配置文件是以block的形式组织的。每个block一般以一个大括号`{}`来表示。block可以分为几个层次，整个配置文件中Main指令位于最高层，在Main层下面可以有Events、HTTP等层级，而在HTTP层中又包含有Server层，即server block。server block 中又可以分为location层，并且一个server block中可以包含有多个location block。

![配置结构图][nginx_config]

ngxin.conf的配置文件详解：


```
	#开启进程数 <= CPU数
	worker_processes 1;
	
	#错误日志保存位置
	#error_log	logs/error.log;
	#error_log	logs/error.log notice;
	#error_log	logs/error.log info;
	
	#进程号保存文件
	#pid logs/nginx.pid;
	
	#等待事件
	events {
	# 每个进程最大连接数（最大连接数=连接数×进程数）
	worker_connections 1024;
	}
	
	
	
	http {
	#文件扩展名与文件类型映射表
	include mime.types;
	
	#默认文件类型
	default_type application/octet-stream;
	
	#日志文件输出格式 这个位置于与全局设置
	#log_format main '$remote_addr - $remote_user [$time_local] "$request"';
	# '$status $body_types_sent "$http_referer"';
	# '$"http_user_agent" "$http_x_forwarded_for"';
	
	#请求日志保存位置
	#access_log logs/access.log.main;
	
	#打开发送文件
	sendfile on;
	#tcp_nopush on;
	
	#连接超时事件
	#keepalive_timeout 0;
	keepalive_timeout 65;
	
	#打开gzip压缩
	#gzip on;
	
	#设定请求缓冲
	client_header_buffer_size 1k;
	large_client_header_buffers4 4k;
	
	#设定负载均衡的服务器列表
	upstream myproject{
	#weight 参数表示权值，全值越高被分配到的几率越大
	#max_fails 当有#max_fails个请求失败，就表示后端的服务器不可用，默认为1，将其设置为0可以关闭检查
	#这里指定多个源服务器，ip：端口，如果是80端口的话可写可不写
	server 192.168.1.78:8080 weight=5 max_fails=2 fail_timeout=600s;
	#server 192.168.1.222:8080 weight=3 max_fails=2 fail_timeout=600s;
	}
	
	#第一个虚拟主机
	server{
	#监听端口
	listen 80;
	
	#主机名
	server_name localhost;
	
	#设置字符集
	#charset koi8-r;
	
	#本虚拟server的访问日志，相当于局部变量
	#access_log logs/host.access.log main;
	
	#对本server"/"启用负载均衡
	location / {
	#root /root;  #定义服务器的默认网站的根目录位置
	#index index.php index.html index.htm; #定义首页索引文件的名称
	proxy_pass http://myproject;  #请求转向myproject定义的服务器列表
	
	#一下是一些反向代理的配置 可删除
	#proxy_redirect off;
	#proxy_set_header Host $host;
	#proxy_set_header X-real-Ip $remote_addr;
	#proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	#client_max_body_size 10m; #允许客户端请求的最大字节数
	...
	}
	
	location / upload {
	alias e:/upload;
	}
	
	#设定查看Nginx状态的地址
	location / NginxStatus {
	stub_staus on;
	access_log off;
	#allow 192.168.0.3
	#deny all;
	#auth_basic "NginxStatus";
	#auth_basic_user_file conf/htpasswd;
	}
	
	#error_page 404 /404.html
	
	#redirect server error pages to the static page /50x.html
	#定义错误提示页面
	error_page 500 502 503 504 /50x.html
	loation = /50x.html {
	root html;
	}
	
	...
	
	}

```



[1]:http://blog.csdn.net/shimiso/article/details/8690897   Nginx的介绍和使用

[nginx_config]:http://ochy83snh.bkt.clouddn.com/blog/img/nginx_config.png "nginx_config"
