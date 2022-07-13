<h1 class="gap">0x0D. SQL - Introduction</h1>
<div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[]}" data-react-cache-id="tags/Tags-0">&nbsp;</div>
<ul id="project-metadata" class="list-group metadata">
<li class="list-group-item">&nbsp;By Guillaume</li>
<li class="list-group-item">&nbsp;Weight: 1</li>
<li class="list-group-item">&nbsp;Ongoing project - started&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:false,&quot;value&quot;:&quot;2022-07-12T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-07-12 00:00 (GMT-05:00)"><span class="datetime">Jul 12, 2022</span></span></div>
, must end by&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:false,&quot;value&quot;:&quot;2022-07-14T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-07-14 00:00 (GMT-05:00)"><span class="datetime">Jul 14, 2022</span></span></div>
&nbsp;- you're done with&nbsp;<span id="student_task_done_percentage">0</span>% of tasks.</li>
<li class="list-group-item">&nbsp;Checker was released at&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:true,&quot;value&quot;:&quot;2022-07-13T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-07-13 00:00 (GMT-05:00)"><span class="datetime">Jul 13, 2022 12:00 AM</span></span></div>
</li>
<li class="list-group-item">&nbsp;An auto review will be launched at the deadline</li>
</ul>
<div class="panel panel-default">
<div class="panel-heading">
<h3 class="panel-title">Concepts</h3>
</div>
<div class="panel-body">
<p><em>For this project, we expect you to look at this concept:</em></p>
<ul>
<li><a href="https://intranet.hbtn.io/concepts/556">Databases</a></li>
</ul>
</div>
</div>
<div id="project-description" class="panel panel-default">
<div class="panel-body">
<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg" alt="" /></p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="What is Database &amp; SQL?" href="https://intranet.hbtn.io/rltoken/khEqMKp1PHvKpfO18d4fLQ" target="_blank">What is Database &amp; SQL?</a></li>
<li><a title="A Basic MySQL Tutorial" href="https://intranet.hbtn.io/rltoken/kK_v6WRoj8aoZ1TbrYNuBQ" target="_blank">A Basic MySQL Tutorial</a></li>
<li><a title="Basic SQL statements: DDL and DML" href="https://intranet.hbtn.io/rltoken/ibCYnC9CDgZg5NQQvccBWw" target="_blank">Basic SQL statements: DDL and DML</a>&nbsp;(<em>no need to read the chapter &ldquo;Privileges&rdquo;</em>)</li>
<li><a title="Basic queries: SQL and RA" href="https://intranet.hbtn.io/rltoken/yelYhpf7l0FcRIPCVfnMLw" target="_blank">Basic queries: SQL and RA</a></li>
<li><a title="SQL technique: functions" href="https://intranet.hbtn.io/rltoken/3aQcovOE-clrD8yIfxFE9Q" target="_blank">SQL technique: functions</a></li>
<li><a title="SQL technique: subqueries" href="https://intranet.hbtn.io/rltoken/lTXnq6pdk59x2h_Y-q0-Hg" target="_blank">SQL technique: subqueries</a></li>
<li><a title="What makes the big difference between a backtick and an apostrophe?" href="https://intranet.hbtn.io/rltoken/R--kAkehyaawZFY4m1inxQ" target="_blank">What makes the big difference between a backtick and an apostrophe?</a></li>
<li><a title="MySQL Cheat Sheet" href="https://intranet.hbtn.io/rltoken/aGZu7ulJpbbKcDhcz49yrg" target="_blank">MySQL Cheat Sheet</a></li>
<li><a title="MySQL 8.0 SQL Statement Syntax" href="https://intranet.hbtn.io/rltoken/4n4nXLDHNPyViz2H0DTGUA" target="_blank">MySQL 8.0 SQL Statement Syntax</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/L7Bww_1KJOUrbES5YSLXbA" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What&rsquo;s a database</li>
<li>What&rsquo;s a relational database</li>
<li>What does SQL stand for</li>
<li>What&rsquo;s MySQL</li>
<li>How to create a database in MySQL</li>
<li>What does&nbsp;<code>DDL</code>&nbsp;and&nbsp;<code>DML</code>&nbsp;stand for</li>
<li>How to&nbsp;<code>CREATE</code>&nbsp;or&nbsp;<code>ALTER</code>&nbsp;a table</li>
<li>How to&nbsp;<code>SELECT</code>&nbsp;data from a table</li>
<li>How to&nbsp;<code>INSERT</code>,&nbsp;<code>UPDATE</code>&nbsp;or&nbsp;<code>DELETE</code>&nbsp;data</li>
<li>What are&nbsp;<code>subqueries</code></li>
<li>How to use MySQL functions</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be executed on Ubuntu 20.04 LTS using&nbsp;<code>MySQL 8.0</code>&nbsp;(version 8.0.25)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>,&nbsp;<code>WHERE</code>&hellip;)</li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
</ul>
<h2>More Info</h2>
<h3>Comments for your SQL file:</h3>
<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>
<h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>
<pre><code>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</code></pre>
<p>Connect to your MySQL server:</p>
<pre><code>$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt;
mysql&gt; quit
Bye
$
</code></pre>
<h3>Use &ldquo;container-on-demand&rdquo; to run MySQL</h3>
<p><strong>In the container, credentials are&nbsp;<code>root/root</code></strong></p>
<ul>
<li>Ask for container&nbsp;<code>Ubuntu 20.04</code></li>
<li>Connect via SSH</li>
<li>OR connect via the Web terminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>
<pre><code>$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
</code></pre>
<p><strong>In the container, credentials are&nbsp;<code>root/root</code></strong></p>
</div>
</div>