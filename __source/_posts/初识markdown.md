title: 初识markdown
date: 2014-10-05 12:10:30
categories: 学习记录
tags: markdown
---

接触
---

_程序猿一只，突然意识到要写点东西，为hexo而接触到了markdown这个为广大码农所用的标记语言，
看来自己不是个合格的程序员那。在这里用这片文字作为自己的第一步，hello world。_


---

##一些语法
<!-- more -->
---
###标题

* Atx方式 加前缀#的个数表明标题层级

		多级标题，1-6级
		#一级标题
		##二级标题

* Setext方式 加前缀#的个数表明标题层级

		大标题
		===
		小标题
		---

---
###列表

- 列表 
	+ 无序列表
		* 无序列表 “- ”

				符号之后的空格不能少，-+*效果一样，但不能混合使用，因混合是嵌套列表，内容可超长
				- 无序列表
				- 无序列表
				- 很长。我也很长！那比一比啊？比就比！我有这么长，你有我长吗？我有这么这么长！好吧，你赢了！

		* 无序列表 “+ ”

				符号之后的空格不能少，-+*效果一样，但不能混合使用，因混合是嵌套列表
				+ 无序列表
				+ 无序列表
		* 无序列表 “* ”

				符号之后的空格不能少，-+*效果一样，但不能混合使用，因混合是嵌套列表
				* 无序列表
				* 无序列表
	+ 有序列表 

			数字不能省略但可无序，点号之后的空格不能少
			1. 有序列表
			2. 有序列表

- 嵌套列表

			-+*可循环使用，但符号之后的空格不能少，符号之前的空格也不能少

			- 嵌套列表
			 + 嵌套列表
			 + 嵌套列表
			  - 嵌套列表
			   * 嵌套列表
			- 嵌套列表

##文字超链接
---
[不如 markdown简明语法](http://ibruce.info/2013/11/26/markdown/ "值得一看，来来来来")

		Tooltips可省略
		[不如 markdown简明语法](http://ibruce.info/2013/11/26/markdown/ "值得一看，来来来来")

##图片超链接
---
![GitHub Mark](https://github.com/xingsheng/quick-cocos2d-x/blob/develop/samples/benchmark/res/UIFont.png "GitHub Mark")

		多个感叹号，Tooltips可省略，要设置大小只能借助HTML标记
		![GitHub Mark](https://github.com/xingsheng/quick-cocos2d-x/blob/develop/samples/benchmark/res/UIFont.png "GitHub Mark")

##图片超链接
---
[不如][1]
![GitHub Octocat][2]

[1]:http://bruce-sha.github.io
[2]:http://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png

		索引，1 2可以是任意字符
		[不如][1]
		![GitHub Octocat][2]

		[1]:http://bruce-sha.github.io
		[2]:http://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png

##自动链接
---
<http://ibruce.info>
<bu.ru@qq.com>

		尖括号
		<http://ibruce.info>
		<bu.ru@qq.com>

##代码：行内代码
---
```scala
  val s = "hello Markdown"
  println( s )
```

			在第一行后指定编程语言，也可以不指定
			```scala
			  val s = "hello Markdown"
			  println( s )
			```

#代码：段落代码
---
	val s = "hello Markdown"
	println( s )
 

		每行文字前加4个空格或者1个Tab
		val s = "hello Markdown"
		println( s )

#代码：hexo
---
	{% codeblock [title] [lang:lua] [url] [link text] %}
		code snippet
	{% endcodeblock %}

	可指定编程语言，『』代表左右大括号
	\{% codeblock [title] [lang:lua] [url] [link text] %\}
		code snippet
	\{% endcodeblock %\}

#注释
---
	用html的注释，好像只有这样？
	<!-- 注释 -->

---
[不如 markdown简明语法](http://ibruce.info/2013/11/26/markdown/ "不如的博客") 
[献给写作者的 Markdown 新手指南](http://www.jianshu.com/p/q81RER "Markdown 新手指南") 

