<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>有关封装和信息隐藏的误区 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">有关封装和信息隐藏的误区</a></h1>
<div class="post-info"><span class="date-header">2010-08-28</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> </div>
<hr>
<div class="post">
　　上次<a href="../../2010/08/why-choose-python-3-oop.md" target="_blank">介绍Python的面对对象特性</a>，其中扯到了封装（Encapsulation）等概念。当时为了不跑题，没有深入聊这些概念。考虑到很多开发人员对这些概念，经常混淆不清。今天再专门来说一下。<!--program-think--><br /><br /><h2>★封装</h2><br /><h3>◇什么是封装？</h3><br />　　从字面意思来看，封装就是把一些<b>相关的</b>东西打包成一坨（看到“坨”这个量词，不要想歪了）。“封装”最广为人知的例子，就是在面向对象编程（以下简称OOP）里面，把数据和针对该数据的操作，统一到一个class里。<br /><br /><h3>◇封装有啥好处？</h3><br />　　那封装有啥好处捏？一个主要的好处，就是增加软件代码的内聚性。通过增加内聚性，进而提高可复用性和可维护性。<br /><br /><h3>◇封装的手段</h3><br />　　很多人把封装的概念局限于类，认为只有OO中的class才算是封装。这实际上是片面滴！在很多不使用"类"的场合，一样能采用封装的手法。下面俺随手举几个和OO无关的例子：<br /><br />1、通过文件<br />　　比如C和C++支持对头文件的包含（#include）。因此，可以把一些相关的常量定义、类型定义、函数声明，统统<b>封装</b>到某个头文件中。<br /><br />2、通过namespace/package/module<br />　　C++的namespace、Java的package、Python的module，想必各自的开发人员都很熟悉。这些语法虽然称呼各不相同，但具有相同的本质。因此，也可以利用这些语法，来进行封装。<br /><br /><h2>★信息隐藏</h2><br /><h3>◇什么是信息隐藏？</h3><br />　　“信息隐藏”——顾名思义——就是把不该暴露的信息藏起来。说到信息隐藏，很多人自然而然地，就联想到某些OO语言（比如C++、Java）提供的，诸如private、protected之类的关键字。这些关键字可以通过访问控制，来达到信息隐藏的目的。<br /><br /><h3>◇信息隐藏有啥好处？</h3><br />　　信息隐藏的好处，正好和“封装”的好处相呼应。封装是为了提高内聚性；而信息隐藏是为了降低耦合性。通过降低耦合，一样可以达到提高可复用性、可维护性这2个目的。<br /><br /><h3>◇信息隐藏的手段</h3><br />　　和封装类似，很多程序员也把信息隐藏的概念片面化——认为信息隐藏仅限于private和protected关键字。所以，俺再随手举几个其它的信息隐藏手段。<br /><br />1、通过接口类<br />　　可以通过定义接口类（Java中的interface、C++中的纯虚类）来实现信息隐藏。具体实现如下：<br />　　定义一个接口类，仅包含一些公有的成员函数的<b>声明</b>（Java的abstract函数，C++的纯虚函数），没有任何函数实现，也没有任何成员变量。然后把具体的实现代码放到该接口类的一个派生子类中。<br />　　由于调用者只看到接口类，看不到实现类。所以，同样可以达到信息隐藏。在某些情况下，使用这种手段达到的效果，会比基于访问控制（使用private关键字）的效果，更好。<br />　　不过这种手段依赖于语言的支持。使用该手法的编程语言，至少要支持继承、虚函数等语法。<br /><br />2、通过pimpl手法<br />　　pimpl手法也叫作“Opaque Pointer”手法。和接口类的手法不同，pimpl手法不需要靠继承、虚函数等语法的支持，因此对诸如C语言来说，很有用。<br />　　为了省事儿，俺就不具体解释该手法的实现细节。有兴趣的同学请看“<a href="http://en.wikipedia.org/wiki/Opaque_pointer" target="_blank" rel="nofollow">这里</a>”（连不同语言的样例代码都展示给你了，要是再看不懂就只有怪自己笨了）。<br /><br /><h2>★一些理解上的误区</h2><br />　　介绍完一些基本概念，再来说一下，关于封装、信息隐藏的一些常见误区。<br /><br /><h3>◇把封装等同于信息隐藏</h3><br />　　这是混淆最严重的一个误区——很多初学OOP的同学都把封装和信息隐藏混为一谈。希望经过俺前面的一番解释，有些人能搞明白其中的差异。顺便提一下，有个老外写了篇小有名气的文章——“<a href="http://www.javaworld.com/javaworld/jw-05-2001/jw-0518-encapsulation.md" target="_blank" rel="nofollow">Encapsulation is not information hiding</a>”。洋文好的同学，可以去瞅一瞅。<br /><br /><h3>◇把封装看得太狭隘</h3><br />　　其实前面已经通过举例，驳斥了狭隘看待封装的误区。此处不再啰嗦。<br /><br /><h3>◇把信息隐藏看得太狭隘</h3><br />　　前面已经通过举例，驳斥了狭隘看待信息隐藏的误区。此处不再啰嗦。<br /><br /><h3>◇混淆可访问性和可见性</h3><br />　　考虑到某些网友可能连这两者的区别都不太清楚，先简单解释一下。所谓可访问性，就是可以对某个东西进行读/写操作；所谓可见性，就是能够感觉到某个东西的存在。<br />　　前面谈到信息隐藏时，我们提及了通过访问控制的关键字（private、protected）来达到信息隐藏的目的。有很多同学认为这几个关键字不光禁止了可访问性（accessibility），还禁止了可见性（visibility）。其实也不尽然。不同的编程语言，对这两者的处理是不同滴。比如在C++语言中，类的私有成员虽然不可访问，但还是可见的。此话怎讲捏？请看下面的例子：<br /><pre><font face="Courier New">int n = 0;<br /><br />class Parent<br />{<br />public:<br />    Parent()<br />    {<br />        n = 1;<br />    }<br /><br />private:<br />    int n;<br />};<br /><br />class Child : public Parent<br />{<br />public:<br />    Child()<br />    {<br />    }<br /><br />    void Func()<br />    {<br />        ::printf(&quot;%d&quot;, n);<br />    }<br />};<br /><br />int main()<br />{<br />    Child c;<br />    c.Func();<br /><br />    return 0;<br />}</font></pre><br />　　如果俺问列位看官，程序执行后会打印出啥？相信一多半的同学会回答：“打印0”。<br />但是，真相是：<b>该程序根本在编译时就报错了</b>。<br />　　问题在于，父类的私有成员变量n虽然对子类是无法访问的，但依然是可见的（可感知的）。所以，对于那个printf语句，编译器会认为是企图访问父类的私有成员，故而报错。<br />　　再悄悄跟大伙儿说一下，这例子是俺从C++它爹所写的《The Design and Evolution of C++》里面剽窃滴 :)<br /><br /><h2>★结尾</h2><br />　　今天的话题，基本上到此结束了。最后，俺想提醒列位看官注意一下：象封装和信息隐藏，都属于编程的基本功，为啥很多开发人员都没有想透彻捏？<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2010/08/encapsulation-and-information-hiding.md">2010/08/encapsulation-and-information-hiding.md</a>
</div>
</div>
</body>
</html>
