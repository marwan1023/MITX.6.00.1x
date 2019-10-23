Wiki of All Things 6.00.1x
❗️ Source ❗️

This is the Wiki myself and fellow students built in a previous course. You are welcome to contribute any resources you think are relevant. -NotAlien

It's now reformatted, contains a FAQ and has an automatic TOC. ;) -rkoe

Table of contents:

FAQ
Turing's Halting Problem
Lectures
Week 1
Week 1 - Lecture 1
Week 1 - Lecture 2
Week 2
Week 2 - Lecture 3
Week 2 - Lecture 4
Week 3
Week 3 - Lecture 5
Week 3 - Lecture 6
Week 3 - Problem Set 3 - Radiation Exposure
Week 4
Week 4 - Lecture 7
Week 4 - Lecture 8
Week 5
Week 5 - Lecture 9
Week 5 - Lecture 10
Week 6
Week 6 - Lecture 11
Week 6 - Lecture 12
Week 7
Week 7 - Lecture 13
Interesting and Useful Links
Online books, tutorials and reading materials
Other useful links.
FAQ
Frequently asked questions: A hopefully growing list of frequently asked questions and answers.
Turing's Halting Problem
Wikipedia Link
An article on the Scientific American on the Halting Problem
Interesting question on the topic from Stack Exchange site
Lectures
(useful resources for every lecture)

The resources should be in the order they are covered in the lecture. Includes material both for the absolute beginner struggling with the new topics and for the experienced programmer seeking new insights.

Week 1
Week 1 - Lecture 1
Instructions per second - Wikipedia

"Instructions per second (IPS) is a measure of a computer's processor speed... The term is commonly used in association with a numeric value such as thousand instructions per second (kIPS), million instructions per second (MIPS), Giga instructions per second (GIPS), or million operations per second (MOPS)."

How computers work: computation - Youtube - Youtube video explaining some topics covered in the lecture.

The history of digital storage - Interesting infographic illustrating the evolution of digital storage.

Is there a perfect algorithm for chess? - StackOverflow - Insightful discussion.

What is cryptography? - A basic explanation of cryptography and a more advanced explanation why some encryption is too hard to crack.

Impossible programs - Not so basic explanation of the impossible program.

Declarative and imperative knowledge - "The contrast between function and procedure is a reflection of the general distinction between describing properties of things and describing how to do things, or, as it is sometimes referred to, the distinction between declarative knowledge and imperative knowledge." (-SICP)

Methods of computing square roots - Wikipedia

Real proper custard - Custard recipe.

The baby: the world's first stored-program computer

A learning model of simple computing machine architecture - Scientific article about basic machine architecture.

Alan turing six primitives:

"Right: Move the Machine's head to the right of the current square"
"Left: Move the Machine's head to the left of the current square"
"Print: Print a symbol on the current square"
"Scan: Identify any symbols on the current square"
"Erase: Erase any symbols presented o the current square"
"Nothing: Do nothing"
What is a turing machine?

"A Turing machine is an idealised computing device consisting of a read/write head (or 'scanner') with a paper tape passing through it. The tape is divided into squares, each square bearing a single symbol--'0' or '1', for example. This tape is the machine's general purpose storage medium, serving both as the vehicle for input and output and as a working memory for storing the results of intermediate steps of the computation."

Turing machines explained - Turing Machines are the basis of modern computing, but what actually is a Turing Machine? Assistant Professor Mark Jago explains.

Semantics - For a deeper understanding of the term.

In terms of programming, what do semantics mean? - StackOverflow - Easy to understand explanation of syntax, semantics, and static semantic defenitions.

Defensive programming - Advanced article about defensive programming in software development process.

"Approximate timing for various operations on a typical PC" Taken from Teach Yourself Programming in Ten Years

execute typical instruction	1/1,000,000,000 sec = 1 nanosec
fetch from L1 cache memory	0.5 nanosec
branch misprediction	5 nanosec
fetch from L2 cache memory	7 nanosec
Mutex lock/unlock	25 nanosec
fetch from main memory	100 nanosec
send 2K bytes over 1Gbps network	20,000 nanosec
read 1MB sequentially from memory	250,000 nanosec
fetch from new disk location (seek)	8,000,000 nanosec
read 1MB sequentially from disk	20,000,000 nanosec
send packet US to Europe and back	150 milliseconds = 150,000,000 nanosec
Week 1 - Lecture 2
Levels of programming languages - Easy and short explanation of the subject. However, some of it may be misleading.

High level vs. low level languages - Long discussion with different directions.

Compiled and interpreted languages - Youtube - Short explanation video.

Differences between compiled and interpreted languages - Detailed article with various examples and language comparisons.

Shell - "Sometimes called command shell, a shell is the command processor interface. The command processor is the program that executes operating system commands. The shell, therefore, is the part of the command processor that accepts commands. After verifying that the commands are valid, the shell sends them to another part of the command processor to be executed." Taken from Wedopedia

Command-line interpreter - Explanation of the term including shell.

Picking an Interpreter - Simple and easy to understand article about different interpreters for Python. (I believe canopy uses CPython but I can be wrong).

Modular arithmetic - Video explaining the modulo concept. It can a challenging idea to understand at first, but it holds great power.

Order of evaluation - Table lists the order of operation (precedence rules) for Python operators. Including advanced topics that will be helpfull later in the course.

Python strings - A guide to using strings in python. Contains advanced material that may be usefull later in the course.

Asking questions - Beginner guide for using raw_input and some good Q&A in the comment section.

Efficient string concatenation in Python - Very in depth analysis of different methods for string concatenation. Might be useful very late in the course.

How to properly comment your code - MIT's quick guide for commenting code.

Coding without comments - Advanced discussion on commenting more useful for experienced programmers.

Indenting code - Simple beginner friendly guide.

Readablity is critical for programing. You will write it only once, and read it MANY times. Some languages(C, Perl) have "conventions" that are most often ignored in the breach as it were. Others like Go pretty much reformat your code to enforce conventions. Python has Pep8, the mostly official stylie guide. It might be a bit more advanced, and might be a big confusing to beginners. I would use what you understand, and keep what you don't understand tucked away in the back of your midn for when you do. See especially A Foolish Consistency is the Hobgoblin and Naming Conventions.

If statements - Starting with basic explanation and examples and progress to very complicated scripts.

Semantic and Syntax Errors - Good guide on differentiating between semantic errors and syntax errors.

Week 2
Week 2 - Lecture 3
Iteration - Comprehensive guide for iteration in Python with examples.

Iteration - source 2 - Another guide to complement the first one.

The guess and check pattern - Youtube - Video explaining this concept.

Bisection method - Wikipedia - Broad explanation.

While statements - In depth guide for the while statements. Good for the beginner and for the experienced programmer.

How to stop an infinite loop - (now that we learned the while loop...) Try CTRL + C If it doesn't work, CTRL + C + ENTER or CTRL + Pause/Break.

Loop with a Decrementing Counter - Little bit of explanation of decrementing function.

Exhaustive enumeration - Explanation.

Python loops - Clear representation of the concept and further reading links for the "for loop" and other loop related information.

Why can't decimal numbers be represented exactly in binary? - StackOverflow - Discussion on the subject. May help understanding the problem.

Helpful video explaining floating point numbers. Quick and engaging video on the topic by Tom Scott.

The Newton-Raphson method - Already the Babylonians knew how to approximate square roots, so you should, too.

Week 2 - Lecture 4
What does abstraction mean in programming? - StackOverflow - Very good explanation in the context of python, too.

Defining functions of your own - In depth explanation with examples. Understanding how to define a function is very important for later in this course and in programming in general.

Python fundamentals tutorial : functional programming - Very advanced explanation on different functions and how to use them. Useful only for the experienced programmers and can confuse beginners.

Python and pointers - Another advanced material. Can confuse beginners and aimed at the experienced programmers.

Naming and binding - You can find here information about local binding and naming in general.

A beginner's guide to python's namespaces, scope resolution, and the LEGB rule - Good overview of scopes in Python.

Improve your python: understanding unit testing - Article about testing your functions, written in a beginner friendly way thought covers topics we still didn't learn in the course.

What is the standard python docstring format? - StackOverflow - Discussion with good answers on how to write good function specification.

Modules - In depth guide to modules in python, how to import files and how to use functions from them.

Not a lot of resources but every one of those (not the advanced links) are important to understand and will make it easier to progress with the course. -NotAlien

Week 3
Week 3 - Lecture 5
Google search recursion - Notice the suggested word google gives you :-)

Recursive functions - Explanations with examples in Python.

Recursion or iteration? - StackOverflow - Great discussion talking about the difference between the two.

Iterative vs. recursive approaches - Comparison with examples.

Base case in a recursive method - StackOverflow - Explanation on the recursive case, what is the right way to end recursion.

Mathematical induction - Basic explanation if you didn't get it in the lecture.

Zero factorial - Numberphile - YouTube - Interesting video about the factorial concept, not related to the course but still interesting.

Tower of Hanoi - Short overview of the tower of Henoi.

Fibonacci numbers and nature - Good explanation of the topic and interesting examples from life.

What is the use of �assert� in Python? - StackOverflow - Plain and simple, very good discussion about assert in Python.

I don't understand dot notation - Good explanation (though covers material we didn't learn) of this very important topic.

Global and local variables - Thorough comparison and explanation.

Can every recursion be converted into iteration? - StackOverflow - 2 questions covers the comparison between iteration and recursion.

Can all iterative algorithms be expressed recursively? - StackOverflow - 2 questions covers the comparison between iteration and recursion.

Problem Solving with Algorithms and Data Structures Using Python - a more visual explanation of recursion

Week 3 - Lecture 6
Python Tuple - Very good and beginner friendly explanation of the tuple and all of its properties.

Are there more ways to define a tuple with only one item? - StackOverflow - Different ways of making a singleton (tuple of one item).

An introduction to Python lists - Good overview of lists and what you can do with them in Python.

Immutable vs mutable types - Python - StackOverflow - Discussion with some good answers explaining what is mutable or not mutable in python.

Python: aliases - Explanations and some interesting code to run by yourself.

List Aliasing Conundrum - StackOverflow - Some important points about aliasing, I think this topic can confuse students so the more explanations the better.

Facts and Myths about Names and Values - A clear, in-depth presentation on names, values, assignment and mutability.

How do I copy an object in Python? - Short yet useful article about copying.

Understanding the Map function. python - StackOverflow - Map is very useful and important function in python and understanding it will help a lot.

Python Dictionary - Good and short overview of dictionaries and their functionality.

Dictionary - python for beginners - More farther reading on dictionaries.

Dictionaries - Yet another thorough explanation of the dictionary, recommended.

Week 3 - Problem Set 3 - Radiation Exposure
Understanding calculating Area Under a Curve - A gentle elabortion on the concept of integration.
Week 4
Week 4 - Lecture 7
Testing your code - Very good explanation of the topic using python as an example.

Python debugging tips - StackOverflow - Big discussion with tons of different tips, very recommended for all the level of knowledge.

Documentation, testing, and debugging - Compact overview of those topics.

Black box testing - Basic and easy to understand explanation.

White box testing (aka glass box testing) - Similar to the one above, basic and clear.

What is regression testing? - What is it, why we need it and how we can use it.

How to investigate intermittent problems - Different techniques and concepts.

Defensive programming - Explanation with examples in Python.

Rubber duck debugging - YouTube - Best kind of debugging.

Rubber Duck Debugging - Yep.

Week 4 - Lecture 8
Exception handling - Wikipedia - Overview of the whole subject.

How to use �raise� keyword in Python - StackOverflow - Little bit of explanation on raise and lots of examples and farther readings.

Try/Except in Python: How do you properly ignore exceptions? - StackOverflow - Another stack discussion with good answers and more resources to read.

Try and except in Python - Contains the list of different errors.

Returns values from a for loop in python - StackOverflow - That's something new concept and that explanation might help understanding it. (return [something for something in somethings]). See also "list comprehensions", below.

List comprehensions. While not yet officially presented in the course, they were used during the lecture ( getSubjectStats function: return [ element for element in list ] ). The python documentation for them is here

Python exceptions handling - Exception handling explained.

Using assertions effectively - Explanation and examples.

Short list for short lecture.

Week 5
Week 5 - Lecture 9
Computational complexity theory - Wikipedia - A wiki in depth article covering this topic.

A random-access machine - RAM - Short explanation for this basic but important topic.

Measuring Complexity - Overview of different complexity algorithms and ways to measure it.

Big-O cheat sheet - Interesting sheet with a small explanation on big-O notation and examples for most popular algorithms.

Examples of algorithms which has O(1), O(n log n) and O(log n) complexities - StackOverflow - Small discussion with examples for different algorithm classes.

Software complexity and Big-O notation - Something with more examples for all

Complexity of Python Operations - Explanations and examples of different complexity classes regarding python basic operations.

Are there any O(1/n) algorithms? - StackOverflow - Very interesting discussion.

Big O, how do you calculate/approximate it? - StackOverflow - Good discussion to close up the topic of approximating an algorithm complexity.

Plain English explanation of Big O - StackOverflow - Discussion containing comparison between different cases of algorithm complexity.

Week 5 - Lecture 10
Software complexity: how do we bring order to chaos? - The only decent piece of information on that topic I found.

How indirection can affect the behaviour of your code - A practical example of what indirection is and why you need to understand it.

Searching- linear and binary search - Very good and long explanation on binary and linear search.

What is amortized analysis of algorithms? - StackOverflow - Basic and simple explanation of what amortizing analysis is.

Amortized analysis - Very in depth explanation of the topic.

Why is binary search,which needs sorted data, considered better than linear search? - StackOverflow - Discussion answering why and when is sorting and searching better then simple linear search.

The Selection Sort - Explanation and visual representation of the sort.

The Merge Sort - Same site as above with good explanation and visualizition.

Sorting, searching and algorithm analysis - Good article to sum up all the material above, with examples and exercises.

What different sorting algorithms sound like - YouTube - Interesting visual and audio representation of different sort algorithms, recomended.

Barack Obama - Computer science question - YouTube - Obama's opinion on sort algorithms (bubble sort is similar to selection sort and is considered the least effective sort).

Week 6
Week 6 - Lecture 11
Python built-in data types - A reminder of the data types built in python.

Lists - linked list - Explanation and implementation of this concept using python, very informative.

What is a �method� in Python? - StackOverflow - Discussion with some short and simple answers.

Object-oriented programming (OOP) definition - Short and simple definition.

Why is Object-Oriented Programming Useful? - In depth explanation with an example from a game.

Classes - good overview from the official Python documentation.

Python init and self what do they do? - StackOverflow - If you got trouble understanding the strange init method this will help.

What is the origin of foo and bar? - StackOverflow - For the curious.

Python: difference between class and instance attributes - StackOverflow - Important difference to know and remember.

Improve your Python: Python classes and object oriented programming - Good summery of this topic.

A guide to Python's magic methods - "underscore underscore methods" very informative and helpful guide for efficient programming in python.

Abstraction Functions, Rep Invariants, and Equality - Article covering representation invariants.

Week 6 - Lecture 12
Everything Is an Object - Compact explanation of objects in Python with further reading material.

Python Types and Objects - In depth overview of those important components of Python.

Python class attributes: an overly thorough guide - Another good and thorough guide on class attributes.

Python: lt() - explanation for the lt method.

An introduction to classes and inheritance - Thorough article about inheritance and classes.

How to detect whether a Python variable is a function? - StackOverflow - Simple explanation and an example of this method.

Inheritance and substitution - Good and thorough chapter from a book about inheritance.

What is the Liskov substitution principle? - StackOverflow - Insightful discussion with some important concepts and ideas.

Python join, why is it string.join(list) instead of list.join(string)? - StackOverflow - Look at different answers for full understanding of the join method.

Structuring Your Project - Article about abstraction.

Why does python not have a mechanism for data hiding? - There are some good answers in this discussion.

What does the yield keyword do in Python? - StackOverflow - Very important concept explained very good, recommended.

Week 7
Week 7 - Lecture 13
Trees - Good article about trees in python.

Working with tree data structures - Another good article with some visual examples.

Depth first search - Very good explanation of this, with real world (chess) examples and visualization. Recommended.

Breadth first search - Another good article with great explanation.

Binary search tree - Lots of explanations and technique examples.

Decision Trees - Some basic explanations with sciescientific for the tree.

Solving the knapsack problem - Explanation and another solution to the problem introduced in the lecture.

How do I build a tree dynamically in Python - StackOverflow - Has some interesting answers and discussion.

Recursion vs iteration for tree traversal in python - In the lecture we've seen examples for both, this article has some information on that.

Graphs in Python - Thorough explanation with examples for this concept in Python.

Interesting and Useful Links
The links are not in any particular order and can be useful for users with any amount of knowledge.

Online books, tutorials and reading materials
Invent with Python - Another recourse for further reading and exploration of development using Python.
A Byte of Python - Good python book for beginners as well as others.

Online Python Tutor - To have better understanding about the Python code you written. Also, learn programming by visualizing Python code execution. (It supports both Python 2.7 and Python 3.3)

Python 3 Cheat Sheet by Laurent Pointal (pdf)

Other useful links.
stackoverflow - Great site with great community all about helping others. Almost every question you will have is already asked and answered on this website. (Make sure you search thoroughly before asking questions).

/r/learnprogramming - A growing reddit community about learning programming.

The Wiki - Very detailed wiki with tons of information for the beginning programmer.
The FAQ - General questions a new programmer can have that might be not answered in the lectures.
geekviewpoint - Great compact website with a lot of examples for basic and complex problems solved using Python.

Computer language chart - Very interesting representation of the different languages of the past and the present.

Teach Yourself Programming in Ten Years - Good article about the philosophy of learning new subjects and particularly programming. (Apparently the site is down and I guess we are partially involved. Be sure to check it out when it's back online)

Koans of unit tests You get a set of failing unit tests that you must fix. Starts very basic and goes up to OOP and then some. Useful if you want extra practice with Python and works well with this class (so far - week 4).

Free Programming Books Github community maintained list of links to free programming books for Python.

Pyschools Python based site to solve programming puzzles and exercise your mind.

nltk Widely used Python library in the field of Natural Language Processing.

Twisted An event driven networking engine written in python.

Beautiful Soup An XML parsing library that is widely used in web-scraping scripts and applications in python.
