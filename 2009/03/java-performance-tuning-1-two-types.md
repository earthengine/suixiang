
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>Java性能优化[1]：基本类型 vs 引用类型 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">Java性能优化[1]：基本类型 vs 引用类型</a></h1>
<div class="post-info"><span class="date-header">2009-03-16</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.E680A7E883BDE4BC98E58C96.md" class="tag">编程.性能优化</a> <a href="../../tags/E7BC96E7A88B.Java.md" class="tag">编程.Java</a> </div>
<hr>
<div class="post">
　　<a href="../../2009/03/java-performance-tuning-0-overview.md">在Java性能优化系列</a>中，内存管理是一个要优先考虑的关键因素。而说到内存分配，就必然会涉及到基本类型和引用类型。所以我们今天就先来介绍一下这两种类型在性能方面各自有什么奥妙（关于引用类型的其它奥妙，请看“<a href="../../2009/03/java-reference-types-detail.md">这里</a>”）。<!--program-think--><br /><br />　　★<b>名词定义</b><br />　　先明确一下什么是基本类型，什么是引用类型。简单地说，所谓基本类型就是Java语言中如下的8种内置类型：boolean、char、byte、short、int、long、float、double。而引用类型就是那些可以通过new来创建对象的类型（基本上都是派生自Object）。<br /><br />　　★<b>两种类型的存储方式</b><br />　　这两种类型的差异，首先体现在存储方式上。<br />　　◇引用类型的创建<br />　　当你在<b>函数中</b>创建一个引用类型的对象时，比如下面的语句：<br />　　<span style="font-family:Courier New;">StringBuffer str = new StringBuffer();</span><br />　　该StringBuffer<b>对象</b>的内容是存储在堆（Heap）上的，需要申请堆内存。而变量str只不过是针对该StringBuffer对象的一个引用（或者叫地址）。变量str的<b>值</b>（也就是StringBuffer对象的地址）是存储在栈上的。<br />　　◇基本类型的创建<br />　　当你在<b>函数中</b>创建一个基本类型的变量时，比如如下语句：<br />　　<span style="font-family:Courier New;">int n = 123;</span><br />　　这个变量n的<b>值</b>也是存储在栈（Stack）上的，但是这个语句不需要再从堆中申请内存了。<br /><br />为了更加形象，便于大伙儿理解，简单画了一个示意图如下：<br /><center><img src="../../images/2009/03/OgAAADfJvtKaB8finO0otLgLKBqGUQ2lYJGlzQAZCE1qUybiJ9XKK8TrbaBfFVYT1g5DbqIza3sKbsWm2MjeZM4mWoEA15jOjE1kRvoUZjXROWyVUiJ7dUWGWSBV" width="480" alt="不见图、请翻墙" /></center><br /><br />　　★<b>堆和栈的性能差异</b><br />　　可能有同学会小声问：堆和栈有啥区别捏？要说堆和栈的差别，那可就大了去了。如果你对这两个概念还是不太明白或者经常混淆，建议先找本操作系统的书拜读一下。<br />　　由于<a href="../../2009/03/java-performance-tuning-0-overview.md">本系列</a>是介绍性能，所以来讨论一下堆和栈在性能方面的差别（这个差异是很大滴）。堆相对进程来说是全局的，能够被所有线程访问；而栈是线程局部的，只能本线程访问。打个比方，栈就好比个人小金库，堆就好比国库。你从个人小金库拿钱去花，不需要办什么手续，拿了就花，但是钱数有限；而国库里面的钱虽然很多，但是每次申请花钱要打报告、盖图章、办N多手续，耗时又费力。<br />　　同样道理，由于堆是所有线程共有的，从堆里面申请内存要进行相关的加锁操作，因此申请堆内存的复杂度和时间开销比栈要大很多；从栈里面申请内存，虽然又简单又快，但是栈的大小有限，分配不了太多内存。<br /><br />　　★<b>为什么这样设计？</b><br />　　可能有同学又问了，干嘛把两种类型分开存储，干嘛不放到一起捏？这个问题问得好！下面我们就来揣测一下，当初Java为啥设计成这样。<br />　　当年Java它爹（<a href="http://en.wikipedia.org/wiki/James_Gosling" target="_blank" rel="nofollow">James Gosling</a>）设计语言的时候，对于这个问题有点进退两难。如果把各种东东都放置到栈中，显然不现实，一来栈是线程私有的（不便于共享），二来栈的大小是有限的，三来栈的结构也间接限制了它的用途。那为啥不把各种东东都放置到堆里面捏？都放堆里面，倒是能绕过上述问题，但是刚才也提到了，申请堆内存要办很多手续，太繁琐。如果仅仅在函数中写一个简单的“<span style="font-family:Courier New;">int n  = 0;</span>”，也要到堆里面去分配内存，那性能就大大滴差了（要知道Java是1995年生出来的，那年头我家的PC配4兆内存就属豪华配置了）。<br />　　左思右想之后，Java它爹只好做了一个折中：把类型分为基本类型和引用类型，两者使用不同的创建方式。这种差异从Java语法上也可以看出来：引用类型可以用new创建对象（对于某些单键，表面上没用new，但是在getInstance()内部也还是用的new）；而基本类型则不需要用new来创建。<br /><br />　　★<b>这样设计的弊端</b><br />　　顺便跑题一下，斗胆评价Java它爹这种设计的弊端（希望Java Fans不要跟我急）。我个人认为：这个折中的决策，带来了许多深远的影响，随手举出几个例子：<br />　　1、由于基本类型不是派生自Object，因此不能算是纯种的对象。这导致了Java的“<span style="color:red;">纯</span>面向对象”招牌打了折扣（当年Sun老是吹嘘Java是<b>纯</b>OO的语言）。<br />　　2、由于基本类型不是派生自Object，出于某些场合（比如容器类）的考虑，不得不为每个基本类型加上对应的包装类（比如Integer、Byte等），使得语言变得有点冗余。<br /><br />　　★<b>结论</b><br />　　从上述的介绍，我们应该明白，使用new创建对象的开销是<b>不小</b>的。在程序中能避免就应该尽量避免。另外，使用new创建对象，不光是创建时开销大，将来垃圾回收时，销毁对象也是有开销的（关于GC的开销，咱们会在后面的帖子细谈）。<a href="../../2009/03/java-performance-tuning-2-string.md">下一个帖子</a>，我们找一个例子来实战一下。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/03/java-performance-tuning-1-two-types.md">2009/03/java-performance-tuning-1-two-types.md</a>
</div>
</div>
</body>
</html>
