<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>Java性能优化[0]：概述 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.html" title="回到首页">Java性能优化[0]：概述</a></h1>
<div class="post-info"><span class="date-header">2009-03-16</span><a href="../../tags/E7BC96E7A88B.html" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.E680A7E883BDE4BC98E58C96.html" class="tag">编程.性能优化</a> <a href="../../tags/E7BC96E7A88B.Java.html" class="tag">编程.Java</a> </div>
<hr>
<div class="post">
　　考虑写性能优化系列，主要是因为之前看到了太多性能其烂无比的Java代码（有些代码看得我口瞪目呆）。很多Java程序员在写程序时，由于不太了解JVM及语言本身的一些运作机制，从而导致了代码的性能出现<b>严重</b>问题<!--program-think-->（性能差一个数量级以上，我才称为“严重”）。<br />　　虽然网上也有针对Java性能的介绍，但是很多内容都仅仅告诉读者“该这么做”，而没有讲“为什么该这么做”。典型的例子就是关于String和StringBuffer（StringBuilder），光介绍如何用，却没有说为什么这样用。这种现象导致了很多Java程序员只知其然，不知其所以然。所以本系列帖子会尽量介绍一些“所以然”的东东（也就是<a href="../../2009/02/study-technology-in-three-steps.html" target="_blank">学习技术三部曲</a>的HOW和WHY），希望对Java程序员有所帮助。<br /><br />　　先初步考虑聊如下几个话题：<br />　　1、<a href="../../2009/03/java-performance-tuning-1-two-types.md">基本类型 vs 引用类型</a><br />　　2、<a href="../../2009/03/java-performance-tuning-2-string.md">字符串过滤实战</a><br />　　3、<a href="../../2009/04/java-performance-tuning-3-gc.md">关于垃圾回收（GC）</a><br />　　4、<a href="../../2009/06/java-performance-tuning-4-finalize.md">finalize函数</a><br />　　5、......<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/03/java-performance-tuning-0-overview.md">2009/03/java-performance-tuning-0-overview.html</a>
</div>
</div>
</body>
</html>
