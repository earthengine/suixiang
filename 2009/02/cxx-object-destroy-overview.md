<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C++对象是怎么死的？为什么要写这个系列？ - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">C++对象是怎么死的？为什么要写这个系列？</a></h1>
<div class="post-info"><span class="date-header">2009-02-26</span><a href="../../tags/E7BC96E7A88B.C.md" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> </div>
<hr>
<div class="post">
　　要说C++对象是怎么死的，得先从C++的析构函数说起。这玩意儿是我本人很喜欢的一个语言特性（可惜有好几个语言没有类似的玩意儿，具体就不点名了，免得引发口水战）。我们可以利用C++的构造和析构函数，来实现Guard模式，写出比较清晰、简练和异常安全的代码。由于Guard模式在C++程序中运用挺多，所以保证<b>所有对象被析构</b>就是一个很重要很严肃的问题。<!--program-think--><br />　　另外，我发现很多C++程序员只关心内存泄露问题，不关心（或不清楚）资源泄露问题（很类似于我在“<a href="../../2009/02/defect-of-java-beginner-3-code-style.html#gc" target="_blank">Java新手通病[3]</a>”提到的现象）。比如昨天的“<a href="../../2009/02/cxx-object-destroy-with-process.md" target="_blank">C++对象是怎么死的？进程篇</a>”发布后，就有同学问了：进程死都死了，对象没销毁又有什么关系捏？其实大有关系啊！虽然操作系统会在进程死后帮它收尸（也就是把某些资源，比如内存进行回收），基本不用担心内存泄露的问题。但是别忘了，除了内存资源，进程中可能还包含有其它业务层面的资源，而这些资源，操作系统是不会帮你自动回收的。所以我要再啰嗦一次：<b>资源泄露往往比内存泄露要严重得多啊</b>。啰嗦完之后，为了加深印象，再举如下一个例子。<br />　　比如某业务逻辑Foo需要操作大量的临时文件（放在某动态生成的临时目录中），为了保证该业务逻辑结束后（可能是正常结束，也可能中途抛出异常），该临时目录总是被删除，可以使用如下的Guard模式。<br /><pre>class CTempDirGuard<br />{<br />public:<br />  CTempDirGuard(const string&amp; sFolderName)<br />  {<br />    // 创建某临时目录<br />  }<br />  virtual ~CTempDirGuard()<br />  {<br />    // 把该临时目录整个儿删除<br />  }<br />};<br /><br />void Foo()<br />{<br />  CTempDirGuard guard(xxx);  // 声明guard对象<br />  // 往临时目录放东西<br />  // 不管是出现return语句还是有异常抛出，guard都会被析构，因而该xxx目录会被删除<br /><br />  // 但是如果程序执行到此处，却发生进程的<b>非</b>自然死亡，<br />  // 在这种情况下，该guard对象将<b>不会</b>被析构，因此会留下一个垃圾目录，浪费了硬盘资源<br />}</pre><br />　　鉴于上述所说的两个原因，所以我一直想写一个这方面的帖子。正好前几天写了帖子讨论“<a href="../../2009/02/multi-process-vs-multi-thread.md" target="_blank">架构设计的多进程问题</a>”，之后就就顺便写了一个帖子：“C++进程是怎么死的？”，讨论了一下由于进程不同的死法对C++对象析构的影响。等写完之后突然想到：除了进程终止的问题可能导致C++对象的<b>不</b>正常析构，还有线程等其它因素也可能会让C++对象<b>不</b>正常析构。所以干脆就改了个名，叫“C++ 对象是怎么死的？” :-)<br /><br />　　另外，为了方便阅读，把本系列帖子的目录整理如下：<br />　　1、<a href="../../2009/02/cxx-object-destroy-with-process.md">进程篇</a><br />　　2、<a href="../../2009/02/cxx-object-destroy-with-io-stream.md">对标准输入输出流的进一步探讨</a><br />　　3、<a href="../../2009/03/cxx-object-destroy-with-thread-win32.md">Win32线程篇</a><br />　　4、<a href="../../2009/03/cxx-object-destroy-with-thread-posix.md">POSIX线程（pthread）篇</a><br />　　5、......<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/02/cxx-object-destroy-overview.md">2009/02/cxx-object-destroy-overview.html</a>
</div>
</div>
</body>
</html>
