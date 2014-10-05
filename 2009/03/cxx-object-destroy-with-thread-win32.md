<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C++对象是怎么死的？Win32线程篇 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.html" title="回到首页">C++对象是怎么死的？Win32线程篇</a></h1>
<div class="post-info"><span class="date-header">2009-03-05</span><a href="../../tags/E7BC96E7A88B.C.html" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.html" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.E5A49AE7BABFE7A88B.html" class="tag">编程.多线程</a> </div>
<hr>
<div class="post">
　　在<a href="../../2009/02/cxx-object-destroy-with-process.md">前面的帖子</a>里聊完了进程终止对C++对象析构的影响。今天咱们来说一下线程对于C++对象析构的影响。<br />　　由于C++ 03标准没有包含线程的概念，而C++ 0x尚未正式发布。所以对线程的讨论只好根据特定的操作系统平台来谈。对于操作系统自带的线程API，目前比较流行的款式是Windows平台提供的线程API和POSIX平台上的pthread API。但是这两种线程API的差异实在是太大，没法拿出来一起聊。我只好把“线程篇”的帖子再拆分一下，今天先来聊一聊Win32的线程API。<!--program-think--><br />　　另外，对于进行跨平台开发的同学，应该已经用上了某些跨平台的第三方线程库（比如ACE、Boost等），对于这些库的介绍，初步打算放到“<a href="../../2009/01/cxx-cross-platform-develop-0-overview.html" target="_blank">C++的可移植性和跨平台开发</a>”系列中。<br /><br />　　★<b>两套API</b>：<b>OS API</b> vs <b>CRT API</b><br />　　本来照例要先介绍线程的几种死法，但是考虑到很多Windows程序员经常混淆线程API，搞不清楚到底该用哪个。所以先来说一下两套线程API的问题。<br />　　首先，Windows操作系统本身提供了线程的创建函数<b>CreateThread</b>和销毁函数<b>ExitThread</b>。其中的<b>CreateThread</b>用于创建线程，<b>ExitThread</b>用于在线程函数内部推出线程（也就是自杀）。<br />　　其次，在Visual C++自带的C运行库（以下简称CRT）中，还带了另外4个API函数，分别是：<b>_beginthread</b>，<b>_endthread</b>，<b>_beginthreadex</b>，<b>_endthreadex</b>。其中的<b>_beginthread</b>和<b>_beginthreadex</b>用于创建线程（它们内部调用了<b>CreateThread</b>），<b>_endthread</b>和<b>_endthreadex</b>用于自杀（它们内部调用了<b>ExitThread</b>）。<br />　　有同学看到这里，被搞懵了，心想：“干嘛要搞这么多玩意儿出来糊弄人？有<b>CreateThread</b>和<b>ExitThread</b>不就够了嘛！”其实你有所不知，此中大有奥妙啊。<br />　　因为OS API作为操作系统本身提供的API函数，它被设计为语言无关的。它们不光可以被C++调用，还可以被其它诸如VB、Python、Delphi等开发语言来调用。所以它们不会（也不能够）帮你处理一些和具体编程语言相关的琐事。<br />　　而CRT API虽然最终还是要调用OS API来完成核心的功能，但是CRT API在不知不觉中多帮我们干了一些虽琐碎但重要的工作。（如果同学们想窥探一下CRT API内部都干了些啥，可以拜读一下Win32编程的经典名著《Windows 核心编程》的<b>6.7</b>章节，里面介绍得挺细致的）<br />　　费了这么多口水，无非是要同学们牢记：以后在Windows平台下开发多线程程序，<b>千万不要</b>直接使用这两个线程API（也就是<b>CreateThread</b>和<b>ExitThread</b>），否则后果自负 :-)<br />　　另外，顺便补充一下。除了上述提到的CRT库。其它一些Windows平台的C++库也可能提供了线程的启动函数（比如MFC的AfxBeginThread），这些函数也对OS API进行了包装，所以用起来也是安全的。<br /><br />　　★<b>三种死法</b><br />　　说完了两套API，开始来讨论一下线程的几种死法。线程和进程一样，也有三种死法。详见如下：<br />　　1、自然死亡<br />　　一般来说，每个线程都会对应某个函数（以下称为“线程函数”）。线程函数是线程运行的主体。所谓的“自然死亡”，就是通过<b>return</b>语句结束线程函数的执行。<br />　　2、自杀<br />　　所谓的“自杀”，就是当前线程通过调用某API把<b>自己</b>给停掉。前面已经说了OS API的坏话，同学们应该明白<b>不能</b>再用它们。那我们能否使用CRT API来进行自杀呢？请看<a href="http://msdn.microsoft.com/en-us/library/hw264s73.aspx" target="_blank" rel="nofollow">MSDN上的相关文档</a>。上面说了，如果使用<b>_endthread</b>和<b>_endthreadex</b>，将导致析构函数<b>不被</b>调用。<br />　　3、它杀<br />　　所谓的“它杀”，很明显，就是其它线程通过调用某API把当前线程给<b>强行</b>停掉。对于Windows平台来说，实现“它杀”比较简单，使用<b>TernimateThread</b>就直接干掉了（它杀也是最野蛮的）。<br /><br />　　★<b>类对象的析构</b><br />　　照<a href="../../2009/02/cxx-object-destroy-with-process.md">前一个帖子</a>的风格，还是把类对象分为三种：局部非静态对象、局部静态对象、非局部对象。由于非局部对象是在main之前就创建、在进程死亡时析构，暂时与线程扯不上太大关系。剩下的两种局部对象，在宿主线程（所谓宿主线程，就是创建该局部对象的线程）死亡时会受到什么影响捏？请看如下的对照表：<br />－－－－－－－－－－－－－－－－－－－－－－－－－<br />　　　　　　　局部非静态对象　　局部静态对象<br />　自然死亡　　　　能　　　　　　　　能<br />　　自杀　　　　　不能　　　　　　　能<br />　　它杀　　　　　不能　　　　　　　能<br />－－－－－－－－－－－－－－－－－－－－－－－－－<br />　　从上述结果可以看出，Windows上线程的死法还是以自然死亡为最安全，这点和进程的死法类似。所以同学们在Windows上开发时，要尽量避免自杀和它杀。<br /><br />　　★<b>关于主线程之死</b><br />　　所谓“主线程”，就是进程启动时，操作系统为该进程默认创建的第一个线程。通俗地讲，可以把<b>main</b>函数看成是主线程的线程函数。<br />　　主线程之死是有讲究的。由于前面已经阐述了非自然死亡的坏处，所以我们只讨论主线程自然死亡这一种情况。当主线程自然死亡时（也就是用<b>return</b>从<b>main</b>返回时），会导致<b>exit</b>函数被调用，<b>exit</b>函数就会开始清除当前进程的各种资源，为进程的死亡作准备。这时候，如果还有其它活着的线程，也会被一起干掉（其效果类似于它杀）。<br />　　为了防止出现上述情况，主线程一定要负责最终的善后工作。务必等到其它线程都死了，它才能死。<br /><br />　　Windows平台上，有关线程的对象析构问题，就聊到这。<a href="../../2009/03/cxx-object-destroy-with-thread-posix.md">下一个帖子</a>，咱们来聊一下pthread相关的对象析构话题。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/03/cxx-object-destroy-with-thread-win32.md">2009/03/cxx-object-destroy-with-thread-win32.html</a>
</div>
</div>
</body>
</html>
