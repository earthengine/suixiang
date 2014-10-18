<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>书评：《C++ 101编程规范》 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">书评：《C++ 101编程规范》</a></h1>
<div class="post-info"><span class="date-header">2009-01-22</span><a href="../../tags/E7BC96E7A88B.C.md" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E4B9A6E8AF842FE5BDB1E8AF84.md" class="tag">书评/影评</a> </div>
<hr>
<div class="post">
今天是头一次聊C++的书，当然要选一本够分量又实用的书。俺想了一炷香的功夫，决定先拿《C++ Coding Standards: 101 Rules, Guidelines, and Best Practices 》开刀。<!--program-think--><br />　　上次俺在“<a href="../../2009/01/choose-it-book.md">如何选择IT技术书籍</a>”中已经介绍了几个鉴别好书的招数，现在可以验证一下。<br /><br />　　先说说此书的作者Herb Sutter和Andrei Alexandrescu。两位都是C++社区的大牛。其中Herb Sutter是标准委员会的主席（光看头衔就知道有多牛了）。Andrei Alexandrescu是《Modern C++ Design》的作者，大凡看过此书的人应该都会被他极具创新的C++模板用法所震惊。鉴于两位作者的分量，大伙儿可以想见该书一定不差。<br />　　然后看看出版时间是2004年，在C++98和C++03标准之后，因此肯定已经涵盖了C++语言新标准的东东。本书的出版社“Addison Wesley”也是国际知名。因此从“出版信息”看，这本书也符合要求。<br />　　再然后，看看目录。在本书之前，俺曾看过许多关于编码规范的书或者文章，但是都仅仅局限于语法层面。而这本书的出众之处在于用了很大的比重来介绍语法之外的条款（例如性能优化、类设计、STL库的使用）。由此看来，本书可以适合不同层次的C++开发人员，即使你是用C++写了多年程序的老手也会从中获益。<br /><br />　　啰嗦了一大堆好处（你估计看烦了），现在开始来具体介绍一下内容。全书的101个条款分布在如下的12部分中，下面来挨个介绍一下。（如果你已经通读过全书，后面内容你可以略过）<br /><br />　　1、组织与策略<br />　　这部分其实不是讲C++，而是更偏向于软件工程方面。如果你是一个部门或者团队的主管，要仔细思考一下：这些条款你的团队/部门是否都做到了？如果你是一个C++新手，可以先略过这部分。<br /><br />　　2、设计风格<br />　　这部分讲的是通用程序设计哲学，并不限于C++，而是适用于所有的编程语言。如果你对C++已经入门，但是想再上一个境界，本部分你必须好好领会。我估计有十年编程经验的老手也未必能够完全吃透该部分的所有条款。<br /><br />　　3、编码风格<br />　　终于开始说到C++语法了！本部分说得都是一些基本的东东，C++新手要好好看看这部分，老手倒未必了。<br /><br />　　4、函数与操作符（运算符）<br />　　如果你是从其它语言Java和C转到C++，可能对操作符重载还不适应，需要了解一下这部分。如果你原来是Python程序员，估计对操作符重载，应该会比较有亲切感。<br /><br />　　5、类设计和继承<br />　　最好你已经有了一定的OO理论功底，然后再来看这部分，效果会更好。<br /><br />　　6、构造、析构、拷贝<br />　　这部分读起来的难度不大。不过有几个几个细节需要注意（即使你已是熟手）。<br /><br />　　7、名空间和模块<br />　　如果你需要从事规模比较大的C++项目的开发，那么本部分一定要了解一下。比较大的项目一般都会涉及到逻辑分割（分名空间）和物力分割（分模块）。<br /><br />　　8、模板与范型<br />　　这部分适合已经比较熟悉C++的开发人员，新手可以先略过。<br /><br />　　9、错误处理与异常<br />　　错误和异常的处理，是编程领域公认的难点。头几条是关于原理性的条款（因此也适用于其它语言），需要深刻领会；后几条是关于C++语法，你如果对try-catch不熟悉的话要注意看看了（即使是2-3年开发经验的，也有许多不熟悉异常处理）。<br /><br />　　10、STL容器　11、STL算法<br />　　如果你是从其它语言（Java、C）转到C++，或者你原先只用MFC，那么估计你的STL会有欠缺，好好看看这两部分吧。<br /><br />　　12、类型安全<br />　　如果你是从C转到C++，这部分尤其要注意看一下。里面提到的几个条款都是和C的缺点有关（这么说，C fans看了可别动怒啊）。<br /><br />　　听完俺滴介绍，感觉怎么样？想去弄一本来看看吗？<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/01/cxx-coding-standards-101-rules.md">2009/01/cxx-coding-standards-101-rules.md</a>
</div>
</div>
</body>
</html>
