<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C++的可移植性和跨平台开发[5]：操作系统 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">C++的可移植性和跨平台开发[5]：操作系统</a></h1>
<div class="post-info"><span class="date-header">2009-02-07</span><a href="../../tags/E7BC96E7A88B.C.md" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> </div>
<hr>
<div class="post">
　　上一个帖子提到了“<a href="../../2009/01/cxx-cross-platform-develop-4-hardware.md">硬件体系</a>”相关的话题，今天来说说和操作系统相关的话题。C++跨平台开发中和OS相关的琐事挺多，所以今天会啰嗦比较长的篇幅，请列位看官见谅 :-)<!--program-think--><br />　　为了不绕口，以下把Linux和各种Unix统称为<a href="http://en.wikipedia.org/wiki/Posix" target="_blank" rel="nofollow">Posix</a>系统。<br /><br />　　★<b>文件系统（FileSystem以下简称FS）</b><br />　　刚开始搞跨平台开发的新手，多半都会碰上和FS相关的问题。所以先来聊一下FS。归纳下来，开发中容易碰上的FS差异主要有如下几个：目录分隔符的差异；大小写敏感的差异；路径中禁用字符的差异。<br />　　为了应对上述差异，你要注意如下几点：<br />　　1、文件和目录命名要规范<br />　　在给文件和目录命名时，尽量只使用字母和数字。不要在同一个目录下放两个名称相似（名称中只有大小写不同，例如foo.cpp与Foo.cpp）的文件。不要使用某些OS的保留字（例如aux、con、nul、prn）作文件名或目录名。<br />　　补充一下，刚才说的命名，包括了源代码文件、二进制文件和运行时创建的其它文件。<br />　　2、<b>#include</b>语句要规范<br />　　当你写<b>#include</b>语句时，要注意使用正斜线“/”（比较通用）而不要使用反斜线“\”（仅在Windows可用）。<b>#include</b>语句中的文件和目录名要和实际名称保持大小写<b>完全</b>一致。<br />　　3、代码中涉及FS操作，尽量使用现成的库<br />　　已经有很多成熟的、用于FS的第三方库（比如<a href="http://www.boost.org/libs/filesystem/" target="_blank" rel="nofollow">boost::filesystem</a>）。如果你的代码涉及到FS的操作（比如目录遍历），尽量使用这些第三方库，可以帮你省不少事情。<br /><br />　　★<b>文本文件的回车CR/换行LF</b><br />　　由于几个知名的操作系统对回车/换行的处理不一致，导致了这个烦人的问题。目前的局面是：Windows同时使用CR和LF；Linux和大部分的Unix使用LF；苹果的Mac系列使用CR。<br />　　对于源代码管理，好在很多版本管理软件（比如CVS、SVN）都会智能地处理这个问题，让你从代码库取回本地的源码能适应本地的格式。<br />　　如果你的程序需要在运行时处理文本文件，要留意本文方式打开和二进制方式打开的区别。另外，如果涉及跨不同系统传输文本文件，要考虑进行适当的处理。<br /><br />　　★<b>文件搜索路径（包括搜索可执行文件和动态库）</b><br />　　在Windows下，如果要执行文件或者加载动态库，一般会搜索当前目录；而Posix系统则不尽然。所以如果你的应用涉及到启动进程或加载动态库，就要小心这个差异。<br /><br />　　★<b>环境变量</b><br />　　对于上述提到的搜索路径问题，有些同学想通过修改PATH和LD_LIBRARY_PATH来引入当前路径。假如使用这种方法，建议你只修改进程级的环境变量，不要修改系统级的环境变量（修改系统级有可能影响到同机的其它软件，产生副作用）。<br /><br />　　★<b>动态库</b><br />　　如果你的应用程序使用动态库，强烈建议动态库导出标准C风格的函数（尽量不要导出类）。如果在Posix系统中加载动态库，切记慎用<b>RTLD_GLOBAL</b>标志位。这个标志位会Enable全局符号表，有可能会导致多个动态库之间的符号名冲突（一旦碰到这种事，会出现匪夷所思的运行时错误，极难调试）。<br />　　关于动态库的话题比较大，限于篇幅，以后单独写一个帖子讨论。<br /><br />　　★<b>服务/看守进程</b><br />　　如果你不清楚服务和看守进程的概念，请看维基百科（<a href="http://en.wikipedia.org/wiki/Windows_service" target="_blank" rel="nofollow">这里</a>和<a href="http://en.wikipedia.org/wiki/Daemon_%28computer_software%29" target="_blank" rel="nofollow">这里</a>）。为了叙述方便，以下统称服务。<br />　　由于C++开发的模块大部分是后台模块，经常会碰到服务的问题。编写服务需要调用好几个系统相关的API，导致了与操作系统的紧密耦合，很难用一套代码搞定。因此比较好的办法是抽象出一个通用的服务外壳，然后把业务逻辑代码作为动态库挂载到它下面。这样的话，至少保证了业务逻辑的代码只需要一套；服务外壳的代码虽然需要两套（一个用于Windows、一个用于Posix），但他们是业务无关的，可以很方便地重用。<br /><br />　　★<b>默认栈大小</b><br />　　不同的操作系统，栈的默认大小差别很大，从几十KB（据说Symbian只有12K，真抠门）到几MB不等。因此你事先要打听一下目标系统的默认栈大小，如果碰上像Symbian这样抠门的，可以考虑用编译器选项调大。当然，养成“<b>不在栈上定义大数组/大对象</b>”的好习惯也很重要，否则再大的栈也会被撑爆的。<br /><br />　　看到这里，可能有同学要问了，为什么没聊进程管理和多线程的话题？欲知后事如何，且听<a href="../../2009/04/cxx-cross-platform-develop-6-thread.md">下回分解</a>。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/02/cxx-cross-platform-develop-5-os.md">2009/02/cxx-cross-platform-develop-5-os.md</a>
</div>
</div>
</body>
</html>
