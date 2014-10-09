<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb18030" />
<meta name="generator" content="Python script by program.think@gmail.com" />
<meta name="provider" content="program-think.blogspot.com" />
<link type="text/css" rel="stylesheet" href="../../css/program-think.css" />
<title>C++的可移植性和跨平台开发[2]：语法 - 编程随想的博客</title>
</head>
<body>
<div id="main" style="width:100%;">
<h1><a href="../../index.md" title="回到首页">C++的可移植性和跨平台开发[2]：语法</a></h1>
<div class="post-info"><span class="date-header">2009-01-28</span><a href="../../tags/E7BC96E7A88B.C.md" class="tag">编程.C</a> <a href="../../tags/E7BC96E7A88B.md" class="tag">编程</a> </div>
<hr>
<div class="post">
　　目前还有相当一部分开发人员在使用老式编译器干活，这些老式编译器可能对C++98支持不够。因此，当你的代码移植到这些老式的编译器上时，可能会碰到一些稀奇古怪的问题（包括编译出错和运行时错误）。下面这些注意事项有助于你绕过这些问题。<br />　　强调一下，后面提到的好几个条款都是通过回避C++的新语法来保证移植性。如果你用的是新式编译器，那么你可以不理会这些条款。<!--program-think--><br /><br />　　★<b>小心for循环变量的作用域（不支持新标准）</b><br />　　在C++98标准中，for循环变量的作用域局限在循环体内。而某些老的编译器（例如Visual C++ 6）认为for循环变量的作用域在循环体外。所以如下的代码可能导致移植问题。<pre><font face="Courier New"><br />{<br />  for(int i=0; i&lt;XX; i++)<br />  {<br />    // ...<br />  }<br /><br />  for(int i=0; i&lt;XXX; i++)<br />  {<br />    // ...<br />  }<br />}</font></pre>建议修改为不同的循环变量，如下所示：<pre><font face="Courier New"><br />{<br />  for(int i=0; i&lt;XX; i++)<br />  {<br />    // ...<br />  }<br /><br />  for(int j=0; j&lt;XXX; j++)<br />  {<br />    // ...<br />  }<br />}</font></pre><br />　　★<b>不要使用全局类对象，改用单键（标准未定义）</b><br />　　全局类对象的构造函数先于main()函数执行，如果某个模块中同时包含若干个全局类对象，则它们的构造函数的调用顺序是不确定的。而单键是在第一次调用时被初始化，能避免此问题。另外，单键虽然解决了构造问题，但是析构依然有隐患。详见“<a href="../../2009/02/cxx-object-destroy-with-process.md">C++ 对象是怎么死的？进程篇</a>”。<br /><br />　　★<b>保持inline函数尽量简单</b><br />　　不要在inline函数内部使用局部静态变量，不要在inline函数使用可变参数。这些都有可能导致移植问题。<br /><br />　　★<b>不要依赖函数参数的求值顺序（标准未定义）</b><br />　　标准没有明确规定函数参数的求值顺序。因此，如下的代码行为是不确定的。<font face="Courier New"><br />void Foo(int a, int b);<br />int n = 1;<br />foo(++n, ++n);<br /></font><br />　　★<b>慎用模板特化（不支持新标准）</b><br />　　有些<b>老式</b>编译器对偏特化或全特化支持不够。<br /><br />　　★<b>模板继承中，引用基类成员要小心（不支持新标准）</b><br />　　看如下例子：<pre><font face="Courier New"><br />template &lt;typename T&gt;<br />class TBase<br />{<br />protected:<br />  typedef std::vector&lt;T&gt; Container;<br />  Container m_container;<br />};<br /><br />template &lt;typename T&gt;<br />class TDerived : public TBase&lt;T&gt;<br />{<br />  typedef TBase&lt;T&gt; BaseClass;<br />public:<br />  void Func()<br />  {<br />    typename BaseClass::Container foo;    //可移植<br />    Container foo;  //不可移植<br />    this->m_container.clear(); //可移植<br />    m_container.clear(); //不可移植<br />  }<br />};</font></pre><br />　　★<b>慎用RTTI（不支持新标准、标准未定义）</b><br />　　先声明一下，我这里说的RTTI主要是指typeid操作符和type_info类型。<br />　　首先，由于某些老式编译器可能不支持typeid操作符和type_info类型，会导致移植性的问题，这是慎用RTTI的一个原因。（如果你用的是新式编译器，不用考虑这个因素）<br />　　其次，由于标准对于type_info类型的约束比较简单。这导致了不同的编译器对type_info的实现有较大差异。如果你确实要使用type_info类型，建议仅仅使用它的operator==和operator!=这两个成员函数。<br />　　所以，如果你确实需要在运行时确定类型，又不想碰到上述问题，可以考虑在自己的类体系中加入类型信息来实现。比如MFC和<a href="http://www.wxwidgets.org/" target="_blank" rel="nofollow">wxWidgets</a>都是这么干的。<br /><br />　　★<b>慎用嵌套类（不支持新标准）</b><br />　　如果在内部类访问外部类的非公有成员，要把内部类声明为外部类的friend。<br />如下代码存在移植问题。<pre><font face="Courier New"><br />class COuter<br />{<br />private:<br />  char* m_name;<br /><br />public:<br />  class CInner<br />  {<br />    void Print(COuter* outer)<br />    {<br />      cout &lt;&lt; outer-&gt;m_name;<br />    }<br />  };<br />};</font></pre>应该改为如下代码<pre><font face="Courier New"><br />class COuter<br />{<br />private:<br />  char* m_name;<br /><br />public:<br />  class CInner; //前置声明<br />  friend class CInner;<br /><br />  class CInner<br />  {<br />    void Print(COuter* outer)<br />    {<br />      cout &lt;&lt; outer-&gt;m_name;<br />    }<br />  };<br />};</font></pre><br />　　★<b>不要定义参数类型相近的函数（标准未定义）</b><br /><font face="Courier New"><br />void Foo(short n);<br />void Foo(long n);<br />Foo(0); //会导致二义性错误<br /></font><br />　　★<b>不要依赖标准类型的字长（标准未定义）</b><br />　　某些标准类型（例如int、wchar_t）的字长会随着具体的平台而改变。<br /><br />　　★<b>用枚举代替类的静态成员常量（不支持新标准）</b><br />　　某些<b>老式</b>的编译器不支持类的静态成员常量，可以用枚举来代替。<pre><font face="Courier New"><br />class CFoo<br />{<br />  static const int MIN = 0; //不可移植<br />  enum { MAX = 64 }; //可移植<br />};</font></pre><br />　　今天说了这么一大堆，都比较琐碎，估计会有遗漏的。日后如果大伙儿发现有补充的，欢迎在本帖的评论中指教一二。由于篇幅有限，我把和异常相关的内容留到<a href="../../2009/01/cxx-cross-platform-develop-3-exception.md">下一个话题</a>。<div class="blogger-post-footer">
</div>
<hr>
<div class="copyright">
<h4>版权声明</h4>
本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者<a href="mailto:program.think@gmail.com">编程随想</a>和本文原始网址：<br>
<a href="/2009/01/cxx-cross-platform-develop-2-language.md">2009/01/cxx-cross-platform-develop-2-language.html</a>
</div>
</div>
</body>
</html>
