Title: Can and Calculator
Date: 2020-6-26 
Modified: 2020-6-27 
Category: Studio
Tags: openscad, blender 
Slug: Models
Authors: Niraj Amalkanti 
State: In-Progress

### Entries
[ Overview ](#overview)

[ 6/26/2020 - Can Model ](#6/26/2020)

[ 6/27/2020 - Blender Tutorials ](#6/27/2020)

[ 6/28/2020 - Coloring Can Model ](#6/28/2020)


<a name="overview"></a>
# Overview

A few months ago, I started to learn Inkscape for 2D vector art. One of the first
projects I did was creating two pictures that I printed on keychains to give to my
parents.

<figure class="center">
    <img src="{attach}/images/keychains.jpg" width="100%" height="auto" class="border">
    <figcaption>Keychains for Parents</figcaption>
</figure>

The objects are a calculator and a can of paint which have personal significance to my 
mom and dad respectively. A natural extension for this would be to make 3D models of the
same objects.

In my [first attempt with OpenSCAD](https://mitigatingfailure.com/Arch-Keychain.html)
, I completed my project, but I didn't feel like I learned much. OpenSCAD was so
well designed, I easily make a logo model with barely any effort. This project 
should be a bit more challenging. I'll probably start with building each model in OpenSCAD,
but then I'll need to apply color/texturing. My preliminary research suggests I can do this
in [Blender](www.blender.org), a powerful 3D modeling software application with a reputation for a high 
learning curve. Blender can import stl files and output x3d files. Shapeways can then take and print those
x3d files.

In theory, I should be able to do the entire modeling project in Blender. But I've heard of Blender's
reputation for difficulty and I think I should try to keep things simple. If the stl import is
creating more problems than it solves; I'll switch over, but I think it's a good starting point.
 
## Objectives
* Create colored 3D models for my 2D designs and print them

<a name="6/26/2020"></a>
# 6/26/2020 - Can Model

I'm starting with the can of paint because I think it'll be the easier of the two projects. For,
simplicity, I will not be trying to add the pain spillover in the model. Even though my last
project was too trivial; I have a history of being too ambitious with projects and want to keep
myself in line. If things go well, I can always choose to add the pain spill over later. But this
is an area I'm very unfamiliar with, so I should be careful.

<figure class="center">
    <img src="{attach}/images/001.png" width="50%" height="auto">
    <figcaption>Rasterized vector art for Can of Paint</figcaption>
</figure>

Making the 3D model was pretty simple; I just created a cylinder and subtracted a smaller one
from the top to create the shape of paint can. The can will be almost full so I kept most 
of it filled in.

<figure class="center">
    <img src="{attach}/images/paint_can_model.png" width="100%" height="auto" class="border">
    <figcaption>Openscad code with 3D model rendered</figcaption>
</figure>

<a name="6/27/2020"></a>
# 6/27/2020 - Blender Tutorials

Unlike with OpenSCAD, I don't think blindly charging in is the correct approach here. I think I'll
start with a few tutorials on Blender's UI and basic features and then see if I can find something
specific on coloring a 3D model.

The first tutorial I found [here](https://www.youtube.com/watch?v=lPVpg4_POww&feature=emb_logo),
suggests that Blender 2.8 had a radical interface redesign that's supposed to address a lot of 
issues Blender previously had with it's initial learning curve. The video does seem to support this.
This is good because it'll hopefully be easier for me to jump into Blender. The downside is that
I'll need to translate older tutorials(probably most of them, right now) to the new interface.
I'll probably have to stick with video tutorials; I find those easiest when interfaces are 
different.

I found this [tutorial](https://www.youtube.com/watch?v=-kziK1XM9PY) ,
which is explicitly for adding color to models for 3D printing. It looks like all I need
to is create different materials for each color and apply them to desired areas. The tutorials
suggests there are better ways to color the model and mentions this will come in future videos.
But they haven't posted them or given any hints so I'll still continue with this approach.
I still need to figure out some details on using Blender, but I think I know enough to start
playing around with the software.

Blender has their own playlist for video tutorials on different functions in 2.8 [here](https://www.youtube.com/playlist?list=PLa1F2ddGya_-UvuAqHAksYnB0qL9yWDO6),
and I will use this as a reference as I start working.

<a name="6/28/2020"></a>
# 6/28/2020 - Coloring Can Model
