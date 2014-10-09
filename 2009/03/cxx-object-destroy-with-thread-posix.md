<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C++对象是怎么死的？POSIX线程（pthread）篇 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">C++对象是怎么死的？POSIX线程（pthread）篇</a></h1>
<div class="post-info"><span class="date-header">2009-03-14</span><a href="../../tags/E7BC96E7A88B.C.md" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.E5A49AE7BABFE7A88B.md" class="tag">编程.多线程</a> </div>
<hr>
<div class="post">
　　<a href="../../2009/03/cxx-object-destroy-with-thread-win32.md">上一个帖子</a>聊完了Win32环境下和线程有关的C++对象死亡问题，今天得说一说POSIX的线程库pthread了。如果你对pthread不太了解，可以先看看<a href="http://en.wikipedia.org/wiki/POSIX_Threads" target="_blank" rel="nofollow">维基百科</a>的介绍。<!--program-think--><br /><br />　　★<b>三种死法</b><br />　　废话少说，照例先介绍三种死法。<br />　　1、自然死亡<br />　　<a href="../../2009/03/cxx-object-destroy-with-thread-win32.md">上一个帖子</a>已经介绍了Win32线程的自然死亡，pthread的自然死亡和它差不多，也是线程对应的线程函数通过return返回。<br />　　2、自杀<br />　　对于“自杀”，POSIX使用<b>pthread_exit</b>函数来实现。就一种方式，相比Win32的自杀简单多了，此处省去不少口水。<br />　　3、它杀<br />　　虽然pthread的自杀简单，但是它杀就比较复杂了。所以，我把口水转移到这里，重点说一下它杀的方式。<br />　　在pthread库中主要使用<b>pthread_cancel</b>杀线程。用<b>pthread_cancel</b>取消线程还分两种情况：<b>异步取消</b>（PTHREAD_CANCEL_ASYNCHRONOUS）和<b>延迟取消</b>（PTHREAD_CANCEL_DEFERRED）。异步取消是相当粗暴的，不管三七二十一，直接把线程干掉；而延迟取消则比较温柔，被取消的线程会继续运行直到遇见某个“取消点”才终止。由于本帖不是pthread的入门扫盲帖，关于什么是“取消点”以及线程取消的其它细节，请参考pthread API手册。<br />　　有同学可能会问了，<b>pthread_kill</b>难道不是用来“它杀”的？其实<b>pthread_kill</b>只不过是给指定的线程发送信号（signal）而已。哎，当初也不知道是哪个家伙起了<b>pthread_kill</b>这个函数名，误导了不少同学。另外，使用<b>pthread_kill</b>有一点要小心，如果对应的线程没有<b>处理</b>收到的信号，则该信号可能会影响线程所在的<b>进程</b>，可能会导致进程终止（相当于进程自杀）。<br /><br />　　★<b>类对象的析构</b><br />　　<a href="../../2009/03/cxx-object-destroy-with-thread-win32.md">上一个帖子</a>已经分析过，和线程有关的C++对象，也就是两种局部对象。请看这两种对象在不同死法上，是否会正常析构。<br />－－－－－－－－－－－－－－－－－－－－－－－－－<br />　　　　　　　　　局部非静态对象　　局部静态对象<br />　　自然死亡　　　　　能　　　　　　　　能<br />　　　自杀　　　　　不一定能　　　　　　能<br />　　它杀（延迟）　　不一定能　　　　　　能<br />　　它杀（异步）　　　不能　　　　　　　能<br />－－－－－－－－－－－－－－－－－－－－－－－－－<br />　　对于上述对照表中的“不一定能”，在Linux平台（具体是RHEL3，GCC 3.2.3）下能够析构，但是在Cygwin（具体是Windows2003，GCC 3.4.4）中不能，所以只好认为是“不一定能析构”。<br />　　由于pthread在不同的操作系统上的实现可能有差异，说不定在某些环境下，自杀和它杀的表现会和上述不一致。假如你发现自己碰到的实际情况和上述不符合，欢迎你通过评论或邮件告诉我，我会补充到本文中 <b>:-)</b><br />　　从上述结果来看，异步它杀是最不安全的，自然死亡还是最安全的。至于自杀和延迟它杀，则要看具体的环境了。<br /><br />　　★<b>关于主线程之死</b><br />　　关于啥是主线程，<a href="../../2009/03/cxx-object-destroy-with-thread-win32.md">上一个帖子</a>已经介绍过了，不再多啰嗦。在POSIX系统里，主线程的自然死亡也会引发<b>exit</b>被调用，从而导致其它线程被野蛮地干掉（这个情形和Windows系统中类似）。如果希望主线程退出不导致进程自杀，可以使用<b>pthread_exit</b>来结束主线程，并让其它线程继续运行。不过由于线程自杀在某些环境下也<b>不安全</b>，我建议还是让主线程最后退出比较稳妥。<br /><br />　　POSIX系统中，线程相关的对象析构问题，就聊到这里。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/03/cxx-object-destroy-with-thread-posix.md">2009/03/cxx-object-destroy-with-thread-posix.html</a>
</div>
</div>
</body>
</html>
