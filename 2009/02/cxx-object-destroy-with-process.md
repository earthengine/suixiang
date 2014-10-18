<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C++对象是怎么死的？进程篇 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">C++对象是怎么死的？进程篇</a></h1>
<div class="post-info"><span class="date-header">2009-02-25</span><a href="../../tags/E7BC96E7A88B.C.md" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> </div>
<hr>
<div class="post">
　　我承认这个帖子的名称有标题党的嫌疑，但是暂时想不出更好的名称了，只好先这样了 <b>:-(</b><br />　　由于前天的帖子聊了<a href="../../2009/02/multi-process-vs-multi-thread.md" target="_blank">架构设计的多进程问题</a>，所以今天想起来要聊一下和“C++进程终止”相关的那些事。与前几个C++帖子的风格类似，今天聊的内容，尽量局限于标准C++范畴，尽量不涉及特定的操作系统平台。<!--program-think--><br /><br />　　★<b>关于进程的三种死法</b><br />　　由于今天讲的是“进程篇”，自然得先搞明白进程的几种死法。其实进程和大活人一样，也有三种死法，分别是“自然死亡、自杀、它杀”。这三种死亡方式具体如下：<br />　　1、自然死亡<br />　　望文生义，自然死亡就是最自然的进程退出方法。具体表现为通过return语句结束main函数。由于这种方法最优雅（后面会说），如果没有其它特殊原因，强烈建议采用这种死法。<br />　　2、自杀<br />　　所谓的自杀，就是进程自己调用某些API来自行了断。在标准C++中，这几个函数（exit、abort、terminate、unexpected）可以用于进程自杀。如果没有额外设置，unexpected函数默认会调用terminate函数，terminate函数默认会调用abort函数。所以自杀的方式基本上也就是exit和abort两种。exit相对abort来说温和一些，所以下文称exit为<b>温和自杀</b>；相对地，把abort称为<b>激进自杀</b>。<br />　　3、它杀<br />　　它杀其实也挺好理解，就是当前进程被其它进程杀死。标准C++没有提供用于它杀的API函数，因此常用的方法是通过某些跨平台的库（如ACE）提供的API函数或者调用某些外部命令（如Posix系统的kill命令）来实现。<br />　　上面说了这几种死法，有同学要问了：进程不同的死法和C++对象有什么关系捏？其实关系大大滴，请听我细细道来。<br /><br />　　★<b>类对象的析构（销毁）</b><br />　　首先把类对象分为三种：局部非静态对象、局部静态对象、非局部对象（出于习惯，以下简称<b>全局对象</b>）。对于尚不清楚这几种对象差异的同学，请先找本C++入门书拜读一下。进程不同的死法对于这几种对象是否能销毁会有很大的影响。请看如下的对照表：<br /> －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－<br />  　　　　　　　　局部非静态对象　　局部静态对象　　全局对象<br />　　自然死亡　　　　能　　　　　　　　能　　　　　　能<br />　　温和自杀　　　　不能　　　　　　　能　　　　　　能<br />　　激进自杀　　　　不能　　　　　　　不能　　　　　不能<br />　　　它杀　　　　　不能　　　　　　　不能　　　　　不能<br />－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－<br />　　从这个对照表可以看出，激进自杀和它杀的效果类似（<b>各种</b>类对象都无法正常销毁）。所以我们在写程序时要极力避免上述这两种情况。<br />　　另外，温和自杀也有不爽之处：不能正确地销毁局部非静态对象。准确地说，应该是：在调用exit之前已经构造但是尚未析构的<b>局部非静态</b>对象将再也不会被析构。所以温和自杀也要避免使用。<br />　　综上所述，最正经、最靠谱的死法就是第一种：自然死亡。<br /><br />　　★<b>析构的顺序</b><br />　　那么，是不是只要让进程自然死亡就万事大吉了？非也！即使所有的类对象都会被析构，还有另一个棘手的问题：析构的顺序。先来看下面一个例子：<br /><pre><br />class CFoo<br />{<br />public:<br />  CFoo()<br />  {<br />    cout &lt;&lt; "CFoo" &lt;&lt; endl;<br />  }<br />  virtual ~CFoo()<br />  {<br />    cout &lt;&lt; "~CFoo" &lt;&lt; endl;<br />  }<br />};</pre><br />　　上述示例挺简单的（有效代码仅6行），大伙儿能看出有什么问题吗？如果你一眼就看出问题之所在，恭喜你，后面的内容你不用看了。<br />　　对于用户定义的全局对象，在C++标准中并没有规定它们构造和析构的先后顺序；对于诸如标准输入输出流的cout、cerr等全局对象，在C++ 03标准中（参见27.4.2.1.6章节）有提及如何保证它们在最后析构。但由于某些老式编译器并未完全遵照标准实现，导致标准输入输出流的几个全局对象也<b>可能</b>被提前析构。<br />　　基于上述原因，假如CFoo类也定义了一个全局对象g_foo。当g_foo析构的时候，cout对象<b>可能</b>已经先死了（取决于具体的环境，详见“<a href="../../2009/02/cxx-object-destroy-with-io-stream.md">关于标准输入输出流的进一步探讨</a>”）。在这种情况下，CFoo析构函数的打印语句由于引用了已死的对象，<b>可能会</b>导致不可预料的后果。<br />　　从上面的例子可以看出，如果你在程序中使用了全局对象或者静态对象，那你要非常小心地编写相关class/struct的析构函数代码，尽量不要在它们的析构函数中引用其它的全局对象或静态对象。当然啦，假如能避免使用全局对象和静态对象，就更好了。<br />　　另外，在C++经典名著《Modern C++ Design》的第6章详细描述了关于单键（Singleton）销毁的一些细节、场景及解决方法。大伙儿可以去拜读一下。<br />　　下一个帖子，会聊一下<a href="../../2009/03/cxx-object-destroy-with-thread-win32.md">和线程有关的C++对象是怎么死的</a>。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/02/cxx-object-destroy-with-process.md">2009/02/cxx-object-destroy-with-process.md</a>
</div>
</div>
</body>
</html>
