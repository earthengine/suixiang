<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>从Google搜索的严重bug想开去 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">从Google搜索的严重bug想开去</a></h1>
<div class="post-info"><span class="date-header">2009-02-01</span><a href="../../tags/IT.md" class="tag">IT</a> <a href="../../tags/IT.E4B89AE7958CE8AF84E8AEBA.md" class="tag">IT.业界评论</a> </div>
<hr>
<div class="post">
　　昨天晚上用Google查资料，看到所有的搜索结果都注明是恶意站点。第一反应以为自己眼花了；然后开始怀疑我的浏览器出问题，换了几个浏览器都是老样子；后来又想，会不会是我的ISP在搞鬼。等了十多分钟没解决，只好换百度查资料...<!--program-think--><br />　　今天早上看新闻才知道居然是Google的<b>人为</b>失误，居然是全球性的，居然持续了40多分钟。以下是Google的官方说法（<a href="http://googleblog.blogspot.com/2009/01/this-site-may-harm-your-computer-on.md" target="_blank" rel="nofollow">原文连接</a>）：<br />　　<i>谷歌表示他们一直在和一家非盈利组织StopBadware.org合作，通过这个组织给出的名单对各个URL进行存在恶意软件的信息标注。这个组织的恶意网站名单是人工审核并添加，所以这份名单是人为生成而不是算法生成的。谷歌昨晚进行列表更新时，在下载回来的名单里，错误的出现了"/"这个URL地址，所以错误的将所有地址判断为恶意网站。</i><br />　　比较有戏剧性的是，Google提到的“非盈利组织StopBadware.org”也发表声明：<br />　　<i>谷歌的恶意网站列表并非是我们提供的，而是其自己生成的。</i><br /><br />　　这件事情改变了我对Google的几个看法。<br />　　第1点：虽然我很看不起中国谷歌，但是美国Google在我看来一直是一个<b>优秀</b>的公司。现在它居然出现这么低级的错误（开发过商业Web网站的，应该都知道这有多低级），而且持续40多分钟才搞定。看来Google“<b>优秀</b>”的名声要打折扣了。<br />　　第2点：假如StopBadware的说法成立，那我就得怀疑Google的诚信了。是否Google有意推卸责任给其它组织机构？看来Google“<b>不做恶</b>”的名声要打折扣了。<br />　　第3点：Google一直声称他的所有数据收集、处理、存储都是依靠程序进行的，不会涉及人工干预。我以前也一直猜测Google的恶意站点列表是依靠诸如神经网络、遗传算法、等等牛X的算法来搞定的，现在Google居然承认是靠手工审核添加。看来Google“<b>不采用人工干预</b>”的名声要打折扣了。<br />　　第4点：Google一直在推动云计算，希望大伙儿尽可能地把桌面应用搬上云端。我本来觉得云计算这玩意也挺不错的（优点多多）。现在出了这档子事，我就得谨慎考虑一下了。假如我的个人数据都委托给Google代管，万一Google出个什么纰漏（比如被Hacker搞了），那可就悬了。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/02/google-search-fatal-bug.md">2009/02/google-search-fatal-bug.md</a>
</div>
</div>
</body>
</html>
