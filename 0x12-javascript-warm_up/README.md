<h1 class="gap">0x12. JavaScript - Warm up</h1>
<h2>Background Context</h2>
<p>JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:</p>
<ul>
<li>Scripting (same as we did with Python)</li>
<li>Web front-end</li>
</ul>
<p>For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.</p>
<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg" alt="" /></p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Writing JavaScript Code" href="https://intranet.hbtn.io/rltoken/OdMLtl6Y9mpQkaoEqJCRSg" target="_blank">Writing JavaScript Code</a></li>
<li><a title="Variables" href="https://intranet.hbtn.io/rltoken/iE6zaLw7pybp648IfRmk5Q" target="_blank">Variables</a></li>
<li><a title="Data Types" href="https://intranet.hbtn.io/rltoken/4td1BbZAYn4Dldi6k0CY7A" target="_blank">Data Types</a></li>
<li><a title="Operators" href="https://intranet.hbtn.io/rltoken/OdMLtl6Y9mpQkaoEqJCRSg" target="_blank">Operators</a></li>
<li><a title="Operator Precedence" href="https://intranet.hbtn.io/rltoken/ALCoiVRvxmsjdqCUdWC_lg" target="_blank">Operator Precedence</a></li>
<li><a title="Controlling Program Flow" href="https://intranet.hbtn.io/rltoken/Nlfhdy6Thyu_WgtBSqoAUw" target="_blank">Controlling Program Flow</a></li>
<li><a title="Functions" href="https://intranet.hbtn.io/rltoken/Ta66PZ6_16K3q99oELvjkQ" target="_blank">Functions</a></li>
<li><a title="Objects and Arrays" href="https://intranet.hbtn.io/rltoken/osu583B5jskDVwmcm50-NQ" target="_blank">Objects and Arrays</a></li>
<li><a title="Intrinsic Objects" href="https://intranet.hbtn.io/rltoken/osu583B5jskDVwmcm50-NQ" target="_blank">Intrinsic Objects</a></li>
<li><a title="Module patterns" href="https://intranet.hbtn.io/rltoken/mduSK-WOoRe6WohU1p2zZQ" target="_blank">Module patterns</a></li>
<li><a title="var, let and const" href="https://intranet.hbtn.io/rltoken/kNWuHjyUvjr74wU2hBqd_A" target="_blank">var, let and const</a></li>
<li><a title="JavaScript Tutorial" href="https://intranet.hbtn.io/rltoken/qkp1hdLiI8DJje88bxcL6w" target="_blank">JavaScript Tutorial</a></li>
<li><a title="Modern JS" href="https://intranet.hbtn.io/rltoken/ieSajamJQ-Nv3XzcS_d5lA" target="_blank">Modern JS</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/kr1GDINhryJdjBSzQxCv0w" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>Why JavaScript programming is amazing</li>
<li>How to run a JavaScript script</li>
<li>How to create variables and constants</li>
<li>What are differences between&nbsp;<code>var</code>,&nbsp;<code>const</code>&nbsp;and&nbsp;<code>let</code></li>
<li>What are all the data types available in JavaScript</li>
<li>How to use the&nbsp;<code>if</code>,&nbsp;<code>if ... else</code>&nbsp;statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use&nbsp;<code>while</code>&nbsp;and&nbsp;<code>for</code>&nbsp;loops</li>
<li>How to use&nbsp;<code>break</code>&nbsp;and&nbsp;<code>continue</code>&nbsp;statements</li>
<li>What is a function and how do you use functions</li>
<li>What does a function that does not use any&nbsp;<code>return</code>&nbsp;statement return</li>
<li>Scope of variables</li>
<li>What are the arithmetic operators and how to use them</li>
<li>How to manipulate dictionary</li>
<li>How to import a file</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS using&nbsp;<code>node</code>&nbsp;(version 14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/node</code></li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be&nbsp;<code>semistandard</code>&nbsp;compliant (version 16.x.x).&nbsp;<a title="Rules of Standard" href="https://intranet.hbtn.io/rltoken/EK3q1S4Ouo08kTMI42cSig" target="_blank">Rules of Standard</a>&nbsp;+&nbsp;<a title="semicolons on top" href="https://intranet.hbtn.io/rltoken/FuXjfOYe18hUXCDoyMxBSg" target="_blank">semicolons on top</a>. Also as reference:&nbsp;<a title="AirBnB style" href="https://intranet.hbtn.io/rltoken/iIDdBVB4HNhPpb_5e5L-Qg" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
</ul>
<h2>More Info</h2>
<h3>Install Node 14</h3>
<pre><code>$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>
<h3>Install semi-standard</h3>
<p><a title="Documentation" href="https://intranet.hbtn.io/rltoken/FuXjfOYe18hUXCDoyMxBSg" target="_blank">Documentation</a></p>
<pre><code>$ sudo npm install semistandard --global</code></pre>
<h2 class="gap">Tasks</h2>
<div id="task-num-0" data-role="task1757" data-position="1">
<div id="task-1757" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">0. First constant, first print</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1757" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that prints &ldquo;JavaScript is amazing&rdquo;:</p>
<ul>
<li>You must create a constant variable called&nbsp;<code>myVar</code>&nbsp;with the value &ldquo;JavaScript is amazing&rdquo;</li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>0-javascript_is_amazing.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1757">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1757" data-batch-id="235" data-toggle="modal" data-target="#task-1757-users-done-modal">Help</button>&nbsp;<button id="task-num-0-check-code-btn" class="btn btn-default btn-sm" data-task-id="1757" data-toggle="modal" data-target="#task-test-correction-1757-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1757" data-toggle="modal" data-target="#task-qa-review-1757-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-1" data-role="task1758" data-position="2">
<div id="task-1758" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">1. 3 languages</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1758" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that prints 3 lines:</p>
<ul>
<li>The first line: &ldquo;C is fun&rdquo;</li>
<li>The second line: &ldquo;Python is cool&rdquo;</li>
<li>The third line: &ldquo;JavaScript is amazing&rdquo;</li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>1-multi_languages.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1758">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1758" data-batch-id="235" data-toggle="modal" data-target="#task-1758-users-done-modal">Help</button>&nbsp;<button id="task-num-1-check-code-btn" class="btn btn-default btn-sm" data-task-id="1758" data-toggle="modal" data-target="#task-test-correction-1758-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1758" data-toggle="modal" data-target="#task-qa-review-1758-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-2" data-role="task1759" data-position="3">
<div id="task-1759" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">2. Arguments</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1759" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that prints a message depending of the number of arguments passed:</p>
<ul>
<li>If no arguments are passed to the script, print &ldquo;No argument&rdquo;</li>
<li>If only one argument is passed to the script, print &ldquo;Argument found&rdquo;</li>
<li>Otherwise, print &ldquo;Arguments found&rdquo;</li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
</ul>
<p>Reference:&nbsp;<a title="process.argv" href="https://intranet.hbtn.io/rltoken/E5x0rMmgii1g_Da9R7DUag" target="_blank">process.argv</a></p>
<pre><code>guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>2-arguments.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1759">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1759" data-batch-id="235" data-toggle="modal" data-target="#task-1759-users-done-modal">Help</button>&nbsp;<button id="task-num-2-check-code-btn" class="btn btn-default btn-sm" data-task-id="1759" data-toggle="modal" data-target="#task-test-correction-1759-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1759" data-toggle="modal" data-target="#task-qa-review-1759-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-3" data-role="task1760" data-position="4">
<div id="task-1760" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">3. Value of my argument</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1760" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that prints the first argument passed to it:</p>
<ul>
<li>If no arguments are passed to the script, print &ldquo;No argument&rdquo;</li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
<li>You are not allowed to use&nbsp;<code>length</code></li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>3-value_argument.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1760">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1760" data-batch-id="235" data-toggle="modal" data-target="#task-1760-users-done-modal">Help</button>&nbsp;<button id="task-num-3-check-code-btn" class="btn btn-default btn-sm" data-task-id="1760" data-toggle="modal" data-target="#task-test-correction-1760-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1760" data-toggle="modal" data-target="#task-qa-review-1760-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-4" data-role="task1761" data-position="5">
<div id="task-1761" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">4. Create a sentence</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1761" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that prints two arguments passed to it, in the following format: &ldquo;&nbsp;is&nbsp;&rdquo;</p>
<ul>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>4-concat.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1761">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1761" data-batch-id="235" data-toggle="modal" data-target="#task-1761-users-done-modal">Help</button>&nbsp;<button id="task-num-4-check-code-btn" class="btn btn-default btn-sm" data-task-id="1761" data-toggle="modal" data-target="#task-test-correction-1761-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1761" data-toggle="modal" data-target="#task-qa-review-1761-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-5" data-role="task1762" data-position="6">
<div id="task-1762" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">5. An Integer</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1762" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that prints&nbsp;<code>My number: &lt;first argument converted in integer&gt;</code>&nbsp;if the first argument can be converted to an integer:</p>
<ul>
<li>If the argument can&rsquo;t be converted to an integer, print &ldquo;Not a number&rdquo;</li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
<li>You are not allowed to use&nbsp;<code>try/catch</code></li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>5-to_integer.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1762">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1762" data-batch-id="235" data-toggle="modal" data-target="#task-1762-users-done-modal">Help</button>&nbsp;<button id="task-num-5-check-code-btn" class="btn btn-default btn-sm" data-task-id="1762" data-toggle="modal" data-target="#task-test-correction-1762-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1762" data-toggle="modal" data-target="#task-qa-review-1762-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-6" data-role="task1763" data-position="7">
<div id="task-1763" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">6. Loop to languages</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1763" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that prints 3 lines: (like&nbsp;<code>1-multi_languages.js</code>) but by using an array of string and a loop</p>
<ul>
<li>The first line: &ldquo;C is fun&rdquo;</li>
<li>The second line: &ldquo;Python is cool&rdquo;</li>
<li>The third line: &ldquo;JavaScript is amazing&rdquo;</li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
<li>You are not allowed to use any&nbsp;<code>if/else</code>&nbsp;statement</li>
<li>You can use only one&nbsp;<code>console.log</code></li>
<li>You must use a loop (<code>while</code>,&nbsp;<code>for</code>, etc.)</li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>6-multi_languages_loop.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1763">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1763" data-batch-id="235" data-toggle="modal" data-target="#task-1763-users-done-modal">Help</button>&nbsp;<button id="task-num-6-check-code-btn" class="btn btn-default btn-sm" data-task-id="1763" data-toggle="modal" data-target="#task-test-correction-1763-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1763" data-toggle="modal" data-target="#task-qa-review-1763-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-7" data-role="task1764" data-position="8">
<div id="task-1764" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">7. I love C</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1764" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that prints&nbsp;<code>x</code>&nbsp;times &ldquo;C is fun&rdquo;</p>
<ul>
<li>Where&nbsp;<code>x</code>&nbsp;is the first argument of the script</li>
<li>If the first argument can&rsquo;t be converted to an integer, print &ldquo;Missing number of occurrences&rdquo;</li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
<li>You can use only two&nbsp;<code>console.log</code></li>
<li>You must use a loop (<code>while</code>,&nbsp;<code>for</code>, etc.)</li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>7-multi_c.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1764">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1764" data-batch-id="235" data-toggle="modal" data-target="#task-1764-users-done-modal">Help</button>&nbsp;<button id="task-num-7-check-code-btn" class="btn btn-default btn-sm" data-task-id="1764" data-toggle="modal" data-target="#task-test-correction-1764-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1764" data-toggle="modal" data-target="#task-qa-review-1764-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-8" data-role="task1765" data-position="9">
<div id="task-1765" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">8. Square</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1765" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that prints a square</p>
<ul>
<li>The first argument is the size of the square</li>
<li>If the first argument can&rsquo;t be converted to an integer, print &ldquo;Missing size&rdquo;</li>
<li>You must use the character&nbsp;<code>X</code>&nbsp;to print the square</li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
<li>You must use a loop (<code>while</code>,&nbsp;<code>for</code>, etc.)</li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js School
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>8-square.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1765">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1765" data-batch-id="235" data-toggle="modal" data-target="#task-1765-users-done-modal">Help</button>&nbsp;<button id="task-num-8-check-code-btn" class="btn btn-default btn-sm" data-task-id="1765" data-toggle="modal" data-target="#task-test-correction-1765-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1765" data-toggle="modal" data-target="#task-qa-review-1765-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-9" data-role="task1766" data-position="10">
<div id="task-1766" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">9. Add</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1766" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that prints the addition of 2 integers</p>
<ul>
<li>The first argument is the first integer</li>
<li>The second argument is the second integer</li>
<li>You have to define a function with this prototype:&nbsp;<code>function add(a, b)</code></li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>9-add.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1766">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1766" data-batch-id="235" data-toggle="modal" data-target="#task-1766-users-done-modal">Help</button>&nbsp;<button id="task-num-9-check-code-btn" class="btn btn-default btn-sm" data-task-id="1766" data-toggle="modal" data-target="#task-test-correction-1766-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1766" data-toggle="modal" data-target="#task-qa-review-1766-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-10" data-role="task1767" data-position="11">
<div id="task-1767" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">10. Factorial</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1767" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that computes and prints a factorial</p>
<ul>
<li>The first argument is integer (argument can be cast as integer) used for computing the factorial</li>
<li>Factorial of&nbsp;<code>NaN</code>&nbsp;is&nbsp;<code>1</code></li>
<li>You must do it recursively</li>
<li>You must use a function</li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>10-factorial.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1767">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1767" data-batch-id="235" data-toggle="modal" data-target="#task-1767-users-done-modal">Help</button>&nbsp;<button id="task-num-10-check-code-btn" class="btn btn-default btn-sm" data-task-id="1767" data-toggle="modal" data-target="#task-test-correction-1767-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1767" data-toggle="modal" data-target="#task-qa-review-1767-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-11" data-role="task1768" data-position="12">
<div id="task-1768" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">11. Second biggest!</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1768" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a script that searches the second biggest integer in the list of arguments.</p>
<ul>
<li>You can assume all arguments can be converted to integer</li>
<li>If no argument passed, print&nbsp;<code>0</code></li>
<li>If the number of arguments is 1, print&nbsp;<code>0</code></li>
<li>You must use&nbsp;<code>console.log(...)</code>&nbsp;to print all output</li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>11-second_biggest.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1768">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1768" data-batch-id="235" data-toggle="modal" data-target="#task-1768-users-done-modal">Help</button>&nbsp;<button id="task-num-11-check-code-btn" class="btn btn-default btn-sm" data-task-id="1768" data-toggle="modal" data-target="#task-test-correction-1768-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1768" data-toggle="modal" data-target="#task-qa-review-1768-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-12" data-role="task1769" data-position="13">
<div id="task-1769" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">12. Object</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1769" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Update this script to replace the value&nbsp;<code>12</code>&nbsp;with&nbsp;<code>89</code>:</p>
<ul>
<li>You are not allowed to use&nbsp;<code>var</code></li>
</ul>
<pre><code>guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>12-object.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1769">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1769" data-batch-id="235" data-toggle="modal" data-target="#task-1769-users-done-modal">Help</button>&nbsp;<button id="task-num-12-check-code-btn" class="btn btn-default btn-sm" data-task-id="1769" data-toggle="modal" data-target="#task-test-correction-1769-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;<button class="btn btn-default btn-sm" data-task-id="1769" data-toggle="modal" data-target="#task-qa-review-1769-modal">QA Review</button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-13" data-role="task1770" data-position="14">
<div id="task-1770" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">13. Add file</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<div class="task_progress_score_bar" data-task-id="1770" data-correction-id="375981">
<div class="task_progress_bar">&nbsp;</div>
<div class="task_progress_score_text">Score:&nbsp;<span class="task_score_value">100.00%</span>&nbsp;(<span class="task_progress_value">Checks completed: 100.00%</span>)</div>
</div>
<p>Write a function that returns the addition of 2 integers.</p>
<ul>
<li>The function must be visible from outside</li>
<li>The name of the function must be&nbsp;<code>add</code></li>
<li>You are not allowed to use&nbsp;<code>var</code></li>
</ul>
<p><a title="Tip" href="https://intranet.hbtn.io/rltoken/M3uMoMlngAtefSYF1c7PNQ" target="_blank">Tip</a></p>
<pre><code>guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x12-javascript-warm_up</code></li>
<li>File:&nbsp;<code>13-add.js</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm yes" data-task-id="1770">&nbsp;Done<span class="yes">!</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1770" data-batch-id="235" data-toggle="modal" data-target="#task-1770-users-done-modal">Help</button>&nbsp;<button id="task-num-13-check-code-btn" class="btn btn-default btn-sm" data-task-id="1770" data-toggle="modal" data-target="#task-test-correction-1770-correction-modal">Check your code</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button>&nbsp;</div>
</div>
</div>
</div>
</div>