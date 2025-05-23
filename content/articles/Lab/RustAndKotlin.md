Title: Rust and Kotlin
Date: 2020-6-2 
Modified: 2020-6-15 
Category: Lab
Tags: rust, kotlin 
Slug: Rust and Kotlin
Authors: Niraj Amalkanti 
State: Partial-Success

### TLDR
I wanted to pick a new language to learn and maintain my skill in. I also wanted to make sure
I had use cases for the new language so I had practical reasons to continue using it. 
I ended up picking Rust as this language,
but I couldn't come up with any concrete use cases.

### Entries
[ Overview ](#overview)

[ 6/2/2020 - Method ](#6/2/2020)

[ 6/3/2020 - Discussion:Python and Django ](#6/3/2020)

[ 6/4/2020 - Discussion:Rust and Rocket ](#6/4/2020)

[ 6/5/2020 - Discussion:Kotlin and Spring Boot ](#6/5/2020)

[ 6/6/2020 - Implementation:Python and Django ](#6/6/2020)

[ 6/7/2020 - Reviewing Rust docs ](#6/7/2020)

[ 6/8/2020 - Reading Rocket docs ](#6/8/2020)

[ 6/9/2020 - Investigating Diesel and Changing the Project ](#6/9/2020)

[ 6/10/2020 - Implementing the New Project ](#6/10/2020)

[ 6/11/2020 - Starting the Kotlin Project ](#6/11/2020)

[ 6/12/2020 - Rethinking My Plan ](#6/12/2020)

[ 6/13/2020 - The Decision ](#6/13/2020)

[ 6/14/2020 - Use Cases ](#6/14/2020)

[ 6/15/2020 - Final Thoughts and Objective Analysis ](#6/15/2020)

[ 10/10/2024 - Update: Kotlin ](#10/10/2024)

[ 10/12/2024 - Update: Rust ](#10/12/2024)

<a name="overview"></a>
# Overview

I consider my "primary" languages to be Python and C/C++. I use both of these languages 
at work and in my personal projects. The other languages I know, I consider to
be "tertiary" languages. These are languages I've done a few projects 
in but I don't regularly use them. What I'd like to do is add a "secondary"
language to my skillset. This would be a language I don't use with extreme regularity
, but a language I pay attention to
and try to use semi-frequently. This language would ideally be useful in areas 
that Python and C/C++ don't cover. A secondary language would require an ongoing 
maintenance commitment which is why it's not a trivial decision. 

I actually tried adding Haskell as a secondary language in the past. I had heard 
a lot of good things about Haskell and was interested in trying it out.
I learned about it through this [book](http://learnyouahaskell.com). It introduced a lot
of interesting ideas and I was initially excited to use it more. 
I decided I would implement this blog using Hakyll, a static site generator in Haskell. 
However, like
most of my side projects, I worked on it infrequently. Because Haskell is so different from
Python and C++ I usually spent my time "working" on my blog instead on Haskell review.
Which I then forgot when I came back to it. Obviously, I got nothing done and decided
to use Pelican instead. Haskell was too different from my existing knowledge base and
honestly; Pelican was a better fit for this kind of project for me. So now, I want to
pick a language that's more similar to Python/C++ while still extending my skillset. I'd also
like to find some clear use cases. I want this work to be useful to me, instead 
of just being a project to maintain my skill in the language. Otherwise I might make
the same mistake and try to force this new language in areas where I shouldn't.

Over the past few years I've been exposed to a lot of languages, but there are two
stand outs; Rust and Kotlin. Both appeal to me for different reasons which I will 
detail later.

The git repo where these projects will be is [here](https://github.com/namalkanti/idfinder-samples).

## Objectives
* Identify a choice for my secondary language 
* Identify use cases for my secondary language

<a name="6/2/2020"></a>
# 6/2/2020 - Method

The method I will use to evaluate this decision is an interesting one. Some time ago;
I made a very simple web app with a friend as a way to learn Django. This web app
was a small site where you would post pictures of lost University IDs along 
with contact info. Somebody who lost their ID would look this up and find the person who
located it. We never planned on deploying it; it was an exercise to learn Django. 

This same exercise would be useful for this investigation as well. Python, Rust, and Kotlin
all have fairly mature frameworks for web development. Not only would I get a chance
to learn more about the language; I would also get to see how libraries in the language
are used. This is better than some toy example which would only require basic code.
But this exercise is simple enough that I won't be spending a huge amount of time on the app;
which is good because I'm repeating it three times. Using the same example will also
give some consistency to my comparison.

I want, to again, emphasize that I won't necessarily use Rust or Kotlin for web dev even though
that's what I'm doing in this exercise. If they are better than Python+Flask for my projects
then I will, but otherwise I'll use what I'm familiar with. That's also why I want to figure
out other use cases for this secondary language. I'm only using a web app because 
it's something simple that all three languages have mature support for. That consistent 
example will be helpful in my comparisons.

<a name="6/3/2020"></a>
# 6/3/2020 - Discussion:Python and Django
I used Django as the framework to implement the original idfinder app. This
was to learn Django, but I mainly use Flask for any needs I have in
building web apps. None of my personal projects need the complexity of Django or Pyramid. 
Most of them need a simple web server that responds to http requests. But this
project will require databases and forms. I could add these modules to flask, but I'd
have to pick all the modules for these tasks myself. Django has a "batteries included"
philosophy. Since this is meant to be a simple control example, I will use
Django again for this project.
But the Django implementation is out of date (Django 1.7, which ran on Python2). 
So my first task will be to redo the app in a recent Django version for a more 
consistent and recent comparison. 

<a name="6/4/2020"></a>
# 6/4/2020 - Discussion:Rust and Rocket
I was initially introduced to Rust when Mozilla began using it for their firefox rendering engine.
The concepts of being safe with memory and fixing issues during compilation appealed to
me. When discord released their Rust api, a friend of mine and I implemented a small chat 
bot. I learned the basics of rust through this project. I found it to be verbose, but I
did like some of their implementation decisions. Their memory management model is very similar
to smart pointers in C++; so I quickly adapted to it. I did not get a chance to really
use the trait system. Normally; I use object oriented languages and this is the paradigm
I'm familiar with. Rust's traits are different in that they emphasize object behavior instead
of identity. This is supposed to be semantically clearer when defining datatypes and how
they should be used. Leaving the traditional object oriented paradigm is a way that
learning Rust can expand how I think about programming.   

[Rocket](rocket.rs) is a web development framework in Rust that's mature. Some initial code samples
suggest it's very similar to Flask; so I hope to adapt to it quickly.

<a name="6/5/2020"></a>
# 6/5/2020 - Discussion:Kotlin and Spring Boot
Kotlin is a language I discovered when investigating Android app development. I'm fairly
familiar with Java and initially felt there was no point in learning another language.
But I started going through a udacity [course](https://www.udacity.com/course/kotlin-bootcamp-for-programmers--ud9011) 
and the more I learned about Kotlin, the more
I began to like it. Kotlin feels like a language that was designed by programmers and 
a lot of the language features are ideas I've wished were in other languages. 
Google also now supports Kotlin as an official android language 
which gives it more weight. The course itself was a little... cringe-worthy... to a 
fault. I couldn't
tell if it was intentional for satire or the instructors just lacked charisma. But 
the material was excellent.

Kotlin's JVM backend is also a benefit. [Clojure](clojure.org) is a language I've wanted to experiment with
for some time. Like Haskell, clojure is a massive departure from what I'm used to, and 
building standalone applications in Clojure could be unecessarily arduous for me. I could
support it with Java, but I don't like Java that much. But I like Kotlin a lot, and it could
help support my clojure experiments.

One question that might come up here is "Why not Scala?". I've held a low key interest in
Scala for some time. It's supposed to combine functional programming with a more traditional
paradigm to be considered a more practical language. While I find this enticing; it doesn't
quite grab me the way Kotlin's syntax and design decisions did. But the ability to explore
Scala later is definitely an attractive aspect of Kotlin.

Rust would expand my view about how I program but Kotlin would expand my views on tooling.
I use IDEs when required to at work, but for personal programming I prefer using Vim 
and the command line(on Linux, course). Kotlin really seems to encourage the use of an
IDE (IntelliJ). So developing Kotlin as a secondary language could increase my familiarity
(and acceptance) of IDEs.

The most well known JVM web framework to me is Spring. Spring requires a lot of configuration
and knowledge, but there seems to be a project called Spring Boot. Spring Boot is supposed
to be a simpler project that defaults a lot of options for you. So I will use Spring Boot 
for this exercise.

<a name="6/6/2020"></a>
# 6/6/2020 - Implementation:Python and Django
The implementation process was relatively straightforward. I was able to copy most of my 
existing code from the older Django version. There were a few things that changed(mostly syntax)
and Python3's default unicode simplified or eliminated some code in the previous version.

Revisiting Django reminded me how pedantic the framework is. I understand the value 
of such a rigorous framework; mainly in situations when you're working on a project
with lots of different people. But it definitely feels like overkill for a personal 
project. But it does do a lot of work for you, unlike flask, where I might spend just
as much time getting everything set up. I've heard pyramid is supposed to fill a gap
between the two projects, and it might be worth looking into some time in the future.
But I don't want to explore that tangent now.

<a name="6/7/2020"></a>
# 6/7/2020 - Reviewing Rust Docs

I started with reviewing the official rust [docs](https://doc.rust-lang.org/book/). I 
note that it's expanded quite a bit since I looked at it back in 2016. The review
reminded me that while Rust seems verbose; it's usually only because the language
wants you to be explicit with what you want. It is capable of type inference and some
constructs have syntactic sugar when appropriate. I wasn't extremely thorough; there 
are a lot of complicated concepts and I'll review them as I start going through Rocket's 
documentation. Some of them I remember from my earlier work with Rust but some are new.

Something I note is that the reccomended way to install and update rust is a new tool called rustup.
Normally I maintain tools using the package manager in my linux distro but 
rustup is what is now suggested. Rustup allows you to easily switch your rust toolchain
based on build type(stable vs nightly) and also makes it easier to handle toolchains
for different CPU architectures. I've cross-compiled C++ for ARM and know that it can be
messy; so I can see the value of this. You can also override the toolchain on a by directory 
basis; so it's a little like Python's virtualenv. 

Another interesting aspect of Rust are its macros. These are meant for syntactic sugar
and to specify Domain Specific Languages. DSLs are a feature that have always interested
me. But I note that macros are definitely a work-in-progress now; and subject to changes.

<a name="6/8/2020"></a>
# 6/8/2020 - Reading Rocket Docs

My next step was Rocket's [docs](https://rocket.rs/v0.4/guide/). They expected a good
understanding of Rust beforehand and I definitely felt that this was tested. Rocket
feels somewhat like a DSL in Rust for building web apps. It's still Rust but there's
a lot of macros and specific ways functions need to be used and called. Rocket doesn't
provide a templating engine or database ORM so I will need to include these.

<a name="6/9/2020"></a>
# 6/9/2020 - Investigating Diesel and Changing the Project
I found a lot of posts that discussed integrating Rocket with an ORM(Diesel seems to
be the best choice), but this was the best [post](https://medium.com/digitalfrontiers/web-service-with-rust-rocket-and-diesel-7425f4a04f4c).
In addition to providing me a tutorial, it also had an excellent analysis of Rust, Rocket,
and Diesel. The author, Marco Amann, seems to have a similar style to mine and his other
posts are investigations into different technologies. I should keep him in mind as a 
good example.

He showed that Diesel actually requires you to write SQL by hand. This is a turn off
to me, but Amann notes this is actually very powerful. There are a lot of database 
modeling tools that generate SQL for you; and this approach allows you to use them and
leverage the unique traits of each database. I recognize that value of this, but as 
somebody whose database needs don't require this level of detail and control; it's not
quite as valuable.

Amann continues to note that Rust and Diesel require fairly tight integration of the 
database layer and views. Each view needs a handle to the database connection in order
to use it. It's not as neatly abstracted as it was in Django.

This new information motivates a change in project. Not only will I have to set up
Diesel, I'll also have to figure out how to use a templating library, if I want to create
the same project in Rocket that I made in Django. My goal here is not to learn web app
development in different languages; it's to simply try the language out. This particular
approach will be a lot more work and I really don't think I'll gain much from it. In fact,
I already feel like I have a good assesment on Rust and Rocket from the docs and examples.
But I don't want to move on without completing something concrete. So instead, I'll
use a json file to store information about the id cards instead of a database. I'll write
two views, one which will return a list of the id cards in json and another which will
return individual id card information, also in json, based on an input id. This will 
mean that I won't need to use a templating library either. But this kind of response is what I
might use if I was using some javascript front-end framework; so it's not total garbage.

I feel this is a much more reasonable project that will satisfy my goals for Rust and Rocket
without adding a lot of unecessary work.

<a name="6/10/2020"></a>
# 6/10/2020 - Implementing the New Project

Now that I've simplified my parameter scope, this was much easier to implement. I used
serde_json; which seems to be the de facto official json library in rust. Creating and 
mounting the views was also simple. But even with this simple example I needed to be
very explicit about when I was borrowing references. Rust definitely makes sure you're
being very explicit about what you want when coding. I was originally going to discuss
what I liked and disliked about Rust but I think I'll save the breakdown for the end
and include Python and C/C++ as well. Now I should move on to Kotlin and Spring Boot.

<a name="6/11/2020"></a>
# 6/11/2020 - Starting the Kotlin Project

There's a lot of tutorials using Kotlin and Spring Boot but I'm focusing on this 
[one](https://spring.io/guides/tutorials/spring-boot-kotlin/).
Getting Spring Boot started was interesting. I'm using the Community version of IntelliJ
so I wasn't able to start the project from the IDE. Instead I went to this [site](https://start.spring.io)
and downloaded a zip with all the configuration files. This was easy enough to set up
but this process feels ... weird to me. I suppose it's not actually different than an IDE setting 
everything up, but it feels different. As I went through the tutorials I started to see
how dense Spring is. Even with Spring Boot handling a lot of set up, it feels like there's
a lot of work that's being done for me and I'm not aware of what's going on. I didn't
really look into other web frameworks but considering how much is hidden from me in Spring
it might be a good idea to find a simpler framework.

I found another framework with a good reptuation called [ktor](https://ktor.io). They have
an excellent tutorial and it feels more like Rocket or Flask than Spring or Django. I can't
help but wonder whether I should've used Flask and SQLAlchemy for a simplied example for Python
to stay consistent. Django doesn't feel like Rocket and I'm not sure all this work is 
important. This level of uncertainty means I should revaluate my plan.

<a name="6/12/2020"></a>
# 6/12/2020 - Rethinking My Plan

I stated in the beginning my goal was to evaluate Rust and Kotlin to select a secondary
language for my skillset. And I emphasized that, even though I'm building web apps, 
I probably won't use either of these languages for web apps and this is supposed to be
to see how to evaluate libraries in each language. 

But despite my claim, this really feels like I'm evaluating web frameworks. When I'm 
thinking about each stage; I'm focusing on differences between Django, Rocket, and now 
Spring. I really should be focusing on Python, Rust, and Kotlin. This means .... I messed
up. I think my idea sounded good but it's not really working. I already learned about 
both languages through their docs and the udacity course. I should've picked a simpler
project or library to use. Or maybe a project wasn't even necessary; I could've just
had a discussion based on the courses/reading I already did. 
At this point I'm focusing too much on web frameworks and 
their idiosyncrasies instead of the language itself.

So what's my new plan? I really don't need to finish this Kotlin project. I also 
don't like leaving things unfinished. But I've already wasted a decent amount of time
on this and I'm not really enjoying this process anymore. Personal projects are supposed
to be fun and useful. I feel like I've already gotten the 
information I need so now it's time to make a decision.

<a name="6/13/2020"></a>
# 6/13/2020 - The Decision

Because of my wasted time I ended up reviewing the Udacity [course](https://www.udacity.com/course/kotlin-bootcamp-for-programmers--ud9011) 
on Kotlin again. I want to make sure I'm giving it a fair assesment since I've spent 
so much time on Rust. First I'll go over what I like about my existing languages.

## Python 
## What I Like
* Easy syntax
* Interpreted language is trivial to debug
* Strong api support almost everwhere
* Fun to program in
* Works well with C/C++ for speed ups

## What I Dislike
* Dynamic typing creates annoying runtime errors and excessive debugging
* Can be difficult to create good style when working with larger groups
* Deployment is messy(virtualenvs help, but it's not an ideal fix)
* Global Interpreter Lock makes multi-threading difficult
* Very slow with out C/C++ support

## C++
## What I Like
* Smart pointers and C++14/17 addons make language far more enjoyable(not quite fun though)
* Works extremely well with Python 

## What I Dislike
* Auto helps but the language feels very rigid due to lack of type inference
* Requires lots of code to enforce type safety

Both languages have weaknesses, but for my own use cases; the combination is extremely
powerful.

## Rust
## What I Like
* Rust compiler is excellent at forcing me to recognize ambiguities and address them
* Memory management is very similar to C++ smart pointers and feels like an easy transition
* Trait system feels really powerful and I'm excited to work with it
* Tooling feels simple
* Easy to build static executables mean deployment can be very simple

## What I Dislike
* Code is very verbose, can be ugly. 
* Can feel very annoying when fighting with the borrow checker

Rust has a lot of interesting features. Forcing extra attention to detail when writing
code and dealing with errors during compilation means I don't have to deal with 
annoying runtime errors. The trait system is really interesting and I'm eager to explore
how I can use it when designing applications.

My biggest issue with rust is how verbose and ... well, ugly it can be. Lifetimes in
particular just look bad. And combining lifetimes with generics makes Rust code look
incredibly busy.

## Kotlin
## What I Like
* Concise syntax feels very simple
* Syntactic sugar feels appropriate and makes coding easier
* Feels fun
* Features like interface delegation make designing and implementing complex designs simple and fun
* JVM integration allows me opportunities to explore other languages like Clojure more easily

## What I Dislike
* Tooling and build system feels incredibly complicated

Kotlin really impressed me with it's concise syntax and interesting features. Interface delegation
is one in particular I can't get over. Rust may be fun to design software in, but I feel
that Kotlin is more fun to actually write code for.

My biggest issue with Kotlin is the tooling. IntelliJ is probably my favorite IDE(the 
only other ones I've used are Eclipse, Visual Studio, and Xcode), but I still can't say
I enjoy IDEs. I recognize their value, especially with large projects with multiple
developers, but it's not something I enjoy dealing with for personal projects. Even if 
I don't use IntelliJ, Kotlin requires Gradle which still feels complex. It's nothing
like Rust and Cargo.

So what's my decision? It's probably obvious, but I think Rust is the best pick for me. 
It might feel like this a biased decision or I didn't give Kotlin a fair chance, but I 
think it comes down to what the language adds to my skillset and how I feel about it. 

Rust expands my viewpoint with traits which are different from the object systems I'm used
to. I'm very excited to see how I can use Rust's trait system to implement my designs.

Kotlin was meant to expand my viewpoint by using IDEs and a more rigid build system. Even
after trying it and noting the advantages, I still think of it a chore.

That really makes the decision clear. I'll still use
Kotlin when I need to (Android apps) but I won't invest in it the same way as Rust.

<a name="6/14/2020"></a>
# 6/14/2020 - Use Cases

In addition to selecting a language, I also decided I wanted to make sure I have some
good use cases. Otherwise it'll be more difficult to keep my familiarity with Rust without
actually making up projects to do so. I want to avoid the same mistake I made with Haskell.

Rust's site defines four main areas the Rust team wants to focus Rust for; so this
is probably what I'll look at.

## Command Line
The first target they mention is command line tools. Currently I use python for all
my command line tools. It's large amount of supporting libraries and ease of debugging
make it easy to quickly prototype tools and start using them. 

However a big issue when distributing command line tools is the environment. Spawning
virtual envs just for command line tools is annoying. And making sure those venvs are all 
consistent is a chore. But for personal tools it's not clear how much of a problem it
is. I have desktop and a laptop so keeping those envs consistent isn't too hard.

Still, Rust definitely has advantages here. I should definitely consider Rust for cli
tools I use.

## WebAssembly

This is an interesting case. WebAssembly seems to be the new kid on the block for front
end web development. I don't really do any front end web stuff and don't really have 
a desire to do so. Probably not a strong use case, but I think it's something I should 
keep an eye on.

## Networking

From my experiences with Rocket, I'm not actually sure I like Rust, personally, for this
use case. Rocket does have benefits but I'm not sure they're for me.

## Embedded Systems

This use case feels powerful. Rust's tooling allows easy cross-compilation for different
architectures. I've done cross-compilation for ARM on iOS devices using cmake and it isn't
pretty. Rust's abilities in memory mangement will make it easier to keep memory issues
in check. And debugging runtime issues in embedded systems can be a nightmare; so having
everything addressed during compilation is attractive. I do have some project ideas with fpgas
and rasberry pis that could make use of this. So this could be a good use case.

My main problem is that I don't have very many of these and they'll likely be inconsistent.
Useful, yes, but not the kind of work that'll help keep my Rust skills sharp over time.

<a name="6/15/2020"></a>
# 6/15/2020 - Final Thoughts and Objective Analysis

So this project's course was a lot more complicated and a lot more embarrassing.
I had an idea at first; but it ended up being a huge distraction. But I did say that
I wanted this blog to show up my screw-ups, not just successes. I should own up to that.

I do feel that I accomplished my first goal of selecting a secondary language. Rust 
does feel like it neatly fills a gap that I have between Python and C/C++. It's a lot 
more fun than C/C++ but doesn't have python's sluggishness. The tooling and dependency
management is also fantastic, some thing both Python and C/C++ can struggle with.

But I don't honestly know when I'll use it. There's potential for use in embedded projects
but I don't have very many of those. I can maybe see it being useful for CLI projects
but I need to remember my lessons from Haskell. I shouldn't just use Rust for projects
I actually need because I want to use Rust. If Python is better for my cli tool I should use it. This may
mean I need to make up projects to develop and maintain my Rust skills and I don't know how easy that
will be for me to do in the long term. Or even if it's something I really will want to
do over time.

So I'm going to mark this project as partial success. I don't really feel like I've come
up with strong use cases for Rust for myself. I'll try to keep it as a "secondary" language
but we'll ultimately see how well that turns out. Rust is a lot more similar to Python and 
C/C++; so it has that in favor of Haskell, at least. But whether I can keep up motivation
to support a language for what's basically "academic" purposes remains to be seen.

<a name="10/10/2024"></a>
# 10/10/2024 - Update: Kotlin

There's been some new developments relevant to this topic so I'm adding updates.

I still haven't found a good use case for Rust as a secondary language. 
One of my co-workers (an Android dev) persuaded me to give Kotlin another
chance. I knew Android app dev is an area I want to improve in and Kotlin is required(unless I 
want to use Java). This motivated me to revaluate Kotlin.

But it was obvious that the same issues remained. Kotlin's IDE dependence put me off, especially 
libraries like [ktor](https://ktor.io) or [spring boot](https://spring.io/projects/spring-boot) 
that expected you to use an online project generator
to start your projects. I can see the value of this in large companies, but I can't imagine
going through this for a personal project. I also notice that Kotlin doesn't have a lot
of adoption outside of Android. The main use case is replacing Java(a good one), but it doesn't 
appear that people are actively creating new Kotlin projects for standard applications.
This differs from Rust or Go; where I see this more frequently. 

However, this let me review my priorities and goals and I now have two main goals with Kotlin/JVM.

* Android Dev
* Clojure

## Android Dev
This has been a lower priority, but I really want to become more comfortable with Android app development.
I'd like to get to the point where I can easily build an app for myself when I need it, just like how I can
easily write a script or small program for these problems on a standard computer. 

## Clojure
I've still been eyeing Haskell but have not pursued it. But the more I look at Clojure, the more I see 
the similarities. And since Clojure is on the JVM, I can use Java libraries to support it along with Kotlin
if needed. I'm not sure I can motivate myself to pursue Haskell further, but I think Clojure has enough utility.


I don't think I will pursue Kotlin as a general purpose programming language for now, but if I really end up
liking it that may change. That could happen from either goal. However, I will continue to regard Kotlin as a 
tertiary language for myself, but now I have more direction in how I want to use it. 

<a name="10/28/2024"></a>
# 10/12/2024 - Update: Rust and perhaps a use case ?

My disappointment in Kotlin motivated me to revaluate Rust but I took a quick detour into Haskell. This ended
up being interesting because it became obvious to me how much Haskell has influenced Rust. Now that I understood
Traits and datatypes like Option/Result, Haskell typeclasses and Maybe/Either made a lot more sense to me. In fact,
maybe one reason for Rust's popularity is converts from Haskell. This new familiarity has lead me to a new idea.

When I learned C, one application was using C for command line tools. C tools are much faster than Python scripts
and compiling into a single, static executable makes for easy deployment(instead of Python virtualenvs).
But creating makefiles and writing C is too much effort for simple tools when a Python script will do.
But Rust's tooling simplifies the build process(and allows for cross-compilation). And it's much easier
to organize Rust code into multiple files instead of a single Python script. I'm also realizing the subtle difference
between a script and command line tool.

## Script vs Command Line Tool
A script is usually a set of instructions for a task that needs to be automated with some minimal configuration.
But a command line tool is a utility like grep, awk, sed, etc; that does some semi-customizable unit of work. They're
similar but a cli tool usually is run more frequently and needs to have more complex customization with flags. Because of this,
Rust has several advantages over Python for command line tools.

### Speed
For scripts that are started and just let run, Python is fine. But if I want a tool I use frequently on the 
command line, the centuries spent waiting for the Python interpreter will add up over time.

### Organization
Python does have [click](https://click.palletsprojects.com/en/stable/); which is neater than argparse, 
but a single python script can get very large
when trying to add subcommands and a lot of functionality. This is true even with click. But Rust's easy
tooling lets me build a single executable while keeping the source organized in multiple files. 
This is an advantage of building cli tools with C that I learned
about when learning C, but the build tooling with C always put me off. Cargo fixes this issue with Rust; 
allowing me to easily build a single statically linked executable. But I can maintain code readability
by splitting it up into as many files/modules I need. With Python I'm force to make trade
offs regarding file size/organization

### Why not Bash?
Bash makes sense for small, simple scripts where the goal is to just chain together commands, but anything
more complex can be difficult in bash. I think it makes sense to improve my bash skills so I can do scripts
in bash but use Rust for command line tools. I will investigate this.

<a name="11/12/2024"></a>
# 11/12/2024 - Update: Bash for Scripts

Interestingly enough, I ended up deciding to keep Python for my scripts. Bash is nice in theory, but anything
even slightly complex is just cleaner in Python. One script I tried converting was a simple one that copies music
files by parsing a text based playlist file and syncing them. This is trivial in Python, but even using tools
like Sed and Awk lead to complex and hard to maintain code. 

Improving my bash is still a good idea, and I think there are scripts I can use better bash skills to create.
But the falloff is very quick and Python becomes a better option with an even moderate amount of complexity.

<a name="11/18/2024"></a>
# 11/18/2024 - Update: Rust for CLI tools

Initially, I was using a bunch of complex bash alises for some build tooling at work. I wanted to use Rust, but
I decided to use bash first. As cool as Rust is, if Bash is better, I should go with it.

But I ran into the same problem.... I had ideas for default/optional flags for easy usage. But implementing this in
bash is not trivial. Using getopts does not handle optional parameters well. It requires state logic and creates
dependencies on the ordering of the flags. The tool, getopt, does this much better,
but the versioning and capabilities differs tremendously depending on the OS. Trying to figure out these version
differences sounds like a giant mess that I really don't want to deal with. 

I ended up using subcommands with semi-arcane bash syntax. This wasn't perfect, but I found that his accomplished
90% of what I wanted with a command line tool. 

But eventually; the 10% forced me to resort to ugly hacks. I then rewrote the tool in Rust. This took longer than the bash script, 
but it wasn't extreme. Now that
this version works, I find that I like using it a lot more. It's much easier to configure and adapt as I need to make
changes. The bash tool could've worked but as my needs for this tool expanded Rust was ultimately the better option.

## Conclusion
I think there's a fine and difficult to assess line between using Rust or Bash for command line tools. It probably
makes sense to start with bash but if I find that bash is too limiting I should switch. But now I FINALLY have 
a personal use case for Rust!
