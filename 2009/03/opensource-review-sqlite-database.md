
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>开源点评：SQLite数据库扫盲 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">开源点评：SQLite数据库扫盲</a></h1>
<div class="post-info"><span class="date-header">2009-03-13</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.E5BC80E6BA90E9A1B9E79BAE.md" class="tag">编程.开源项目</a> </div>
<hr>
<div class="post">
今天注意到<a href="http://www.sqlite.org/" target="_blank" rel="nofollow">SQLite</a> 3.6.11（上个月发布的）增加了一个我期待已久的<a href="http://www.sqlite.org/backup.md" target="_blank" rel="nofollow">online backup</a>接口，激动之余就顺便和大伙儿聊一下SQLite数据库。本帖权当是SQLite扫盲，如果你对SQLite已经很熟悉，本文就不必再看了。另外，假如你想了解SQLite在软件项目中的具体应用，可以看“<a href="../../2009/04/how-to-use-sqlite.md" target="_blank">这里</a>”。<!--program-think--><br /><br /><h2>★技术上的优点和特性</h2><br />　　SQLite是一个轻量级、跨平台的关系型数据库。既然号称关系型数据库，支持SQL92标准中常用的玩意儿（比如视图、事务、触发器等）就是理所当然的了，咱今天就不细说了。今天主要聊聊一些有点特色的玩意儿。<br /><br /><h3>◇轻量级</h3><br />　　先说它的第一个特色：轻量级。想必SQLite的作者很看重这个特性，连它的Logo都是用的“羽毛”，来显摆它的轻飘飘。<br />　　SQLite和C/S模式的数据库软件不同，它是进程内的数据库引擎，因此不存在数据库的客户端和服务器。使用SQLite一般只需要带上它的一个动态库，就可以享受它的全部功能。而且那个动态库的尺寸也挺小，以版本3.6.11为例，Windows下487KB、Linux下347KB。<br /><br /><h3>◇绿色软件</h3><br />　　SQLite的另外一个特点是绿色：它的核心引擎本身不依赖第三方的软件，使用它也不需要“安装”。所以在部署的时候能够省去不少麻烦。<br /><br /><h3>◇单一文件</h3><br />　　所谓的“单一文件”，就是数据库中所有的信息（比如表、视图、触发器、等）都包含在一个文件内。这个文件可以copy到其它目录或其它机器上，也照用不误。<br /><br /><h3>◇跨平台/可移植性</h3><br />　　如果光支持主流操作系统，那就没啥好吹嘘的了。除了主流操作系统，SQLite还支持了很多冷门的操作系统。我个人比较感兴趣的是它对很多嵌入式系统（比如Android、Windows Mobile、Symbin、Palm、VxWorks等）的支持。<br /><br /><h3>◇内存数据库（in-memory database）</h3><br />　　这年头，内存越来越便宜，很多普通PC都开始以GB为单位来衡量内存（服务器就更甭提了）。这时候，SQLite的内存数据库特性就越发显得好用。<br />　　SQLite的API不区分当前操作的数据库是在内存还是在文件（对于存储介质是透明的）。所以如果你觉得DISK I/O有可能成为瓶颈的话，可以考虑切换为内存方式。切换的时候，操作SQLite的代码基本不用大改，只要在开始时把文件从磁盘Load到内存，结束时把内存的数据库Dump回文件就OK了。在这种情况下，前面提到的“<a href="http://www.sqlite.org/backup.md" target="_blank" rel="nofollow">online backup API</a>”就派上用场了，聪明的同学应该明白我为啥这么期待backup功能了吧？<br /><br /><h2>★技术上的缺点和不足</h2><br />　　前面光聊了特性和优点，为了避免枪手写软文的嫌疑，再来说说SQLite的一些缺点。列位看官将来如果想用它，这些缺点要权衡一下。<br /><br /><h3>◇并发访问的锁机制</h3><br />　　SQLite在并发（包括多进程和多线程）读写方面的性能一直不太理想。它使用文件锁的方式，整个数据库可能会被写操作独占，从而导致其它读写操作阻塞或出错。这导致了严重的并发瓶颈。<br /><br /><h3>◇SQL标准支持不全</h3><br />　　在它的<a href="http://www.sqlite.org/omitted.md" target="_blank" rel="nofollow">官方网站</a>上，具体列举了不支持哪些SQL92标准。我个人感觉比较不爽的是不支持外键约束。<br /><br /><h3>◇网络文件系统（以下简称NFS）</h3><br />　　有时候需要访问其它机器上的SQLite数据库文件，就会把数据库文件放置到网络共享目录上。这时候你就要小心了。当SQLite文件放置于NFS时，在并发读写的情况下可能会出问题（比如数据损坏）。原因据说是由于某些NFS的文件锁实现上有Bug。<br /><br /><h2>★编程语言接口</h2><br />　　SQLite支持很多种语言的编程接口。这对于我这种喜欢混用多种编程语言的人来说，是很爽的。下面我大概介绍一下。<br /><br /><h3>◇C/C++</h3><br />　　由于SQLite本身是C写的，它<a href="http://www.sqlite.org/cintro.md" target="_blank" rel="nofollow">自带的API</a>也是C接口的。所以C/C++用起来最直接了。假如你不喜欢面向过程的C API风格，可以另外找个C++的包装库。想重新发明轮子的同学，也可以自己包装一个。<br /><br /><h3>◇Java</h3><br />　　如果要用Java访问SQLite，可以通过SQLite的JDBC驱动，或者通过专门的SQLite包装库。我个人建议走JDBC方式，万一将来要换数据库，代码就不用大改。<br /><br /><h3>◇Python</h3><br />　　<a href="http://www.pysqlite.org/" target="_blank" rel="nofollow">pysqlite</a>是Python操作SQLite的首选。从Python 2.5开始，它已经被整合到Python的标准库中。看来Python社区还是蛮喜欢SQLite嘛。<br /><br /><h3>◇dotNet</h3><br />　　对于喜欢dotNet的同学，可以通过SQLite的<a href="http://sqlite.phxsoftware.com/" target="_blank" rel="nofollow">ADO.NET</a>驱动来访问。<br /><br /><h3>◇Ruby</h3><br />　　Ruby可以通过<a href="http://rubyforge.org/projects/sqlite-ruby/" target="_blank" rel="nofollow">SQLite-Ruby</a>操作SQLite数据库，不过我没用过。<br /><br /><h3>◇Perl</h3><br />　　在CPAN上有<a href="http://search.cpan.org/search%3fmodule=DBD::SQLite" target="_blank" rel="nofollow">DBD::SQLite</a>，不过我也没用过。<br /><br /><h2>★一些非技术的参考因素</h2><br />　　前面讲的都是技术层面的话题，如果你考虑在公司的商业软件项目中使用SQLite。还需要根据“<a href="../../2009/02/how-to-choose-opensource-project.md" target="_blank">如何选择开源项目</a>”里面提到的几个参考因素，再评估一下。<br /><br /><h3>◇授权协议（License）</h3><br />　　SQLite使用的是<a href="http://en.wikipedia.org/wiki/Public_domain" target="_blank" rel="nofollow">Public Domain</a>协议，这是最爽一种，可以放心大胆地用。<br /><br /><h3>◇用户的普及程度</h3><br />　　最近这几年，使用SQLite的人越来越多（从“<a href="http://www.google.com/trends?q=sqlite" target="_blank" rel="nofollow">这里</a>”可以反应出来）。包括一些大公司也开始把它整合到产品中（比如Google的Gears、Apple的Safari、Adobe的AIR）。这说明它的健壮性、稳定性等方面<b>不会</b>有太大问题。<br /><br /><h3>◇开发的活跃程度</h3><br />　　如果到SQLite的<a href="http://www.sqlite.org/changes.md" target="_blank" rel="nofollow">Change Log</a>上大致了解一下，可以看出最近5年基本上每1-2个月都会有更新。说明开发的活跃度还是非常高的。<br />　　从上述几个<b>非技术</b>因素来看，SQLite用于商业公司的软件项目还是非常靠谱的。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/03/opensource-review-sqlite-database.md">2009/03/opensource-review-sqlite-database.md</a>
</div>
</div>
</body>
</html>
