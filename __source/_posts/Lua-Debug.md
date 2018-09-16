title: Lua Debug
date: 2014-10-16 14:18:54
tags: Lua
---

_当要定位lua某个方法被调用的位置通常可以通过打印堆栈信息来做到，刚接触，找到这篇文章["Lua debug"](http://see.sl088.com/wiki/Lua_debug "Lua Debug")_

<!-- more -->

---
###debug
返回当前的堆栈信息
	```
	debug.traceback()
	```

###sethook
一个非常有意思的机制，注册一个函数，在程序运行中某一事件触发时调用这个函数。监听的事件有"call"、"return"、"line"、"count"。[Hooks](http://book.luaer.cn/_130.htm)

		```
			-- 打印解释器执行的每一个新行的行号：
			debug.traceback()
		```