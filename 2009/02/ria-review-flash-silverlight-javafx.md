<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>三种主流RIA技术之争，你该如何选型？ - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">三种主流RIA技术之争，你该如何选型？</a></h1>
<div class="post-info"><span class="date-header">2009-02-05</span><a href="../../tags/IT.md" class="tag">IT</a> <a href="../../tags/IT.E4B89AE7958CE8AF84E8AEBA.md" class="tag">IT.业界评论</a> </div>
<hr>
<div class="post">
　　前几天听说Adobe发布了用于Flash Player的RTMP（实时消息协议），在“<a href="http://www.adobe.com/aboutadobe/pressroom/pressreleases/200901/012009RTMP.html" target="_blank" rel="nofollow">这里</a>”。乍一看，好像是一个不错的东东。号称有如下优点：支持高性能地把数据（主要是音频、视频）PUSH给Flash Player；支持over HTTP和HTTPS。再联想到最近1-2年，微软在Silverlight（详细介绍看“<a href="http://en.wikipedia.org/wiki/Silverlight" target="_blank" rel="nofollow">这里</a>”）上也是频频出击。而Sun也不甘寂寞，搞出了一个JavaFX（2个月前刚发布，详细介绍见“<a href="http://en.wikipedia.org/wiki/JavaFX" target="_blank" rel="nofollow">这里</a>”）。看来RIA领域的竞争有白热化的趋势。干脆今天就来八卦一下这三个技术。<!--program-think--><br />&#12288;&#12288;有同学可能会问了，为啥不顺便提一下AJAX捏？主要是因为AJAX和那三个玩意儿有很大的差别，不属于同一个维度，没有可比性（绝没有贬低AJAX的意思）。所以今天暂且抛开不谈（下次如果有空再聊AJAX）。<br /><br />&#12288;&#12288;★<b>先说说Flash/Flex</b><br />&#12288;&#12288;Flash/Flex早先是由Macromedia搞出来的。Adobe目光独到，在05年把Macromedia吞并了。于是Flash/Flex就成了Adobe的如意法宝。其实当初收购Macromedia的价格并不高，也就34亿美金。这个数字对微软来说是小意思，可惜当初微软真是瞎了眼，没有先下手。否则现在RIA市场的格局就是另外一番景象了。话说回来，Adobe买下Macromedia后，对Flash也是下了大本钱，再加上那几年没有直接的竞争对手。因此到了07年，Flash/Flex已经成为RIA市场的事实标准，当时的PC占有率少说也有70%。而且开始进入手机市场。<br />&#12288;&#12288;目前Flash/Flex主要的优势一个是用户群大，还有一个是跨平台（包括操作系统、浏览器、移动设备）。<br />&#12288;&#12288;不过我这2-3年用下来，感觉Flash/Flex也有不少问题。一个主要的问题是语言的兼容性不够好，当初从ActionScript2迁移到ActionScript3，团队里的人怨声载道（很多代码几乎要重写）。还有一个问题是功能不够强，让人感觉很不爽。比如至今不能够很好地支持多线程（仅支持异步回调）；比如不能很好地整合PDF（照理说都是自家公司产品，整合应该不难）。<br /><br />&#12288;&#12288;★<b>再说说Silverlight</b><br />&#12288;&#12288;估计是到了06年后，微软发觉苗头不对，赶紧下大力气自己搞。在07年底和08年底分别发布了Silverlight 1.0和Silverlight 2.0（3.0据说09年也有望推出）。然后商务层面也接连出手：先是08奥运期间与NBC（美国国家广播公司）合作，用Silverlight进行赛事直播；接着在上个月美国总统就职典礼，也用上了Silverlight。微软的意图非常明显，就是市场方面利用各种机会争夺用户占有率，弥补对Flash的劣势；技术方面不断强化功能，力图甩开Flex，吸引开发人员加入。<br />&#12288;&#12288;要说Silverlight的优点，我觉得依托于dotNET是主要优势。借着dotNET这个靠山，Silverlight能整合现有的某些语言（据说已能支持JScript、<a href="http://en.wikipedia.org/wiki/IronPython" target="_blank" rel="nofollow">IronPython</a>、<a href="http://en.wikipedia.org/wiki/IronRuby" target="_blank" rel="nofollow">IronRuby</a>、VB）和库；还能够方便原有的dotNET程序员上手。Silverlight在功能上也显得比Flex更强大（比如多线程和3D方面）。<br />&#12288;&#12288;不过依托于dotNET也导致了Silverlight的主要缺点：跨平台不够好。虽说现在有Moonlight的帮忙，但依然不够理想（尤其是对Linux的支持）。<br /><br />&#12288;&#12288;★<b>最后顺便提一下JavaFX</b><br />&#12288;&#12288;坦白讲，JavaFX实在是乏善可陈。Sun的一个主要失策就在于后知后觉，跟进太慢。微软下手已经慢了，结果Sun比它还慢。而Sun在财力上又比微软差了很多（Sun现在自身难保，根本没法像微软那样烧钱搞推广），做IDE也不如微软拿手。真是天时、地利、人和皆无。难怪连Java社区对它也热情不高（有Java大牛<a href="http://en.wikipedia.org/wiki/Bruce_Eckel" target="_blank" rel="nofollow">Bruce Eckel</a>的文章“<a href="http://www.artima.com/weblogs/viewpost.jsp?thread=234900" target="_blank" rel="nofollow">Does Anyone Really Care About Desktop Java?</a>”为证）。<br /><br />&#12288;&#12288;★<b>结论</b><br />&#12288;&#12288;假如你要开发一个Web系统，打算从上述三种RIA技术中挑选一个。那么你先要评估一下你的Web应用对跨平台的需求如何？如果你需要同时支持各种各样的客户端操作系统和浏览器，那强烈建议你选择Flex（我的部门现在面临的就是这种情况）；反之，如果你铁定<b>只要</b>支持Windows，或许也可以考虑Silverlight。至于说JavaFX，短期内就先不要考虑啦。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/02/ria-review-flash-silverlight-javafx.md">2009/02/ria-review-flash-silverlight-javafx.md</a>
</div>
</div>
</body>
</html>
