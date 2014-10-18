<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>Java新手的通病[4]：异常处理使用不当 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">Java新手的通病[4]：异常处理使用不当</a></h1>
<div class="post-info"><span class="date-header">2009-02-12</span><a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> <a href="../../tags/E7BC96E7A88B.Java.md" class="tag">编程.Java</a> </div>
<hr>
<div class="post">
　　上一个帖子讨论了“<a href="../../2009/02/defect-of-java-beginner-3-code-style.md">编程习惯的问题</a>”，今天来聊聊关于异常处理的话题。<!--program-think--><br /><br />　　★<b>空catch语句块</b><br />　　犯这种错误的人比较少，一般发生在刚学会Java或者刚参加工作不久的人身上。<br />　　所谓“空catch语句块”就是在catch语句块中没有对异常作任何log处理，导致异常信息被丢弃掉。一旦程序不能正确运行，由于查不到任何log信息，只好从头看代码，靠肉眼找bug。<br /><br />　　★<b>没有使用finally</b><br />　　很多人在catch语句之后不使用finally语句。由于在try语句中可能会涉及资源的申请和释放。如果在资源申请之后、资源释放之前抛出异常，就会发生资源泄露（资源泄露的严重性，<a href="../../2009/02/defect-of-java-beginner-3-code-style.md#gc">上一个帖子</a>已经聊过了）。<br /><br />　　★<b>笼统的catch语句块</b><br />　　有些人为了省事，只在自己模块的最外层代码包一个try语句块，然后catch(Exception)。不管捕获到什么异常，都作统一log了事。这种做法比“空catch语句块”稍好，但由于不能对具体的异常进行具体处理，对一些可恢复的异常（下面会提到），丧失了恢复的机会。而且也可能导致上述提到的资源泄露的问题。<br /><br />　　★<b>使用函数返回值进行错误处理</b><br />　　有些人放着Java的异常机制不用，而用函数返回值来表示成功/失败（比如返回true表示成功、返回false表示失败），简直是“捧着金碗要饭”。个人感觉，从C转到Java的人比较容易有此毛病。这种做法会导致如下几个问题：<br />　　返回值一般用整数值或布尔值表示，传递的信息过于简陋；<br />　　一旦调用者忽略了错误返回码，就会导致和“空catch语句块”类似的问题；<br />　　对同一个函数的多处调用，都需要对返回值进行重复判断，导致代码冗余（代码冗余的坏处，<a href="../../2009/02/defect-of-java-beginner-3-code-style.md#copy_and_paste">上一个帖子</a>也已经聊过了）。<br /><br />　　★<b>不清楚Checked Exception和Runtime Exception的区别</b><br />　　这个现象比较普遍，我发现很多2年以上Java工作经验的人尚未完全搞明白两者的区别。看来这个问题得详细说一下。<br />　　当初Java的设计者有意区分这两种异常，是别有深意的。其中“Checked Exception”用于表示可恢复的异常（也就是你必须检查的异常）；而“Runtime Exception”表示不可恢复的异常（也就是运行时异常，主要是程序bug和致命错误，你<b>不需要</b>检查）。不过这种做法引来了很多争议（包括很多Java大牛），鉴于本帖子主要针对新手，以后再专门来聊这个争议的话题。<br />　　为了便于理解，下面我举一个例子来说明。假设你要写一个Download函数，根据传入的URL（String参数）返回对应网页的内容文本。这时候有两种情况你需要处理：<br />　　1、如果传入的URL参数是null，这表明该函数的调用者出bug了，而程序本身的bug是很难在运行时自我恢复的。这时候Download函数必须抛出Runtime Exception。并且Download函数的调用者<b>不应该</b>尝试去处理这个异常，必须让它<b>尽早</b>暴露出来（比如让JVM自己终止运行）。<br />　　2、如果传入的URL参数非null，但是它包含的字符串不是一个合法的URL格式（可能由于用户输入错误导致）。这时候Download函数必须抛出Checked Exception。并且Download函数的调用者必须捕获该异常并进行相应的处理（比如提示用户重新输入URL）。<br /><br />　　上面就是几种常见的Java异常处理的误用。下一个帖子我们来聊一下“<a href="../../2009/05/defect-of-java-beginner-5-jvm.md">对虚拟机（JVM）了解不足</a>”。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/02/defect-of-java-beginner-4-exception.md">2009/02/defect-of-java-beginner-4-exception.md</a>
</div>
</div>
</body>
</html>
