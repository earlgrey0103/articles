http://blog.techrocket.com/2016/04/21/python-creator-guido-van-rossum-on-how-he-got-his-start-in-programming/

Guido van Rossum is the creator of Python, one of the world’s most popular programming languages. Guido was kind enough to tell us his story, from growing up and discovering computers in the Netherlands, to creating Python and landing at Dropbox in San Francisco.

 

How did you first become interested in computers and programming?
That’s an interesting story. It was in the mid 70s. I had never heard of computers until my last year in high school. When I went to the University of Amsterdam with a major in mathematics, there were programming classes and a mainframe computer (a Control Data Corporation Cyber-170) in the basement, and within half a year I was hooked. Within two years I was neglecting my classwork in favor of writing and debugging programs in Algol and Pascal.

 

A CDC 170 computer room in 1986.

1280px-PAVE_Paws_Computer_Room

 

I remember writing an implementation of Conway’s Game of Life in Pascal that produced output on the line printer. I used Pascal’s sets, which were mapped to the hardware’s unique 60-bit word size, and implemented very fast bitwise and/or/shift operations, which I used to implement essentially the digital circuits for adding and comparing 3-bit numbers (this only makes sense if you know the rules of that game). I knew that kind of digital logic from my former life as an electronics hobbyist (which I gave up as soon as I gained access to the mainframe :-) ).

 

How did you explore your interest in math and science while in high school? Were there people who encouraged you along the way?
In high school (actually starting in the higher grades of elementary school) I was an electronics hobbyist. I started out building little transistor radios from kits, then moved on to small digital circuits. My dream was to build my own calculator out of discrete components or very simple ICs (on the order of 4 NAND gates or perhaps 4 BCD counters per chip) and I think I had a working design but my allowance wasn’t enough to afford the vast number of ICs required. Also I’m sure my soldering skills weren’t up to scratch. :-)

I mostly got encouragement from my physics teacher — with a few fellow nerds I built a digital counter that was hooked up to the 100 Hz signal from European AC power, which we used to precisely measure small time intervals to demonstrate Galileo’s laws of gravity to the lower graders.

 

What was your first job in programming? How did you get your foot in the door?
When I was in University for almost three years, the group that ran the mainframe put an ad on our bulletin board looking for a student to be a part-time programmer on the operating system team. By then I knew several languages and even some assembly, I applied, and got the job. It was a gift from heaven since a perk of the job was unlimited computer time, on a terminal no less (many people still had to use punched cards, and that was what most students had to use).

That job paid my way through college over the next five years (there was no requirement to finish up within a certain time in those days in the Netherlands). But most importantly it gave me an enormous and varied experience programming a variety of systems (Apple II, PDP 11/50 running UNIX, the aforementioned CDC mainframe) and in many different languages.

 

Why did you decide to create your own programming language?
My first job out of college was at CWI, on a team that was implementing a programming language for beginners named ABC. After 3-4 years of hard work that project flopped and was discontinued, and I moved to other projects at CWI. I worked on Amoeba for a few years (Andrew Tanenbaum’s micro-kernel-based distributed operating system) and at some point I got tired of writing apps in C. I longed for something like ABC (which had many good features) but realized that porting ABC would be unsatisfactory, and I really didn’t like Perl 3, which had just come out. So I decided to create my own language instead, inspired primarily by ABC and C. I took all the things from ABC that I liked, and for all the things in ABC that I disliked, I did the opposite (often borrowing from C).

 

It must take a lot of effort and dedication to create a programming language. What was this process like for you? Intense? Fun? Did you have doubts along the way?
Looking back I don’t think I ever really doubted Python, and I always had fun. I had a lot of doubts about myself, but Python’s ever-increasing success, and encouragement from people to whom I looked up (even Larry Wall!), made me forget that.

 

You’re known as Python’s Benevolent Dictator for Life. What does that mean?
It’s a joke term meaning that the community trusts me to take their best interest at heart. I try to live up to it by listening to Python users and developers. It’s quite possible for the community to change my mind!

 

Guido giving a talk at Dropbox HQ. Photo via Dan Stroud. 

guido-van-rossum-dropbox

 

How would you like Python to evolve in the next decade?
I want Python to be more effective for large projects, without losing sight of its use for small projects and teaching. It’s quite a challenge; my current hope lies in PEP 484 and mypy, an approach to optional static typing (a.k.a. gradual typing). It’s super exciting. There are also other things happening in the community that make Python faster.

 

What’s the most astonishing thing you’ve seen built with Python?
That’s probably the Dropbox server. Two million lines of code and counting, and it serves hundreds of millions of users.