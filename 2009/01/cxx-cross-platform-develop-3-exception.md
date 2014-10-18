<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C++的可移植性和跨平台开发[3]：异常处理 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">C++的可移植性和跨平台开发[3]：异常处理</a></h1>
<div class="post-info"><span class="date-header">2009-01-30</span><a href="../../tags/E7BC96E7A88B.C.md" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> </div>
<hr>
<div class="post">
　　上一个帖子“<a href="../../2009/01/cxx-cross-platform-develop-2-language.md">语法</a>”由于篇幅有限，没来得及聊异常，现在把和异常相关的部分单独拿出来说一下。<!--program-think--><br /><br />　　★<b>小心new分配内存失败</b><br />　　早期的老式编译器生成的代码，如果new失败会返回空指针。我当年用的Borland C++ 3.1似乎就是这样的，现在这种编译器应该不多见了。如果你目前用的编译器还有这种行为，那你就惨了。你可以考虑重载new操作符来抛出bad_alloc异常，便于进行异常处理。<br />　　稍微新式一点的编译器，就不是仅仅返回空指针了。当new操作符发现内存告急，按照标准的规定（参见C++ 03标准18.4.2章节），它应该去调用new_handler函数（原型为typedef void (*new_handler)();）。标准建议new_handler函数干如下三件事：1、设法去多搞点内存来；2、抛出bad_alloc异常；3、调用abort()或者exit()退出进程。由于new_handler函数是可以被重新设置的（通过调用set_new_handler），所以上述的行为它都可能有。<br />　　综上所述，new分配内存失败，有可能三种可能：1、返回空指针；2、抛出异常；3、进程立即终止。如果你希望你的代码具有较好的移植性，你就得把这三种情况都考虑到。<br /><br />　　★<b>慎用异常规格</b><br />　　异常规格在我看来不是一个好东西，不信可以去看看<a href="../../2009/01/cxx-coding-standards-101-rules.md">《C++ Coding Standards - 101 Rules, Guidelines &amp; Best Practices》</a>的第75条。（具体有哪些坏处以后专门开一个C++异常和错误处理的帖子来聊）言归正传，按照标准（参见03标准18.6.2章节），如果一个函数抛到外面的异常没有包含在该函数的异常规范中，那么应该调用unexcepted()。但是并非所有编译器生成的代码都遵守标准（比如某些版本的VC编译器）。如果你的需要支持的编译器在异常规范上的行为不一致，那就得考虑去掉异常规范声明。<br /><br />　　★<b>不要跨模块抛出异常</b><br />　　此处说的模块是指动态库。如果你的程序包含有多个动态库，不要把异常抛到模块的导出函数之外。毕竟现在C++还没有ABI标准（估计将来也未必会有），跨模块抛出异常会有很多不可预料的行为。<br /><br />　　★<b>不要使用结构化异常处理（SEH）</b><br />　　如果你从来没有听说过SEH，那就当我没说，跳过这段。如果你以前习惯于用SEH，在你打算写跨平台代码之前，要改掉这个习惯。包含有SEH的代码只能在Windows平台上编译通过，肯定无法跨平台的。<br /><br />　　★<b>关于catch(...)</b><br />　　照理说，catch(...)语句只能够捕获C++的异常类型，对于访问违例、除零错等非C++异常是无能为力的。但是某些情况下（比如某些VC编译器），诸如访问违例、除零错也可以被catch(...)捕获。所以，你如果希望代码移植性好，就不能在程序逻辑中依赖上述catch(...)的行为。<br /><br />　　下一个帖子，准备聊一下和“<a href="../../2009/01/cxx-cross-platform-develop-4-hardware.md">硬件有关的跨平台问题</a>”。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/01/cxx-cross-platform-develop-3-exception.md">2009/01/cxx-cross-platform-develop-3-exception.md</a>
</div>
</div>
</body>
</html>
