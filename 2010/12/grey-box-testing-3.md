
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>如何开展灰盒测试[3]：模块接口类型概述 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">如何开展灰盒测试[3]：模块接口类型概述</a></h1>
<div class="post-info"><span class="date-header">2010-12-26</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.E8BDAFE4BBB6E5B7A5E7A88B.md" class="tag">编程.软件工程</a> </div>
<hr>
<div class="post">
　　经过前面几个帖子的铺垫（或许有些网友认为俺是卖关子:），今天开始介绍技术方面的话题。<!--program-think--><br /><br /><h2>★关于实现方式</h2><br />　　在<a href="../../2010/11/grey-box-testing-1.md" target="_blank">前面的帖子</a>里，俺提到过<b>基于脚本</b>的灰盒测试。后面聊具体的技术手段时，会侧重于Python脚本（这正好可以跟俺写的另一个系列“<a href="../../2009/08/why-choose-python-0-overview.md" target="_blank">为什么俺推荐Python</a>”遥相呼应）。当然啦，为了照顾那些不用Python的同学，其它的技术手段，俺也会顺带提一下。<br />　　关于Python的版本，（截至到目前）有两个系列：2.x版本和3.x版本。这两种版本不但在语法上有一定的差异，而且内置的标准库也有不同。考虑到目前那些使用Python的开源项目，还是用2.x版本居多，所以俺后续在介绍Python脚本实现时，也会侧重于2.x版本。<br /><br /><h2>★各种接口的分类</h2><br />　　由于灰盒测试的技术实现，是一个比较大的话题，涉及面会比较宽。为了保持一定的条理性，避免大伙儿看着看着就迷糊了，俺打算根据模块的接口类型（也就是模块间的交互类型）来叙述。每种类型，单独开一个帖子来具体介绍。<br /><br /><h3>◇根据是否跨进程来分类</h3><br />　　如果从进程的角度来看，交互双方的模块可能在同一个进程，也可能在不同的进程。因此，模块间的交互可以分为“进程内”、“跨进程”两大类（不知<b>进程</b>为何物，请看<a href="http://zh.wikipedia.org/zh-cn/%E8%A1%8C%E7%A8%8B" target="_blank">这里</a>的介绍）。对于进程间的交互，还专门有一个洋文的缩写——<a href="http://en.wikipedia.org/wiki/Inter-process_communication" target="_blank">IPC</a>。<br /><br /><h3>◇根据是否跨主机来分类</h3><br />　　如果从机器的角度看，交互的双方可能在同一个主机，也可能在不同的主机。因此，模块间的交互类型还可以分为“主机内”、“跨主机”两大类。“主机间”的交互，必定也是“跨进程”的。反之则<b>不然</b>。<br />　　顺便提一下：如果从耦合的角度来看，跨主机的交互比主机内的交互，耦合低；跨进程的交互比进程间的交互，耦合低。（不知道<b>耦合</b>为何物的同学，请看<a href="http://www.hudong.com/wiki/%E8%80%A6%E5%90%88" target="_blank">这里</a>的介绍）<br /><br />　　由于不存在“跨主机不跨进程”的接口方式，所以上述两种分类维度排列组合之后，有3种可能。每种俺单独开一个帖子，请看：<br />　　<a href="../../2010/12/grey-box-testing-4.md">接口测试实战——跨主机的交互方式</a><br />　　接口测试实战——主机内的跨进程交互方式<br />　　接口测试实战——进程内的交互方式<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2010/12/grey-box-testing-3.md">2010/12/grey-box-testing-3.md</a>
</div>
</div>
</body>
</html>
