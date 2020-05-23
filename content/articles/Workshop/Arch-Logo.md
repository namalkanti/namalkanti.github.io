Title: Arch Linux Logo Keychain
Date: 2020-5-22 
Modified: 2020-5-22 
Category: Workshop
Tags: openscad 
Slug: Arch-Keychain
Authors: Niraj Amalkanti 
State: Stalled

### Entries
[ Overview ](#overview)

[ 5/22/2020 - Initial Fumbling ](#5/22/2020)

[ 5/23/2020 - Tutorials ](#5/23/2020)

[ 5/24/2020 - 3D Printing Service ](#5/24/2020)

<a name="overview"></a>
# Overview

As a Linux user I love opportunities to show off my preferred operating system.
Recently I tried looking for a keychain for the Arch Linux logo. I wanted a 3D model
of the logo, but I couldn't find one for sale. The closest I found was a 3D model 
somebody else made and printed for themselves.
I have no experience in 3D modeling or printing, but it's something 
I've wanted to learn. This sounds like a good, simple project to get started with. 

For 3D printing what I'd like to do is learn a program called [OpenSCAD](https://www.openscad.org).
It's a CAD tool intended for programmers because it uses a text based file format. Some
googling suggests it doesn't have the same professional reputation as SolidWorks or 
AutoCAD but it can be a powerful tool if you learn to use it. The main criticism is that
it's so drastically different from other CAD tools, it doesn't make sense for most
people to bother learning it. Especially since there's no professional value. But I've 
never used any other CAD tool and have no interest in pursuing CAD professionally. 
However, a text format is something I'm
very comfortable with. Anther advantage with text formats is it 
makes version control very easy. So it makes sense for me to try learning OpenSCAD
instead of a more conventional CAD tool.

I'm going to use github to keep track of my files the repo is [here](https://github.com/namalkanti/Arch-Keychain-Model)

## Objectives
* Use OpenSCAD to create a STL file of the Arch Linux logo as a keychain
* Learn the basics of OpenSCAD
* Print the stl file using some online service

<a name="5/22/2020"></a>
# 5/22/2020 - Initial Fumbling
Normally, I'd search a bunch of tutorials on OpenSCAD and view them before opening the
application. But the simplicity of this project suggests a different approach. Maybe I'll
start with fumbling my way through the application and see what happens. I have an
svg of the arch linux logo; maybe I can export that to a format and import it into 
OpenSCAD? If I could do that, I could try extending the logo in the third dimension. Then
I'd just need to cut a hole out for the keyring and I'd be done. I don't know if this
is how CAD is supposed to work but it's worth a shot.

First, I note that OpenSCAD works well with external text editors. The built in editor
can be hidden and the preview window will update when saving files with an external 
editor. So I can happily use vim to edit my scad files.

Googling my approach lead to an interesting result. Normally, you should export your svg
as another file type intedend for 2d machine work(dxf). That can be imported into OpenSCAD.
But very recently(5/2019), OpenSCAD actually added an svg import. So I can import my 
svg into OpenSCAD directly.

<figure class="center">
    <img src="{attach}/images/openscad_after_import.png" width="90%" height="auto" class="border">
    <figcaption>Workspace after attempting svg import</figcaption>
</figure>

This doesn't look bad for 30 minutes of blind fumbling. I tried an stl export
for the hell of it, but my object isn't considered a 3D object. When I switch
to render mode; I see that the object is flat. This makes sense since an svg is 2D. So 
this preview mode(pictured above) is just an approximation.

So then I need to extend this object next. Before I do that, I should probably try to 
cut out a circle for the keyring. The best way to do this would be to reload the svg
in inkscape and cut the hole out there. It's possible to use OpenSCAD's difference 
function, but since the difference is based in 2D, I think it makes sense to handle
it in inkscape.

I also wanted to see if OpenSCAD would automatically load my changes when I saved them 
in Inkscape; this does work. I'll admit to being very impressed with OpenSCAD so far. 
They claim to be a CAD tool for programmers, but I didn't expect them to live up to
that claim so well.

The extension to 3D is a function called "Linear Extrusion"; I found a beginner tutorial [here](http://edutechwiki.unige.ch/en/OpenScad_beginners_tutorial#Import_and_extrude_2D_graphics_from_SVG)
that does exactly what I want. It's a little outdated because it claims I need to export
my svg as a dxf file. But I can extrude my svg with the current version of OpenSCAD.

At this point, I can actually get an stl import. But I have no idea what the units or
the size of the output will be. I also have no idea how the flow of execution for OpenSCAD
works; I'm just following the tutorials ordering.

Google quickly tells me stl doesn't enforce units and you need to specify them at print. 
Often, 1 unit
length is just 1mm so I will use that convention. My desired length for the keychain is 
48mm so I need to resize my object to that length. This can be done with the scale 
function which can also auto scale the y dimension.

I'm not sure but this might mean I'm done? I have an stl file scaled for 1mm. I think 
my next step should be to look at actual OpenSCAD tutorials to see if I'm missing something. If 
not I can try to find 3d printing services and send off my design. Perhaps my project
is a little too simple...

<a name="5/23/2020"></a>
# 5/23/2020 - Tutorials

Googling some tutorials gave me the basics. An openscad file is basically a collection of
"actions" which create objects and operators which act on those actions. Compiling these
together creates a model. You can also define variables and functions(functions are called
modules) for more complex projects. Vectors and Loops also exist and have the expected
functions. This kind of reminds me of verilog; where a somewhat simple, specialized 
language can be very expressive for its domain. It looks like I fumbled my way into the
right approach. Now I feel a bit more confident that my file is correct; so next 
I'll look up 3D printing services.

<a name="5/24/2020"></a>
# 5/24/2020 - 3D Printing Services

Some quick googling lead to a large list of 3D printing services. I'm not really sure
how to pick them but [Shapeways](https://www.shapeways.com) seems like a good fit. It's not meant for industrial printing
and they'll let me print a single object. They have a lot of materials but it looks like
their versatile plastic is available in a blue for the arch linux logo. It's not terribly
expensive ($12.00) but the shipping cost is almost the same as the model($9.00). They 
don't offer any cheaper version, so I'll have to deal with it. This feels too easy....
But I'm not sure what else to do. They estimate it'll take a month until my print arrives
so I guess I'll see how well I did when it gets here.
