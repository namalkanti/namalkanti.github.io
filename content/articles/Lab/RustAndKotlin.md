Title: Rust and Kotlin
Date: 2020-6-2 
Modified: 2020-6-2 
Category: Lab
Tags: rust, kotlin 
Slug: Rust and Kotlin
Authors: Niraj Amalkanti 
State: In-Progress

### Entries
[ Overview ](#overview)

[ 6/2/2020 - Method ](#6/2/2020)

[ 6/3/2020 - Discussion:Python and Django ](#6/3/2020)

[ 6/4/2020 - Discussion:Rust and Rocket ](#6/4/2020)

[ 6/5/2020 - Discussion:Kotlin and Spring Boot ](#6/5/2020)

[ 6/6/2020 - Implementation:Python and Django ](#6/6/2020)

[ 6/7/2020 - Implementation:Rust and Rock ](#6/7/2020)


<a name="overview"></a>
# Overview

I consider my "primary" languages to be Python and C/C++. I use both of these languages 
at work and in my personal projects. The other languages I know, I consider to
be "tertiary" languages. These are languages I've done a few projects or work
with in the past but I don't regularly use them. What I'd like to do is add a "secondary"
language to my skillset. This would be a language I don't use with extreme regularity
or for work (where I don't necessarily have choice), but a language I pay attention to
and try to use semi-frequently. This language would ideally be useful in areas or aspects
that Python and C/C++ don't cover. A secondary language also requires an ongoing 
maintenace commitment which is why it's not a trivial decision or one I can simply 
add languages to easily.

I actually tried adding Haskell as a secondary language in the past. I had heard 
a lot of good things about Haskell and was interested in trying it out.
I learned about it through this [book](http://learnyouahaskell.com). It introduced a lot
of interesting ideas and I decided I would implement this blog using Hakyll. However, like
most of my side projects I worked on it infrequently. Because Haskell is so different from
Python and C++ I usually spent my time "working" on my blog as a bit of Haskell review.
Which I then forgot when I came back to it. Obviously, I got nothing done and decided
to use Pelican instead. Haskell was too different from my existing knowledge base and
honestly; Pelican was a better fit for this kind of project for me. So now, I want to
pick a language that's more similar to Python/C++ while still extending my skillset. I'd also
like to find some clear use cases. I want this work to be useful to me, instead 
of just being a project to maintain my skill in the language.

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
was basically a small site where you would post pictures of lost University IDs along 
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
it's something simple all three languages have mature support for. That consistent 
example will be helpful in my comparisons.

<a name="6/3/2020"></a>
# 6/3/2020 - Discussion:Python and Django
I used Django as the framework to implement the original idfinder app. This
was to learn Django, but I mainly used and still use Flask for any needs I have in
building web apps. None of my personal projects need the complexity of Django or Pyramid. 
Most of them simply need a simple web server that responds to http requests. But this
project will require databases and forms. I could add these modules to flask, but I'd
have to pick all the modules for these tasks myself. Django has a "batteries included"
philosophy. Since this is meant to be a simple control example. I will use
Django again for this project.
But the Django implementation is out of date (Django 1.7, which ran on Python2). 
So my first task will be to redo the app in a recent Django version for a more 
consistent and recent comparison. 

<a name="6/4/2020"></a>
# 6/4/2020 - Discussion:Rust and Rocket
I was initially introduced to Rust when Mozilla began using it for their rendering engine.
The concepts of being safe with memory and fixing issues during compilation appealled to
me. When discord released their Rust api, a friend of mine and I implemented a small chat 
bot. I learned the basics of rust through this project. I found it to be verbose, but I
did like some of their implementation decisions. Their memory management model is very similar
to smart pointers in C++; so I quickly adapted to it. I did not get a chance to really
use the trait system. Normally; I use object oriented languages and this is the paradigm
I'm familiar with. Rust's traits are different in that they emphasize object behavior instead
of identity. This is supposed to be semantically clearer when defining datatypes and how
they should be used. Leaving the traditional object oriented paradigm is a way that
learning Rust can expand how I think about programming. The combination of speed and type
safety is also something that neither Python or C++ have.  

[Rocket](rocket.rs) is a web development framework in Rust that's mature. Some initial code samples
suggest it's very similar to Flask; so I hope to adapt to it quickly.

<a name="6/5/2020"></a>
# 6/5/2020 - Discussion:Kotlin and Spring Boot
Kotlin is a language I discovered when investigating Android app development. I'm fairly
familiar with Java and initially felt there was no point in learning another language.
But I started going through some courses and the more I learned about Kotlin, the more
I began to like it. Kotlin feels like a language that was designed by programmers and 
a lot of the language features are ideas I've wished were in other languages. 
Google also now supports Kotlin as an official android language 
which gives it more weight.

Kotlin's JVM backend is also a benefit. [Clojure](clojure.org) is a language I've wanted to experiment with
for some time. Like Haskell, clojure is a massive departure from what I'm used to, and 
building standalone applications in Clojure could be unecessarily arduous for me. I could
support it with Java, but I don't like Java that much. But I like Kotlin a lot, and it could
be a way to support my clojure experiments.

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
# 6/7/2020 - Implementation:Rust and Rocket
