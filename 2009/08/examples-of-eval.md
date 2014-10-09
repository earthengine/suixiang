<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>再举几个动态语言eval手法的例子 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">再举几个动态语言eval手法的例子</a></h1>
<div class="post-info"><span class="date-header">2009-08-30</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.Python.md" class="tag">编程.Python</a> </div>
<hr>
<div class="post">
　　在前一个帖子“<a href="../../2009/08/why-choose-python-2-dynamic.md">什么俺推荐Python[2]</a>”里面，顺便提到了动态语言中常用的eval手法。当时为了给大伙儿加深印象，俺举了个数字运算的例子（详见“<a href="../../2009/08/why-choose-python-2-dynamic.md" target="_blank">原文</a>”）来说明eval的好处。<!--program-think--><br />　　后来有一个“很有才”的同学，在回复中提到说，可以用如下编译预处理语句来搞定：<br /><font face="Courier New">#define Foo(op, p1, p2)    (p1 op p2)</font><br />对此，俺颇不以为然。且不论用C/C++预处理语法来定义宏函数，有若干先天缺陷；单说用此方法来满足本例的需求，其<b>可扩展性</b>就很成问题。<br />　　俺估摸着：一来，上周的那个例子过于简单，未能充分show出 eval 的特长；二来，尚有一些同学没有体验到 eval 带来的强烈快感。所以，俺决定把 eval 的话题再发挥一下，再举几个例子来说事儿。事先声明：本文忽悠的eval技巧，大多数<a href="http://en.wikipedia.org/wiki/Dynamic_programming_language" target="_blank" rel="nofollow">动态语言</a>都能实现。考虑到俺相对熟悉Python，所以本文的例子都拿py代码来show。<br />  <br />　　★<b>示例１</b><br />　　先稍微扩展一下之前的例子，把两个数的某种运算扩展为多个数的某种运算。也就是说，给定某种运算类型（比如"*"表示乘法、"+"表示加法）以及若干个数，要求返回运算结果。<br />举例：<br />给定："+" 和 4、5、6，返回15。<br />给定："*" 和 2、3、4、5，返回120。<br />　　对于诸如C/C++/Java等非动态的语言，多半得定义具有两参数的函数：其中一个参数表示运算类型，另一个参数表示数组。至于函数实现，基本上还是那几招。要么通过switch来搞定——面向过程的路子；要么抽象出一个用于运算的接口类（纯虚类），然后针对每一种操作符去派生出不同的实现（比如加法类、乘法类）——也就是面向对象的路子。当然，想卖弄C/C++宏技巧的同学，或许也能用宏函数搞定，但代码会比原先复杂得多。<br />　　现在，来看看Python的 eval 函数，是如何满足该需求的。相比原先的2行代码，这次稍微复杂点，变为5行。思路还是和原来一样，先格式化一个运算表达式的字符串，然后把其它工作统统丢给eval搞定即可。<br /><br /><pre><font face="Courier New"><br />def Foo(sOperator, lstValues) :<br />    sExpr = "";<br />    for n in lstValues[1:] :    # 略过第一个元素<br />        sExpr += (sOperator + str(n));<br />    return eval(str(lstValues[0]) + sExpr);    # 补上第一个元素并求值<br /></font></pre><br /><br />调用的时候，只需写 print Foo("+", [2,3,4,5])，即可打印出14。<br /><br />　　★<b>示例２</b><br />　　在示例２中，我们继续把需求复杂化。假设要实现一个类似计算器的玩意儿，让用户在<b>运行时</b>输入一个四则运算表达式并计算结果。要求支持常见的四则运算符，要求支持运算符之间的优先级（也就是小括号）。这时候，假如你企图用静态语言自己来实现该功能（不依靠第三方的库），那你就要费老大老大的劲了。而用Python，代码反而比示例１还简单（一个 eval 语句搞定）。<br /> <br />　　★<b>示例３</b><br />　　看到这里，肯定有同学不服气了：你玩来玩去，都是在搞数值运算，有没有啥新花样啊？eval 手法当然不仅仅限于玩数字运算啦！下面就来说说 eval 如何运用于新的场合。<br />　　为了通俗易懂，俺就以邮件客户端为例（估计99.9%的同学都用过）。邮件客户端有一个常见的需求是：用户可以自行配置一些过滤规则，用来过滤一些垃圾邮件。<br />　　假设咱们要开发的是一个比较牛X的客户端，其过滤规则要足够强大：可以根据邮件的不同属性进行条件判定（需求人员要求支持的属性有：标题、正文、发件人、收件人、附件数）。为了体现该软件的牛X，需求人员要求：可以让用户设定各种灵活的嵌套逻辑组合。比如用户可以配置如下这条判定规则：<br /><br />如果（（标题包含"交友" AND （发件人来自"qq.com" OR 发件人来自"kaixin.com"）） OR 附件数大于10） 就认定为垃圾邮件<br /><br />　　当然，俺为了叙述方便，用了上面这种伪代码来阐述。真正的用户都是比较傻瓜的，咱肯定要提供一个足够傻瓜的界面来让用户配置过滤规则。<br />　　至于界面如何设计，不是本文的重点，略过不提。目前的关键问题是，如果要支持这种复杂的嵌套逻辑表达式，后台的过滤引擎要如何处理才好？估计有些同学已经看出来了，用静态语言来处理是很棘手滴——因为规则是由用户在运行时任意配置，逻辑嵌套的层次不定，邮件的属性在将来也很可能会扩展。<br />　　这时候，eval 手法又可以大放异彩了。如果用户配置了刚才那条过滤规则，那么界面模块只需要生成如下一个Python函数的源代码（说白了就是一个字符串）。<br /><pre><font face="Courier New"><br />def Filter(sTitle, sContent, sFrom, sTo, nAttachNum) :<br />    if (sTitle.find("交友")!=-1 and (sFrom.find("@qq.com")!=-1 or <br />sTo.find("@kaixin.com")!=-1)) or nAttacheNum&gt;10 :<br />        return True;<br />    else :<br />        return False;<br /></font></pre><br />　　后台模块可以先通过Python内置的exec函数，拿上述字符串创建出一个Filter函数。以后，每当收到一个邮件，只需把该邮件的各个属性传递给该Filter函数，即可完成垃圾邮件判定。<br />　　顺便说一下：喜欢ＯＯ风格的同学，可以把上述代码重构一下，加入一个Mail的类，把Filter作为Mail的一个方法；喜欢Pythonic风格的同学，也可以把上述代码改为更简洁的写法。<br /><br />　　★<b>总结</b><br />　　最后，来个总结发言。这种玩法的奥妙在于：那个传递给 eval / exec 的字符串，既可以看成是<b>数据</b>，也可以看成是可执行的<b>代码</b>。在动态语言的 eval 手法中，数据和代码得到了完美的结合。有了这种结合，你就获得了在运行时生成代码的能力。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/08/examples-of-eval.md">2009/08/examples-of-eval.html</a>
</div>
</div>
</body>
</html>
