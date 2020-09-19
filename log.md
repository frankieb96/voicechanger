# Development log
Which is basically little more than a rant when I am unable to accomplish
anything.


### 16/09/2020, 22:28
New project! This is my first, non-uni-related, just-for-fun project :D

My idea is to develop a very simple, real-time voice changer. This should
allow me to understand 
- how to work and process audio signals (DSP course should be useful here)
- how to develop a simple user interface in python, using Qt or Tkinter 

Every projects starts by collecting the necessary information. 
I will do it tomorrow.


### 17/09/2020, 17:17
Now, I have already worked with audio signals, but I never developed a
real-time application with non-blocking I/O, so this may be a challenge.
First, it is worth starting with the **PyAudio** documentation:
> https://people.csail.mit.edu/hubert/pyaudio/docs/

which shall be my first resource. I'll copy-paste the basic code just to
verify it works.

It works! I also copy-pasted a few more examples from the internet. There
seems to be some kind of artefact in these naive implementations.

Another big audio dsp module is **pyo**, here's the documentation:
> http://ajaxsoundstudio.com/pyodoc/index.html

I have tried the basic examples .py files. For sure it's a very complete
module for audio dsp. It could be exactly what I'm looking for.
On the other hand it seems a bit overkill, for my scope, and it appears
it doesn't handle direct input-to-output streams. 

Another one, **audiolazy**:
> https://github.com/danilobellini/audiolazy/

this has an example of direct input-to-output streams. 
Also this one seems to introduce a lot of distortion. I need to try it
with an headset, or to cope with it with some filter. I'll think about
it tomorrow.


### 19/09/2020, 09:46
I've been experimenting all the morning. Now, audiolazy has a very
uncomfortable lack of proper documentation, so, being this an amateur
project, I think I'll discard it. Besides, i/o wiring has the same
problems as the pyaudio one. 
I'll stick with it for I/O.
On the other hand, pyaudio does not include signal processing tools,
so I hope to find a workaround with pyo.
I haven't check any other libraries in other programming languages,
but now I'm fairly sure this would be better done in C/C++.

Yahoo! Ok, I have found an example to reroute i/o in pyo. Furthermore,
official documentation discourages using both pyo and pyaudio.
I have decided to use pyo from begin to end. Don't know if it will
work with Discord, but it doesn't matter right now.