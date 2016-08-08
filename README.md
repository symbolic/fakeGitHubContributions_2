# 让你的 Github 贡献值满满
无意中发现，github的贡献值就是commit的次数，commit的时间对应你的 github 主页上的小方格。
于是，可以通过修改电脑的时间，然后多次commit就可以让你的贡献值慢慢的深绿了

官方的[贡献值说明](https://help.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile/)

# 实现方式
使用 `win32api` 模块的 `SetSystemTime` 方法修改系统时间（**vista 及以上系统，需要管理员权限**）
获取一个随机数，写到文件里，然后 add、commit就 OK 了。

## 拓展
如果你觉得不过瘾，可以多建立几个仓库，同时commit。反正系统时间已经修改了。

因此就产生了2个版本：

**主程序**：修改系统时间，反复修改文件，然后add，commit

**附属程序**：不改时间，反复修改文件，然后add，commit
