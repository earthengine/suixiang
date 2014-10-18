<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>软件工程进阶之每日构建[0]：概述 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">软件工程进阶之每日构建[0]：概述</a></h1>
<div class="post-info"><span class="date-header">2009-02-16</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.E8BDAFE4BBB6E5B7A5E7A88B.md" class="tag">编程.软件工程</a> </div>
<hr>
<div class="post">
　　在昨天“<a href="../../2009/02/6.md">正确地做事(善用工具)</a>”的帖子里提到了代码提交频度的问题。当时我特别强调了“<b>要保证提交的代码能编译通过</b>”，理由是“对于每日构建很重要”。我估计列位看官中，不太熟悉每日构建的，大有人在；而且国内停留在手工作坊阶段的软件公司，为数也不少。因此今天我们就来说一下"每日构建"这个话题。假如你平时已经很善于运用"每日构建"这一有效的手段，可以直接略过本系列，去看其它帖子。<!--program-think--><br />　　照例先来说说什么是“每日构建”，每日构建在洋文里也称为Daily Build或者Nightly Build。具体定义见“<a href="http://en.wikipedia.org/wiki/Daily_build" target="_blank" rel="nofollow">这里</a>”。简单地讲，就是每天都把<b>整个</b>软件项目<b>自动</b>编译一遍，最终生成的产出物必须和交付到用户手中的一样（比如你最终提交给用户的是一个安装程序，那就必须在开发过程中每天编译出一个安装包）。<br />　　为了表明每日构建是一个很有效的手段，我可以给大伙举几个知名软件公司或者著名开源项目的例子：<br />　　1、微软公司内部几乎所有产品的开发过程，都会使用每日构建。<br />　　2、我不确定Google是否所有产品都采用，但至少Google的Chrome浏览器是采用每日构建。<br />　　3、知名的开源组织Mozilla也大量使用每日构建。<br />　　4、知名的Linux发行版Ubuntu也使用每日构建。<br />　　......<br />　　上面这个列表还可以罗列很长。举这么多例子，无非想说，每日构建是一种牛X的软件工程手段。尤其对于复杂项目和大型团队，它的好处更加明显。看到这儿，有同学可能要问了，具体有些什么好处捏？请看“<a href="../../2009/02/daily-build-1-advantage.md">软件工程进阶之每日构建[1]：好处和优点</a>”。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/02/daily-build-0-overview.md">2009/02/daily-build-0-overview.md</a>
</div>
</div>
</body>
</html>
