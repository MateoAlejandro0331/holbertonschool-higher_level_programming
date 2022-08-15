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