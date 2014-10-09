<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C/C++中一个简单的enum手法(idiom) - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">C/C++中一个简单的enum手法(idiom)</a></h1>
<div class="post-info"><span class="date-header">2009-04-18</span><a href="../../tags/E7BC96E7A88B.C.md" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> </div>
<hr>
<div class="post">
　　今天写程序的时候，又用到这个idiom了，于是顺便贴出来。这个idiom蛮简单的，估计很多人都用过。今天主要是贴出来给新手参考（老手们就甭费时看此帖了）。<!--program-think--><br />　　为了说明这个手法具体该咋用，咱举一个简单的例子来说事儿。比方说要开发一个网络程序，其中需要统计各种网络协议的数据包数量。<br /><br />　　★<b>版本1</b><br />　　假设一开始只需要处理HTTP和FTP两种协议。有些同学不假思索，立即会声明如下两个整数用于统计：<br /><font face="Courier New"><br />int nCntHttp = 0;<br />int nCntFtp = 0;<br /></font><br />　　猛一看，似乎没啥问题。但是，如果需求发生变更，又要增加两种协议：SMTP和SSH。然后，该同学会继续扩展上述代码，变为如下：<br /><font face="Courier New"><br />int nCntHttp = 0;<br />int nCntFtp = 0;<br />int nCntSmtp = 0;<br />int nCntSsh = 0;<br /></font><br />　　这时候，问题开始显露出来了。比方说要打印上述4统计值，就得写4个printf；再假如要用断言确保所有统计值大于零，也得写4个assert。这都是挺烦人的事儿。（当然啦，有些同学会把4个变量的打印写在一个printf中，但还是一样烦人）<br /><br />　　★<b>版本2</b><br />　　这可咋办捏？某些同学就灵机一动，把上述代码修改为数组形式，上述的4个统计值<b>依次</b>放入数组中。具体如下：<br /><font face="Courier New"><br />int nCntProto[4];<br />/* 第0个是HTTP，第1个是FTP，第2个是SMTP，第3个是SSH */<br /></font><br />　　这样，无论是打印还是断言，都可以用for循环搞定，貌似挺方便的。但这么一来，引入了另一个问题。假设我在程序中要用到SMTP的统计数字，就得这么写代码：nCntProto[<b><font color="red">2</font></b>]。这就造成了很不雅观的“<a href="http://en.wikipedia.org/wiki/Magic_number_(programming)#Unnamed_numerical_constant" target="_blank" rel="nofollow">Magic Number</a>”！要知道，Magic Number可是代码的臭味之一啊（其弊端在“<a href="../../2009/02/defect-of-java-beginner-3-code-style.html#magic_number" target="_blank">这里</a>”曾经介绍过）。万一将来，数组中的存放顺序发生变化，那就完蛋了：好多用到Magic Number的代码都得跟着改。一旦漏改某处，引出Bug无数！<br /><br />　　★<b>版本3</b><br />　　为了消除Magic Number，增加代码可读性和可维护性，有些同学开始打起enum的主意。在代码中增加了一组enum，具体如下：<br /><pre><font face="Courier New">enum PROTO<br />{<br />  PROTO_HTTP,<br />  PROTO_FTP,<br />  PROTO_SMTP,<br />  PROTO_SSH,<br />};<br /><br />int nCntProto[4];</font></pre><br />　　这样，如果我需要用到SMTP的统计数字，我就不用写nCntProto[2]，而是写nCntProto[PROTO_SMTP]。这样，可读性明显好多了。即使将来数组中的存放顺序发生变化，也没关系：只需稍微调整enum中常量的顺序即可，其它代码不用动。<br /><br />　　★<b>版本4</b><br />　　但是，还是有一个不爽的地方。定义数组的语句用到了“4”这个Magic Number。万一将来需求继续变更，继续增加协议，那这个数字还得不断调整。不爽！<br />　　这时候，终极版本隆重登场。请看如下代码：<br /><pre><font face="Courier New">enum PROTO<br />{<br />  PROTO_HTTP,<br />  PROTO_FTP,<br />  PROTO_SMTP,<br />  PROTO_SSH,<br /><br />  PROTO_NUM /* 表示协议数量 */<br />};<br /><br />int nCntProto[PROTO_NUM];</font></pre><br />　　这种写法的好处在于，<b>没有任何一个</b>Magic Number。不管是引用某个统计值还是循环遍历数组，都使用的是定义好的常量。<br />　　当需求变更，需要增加新的协议，只要往enum中增加相应的enum常量即可（但要记得保证PROTO_NUM位于enum定义的末尾）。由于PROTO_NUM会自动跟着增长，所以其它的代码几乎不会受到影响。<br /><br />　　★<b>C++的补充说明</b><br />　　上述代码同时适用于C和C++。不过，对于某些C++程序员，或许看不惯原始数组，觉得STL的容器类看起来比较顺眼。那也没啥大关系：只要把上述代码的数组声明修改为如下，其它的代码基本照旧。<br /><font face="Courier New"><br />std::vector&lt;int&gt; vctCntProto(PROTO_NUM);<br /></font><div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/04/c-cxx-enum-idiom.md">2009/04/c-cxx-enum-idiom.html</a>
</div>
</div>
</body>
</html>
