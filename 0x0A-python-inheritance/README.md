<h1 class="gap">0x0A. Python - Inheritance</h1>
<div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[]}" data-react-cache-id="tags/Tags-0">&nbsp;</div>
<ul id="project-metadata" class="list-group metadata">
<li class="list-group-item">&nbsp;By Guillaume</li>
<li class="list-group-item">&nbsp;Weight: 1</li>
<li class="list-group-item">&nbsp;Ongoing project - started&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:false,&quot;value&quot;:&quot;2022-06-07T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-06-07 00:00 (GMT-05:00)"><span class="datetime">Jun 7, 2022</span></span></div>
, must end by&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:false,&quot;value&quot;:&quot;2022-06-08T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-06-08 00:00 (GMT-05:00)"><span class="datetime">Jun 8, 2022</span></span></div>
&nbsp;- you're done with&nbsp;<span id="student_task_done_percentage">0</span>% of tasks.</li>
<li class="list-group-item">&nbsp;Checker will be released at&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:true,&quot;value&quot;:&quot;2022-06-07T18:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-06-07 18:00 (GMT-05:00)"><span class="datetime">Jun 7, 2022 6:00 PM</span></span></div>
</li>
<li class="list-group-item">&nbsp;An auto review will be launched at the deadline</li>
</ul>
<div id="project-description" class="panel panel-default">
<div class="panel-body">
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Inheritance" href="https://intranet.hbtn.io/rltoken/99aGWGmLu8zsaiiJg7HCYQ" target="_blank">Inheritance</a></li>
<li><a title="Multiple inheritance" href="https://intranet.hbtn.io/rltoken/ozYK1JSbEU4U6BqTggCjSA" target="_blank">Multiple inheritance</a></li>
<li><a title="Inheritance in Python" href="https://intranet.hbtn.io/rltoken/iq146hXJLxru-ycAeUOCHQ" target="_blank">Inheritance in Python</a></li>
<li><a title="Learn to Program 10 : Inheritance Magic Methods" href="https://intranet.hbtn.io/rltoken/F8LUzmvPI4yur1Z37ZM1fQ" target="_blank">Learn to Program 10 : Inheritance Magic Methods</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/3SOprDVZKpDNFQeEMQIyAQ" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>Why Python programming is awesome</li>
<li>What is a superclass, baseclass or parentclass</li>
<li>What is a subclass</li>
<li>How to list all attributes and methods of a class or instance</li>
<li>When can an instance have new attributes</li>
<li>How to inherit class from another</li>
<li>How to define a class with multiple base classes</li>
<li>What is the default class every class inherit from</li>
<li>How to override a method or attribute inherited from the base class</li>
<li>Which attributes or methods are available by heritage to subclasses</li>
<li>What is the purpose of inheritance</li>
<li>What are, when and how to use&nbsp;<code>isinstance</code>,&nbsp;<code>issubclass</code>,&nbsp;<code>type</code>&nbsp;and&nbsp;<code>super</code>&nbsp;built-in functions</li>
</ul>
<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version&nbsp;<code>2.8.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
</ul>
<h3>Python Test Cases</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder&nbsp;<code>tests</code></li>
<li>All your test files should be text files (extension:&nbsp;<code>.txt</code>)</li>
<li>All your tests should be executed by using this command:&nbsp;<code>python3 -m doctest ./tests/*</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code>&nbsp;and&nbsp;<code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>
<h3>Documentation</h3>
<ul>
<li>Do not use the works&nbsp;<code>import</code>&nbsp;or&nbsp;<code>from</code>&nbsp;inside your comments, the checker will think you try to import some modules</li>
</ul>
</div>
</div>
<div id="project-quiz-questions-title" class="panel panel-default">
<div class="panel-heading">
<h3 class="panel-title">Quiz questions</h3>
</div>
<div class="panel-body">
<div class="alert alert-info"><strong>Great!</strong>&nbsp;You've completed the quiz successfully! Keep going!&nbsp;<span id="quiz_questions_collapse_toggle">(Show quiz)</span></div>
</div>
</div>
<h2 class="gap">Tasks</h2>
<div id="task-num-0" data-role="task1292" data-position="1">
<div id="task-1292" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">0. Lookup</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<p>Write a function that returns the list of available attributes and methods of an object:</p>
<ul>
<li>Prototype:&nbsp;<code>def lookup(obj):</code></li>
<li>Returns a&nbsp;<code>list</code>&nbsp;object</li>
<li>You are not allowed to import any module</li>
</ul>
<pre><code>guillaume@ubuntu:~/0x0A$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

guillaume@ubuntu:~/0x0A$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
guillaume@ubuntu:~/0x0A$ 
</code></pre>
<p><strong>No test cases needed</strong></p>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x0A-python-inheritance</code></li>
<li>File:&nbsp;<code>0-lookup.py</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm no" data-task-id="1292">&nbsp;Done<span class="no pending">?</span></button>&nbsp;<button class="users_done_for_task btn btn-default btn-sm" data-task-id="1292" data-project-id="254" data-toggle="modal" data-target="#task-1292-users-done-modal">Help</button>&nbsp;</div>
</div>
</div>
</div>
</div>