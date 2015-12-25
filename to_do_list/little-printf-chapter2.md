## 第二章

> -[上一章](http://codingpy.com/article/story-of-little-printf-chapter1/)
> -[下一章](http://codingpy.com/article/story-of-little-printf-chapter3/)

So I lived my life flying around the world, telling people how to do things I had sometimes never done myself, while everyone suddenly seemed to believe I was a real programmer because of things I did that were mostly not related to programming in the first place.
One day, I was stuck in an airport coming back from a conference, furiously typing at a terminal, when an odd, gentle voice asked me:
If you please, design me a system!
What?!
Design me a system!
I looked up from my screen, surprised by the request. I looked around and saw this kid who aspired to be a developer and wanted me to call him "printf", which I felt was very stupid and gimmicky. He looked a bit like this:

![](http://ferd.ca/static/img/printf/printf-nocover.png)

little printf, with a red and yellow tuque, similarly colored scarf, green coat, red mittens, and beige-yellow pants, standing in snow with a broken laptop at his sides

I don't know computers much yet, but it seems you do. I want to write programs and blog about them and have people use and read them. Please, design me a system!

Now that was a surprising request, and I had been awake for 20 hours by then, not too sure I fully understood or felt like it. I told him systems were hard. I didn't know what he wanted to do, how he wanted it to fail, how many readers it should support, where he'd want to host it, and I could therefore not design a proper system with so little information.

That doesn't matter. Design me a system.

So I made the following architecture diagram:

![somewhat complex architecture diagram](http://ferd.ca/static/img/printf/arch1.png)


He looked at it and said No, this system is not good enough. Make me another.
So I did:


![a rather complex architecture diagram](http://ferd.ca/static/img/printf/arch2.png)

and I gave him a rundown of how it would work.
My new friend smiled politely. That is not what I want, it's way too complex and does a lot of stuff I don't need
I felt a bit insulted, having considered redundancy, monitoring, backups, caches and other mechanisms to reduce load, external payment processor for legal protection, failovers, easy deployment, and so on. I could have charged decent money as a consulting fee for that! Out of patience, I just drew this:

![a black box with the text 'enjoy!' written under.](http://ferd.ca/static/img/printf/blackbox.png)

And I added: this is your design. The system you want is inside the black box, hoping this shitty answer would have him leave me alone. But I was surprised to hear back:

That is exactly the way I wanted it!

And that is how I made the acquaintance of the little printf.
