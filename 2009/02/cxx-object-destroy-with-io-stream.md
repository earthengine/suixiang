
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C++对象是怎么死的？关于标准输入输出流(cout,cerr,clog,etc)的进一步探讨 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">C++对象是怎么死的？关于标准输入输出流(cout,cerr,clog,etc)的进一步探讨</a></h1>
<div class="post-info"><span class="date-header">2009-02-26</span><a href="../../tags/E7BC96E7A88B.C.md" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> </div>
<hr>
<div class="post">
　　昨天的帖子“<a href="../../2009/02/cxx-object-destroy-with-process.md" target="_blank">C++ 对象是怎么死的？进程篇</a>”里面，谈到全局对象的析构顺序，当时我举了一个“在析构函数中使用cout”的例子（详见<a href="../../2009/02/cxx-object-destroy-with-process.md" target="_blank">原文</a>）。我当时的本意是想说明：全局对象的析构顺序是不确定的，最好不要在程序逻辑中依赖这个顺序（免得出现移植问题）。<br />　　没成想该帖子引来热烈的评论（我有点受宠若惊了），<!--program-think-->关注的焦点主要集中在：“cout是否会最后析构”。有些网友质疑我所提到的有关VC6的行为；有网友引用了TC++PL上的相关章节（21.5.2）来说明“cout会最先构造、最后析构”。既然大伙儿对标准流类库的构造和析构挺有兴趣，咱们今天就针对这个话题补充说明一下。<br /><br />　　★标准都说了些啥？<br />　　C++ 03标准的18.3章节提到了进程启动和终止。其中对进程的自然死亡有比较具体的描述，包括：各种类型的对象啥时候销毁、用atexit注册的退出函数啥时候被调用、还有输入输出流啥时候flush和close等等。<br />　　另外，在27.4.2.1.6章节中阐述了ios_base::Init如何通过包含一个引用计数，对八个标准流类库的全局对象进行适当的初始化和销毁。<br />　　那么，有了C++ 03标准作书面担保，我们是否就高枕无忧呢？<br /><br />　　★关于老式编译器（03年之前推出）<br />　　由于老式编译器在标准发布之前推出，因此对标准的实现不够好（这不是废话嘛）。关于老式编译器的标准兼容性，在“<a href="../../2009/01/cxx-cross-platform-develop-2-language.md">C++移植性和跨平台开发[2]</a>”有进一步说明。<br />　　老式编译器的典型代表就是VC++ 6.0。其实已经有很多人碰到了“VC6的cout提前析构”的问题，不信大伙儿可以在Google上搜一下。另外，如果你手头上正好有VC6，可以试试附在本文末尾的示例1的代码，看是否能够正常打印，就知道了。<br />　　当然啦，VC6可以称得上是古董级的编译器了，从98年推出到现在，已经超过10个年头。所以它对标准的实现不好也无可厚非。<br /><br />　　★关于新式编译器（03年之后推出）<br />　　那么新式编译器是否就完美地支持C++ 03标准呢？我感觉有点玄。所以今天特地试验了手头能找到的几个C++编译器。看看它们是否能够保证cout最先构造、最后析构。另外，为了给这些新式编译器增加点挑战，我把上述的示例1代码稍微修改了一下，成为示例2代码（说实话，这么写代码确实有点夸张），也附在本文末尾。<br />　　手头的几种编译器测试下来，结果如下：<br />－－－－－－－－－－－－－－－－－－－－－－－－－－－－<br />　　操作系统　编译器版本　　　　　示例1　　示例2<br />　　Win2000　　VC 7.1　　　　　　　OK　　　OK<br />　　RHEL3　　　GCC 3.2.3　　　　　　OK　　　OK<br />　　Win2000　　GCC 3.4.2(MingW)　　OK　　　启动时崩溃<br />　　Win2003　　GCC 3.4.4(Cygwin)　　OK　　　启动时崩溃<br />－－－－－－－－－－－－－－－－－－－－－－－－－－－－<br />　　对于示例2代码造成的崩溃，经过简单排查，基本可以推断是cout滞后构造导致（也就是用到cout时，它还没生出来）。而且GCC 3.4.2版本是2004年出品的，应该不算太老啊（至少03标准已经发布一年了）。从上面的结果看，Linux上版本较老的GCC反而没有问题。所以我<b>猜测</b>或许GCC在Windows上的移植版本有这个缺陷（仅仅是猜测啊）。<br />　　由于时间关系，没来得及深入研究。如果有同学不信，可以找个类似的环境试验一下（没准儿最后发现是我搞错了，也有可能哦）。另外，想打破砂锅的同学，可以去琢磨一下出问题的编译器，看看它们的内部实现。<br /><br />　　★总结<br />　　根据上述的情况，我个人建议：如果你的代码有全局对象，并且你的代码<b>可能</b>会跨编译器，那就避免在全局对象的构造函数和析构函数中使用标准流类库的那八个玩意儿（包括cout、cerr、clog等）。<br />　　毕竟这八个全局对象，都有对应的标准C替代品，并不是不可替代的嘛。大伙儿犯不着冒险嘛。如果你确实舍不得流式操作符（&lt;&lt;和&gt;&gt;）或者确实看不惯<b>printf</b>的变参，你可以用字符串流先格式化好，再用标准C的函数输出嘛（也就多一两行代码而已嘛）。<br /><br />　　最后附上示例代码，供有兴趣的同学尝试。大伙儿如果有新的发现，欢迎发评论告诉我。<pre><br />// ========示例1代码========<br />#include &lt;iostream&gt;<br />using namespace std;<br /><br />class CFoo<br />{<br />public:<br />  CFoo()<br />  {<br />    cout &lt;&lt; "CFoo" &lt;&lt; endl;<br />  }<br /><br />  ~CFoo()<br />  {<br />    cout &lt;&lt; "~CFoo" &lt;&lt; endl;<br />  }<br />};<br /><br />CFoo g_foo;<br /><br />int main()<br />{<br />  return 0;<br />}<br /><br />// ========示例2代码========<br />class CFoo<br />{<br />public:<br />  CFoo();<br />  ~CFoo();<br />};<br /><br />CFoo g_foo;<br /><br />#include &lt;cstdio&gt;<br />#include &lt;iostream&gt;<br />using namespace std;<br /><br />CFoo::CFoo()<br />{<br />  puts("puts CFoo");<br />  cout &lt;&lt; "cout CFoo" &lt;&lt; endl;<br />}<br /><br />CFoo::~CFoo()<br />{<br />  cout &lt;&lt; "cout ~CFoo" &lt;&lt; endl;<br />  puts("puts ~CFoo");<br />}<br /><br />int main()<br />{<br />  return 0;<br />}</pre><div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/02/cxx-object-destroy-with-io-stream.md">2009/02/cxx-object-destroy-with-io-stream.md</a>
</div>
</div>
</body>
</html>
