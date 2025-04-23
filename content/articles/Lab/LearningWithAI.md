Title: Leaning with AI
Date: 2024-11-10 
Modified: 2025-3-11 
Category: Lab
Tags: llms
Slug: My experiences learning with AI
Authors: Niraj Amalkanti 
State: In-Progress

TL;DR: AI is at its best when it helps you think better, not when it tries to think for you.

### Entries
[ Overview ](#overview)

[ Story So Far - Learning with ChatGPT ](#Story-So-Far)

[ 3/5/2025 - Claude vs ChatGPT vs Gemini](#3/5/2025)

[3/6/2025 - Ikon vs Epic](#3-6-2025)

[3/7/2025 - Memories](#3-7-2025)

[3/28/2025 - Specialized Interfaces Matter](#3-28-2025)

[4/10/2025 - Canvas vs Artifacts: The Plot Thickens](#4-10-2025)

[4/11/2025 - Slip Coding: Reclaiming Vibe Coding For Productivity](#4-11-2025)

[Conclusion](#conclusion)

<a name="overview"></a>
# Overview

I've had a complicated relationship with AI tools. This post documents my journey from skepticism to finding genuine value in AI assistants—not as code generators, but as learning companions and thought organizers. I'll share my evolving understanding of how to use these tools effectively and compare different platforms to help others find approaches that might be useful.

## Objectives
* Document how AI assistants can amplify learning when used intelligently
* Demostrate the organizational capabilities of LLMs
* Share strategies for effective AI collaboration that go beyond basic prompting

<a name="Story-So-Far"></a>
# Story So Far - Learning with ChatGPT

My initial experiences with generative AI were deeply disappointing. I work in Edge AI and often have to build specialized models that work on compute constrained enviroments. In this space, I found the code generation capabilities fell far short of the hype. Prototype code in Python was okay, but anything in C++ was barely usable(if it even compiled). I needed heavy prompt engineering to get some of this to work and it was comparable in effort to writing it out in the first place.

The turning point came in November 2024. I had a realization: what if I stopped expecting AI to solve my problems and instead used it as a learning tool?

I began using ChatGPT not to generate solutions, but to:
- Take notes during my learning process
- Organize my thoughts and exploration
- "Pair program" as I wrote my own code
- Distill software engineering expertise into prompts that helped me write cleaner code

But this wasn't just limited to work and coding. I soon found that ChatGPT was great for learning about... well almost anything. Being able to take notes and looking up items in a single chat keeps things organized. I could have different lines of thought or exploration for whatever I wanted. Normally, taking notes seperately and keeping them organized is a lot of effort/upkeep. But with ChatGPT, it became trivial. And if I wanted to revisit the thread after a break(because I'm busy with other things), ChatGPT could summarize this and let me jump back in.

Now, if I wanted to study something, plan a vacation, or learn anything, my first response is to create a ChatGPT chat. I can immediately learn and get some context. And if it's relevant, revisit/reorganize the chat later. If not, just delete it and move on.

Of course, hallucinations are always a threat. But in today's era of fake news, I have to be vigilant all the time anyways as bad info is everywhere and can be hard to track down. And even if it hallucinates, ChatGPT can often correct itself on direct cross-examination. And this is a lot easier than constantly searching and cross-checking everything myself.

The ability to maintain threads and have ChatGPT function as an intelligent "notetaker" proved incredibly valuable—even for topics it likely knew nothing about. I could feed it my own knowledge and have it help organize information and potentially illuminate patterns I might have missed. This was a key insight, even if ChatGPT didn't know about a topic; it could still help me learn, by diligently taking notes and finding patterns. In this case, it helped me analyze/organize my own information instead of providing it to me.

This shift in approach changed everything. By leveraging my own intelligence and creativity, AI became an incredibly powerful force multiplier for learning and productivity.

I eventually purchased a ChatGPT Pro subscription specifically for the "Projects" feature, which let me better organize conversations by topic. This further improved its organizational ability. I could create a ChatGPT project for my personal projects and keep several different threads within the project with a shared context. Or if I had a ton of questions about science, I could create a "science" project and let ChatGPT keep all my science question threads in a single project.

What I realized was that most people use AI ineffectively— throwing problems at it and expecting perfect solutions. No wonder it never resonated with me before. The real power came from collaboration, using AI to enhance my own thinking rather than replace it.

Of course, now that I realized the power of this new tool, I had to figure out which platform was best.

<a name="3-5-2025"></a>
# 3/5/2025 - Claude vs ChatGPT vs Gemini

I evaluated the three major AI platforms specifically for my personal use cases. While my journey started with ChatGPT, I wanted to make sure I wasn't missing out on potential benefits from competitors.

## Platform Evaluation

My first priority was chat organization — the ability to keep my learning projects separate and structured. This quickly became a decisive factor:

**ChatGPT:**
- Strong project organization with the ability to create and name different projects
- Clean interface for managing conversation history
- Easy to move convos in and out of projects

**Claude:**
- Does have project-level organization 
- Does not remove project convos from main convo list
- Not easy to move convos into projects after they've been created

**Gemini:**
- Lacks any project support

This initial assessment immediately led me to eliminate Gemini from consideration. Without proper project organization, it simply wouldn't meet my needs for structured learning and note-taking.

Between ChatGPT and Claude, the differences weren't immediately obvious. Both offered solid organizational features, though ChatGPT felt a little better. However, I've heard that Claude's models are better than OpenAIs(though I realize this is very subjective) so I wanted to compare them directly.

One observation I found surprising: none of the AI assistants themselves were aware of their own features. When asked about their project organization capabilities, they all provided generic responses rather than specific information about their implementation. Claude claimed it didn't have projects, though online resources implied otherwise. I had to purchase a Claude Pro sub to confirm that it did. 

<a name="3-6-2025"></a>
# 3/6/2025 - Ikon vs Epic

I utilized both ChatGPT-4 and Claude 3.5 to evaluate ski pass options, specifically comparing the Ikon and Epic passes for the upcoming season. This served as a practical test case to assess how these tools handle detailed, research-oriented queries.

However, the results were inconclusive, as both models provided very similar answers. While ChatGPT seemed slightly more tailored to my needs, this is likely because I have used it more extensively. Further evaluation will be necessary.

<a name="3-7-2025"></a>
# 3/7/2025 - Memory is the Key

Now I've finally found the killer feature I'm looking for. I assumed all platforms have it but it's just ChatGPT. 

ChatGPT has an explicit "memory" feature that allows it to recall information across separate chat sessions. This means it can reference projects, preferences, and past work without needing to review, creating a more continuous learning experience. Over time, its memory seems to improve as more interactions occur and the platform customizes itself to me.

Claude only remembers context within a single conversation, so each new chat means starting over. You can encode instructions for projects, and Claude can retrieve them, but it’s nowhere near ChatGPT’s capabilities. Anthropic values this for privacy, which I get, but I prefer ChatGPT remembering what I’ve told it—it makes my experience better. 

Interestingly, Gemini does not do this. It mentions that Google has faced accusations of data privacy violations, and attempting to use a feature like this might be perceived as overly aggressive. I found this to be a very self-aware perspective. In theory, Google should have the most information about me, but if Gemini cannot leverage that, it becomes irrelevant.

Based on this observation, I plan on continuing using ChatGPT pro. I will keep the other platforms in mind to see what other advantages they confer.

<a name="3-28-2025"></a>
# 3/28/2025 - Specialized Interfaces Matter

I've been testing Claude for blog writing, and its dual-pane editing interface (artifacts) is a game-changer for working with markdown. Being able to see both the raw markdown and rendered output simultaneously makes the writing process much more fluid. I can then use natural language to more effectively brainstorm and generate something usable. 

<figure class="center">
    <img src="{attach}/images/claude_dual_pane.png" width="60%" height="auto" class="border">
    <figcaption>Claude's Artifact Interface</figcaption>
</figure>

This is especially powerful on mobile, where I can shrink the artifact and swap between the artifact the chat easily. This makes it easy to develop from my phone on the go.

What's particularly interesting is that this valuable feature remains available on Claude's free tier (at least for now). 

When editing code neovim, I use Github Copilot with CodeCompanion to get a similar in-editor experience(I use this for coding but could see it working for blog writing too), but being able to brainstorm and make edits from my phone is huge for working on the go. It means I don't have to be at my desk to get work done.

<a name="4-10-2025"></a>
# 4/10/2025 - Canvas vs Artifacts: The Plot Thickens

Today, I discovered something that complicates my previous assessment: ChatGPT has a Canvas feature that's almost as good as Claude's dual-pane editing for coding or markdown work. It provides similar functionality, allowing you to view both raw and rendered content side by side. However, ChatGPT's Canvas performs slightly worse on mobile compared to Claude's dual-pane interface because it can't be collapsed. While this limitation isn't ideal, it doesn't justify upgrading to Claude Pro. 

On a related note, I also found out that Claude's artifact editing actually requires a Pro subscription—contrary to what I believed on 3/28.

This was a little awkward because I originally asked Claude and ChatGPT about this feature and neither of them recognized this it. I didn't realize it myself until I told me friend about this idea and he reminded me that ChatGPT DOES have something similar(Canvas).

An interesting pattern emerges: AI assistants like ChatGPT and Claude seem unaware of their own interface features and platform capabilities. This highlights the separation between the AI models and the applications built around them, reinforcing my earlier observation that they don't "know themselves" very well. But my decision to remain stick with ChatGPT pro becomes easy at this point.

<a name="4-11-2025"></a>
# 4/11/2025 - Slip Coding: Reclaiming Vibe Coding For Productivity

Today I want to introduce a concept I've been developing through my AI-assisted learning journey: Slip Coding.

## From Vibe Coding to Slip Coding

Vibe coding is the process of using emotions, feel, and basic requests; feeding them into an LLM, and using that process to build something. It's more about the feeling and environment than rigorous output. While there's nothing wrong with coding for the vibe, I've found that this framing often leads to aimless tinkering rather than meaningful progress.

Slip Coding is my attempt to reclaim and refine this concept. It's about using small, otherwise "slippery" pockets of time—a train commute, waiting for a friend at a café, or those 15 minutes before a meeting—to make incremental but meaningful progress on personal projects with the help of AI.

## How Slip Coding Works

Instead of opening social media during these micro-breaks, I open ChatGPT and:
- Brainstorm solutions to coding problems I'm stuck on
- Learn about new tools or libraries in conversational format(Canvas)
- Outline ideas in natural language that will later become code(Canvas)
- Review and refine project structures 
- Think through potential approaches to technical challenges

Canvas is huge for this, instead of just reading/discussing docs, I can actually start building an actual code file for a project. This isn't going to be perfect(it may not even compile), but it gives me a starting point and lets me think about what I want to do. Then, when I sit down and work, I can be efficient and productive with time spent on personal projects. I can skip the "settling in" part of personal projects and jump right in. And when I finish, I can update my chat with me edits and continue iterating from my phone.

Voice input provides another layer. If I'm doing chores or an activity where I need my hands, I can still do work, by speaking to the LLM. This is even less rigorous that slip coding from my phone(no visual feedback), but it's just another way to take time back.

The key insight is that I'm "preloading" my thinking. By the time I actually sit down for a dedicated coding session, I'm not starting cold. My mind has already worked through preliminary obstacles, explored potential approaches, and organized my thoughts.

## AI's Role in Slip Coding

AI assistants are particularly well-suited for Slip Coding because:
1. They're accessible anywhere via mobile
2. The conversational format works well for brief sessions
3. They maintain context long enough to make progress
4. They can switch between high-level abstract thinking and technical specifics
5. They don't require me to actually run code or have a development environment set up

This approach turns what would otherwise be lost time into creative momentum. It's not about coding without a computer—it's about preparing my mind so that when I do have my development environment, I can hit the ground running.

## Beyond Aesthetics

While vibe coding often focuses on the aesthetics and feel of the programming experience, Slip Coding focuses on building sustainable habits that convert micro-moments into meaningful progress. It's less about the perfect playlist or cozy environment and more about finding ways to keep your projects moving forward in the in-between spaces of life.

The habit-forming aspect is crucial—once you get used to opening an AI chat instead of social media during these slip spaces, you'll find yourself making steady progress on projects that might otherwise languish.

A key detail is this only works for personal projects that you really want to work on, but don't have time for. I can't imagine myself being motivated to do work related to my job this way. And the lack of rigor means it's not great for things that have to get done and be right(work tasks). But for personal projects, which are much more flexible, it works beautifully.

<a name="conclusion"></a>
# Conclusion

After several months of experimenting with AI assistants as learning tools, I've arrived at some clear insights:

## What Actually Works

1. **Intelligence Amplification, Not Replacement**: The most valuable approach is using AI to enhance my own thinking rather than expecting it to replace it. This fundamental shift;from treating AI as a solution generator, to using it as a thought partner—transformed its utility for me.

2. **Interface Matters As Much As Intelligence**: The right interface for the task often determines an AI's usefulness more than the raw capabilities of the model itself. Claude's dual-pane editing for markdown and ChatGPT's Canvas feature demonstrate how purpose-built interfaces dramatically improve specific workflows.

3. **Organization Is Critical For Learning**: Project-level organization and the ability to maintain context across sessions proved essential for deep learning. This quickly eliminated Gemini from consideration and made ChatGPT's memory feature a key advantage.

4. **The AI Doesn't Know Itself**: A consistent pattern emerged—AI assistants have little awareness of their own platform features and capabilities. This separation between model and interface reinforces that we're not working with truly self-aware systems but with tools that require our direction.

My journey from AI skeptic to effective user didn't come from better prompting or finding the "right" AI—it came from fundamentally rethinking how I approach these tools. By leveraging my own intelligence first and using AI as an amplifier for learning and organizing thoughts, I've found genuine value that wasn't apparent when I was attempting to use these tools as code generators or problem solvers.

The key insight remains: AI is at its best when it helps you think better, not when it tries to think for you.

