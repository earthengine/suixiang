
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>学习技术的三部曲：WHAT、HOW、WHY - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">学习技术的三部曲：WHAT、HOW、WHY</a></h1>
<div class="post-info"><span class="date-header">2009-02-19</span><a href="../../tags/E5ADA6E4B9A0E696B9E6B395.md" class="tag">学习方法</a> </div>
<hr>
<div class="post">
最近几天有些网友在邮件里面问我关于学习的问题。有好几个人觉得工作了几年，也学会了不少的类库、框架、甚至语言，但是感觉自己的能力没有太大的提高。因此今天来说一下我个人对这方面的体会，希望对大伙儿（尤其是新手）有帮助。<br />先声明一下，本帖子讨论的三部曲是指你已经选定了某个技术方向之后，该如何学习；至于如何选定技术方向，则属于另一个话题，不在今天的讨论之列。<!--program-think--><br />我把学习归类为三个步骤：What、How、Why。经过我对周围同事和朋友的观察，大部分感觉自己技术没有提高的人，都仅仅停留在What阶段。下面我把这三个步骤解释一下。<br /><br /><h2>★第一步：WHAT</h2><br />“<b>WHAT</b>”也就是“What is it?”——这是最简单的层次。在这个层次，你要搞清楚某个东东是<b>什么</b>样子的？有<b>什么</b>用？有<b>什么</b>功能特性？有<b>什么</b>语法？......<br />举例如下：<br />对于学习语言（比如C++、Java、Python），大部分人都能够掌握基本的语法和标准库，然后用它写一些小程序（诸如二分查找、冒泡排序、简单文件操作等）。<br />对于学习类库（比如JDBC类库），大部分Java程序员都能明白JDBC主要包含哪些类，也能够用JDBC进行简单的数据库查询和增删改操作。<br />由于这个步骤是最基本的，假如你连这都做不到（可能你的理解力不够好），也别在IT界混了。<br />但是光会What是不够的。仅仅停留在这个步骤，导致了很多程序员<b>只知其然，不知其所以然</b>。这就是目前大部分开发人员的现状。<br /><br /><h2>★第二步：HOW</h2><br />所谓的“<b>HOW</b>”就是“How to do?”。在这个层次，你要搞清楚某个东西，其内部是<b>如何</b>运作的？<b>如何</b>实现的？......<br />举例如下：<br />假如你在学习C++语言，你是否搞明白函数传参数的实现机制？虚函数是如何实现？抛出异常时的栈回退是怎么回事？......<br />假如你在学习Java语言，你是否搞清楚GC如何实现？反射是如何实现？......<br />假如你在学习JDBC库，你是否清楚JDBC Driver的4种类型？不同游标类型的实现机制？事务的机制？......<br />在这个阶段，你必须多想想类似这些问题。然后通过各种途径（参见“<a href="../../2009/01/2.md">关于自学能力</a>”的几个方法），把问题彻底搞清楚。自然而然，你的提高就会比较明显。而且如果碰到一些深层次的问题（比如性能优化），也就知道该如何去解决。<br />完成这个阶段之后，你基本上就属于该技术领域最优秀的20%的人（根据<a href="../../2009/02/80-20-principle-0-overview.md">二八原理</a>，80%的人不会去思考HOW的问题）。<br /><br /><h2>★第三步：WHY</h2><br />一般来说，只有想清楚HOW之后，才能继续去考虑WHY。<br />所谓的“<b>WHY</b>”，就是搞清楚某个东西<b>为什么</b>设计成这样？<b>为什么</b>不是另外的样子？这样的设计有什么讲究？......<br />说实在的，善于问“<b>为什么</b>”有一定的天赋成分？好像某个科学大牛曾经说过“提出问题有时候比解决问题更难”。一般来说，只有当你<b>深刻</b>理解了某个东西，才能够针对这个东东的<b>设计</b>问出一些问题。所以，我前面强调过，要先把HOW的问题搞清楚，再来考虑WHY的问题。<br />举例如下：<br />对于C++语言：为什么C++没有类似Java的finally关键字？为什么C++当初没有考虑GC？......<br />对于Java语言：为什么Java没有类似C++的类析构函数？为什么Java要同时提供String和StringBuffer两个似乎冗余的类？......<br />对于Python语言：为什么Python不提供类似C++/Java的访问控制机制？......<br />如果你能够<b>自己</b>问出诸如上述的“为什么”问题，并且能够通过各种途径找到解答，那你基本上已经吃透这个技术了，并且你已经<b>有可能</b>自己去<b>设计</b>一个类似的玩意儿了。到这时，你已经踏上了通向技术高手的康庄大道。<br /><br />由于本博客偏重IT方面，所以今天举的这些例子多半都是IT相关的，但是这个三部曲在IT之外的行业和领域，其实也能适用。如何举一反三，就看各位的悟性了。<br /><br /><b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br /><a href="../../2012/03/think-what-how-why.md">用提问来促进思维——再谈 WHAT HOW WHY 三部曲</a><br /><a href="../../2013/09/knowledge-structure.md">如何完善自己的知识结构</a><br /><a href="../../2009/07/book-review-are-your-lights-on.md">书评：《你的灯亮着吗？——找到问题的真正所在》</a><br /><a href="../../2010/07/silent-proof.md">思维的误区：忽视沉默的大多数</a><br /><a href="../../2009/02/from-surface-to-essence.md" target="_blank">学会透过现象看本质，即使现象有时候挺诡异</a><div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/02/study-technology-in-three-steps.md">2009/02/study-technology-in-three-steps.md</a>
</div>
</div>
</body>
</html>
