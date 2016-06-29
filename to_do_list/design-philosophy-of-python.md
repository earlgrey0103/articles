http://python-history.blogspot.com/2009/01/pythons-design-philosophy.html

Later blog entries will dive into the gory details of Python's history. However, before I do that, I would like to elaborate on the philosophical guidelines that helped me make decisions while designing and implementing Python.

First of all, Python was originally conceived as a one-person “skunkworks” project – there was no official budget, and I wanted results quickly, in part so that I could convince management to support the project (in which I was fairly successful). This led to a number of timesaving rules:
Borrow ideas from elsewhere whenever it makes sense.
“Things should be as simple as possible, but no simpler.” (Einstein)
Do one thing well (The "UNIX philosophy").
Don’t fret too much about performance--plan to optimize later when needed.
Don’t fight the environment and go with the flow.
Don’t try for perfection because “good enough” is often just that.
(Hence) it’s okay to cut corners sometimes, especially if you can do it right later.
Other principles weren’t intended as timesavers. Sometimes they were quite the opposite:
The Python implementation should not be tied to a particular platform. It’s okay if some functionality is not always available, but the core should work everywhere.
Don’t bother users with details that the machine can handle (I didn’t always follow this rule and some of the of the disastrous consequences are described in later sections).
Support and encourage platform-independent user code, but don’t cut off access to platform capabilities or properties (This is in sharp contrast to Java.)
A large complex system should have multiple levels of extensibility. This maximizes the opportunities for users, sophisticated or not, to help themselves.
Errors should not be fatal. That is, user code should be able to recover from error conditions as long as the virtual machine is still functional.
At the same time, errors should not pass silently (These last two items naturally led to the decision to use exceptions throughout the implementation.)
A bug in the user’s Python code should not be allowed to lead to undefined behavior of the Python interpreter; a core dump is never the user’s fault.
Finally, I had various ideas about good programming language design, which were largely imprinted on me by the ABC group where I had my first real experience with language implementation and design. These ideas are the hardest to put into words, as they mostly revolved around subjective concepts like elegance, simplicity and readability.

Although I will discuss more of ABC's influence on Python a little later, I’d like to mention one readability rule specifically: punctuation characters should be used conservatively, in line with their common use in written English or high-school algebra. Exceptions are made when a particular notation is a long-standing tradition in programming languages, such as “x*y” for multiplication, “a[i]” for array subscription, or “x.foo” for attribute selection, but Python does not use “$” to indicate variables, nor “!” to indicate operations with side effects.

Tim Peters, a long time Python user who eventually became its most prolific and tenacious core developer, attempted to capture my unstated design principles in what he calls the “Zen of Python.” I quote it here in its entirety:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
Although my experience with ABC greatly influenced Python, the ABC group had a few design principles that were radically different from Python’s. In many ways, Python is a conscious departure from these:

The ABC group strived for perfection. For example, they used tree-based data structure algorithms that were proven to be optimal for asymptotically large collections (but were not so great for small collections).
The ABC group wanted to isolate the user, as completely as possible, from the “big, bad world of computers” out there. Not only should there be no limit on the range of numbers, the length of strings, or the size of collections (other than the total memory available), but users should also not be required to deal with files, disks, “saving”, or other programs. ABC should be the only tool they ever needed. This desire also caused the ABC group to create a complete integrated editing environment, unique to ABC (There was an escape possible from ABC’s environment, for sure, but it was mostly an afterthought, and not accessible directly from the language.)
The ABC group assumed that the users had no prior computer experience (or were willing to forget it). Thus, alternative terminology was introduced that was considered more “newbie-friendly” than standard programming terms. For example, procedures were called “how-tos” and variables “locations”.
The ABC group designed ABC without an evolutionary path in mind, and without expecting user participation in the design of the language. ABC was created as a closed system, as flawless as its designers could make it. Users were not encouraged to “look under the hood”. Although there was talk of opening up parts of the implementation to advanced users in later stages of the project, this was never realized.
In many ways, the design philosophy I used when creating Python is probably one of the main reasons for its ultimate success. Rather than striving for perfection, early adopters found that Python worked "well enough" for their purposes. As the user-base grew, suggestions for improvement were gradually incorporated into the language. As we will seen in later sections, many of these improvements have involved substantial changes and reworking of core parts of the language. Even today, Python continues to evolve.
Posted by Guido van Rossum at 9:29 AM 
19 comments:


