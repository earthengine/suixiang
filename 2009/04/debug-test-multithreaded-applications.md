<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C++多线程调试和测试的注意事项 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.html" title="回到首页">C++多线程调试和测试的注意事项</a></h1>
<div class="post-info"><span class="date-header">2009-04-10</span><a href="../../tags/E7BC96E7A88B.C.html" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.html" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.E5A49AE7BABFE7A88B.html" class="tag">编程.多线程</a> </div>
<hr>
<div class="post">
　　在<a href="../../2009/04/cxx-cross-platform-develop-6-thread.html" target="_blank">上次的帖子</a>聊了C++多线程的跨平台问题，后来感觉意犹未尽。今天顺便说一下开发C++多线程应用程序时，有关调试和测试的一些注意事项。下面这些注意事项主要是针对C++，不过有些对于其它的语言也适用。<!--program-think--><br /> <br />　　★<b>关于设置断点和单步执行</b><br />　　很多同学非常依赖于调试器的断点功能和单步功能。这在单线程情况下倒还好（不过有些单线程但涉及GUI的程序，也会有点麻烦）。至于多线程程序的调试，这两种手段简直就是噩梦的开始。多线程造成的主要问题大都和竞态条件（Race Condition，详细解释看“<a href="http://en.wikipedia.org/wiki/Race_condition#Computing" target="_blank" rel="nofollow">这里</a>”）有关。而设置断点或单步跟踪可能会<b>严重干扰</b>多线程之间的竞争状态。导致你看到的是一个假象。比如本来有两个线程并发执行，存在某些不和谐的Bug（由竞态引起）。一旦你在某一个线程设置了断点，该线程在断点处停住了，只剩下另一个线程在跑。这时候，并发的场景已经完全被破坏了，你通过调试器看到的<b>可能</b>是一个和谐的场景。<br />　　稍微跑一下题。这很类似量子力学的“测不准原理”，观测者的观测行为干扰了被测量的客体，导致观测者看到的是一个干扰后的现象。<br /><br />　　★<b>关于Log输出</b><br />　　既然断点和单步不好用。那咋办捏？一个替代方案是输出log日志。它可以有效减轻断点和单步所导致的（针对竞态条件的）副作用。<br /><br />　　◇传统Log机制的问题<br />　　传统的log输出主要是打印到屏幕或者输出到文件。对于C++而言，标准库内置的类和函数（比如cout、printf、fputs）可能会有线程安全的问题（和编译器的具体实现有关）。尤其是标准流类库（iostream）的八个全局对象，更是要小心慎用。轻则输出的log文本混杂，重则导致程序崩溃。<br />　　鉴于上述原因，应该尽量使用第三方线程库内置的log机制来搞定log输出功能。比如ACE内置的ACE_Log_Msg等。<br /><br />　　◇Log函数要短小精悍<br />　　很多情况下，我们会包装一个公用的函数来实现log输出功能。然后在该函数内部调用线程库的log类/函数。为了不影响线程的竞态条件，这个log函数要尽可能简单轻便：不要涉及太多杂七杂八的琐事、千万别进行耗时的操作、尽量不操作一些全局的变量。<br /><br />　　◇Log的副作用<br />　　不过捏，即使log函数再短小精悍，也还是有可能影响竞态条件（毕竟log也有开销，也要消耗CPU时间）。<br />　　万一竞态条件受到log的影响，那就比较棘手了。我以前就碰到过这种情况：加了log，程序没有问题；去掉log，程序随机崩溃。这种情况一般有两种可能：要么是log功能本身有问题，要么是程序的竞态条件非常敏感（连log的开销都会有影响）。<br />　　这时候你能依靠的就只有肉眼和人脑了。先把相关的代码和文档仔细看上几遍（最好再找其他有经验的人一起Code Review），然后大家一起开动脑筋使劲琢磨。<br /><br />　　★<b>关于Debug版本和Release版本</b><br />　　C++程序经常有Debug版本和Release版本的区别。有些时候，这也会导致一些多线程的问题。<br />　　由于Debug版本包含了一些调试信息、启用了某些调试机制（比如assert宏）。所以就<b>可能</b>影响到多线程的竞争状态。在倒霉的时候，会碰上Debug版本工作正常，Release版本程序随机崩溃。要避免这种情况，可以考虑下面两个办法：<br /><br />　　◇放弃使用Debug版本<br />　　你可以干脆放弃使用Debug版本。在这种情况下，你需要考虑把诸如assert之类调试相关的宏替换成自己的一套宏，使得在非Debug版本下也可以生效。<br /><br />　　◇两种版本同步测试<br />　　使用此方法，程序员平时自测可以使用Debug版本，但是测试人员日常测试的必须是Release版本。具体的操作步骤可以利用每日构建来辅助进行（每日构建的介绍参见“<a href="../../2009/02/daily-build-0-overview.html" target="_blank">这里</a>”）。一定要避免：在平时仅仅搞Debug版本的测试，等到发布前夕再制作Release版本。这种做法是非常危险的！<br /> <br />　　★<b>关于测试的机器（硬件）</b><br />　　说一个亲身经历、印象深刻的事情。<br />　　当年用ACE开发跨平台程序的时候，公司内的的开发环境和测试环境都是单CPU的机器。因为当时多核的机器还没有面世，多CPU的机器又挺贵，公司没舍得花钱配置。<br />　　软件开发完之后，测试人员经过几轮回归测试，也没发现太大问题。但是拿到客户的环境中运行，却经常会随机性崩溃。因为不能在客户环境中Debug，自己的环境又死活没问题，开发组的几个人只好充分发挥肉眼和人脑的功能（盯着代码和设计文档猛想）。经过N长时间，差点把脑袋想破，最后才意识到客户的机器是多CPU的。然后赶紧从其它部门借了一台多CPU机器，装上软件调试，最后查出是一个第三方库有问题。此事过后，我立即想出各种法子，去申请了几台多CPU机器给测试人员用。<br />　　由于上述的前车之鉴，所以我强烈建议：如果是开发多线程的应用程序，尽量给<b>每一个</b>编程人员和测试人员都配置多核/多CPU的机器。毕竟现在多核机器已经很普及了，即使多CPU的机器，价格也还凑合。实在没必要为了省那点小钱而引入开发风险（不光会浪费开发/测试人员的时间，还可能增加实施和维护的成本）。<br />　　另外，可能有同学会问“超线程的机器如何捏？”关于<a href="http://en.wikipedia.org/wiki/Multiprocessing" target="_blank" rel="nofollow">多CPU</a>、<a href="http://en.wikipedia.org/wiki/Multi-core_(computing)" target="_blank" rel="nofollow">多核</a>、<a href="http://en.wikipedia.org/wiki/Hyper-threading" target="_blank" rel="nofollow">超线程</a>三者之间的差异，有兴趣的同学可以看“<a href="http://www.intel.com/cd/ids/developer/asmo-na/eng/200677.htm" target="_blank" rel="nofollow">这里</a>”。我个人感觉超线程不如多核与多CPU爽。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/04/debug-test-multithreaded-applications.md">2009/04/debug-test-multithreaded-applications.html</a>
</div>
</div>
</body>
</html>
