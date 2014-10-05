<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>如何选择开源项目 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.html" title="回到首页">如何选择开源项目</a></h1>
<div class="post-info"><span class="date-header">2009-02-13</span><a href="../../tags/E7BC96E7A88B.html" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.E5BC80E6BA90E9A1B9E79BAE.html" class="tag">编程.开源项目</a> </div>
<hr>
<div class="post">
近几年开源项目越发普及，很多商业软件都逐渐引入开源项目。由于我负责的产品线采用了不少开源项目（主要是C++、Java、Python），这几年就经常会碰到开源项目选型的问题（从几个具有类似功能的开源软件项目中进行抉择）。今天我就大概聊一下自己的几点看法，供大伙儿参考。<!--program-think--><br /><br /><h2>★License（授权协议）</h2><br />　　License是很多人容易忽略的一个问题，所以我们先来聊一下License的问题。因为公司里面开发的软件基本上都属于商业软件，根据开源协议和商业的冲突程度，可以分为三种：非常友好、不太友好、很敌对。下面分别介绍一下：<br />　　先说说“很敌对”的协议：GPL（详细解释请看“<a href="http://en.wikipedia.org/wiki/GNU_General_Public_License" target="_blank" rel="nofollow">这里</a>”）。GPL和商业软件是严重冲突的。通俗地说，如果某个软件产品使用了某个基于GPL协议的库，则这个产品必须也使用GPL协议发布（这就是大名鼎鼎的GPL传染性）。因此，一旦发现某个开源项目是遵从GPL协议的，即使功能再强再好用，也只好忍痛割爱了。在此郑重提醒大伙儿，<b>切莫</b>抱侥幸心理，偷偷使用。一旦被雪亮的群众眼睛所发现，不光害了自己的名节，公司的名节也不保。<br />　　由于GPL对于商业软件太不友好，估计当年很多开源库的作者怨声载道。GNU组织为了缓和一下矛盾，搞出了一个折衷的LGPL协议（详细解释看“<a href="http://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License" target="_blank" rel="nofollow">这里</a>”）。这个协议相对GPL来说，宽松了一些：商业软件在<b>不修改</b>代码的前提下，可以在产品中使用LGPL的开源库。所以LGPL属于商业“不太友好”的协议。<br />　　最后来说一下“非常友好”的协议，比较出名的有这几种：<a href="http://en.wikipedia.org/wiki/BSD_license" target="_blank" rel="nofollow">BSD</a>、<a href="http://en.wikipedia.org/wiki/Mozilla_Public_License" target="_blank" rel="nofollow">MPL（Mozilla）</a>、<a href="http://en.wikipedia.org/wiki/Apache_License" target="_blank" rel="nofollow">Apache</a>、<a href="http://en.wikipedia.org/wiki/MIT_License" target="_blank" rel="nofollow">MIT</a>。这些协议不但允许项目的使用者使用开源库，有些还允许对开源库进行修改并重新分发。因此用起来特别爽。上述这几个协议在细节上有些小差异，大伙儿可以去它们官网瞧一下。<br />　　另外，有些开源软件使用公共域授权（Public Domain，详细解释看“<a href="http://en.wikipedia.org/wiki/Public_domain" target="_blank" rel="nofollow">这里</a>”）。简单说，就是不作任何限制，软件的使用者可以为所欲为 :)<br />　　上面提到的几种协议都是知名协议。还有少数开源项目不是采用知名协议，而是自己搞了一套协议。如果你碰到这种情况，就得硬着头皮认真读一遍协议上的洋文，看看它对于使用者有些什么限制了。<br /><br /><h2>★技术层面的因素</h2><br />　　由于技术层面的考量和你所开发的软件密切相关，因此这方面的评判依据千差万别。我只能挑几个比较通用的说一下。<br />　　假如你开发的是跨平台的项目，那么你选择开源项目就得考虑它支持哪些平台（操作系统、数据库等）。如果你想支持的平台它不能支持，那就赶紧另找一个。<br />　　有时候编译器的支持也是考虑的指标之一。比如我在“<a href="../../2009/01/cxx-cross-platform-develop-0-overview.md">C++的可移植性和跨平台开发</a>”里面提到的老式编译器问题。再比如我曾经实施一个Java项目，用户的环境是JDK 1.4。那么有些用了Java 1.5新语法的开源库就不能使用。<br />　　假如你开发的软件是性能敏感的，那选型的时候就要测试一下几个候选项目的性能指标。<br />　　现在安全问题越来越严重。如果你比较在意安全性的话，还得顺便调查一下候选项目是否有安全问题（比如缓冲区溢出的bug、比如跨站脚本注入等）。<br /><br /><h2>★普及程度（用户的人气）</h2><br />　　所谓的普及程度，就是看开源项目的用户占有率。当然大伙儿不是搞市场调查的，花钱请市场调查公司也不现实。简单的办法就是用搜索引擎大致搜一下，就能看出几个候选项目使用的广泛度了。<br />　　还有另外一个判断普及程度的方式，就是看某个开源项目是否被知名的软件或者公司采用。比如Firefox（算是知名软件）采用Sqlite来存储页面缓存，这至少可以从侧面反映出Sqlite项目的优秀程度。<br />　　对于若干个候选项目，显然要优先考虑普及度高的那个。因为某个项目普及度高，至少说明（但不绝对）它比较成熟、稳定、安全。而且用的人多了之后，相应的文档也会多一些，碰到问题也容易找到人咨询。<br /><br /><h2>★活跃程度（开发的人气）</h2><br />　　这里说的"活跃"，是指开发层面。一般来说，一个项目越活越，则新功能的推出越快，对提交bug的响应也越快。有些项目，由于开发人员不再继续开发（可能开发人员厌倦了、可能开发人员太忙了），从而导致活跃度很低。<br />　　不过也有例外。有些项目由于已经非常完善了，因此反而活跃程度很低。我印象当中bzip2最近几年就很少有更新。<br /><br /><h2>★其它的风险</h2><br />　　最后来说说一些其它的风险。一般来说，只有当前几个因素都差不多的时候，才会来考虑其它风险。<br />　　有些项目过于依赖个人英雄主义，靠1-2个大牛完成整个项目。一旦大牛出现意外，导致整个项目受到严重影响。典型的例子就是ReiserFS文件系统的创始人Hans Reiser。这位老兄由于谋杀妻子的罪名成立，被判入狱15年（对IT八卦有兴趣的同学可以看“<a href="http://en.wikipedia.org/wiki/Hans_Reiser" target="_blank" rel="nofollow">这里</a>”）。导致ReiserFS项目受到严重影响。<br />　　还有些开源项目被商业公司收购后，由于种种原因（商业、管理、政治等）导致该开源项目受到不利影响。比如上星期听说Michael Widenius（MySQL共同创始人）和Marten Mickos（MySQL前CEO）从Sun离职。再加上去年10月走掉了的David Axmark（MySQL共同创始人）。估计对MySQL的影响不小。<br /><br />　　上述提到的几个考量指标，越前面的，权重越高。你在选型时需要综合考虑这几个因素。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/02/how-to-choose-opensource-project.md">2009/02/how-to-choose-opensource-project.html</a>
</div>
</div>
</body>
</html>
