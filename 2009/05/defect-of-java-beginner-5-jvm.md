<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>Java新手的通病[5]：不了解JVM - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">Java新手的通病[5]：不了解JVM</a></h1>
<div class="post-info"><span class="date-header">2009-05-22</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.Java.md" class="tag">编程.Java</a> </div>
<hr>
<div class="post">
　　<a href="../../2009/02/defect-of-java-beginner-4-exception.md">上次的帖子</a>讨论了Java异常机制的几种误用，今天咱们来说说JVM（以及Java编译器）相关的话题。为啥要聊JVM捏？因为有很多Java程序员，由于对JVM缺乏了解，在碰到某些技术问题时无从下手；另外，由于缺乏对JVM的了解，可能导致写出来的代码性能巨差或者有严重的Bug。所以俺在之前的帖子“<a href="../../2009/02/study-technology-in-three-steps.md" target="_blank">学习技术的三部曲：WHAT、HOW、WHY</a>”中，强调了掌握内部机制的重要性。对于一个Java程序员来说，你不一定要非常清楚JVM的细节，但是对于一些关键的运作机制，还是要掌握大致的概念。<!--program-think--><br /><br />　　按照本系列的惯例，俺会问几个和JVM相关的问题，你如果对这些问题不是很明白，那得考虑花点时间去了解一下了。另外，鉴于有网友批评“<a href="../../2009/01/defect-of-java-beginner-0-overview.md" target="_blank">本系列</a>”帖子：光诊断毛病，不开出药方。（说得很形象，也很中肯）俺会针对下面提出的问题，写一些帖子来解答。<br /><br />　　★<b>关于基本类型和引用类型</b><br />　　很多新手不理解Java的基本类型和引用类型在本质上有什么区别。请看如下的问题：<br />　　◇这两种类型在内存存储上有什么区别？<br />　　◇这两种类型在性能上有什么区别？<br />　　◇这两种类型对于GC有什么区别？<br />　　关于前两个问题，请看之前的帖子“<a href="../../2009/03/java-performance-tuning-1-two-types.md" target="_blank">Java性能优化[1]：基本类型 vs 引用类型</a>”。<br /><br />　　★<b>关于垃圾回收（Garbage Collection）</b><br />　　很多新手不理解GC的实现机制。请看如下的问题：<br />　　◇GC是如何判断哪些对象已经失效？<br />　　◇GC对性能会有哪些影响？<br />　　◇如何通过JVM的参数调优GC的性能？<br />　　关于GC的问题，可以参见之前的帖子“<a href="../../2009/04/java-performance-tuning-3-gc.md" target="_blank">Java性能优化[3]：关于垃圾回收（GC）</a>”。<br /><br />　　★<b>关于字符串</b><br />　　对于Java提供的String和StringBuilder，想必很多人都知道：String用于常量字符串，StringBuilder用于可变字符串。那Java当初为什么要这样设计捏？为啥不用一个类来统一搞定捏？<br /><br />　　★<b>关于范型（Generic Programming）</b><br />　　从JDK 1.5开始，Java引入了一个重量级的语法：范型。不过捏，很多新手仅仅知道范型的皮毛，而对于很多本质的东东，不甚了解。<br />　　◇GP是在编译时实现的还是在运行时实现的？为什么要这么实现？<br />　　◇GP的类型擦除机制是咋回事？有啥优点/缺点？<br />　　◇使用范型容器（相对于传统容器）在性能上有啥影响？为什么？<br /><br />　　★<b>关于多线程</b><br />　　另外，多线程也是大部分Java新手的短板。所以俺最后再来提几个关于多线程的问题。<br />　　◇synchronized关键字是怎么起作用滴？<br />　　◇synchronized的颗粒度（或者说作用域）如何？是针对某个类还是针对某个类对象实例？<br />　　◇synchronized对性能有没有影响？为什么？<br />　　◇volatile关键字又是派啥用滴？啥时候需要用这个关键字捏？<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/05/defect-of-java-beginner-5-jvm.md">2009/05/defect-of-java-beginner-5-jvm.md</a>
</div>
</div>
</body>
</html>
