
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>Java性能优化[4]：关于finalize函数 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">Java性能优化[4]：关于finalize函数</a></h1>
<div class="post-info"><span class="date-header">2009-06-26</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.E680A7E883BDE4BC98E58C96.md" class="tag">编程.性能优化</a> <a href="../../tags/E7BC96E7A88B.Java.md" class="tag">编程.Java</a> </div>
<hr>
<div class="post">
　　<a href="../../2009/04/java-performance-tuning-3-gc.md" target="_blank">上次的帖子</a>聊了垃圾回收器的调优，当时啰嗦了比较长的篇幅，就没再继续提finalize的事儿（其实这玩意儿和GC是沾点儿边的）。今天咱就把finalize函数相关的性能话题拿来说一下。<!--program-think--><br /><br />　　★<b>finalize函数的调用机制</b><br />　　俺经常啰嗦了解本质机制的重要性。所以今天也得先谈谈finalize函数的调用机制。在聊之前，先声明一下：Java虚拟机规范（见“<a href="http://java.sun.com/docs/books/jvms/second_edition/html/VMSpecTOC.doc.md" target="_blank" rel="nofollow">这里</a>”），并没有硬性规定垃圾回收该不该搞，以及该如何搞。所以俺这里提到的finalize函数的调用机制，或许适用于大多数JVM，但不保证能适用于<b>所有</b>的JVM。<br />　　◇何时被调用？<br />　　finalize啥时候才会被调用捏？一般来说，要等到JVM开始进行垃圾回收的时候，它才<u><b>有可能</b></u>被调用。而JVM进行垃圾回收的时间点是<b>非常</b>不确定的，依赖于各种运行时的环境因素。具体细节可以参见“<a href="../../2009/04/java-performance-tuning-3-gc.md" target="_blank">本系列前一帖</a>”。正是由于finalize函数调用时间点的不确定，导致了后面提到的某些缺点。<br />　　◇谁来调用？<br />　　说完何时调用，咱接着来聊一下被谁调用？<br />　　常见的JVM会通过GC的垃圾回收线程来进行finalize函数的调用。由于垃圾回收线程比较重要（人家好歹也是JVM的一个组成部分嘛），为了防止finalize函数抛出的异常影响到垃圾回收线程的运作，垃圾回收线程会在调用每一个finalize函数时进行try catch，如果捕获到异常，就直接丢弃，然后接着处理下一个失效对象的finalize函数。<br /><br />　　★<b>finalize函数的误解和误用</b><br />　　◇把finalize当成“析构函数”<br />　　学过C++的同学应该都知道“析构函数”（不懂C++的同学直接跳过此小节）。C++析构函数是在对象离开作用域的当口，<b>立即</b>被调用的。很多从C++转Java的同学会想当然地把finalize函数牵强附会成C++的析构函数（两者确实有某些相似之处）。然而，现实往往不是这么美好滴。由于Java的finalize函数和C++的析构函数之间有许多非常<b>显著</b>的差异，那些把finalize拿来当析构函数用的同学，注定是要碰壁滴（具体请看本文后面“finalize函数的缺点”）。<br />　　◇依靠finalize来释放资源<br />　　很多同学寄希望于通过finalize()来完成类对象中某些资源的释放（比如关闭数据库连接之类）。有这种企图的同学，请注意看本文后面的“finalize函数的缺点”！<br /><br />　　★<b>使用finalize函数的注意事项</b><br />　　下面介绍的注意事项，有些可能和性能优化关系不大，俺也一并列出来。<br />　　◇调用时间不确定——有资源浪费的风险<br />　　前面已经介绍了调用机制。同学们应该认清“<b>finalize的调用时机是很不确定的</b>”这样一个事实。所以，假如你把某些稀缺资源放到finalize()中释放，可能会导致该稀缺资源等上很久很久很久以后才被释放。这可是资源的浪费啊！另外，某些类对象所携带的资源（比如某些JDBC的类）可能本身就很耗费内存，这些资源的延迟释放会造成很大的性能问题。<br />　　◇可能不被调用——有资源泄漏的风险<br />　　很多同学以为finalize()<b>总是会</b>被调用，其实不然。在某些情况下，finalize()压根儿不被调用。比如在JVM退出的当口，内存中那些对象的finalize函数可能就不会被调用了。<br />　　俺估摸着会有同学在打“runFinalizersOnExit”的主意，来确保所有的finalize在JVM退出前被调用。很可惜也很遗憾，该方法从JDK 1.2开始，就已经被废弃了。即使该方法不被废弃，也是有很大的线程安全隐患滴！企图打这个主意的同学，趁早死了这条心吧。<br />　　从上述可以看出，一旦你依赖finalize()来帮你释放资源，那可是很不妙啊（<b>有资源泄漏的危险</b>）！关于资源泄漏的严重性，俺在“<a href="../../2009/02/defect-of-java-beginner-3-code-style.md#gc" target="_blank">这里</a>”曾经提到过。很多时候，资源泄露导致的性能问题更加严重，万万不可小看。<br />　　◇对象可能在finalize函数调用时复活——有诈尸的风险<br />　　诈尸的情况比较少见，不过俺还是稍微提一下。<br />　　本来，只有当某个对象已经失效（没有引用），垃圾回收器才会调用该对象的finalize函数。但是，万一碰上某个变态的程序员，在finalize()函数内部再把对象自身的引用（也就是this）重新保存在某处，也就相当于把自己复活了（因为这个对象重新有了引用，不再处于失效状态）。这种做法是不是够变态啊 <b>:-)</b><br />　　为了防止发生这种诡异的事情，垃圾回收器只能在每次调用完finalize()之后再次去检查该对象是否还处于失效状态。这无形中又增加了JVM的开销。<br />　　随便提一下。由于JDK的文档中规定了（具体见“<a href="http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.md#finalize%28%29" target="_blank" rel="nofollow">这里</a>”），JVM对于每一个类对象实例最多只会调用一次finalize()。所以，对于那些诈尸的实例，当它们真正死亡时，finalize()反而不会被调用了。这看起来是不是很奇怪？<br />　　◇要记得自己做异常捕获<br />　　刚才在介绍finalize()调用机制时提到，一旦有异常抛出到finalize函数外面，会被垃圾回收线程捕获并丢弃。也就是说，异常被忽略掉了（异常被忽略的危害，“<a href="../../2009/02/defect-of-java-beginner-4-exception.md" target="_blank">这里</a>”有提到）。为了防止这种事儿，凡是finalize()中有可能抛出异常的代码，你都得写上try catch语句，自己进行捕获。<br />　　◇要小心线程安全<br />　　由于调用finalize()的是垃圾回收线程，和你自己代码的线程不是同一个线程；甚至不同对象的finalize()可能会被不同的垃圾回收线程调用（比如使用“并行收集器”的时候）。所以，当你在finalize()里面访问某些数据的时候，还得时刻留心线程安全的问题。<br /><br />　　★<b>结论</b><br />　　前面废了这么多话，最后稍微总结一下。俺窃以为：finalize实在是Java的鸡肋。或许它对于<b>极少数</b>程序员有用，但对于大多数人（包括俺自个儿），这玩意儿没啥明显的好处。大伙儿还是尽量不用为妙。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/06/java-performance-tuning-4-finalize.md">2009/06/java-performance-tuning-4-finalize.md</a>
</div>
</div>
</body>
</html>
