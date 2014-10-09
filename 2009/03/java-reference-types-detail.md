<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>Java新手进阶：细说引用类型 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">Java新手进阶：细说引用类型</a></h1>
<div class="post-info"><span class="date-header">2009-03-20</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.Java.md" class="tag">编程.Java</a> </div>
<hr>
<div class="post">
在前几天的帖子“<a href="../../2009/03/java-performance-tuning-1-two-types.md" target="_blank">Java性能优化[1]：基本类型 vs 引用类型</a>”里，大概介绍了引用类型和基本类型在存储上的区别。昨天有网友在评论中批评说“引用类型变量和它所引用的对象”没区分清楚，容易混淆。所以今天专门来说一下引用类型的相关细节。<!--program-think-->另外，也把<a href="../../2009/03/java-performance-tuning-1-two-types.md">原先的帖子</a>中，关于“两种类型的存储方式”这节修改了一下，加点插图，有助于大伙儿的理解。<br />　　其实，引用类型的变量非常类似于C/C++的指针。为了形象起见，也为了打字方便，本文后面的内容，都把“引用类型的变量”称为<b>指针</b>。所以，如果你原先有C/C++背景，今天讲的内容对你来说应该很好理解；否则的话，可能要多琢磨琢磨了。<br /><br /><h2>★创建问题</h2><br />　　假设我们在<b>函数中</b>写了如下这个简单的语句：<br /><font face="Courier New">StringBuffer str = new StringBuffer("Hello world");</font><br />别看这个语句简单，其实包含了如下三个步骤：<br />　　首先，<u><font face="Courier New">new StringBuffer("Hello world")</font></u>在<b>堆</b>里申请了一坨内存，把创建好的StringBuffer对象放进去。<br />　　其次，<u><font face="Courier New">StringBuffer str</font></u>声明了一个指针。这个指针本身是存储在<b>栈</b>上的（因为语句写在<b>函数中</b>），可以用来指向某个StringBuffer类型的对象。或者换一种说法，这个指针可以用来保存某个StringBuffer对象的地址。<br />　　最后，当中这个<b>等于号</b>（赋值符号）把两者关联起来，也就是把刚申请的那一坨内存的地址保存成str的值。<br />　　把<a href="../../2009/03/java-performance-tuning-1-two-types.md">上次帖子</a>的图片再拿出来秀一下：<br /><center><img src="../../images/2009/03/OgAAADfJvtKaB8finO0otLgLKBqGUQ2lYJGlzQAZCE1qUybiJ9XKK8TrbaBfFVYT1g5DbqIza3sKbsWm2MjeZM4mWoEA15jOjE1kRvoUZjXROWyVUiJ7dUWGWSBV" width="480" alt="不见图、请翻墙" /></center><br /><br /><h2>★引用对象之间的赋值、判相等</h2><br />　　通过上述的图解，大伙儿应该明白指针变量和该指针变量指向的<b>对象</b>是一个什么关系了吧。<br />　　还是接着刚才的例子，再来看赋值的问题。对于如下语句：<br />　　<font face="Courier New">StringBuffer str2 = str;</font><br />　　这个赋值语句是啥意思捏？实际上就是把str的地址复制给str2，记住，是地址的复制，StringBuffer对象本身并没有复制。所以两个指针指向的是同一个东东。<br />　　再搞一张示意图，如下（今天画这些图把我累坏了）：<br /><center><img src="../../images/2009/03/OgAAAFBhvdXRlvyvQDGIx1SIbKQN0SJeETiM6NSzPxyDPhxj7ogBnwnANh3FbZuzWEQPOGL2adM1l8nNYxbDd9ZdU9AA15jOjNeEMKZWr7_YDfanK_l5_FgAwQH2" width="480" alt="不见图、请翻墙" /></center><br /><br />　　明白了赋值，判断相等的问题（就是==操作符）也就简单了。当我们写如下语句“<font face="Courier New">if(str2 == str)</font>”时，只是判断两个指针的<b>值</b>（也就是对象的地址）是否相等，并不是判断<b>被指向的对象</b>是否内容相同。<br />　　实际上两个指针的值相同，则肯定是指向同一个对象（所以对象内容必定相同）。但是两个内容相同的对象，它们的地址可能不一样（比如克隆出来的多个对象之间，地址就不同）。<br /><br /><h2>★final常量的问题</h2><br />　　针对引用类型变量的final修饰符也是很多人搞混淆的地方。实际上final只是修饰指针的值（也就是限定指针保存的地址不能变）。至于该指针指向的对象，内容是否能变，那就管不着了。所以，对于如下语句：<br />　　<font face="Courier New">final StringBuffer strConst = new StringBuffer();</font><br />　　你可以修改它指向的对象的内容，比如：<br />　　<font face="Courier New">strConst.append(" ");</font><br />　　但是<b>不能</b>修改它的值，比如：<br />　　<font face="Courier New">strConst = null;</font><br /><br /><h2>★传参的问题</h2><br />　　引用类型（在函数调用中）的传参问题，是一个相当扯的问题。有些书上说是传值，有些书上说是传引用。搞得Java程序员都快成神经分裂了。所以，我们最后来谈一下“引用类型参数传递”的问题。<br />　　还是拿刚才的例子，假设现在要把刚才创建的那一坨字符串打印出来，我们会使用如下语句：<br /><font face="Courier New">System.out.println(str);</font><br />这个语句又是什么意思捏？这时候就两说了。<br />　　第一种理解：<br />可以认为传进函数的是str这个指针，指针说白了就是一个地址的值，说得再白一点，就是个整数。按照这种理解，就是传值的方式。也就是说，参数传递的是指针本身，所以是传值的。<br />　　第二种理解：<br />可以认为传进去的是StringBuffer对象，按照这种理解，就是传引用方式了。因为我们确实是把对象的地址（也就是引用）给传了进去。<br />　　费了这么多口水，其实不论是<b>传引用</b>还是<b>传值</b>，都可以讲得通，关键取决于你是<b>如何看待</b>参数所传递的<b>东西</b>。这就好比量子力学中“光的波粒二象性”，如果你以粒子的方式去测量它，它看起来像粒子；如果你以波动的方式去观测它，它看起来像波动。假如你不太懂量子力学，前面这话当我没说 <b>:-)</b><div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/03/java-reference-types-detail.md">2009/03/java-reference-types-detail.html</a>
</div>
</div>
</body>
</html>
