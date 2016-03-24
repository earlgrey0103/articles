http://www.infoworld.com/article/3044088/application-development/10-hard-core-coding-tips-for-faster-python.html?upd=1458833520197

By and large, people use Python because it’s convenient and programmer-friendly, not because it’s fast. The plethora of third-party libraries and the breadth of industry support for Python compensate heavily for its not having the raw performance of Java or C. Speed of development takes precedence over speed of execution.

But in many cases, it doesn’t have to be an either/or proposition. Properly optimized, Python applications can run with surprising speed -- perhaps not Java or C fast, but fast enough for Web applications, data analysis, management and automation tools, and most other purposes. You might actually forget that you were trading application performance for developer productivity.

[ Get the most out of collaborative programming with InfoWorld's 20 essential pointers for Git and GitHub. | Keep up with hot topics in programming with InfoWorld's Application Development newsletter. ]
Optimizing Python performance doesn’t come down to any one factor. Rather, it’s about applying all the available best practices and choosing the ones that best fit the scenario at hand. (The folks at Dropbox have one of the most eye-popping examples of the power of Python optimizations.)

In this piece I’ll outline many common Python optimizations. Some are drop-in measures that require little more than switching one item for another (such as changing the Python interpreter), but the ones that deliver the biggest payoffs will require more detailed work.

1. Measure, measure, measure

You can’t miss what you don’t measure, as the old adage goes. Likewise, you can’t find out why any given Python application runs suboptimally without finding out where the slowness actually resides.

Start with simple profiling by way of Python’s built-in cProfile module, and move to a line-level profiler if you need greater precision. Often, the insights gleaned by basic function-level inspection of an application provide more than enough perspective. (You can pull profile data for a single function via the profilehooks module.)

Why a particular part of the app is so slow, and how to fix it, may take more digging. The point is to narrow the focus, establish a baseline with hard numbers, and test across a variety of usage and deployment scenarios whenever possible. Don’t optimize prematurely. Guessing gets you nowhere.

2. Memoize (cache) repeatedly used data

Never do work a thousand times when you can do it once and save the results. If you have a frequently called function that returns predictable results, Python provides you with options to cache the results into memory. Subsequent calls that return the same result will return almost immediately.

Various examples show how to do this; my favorite memoization is nearly as minimal as it gets. One of Python’s native libraries, functools, has the @functools.lru_cache decorator, which caches the n most recent calls to a function. This is handy when the value you’re caching changes but is relatively static within a particular window of time. A list of most recently used items over the course of a day would be a good example.

3. Move math to NumPy

If you are doing matrix- or array-based math and don’t want the Python interpreter getting in the way, use NumPy. By drawing on C libraries for the heavy lifting, NumPy offers faster array processing than native Python. It also stores numerical data more efficiently than Python’s built-in data structures.

Relatively unexotic math can be sped up enormously by NumPy, too. The package provides replacements for many common Python math operations, like min and max, that operate many times faster than the Python originals.

Another boon with NumPy is more efficient use of memory for large objects, such as lists with millions of items. On the average, large objects like that in NumPy take up around one-fourth of the memory required if they were expressed in conventional Python. Note that it helps to begin with the right data structure for a job, an optimization itself.

Rewriting Python algorithms to use NumPy takes some work since array objects need to be declared using NumPy’s syntax. But NumPy uses Python’s existing idioms for actual math operations (+, -, and so on), so switching to NumPy isn’t too disorienting in the long run.

4. Use a C library

NumPy’s use of libraries written in C is a good strategy to emulate. If there’s an existing C library that does what you need, Python and its ecosystem provide several options to connect to the library and leverage its speed.

The most common way to do this is Python’s ctypes library. Because ctypes is broadly compatible with other Python applications (and runtimes), it’s the best place to start, but it’s far from the only game in town. The CFFI project provides a more elegant interface to C. Cython (see below) also can be used to wrap external libraries, although at the cost of having to learn Cython’s markup.

5. Convert to Cython

If you want speed, use C, not Python. But for Pythonistas, writing C code brings a host of distractions -- learning C’s syntax, wrangling the C toolchain (what’s wrong with my header files now?), and so on.

Cython allows Python users to conveniently access C’s speed. Existing Python code can be converted to C incrementally -- first by compiling said code to C with Cython, then by adding type annotations for more speed.

Cython isn’t a magic wand. Code converted as-is to Cython doesn’t generally run more than 15 to 50 percent faster because most of the optimizations at that level focus on reducing the overhead of the Python interpreter. The biggest gains in speed come only when you provide type annotations for a Cython module, allowing the code in question to be converted to pure C.

CPU-bound code benefits the most from Cython. If you’ve profiled (you have profiled, haven’t you?) and found that certain parts of your code use the vast majority of the CPU time, those are excellent candidates for Cython conversion. Code that is I/O bound, like long-running network operations, will see little or no benefit from Cython.

6. Go parallel with multiprocessing

Traditional Python apps -- those implemented in CPython -- execute only a single thread at a time, in order to avoid the problems of state that arise when using multiple threads. This is the infamous Global Interpreter Lock (GIL). That there are good reasons for its existence doesn’t make it any less ornery.

The GIL has grown dramatically more efficient over time (another reason to run Python 3 instead of Python 2), but the core issue remains. A CPython app can be multithreaded, but CPython doesn’t really allow those threads to run in parallel on multiple cores.

To get around that, Python provides the multiprocessing module to run multiple instances of the Python interpreter on separate cores. State can be shared by way of shared memory or server processes, and data can be passed between process instances via queues or pipes.

You still have to manage state manually between the processes. Plus, there’s no small amount of overhead involved in starting multiple instances of Python and passing objects among them. But for long-running processes that benefit from parallelism across cores, the multiprocessing library is useful.

As an aside, Python modules and packages (such as NumPy) that use C libraries avoid the GIL entirely. That’s another reason they’re recommended for a speed boost.

7. Know what your libraries are doing

How convenient it is to simply type include xyz and tap into the work of countless other programmers! But you need to be aware that third-party libraries can change the performance of your application, not always for the better.

Sometimes this manifests in obvious ways, as when a module from a particular library constitutes a bottleneck. (Again, profiling will help.) Sometimes it’s less obvious. Example: Pyglet, a handy library for creating windowed graphical applications, automatically enables a debug mode, which dramatically impacts performance until it’s explicitly disabled. You might never realize this unless you read the documentation. Read up and be informed.

8. Be conscious of the platform

Python runs cross-platform, but that doesn’t mean the peculiarities of each operating system -- Windows, Linux, OS X -- are abstracted away under Python. Most of the time, this means being aware of platform specifics like path naming conventions, for which there are helper functions.

But understanding platform differences is also important when it comes to performance. On Windows, for instance, Python scripts that need timer accuracy finer than 15 milliseconds (say, for multimedia) will need to use Windows API calls to access high-resolution timers or raise the timer resolution.

9. Run with PyPy

CPython, the most commonly used implementation of Python, prioritizes compatibility over raw speed. For programmers who want to put speed first, there’s PyPy, a Python implementation outfitted with a JIT compiler to accelerate code execution.

Because PyPy was designed as a drop-in replacement for CPython, it’s one of the simplest ways to get a quick performance boost. Many common Python applications will run on PyPy exactly as they are. Generally, the more the app relies on “vanilla” Python, the more likely it will run on PyPy without modification.

However, taking best advantage of PyPy may require testing and study. You’ll find that long-running apps derive the biggest performance gains from PyPy, because the compiler analyzes the execution over time. For short scripts that run and exit, you’re probably better off using CPython, since the performance gains won’t be sufficient to overcome the overhead of the JIT.

Note that PyPy’s support for Python 3 is still several versions behind; it currently stands at Python 3.2.5. Code that uses late-breaking Python features, like async and await co-routines, won’t work. Finally, Python apps that use ctypes may not always behave as expected. If you’re writing something that might run on both PyPy and CPython, it might make sense to handle use cases separately for each interpreter.

Other experiments in speeding up Python through JITting are still yielding fruit. Among them is Pyjion, a Microsoft project that outfits CPython with an interface for JITs. Microsoft provides a JIT of its own as a proof of concept.

10. Upgrade to Python 3

If you’re using Python 2.x and there is no overriding reason (such as an incompatible module) to stick with it, you should make the jump to Python 3.

Aside from Python 3 as the future of the language generally, many constructs and optimizations are available in Python 3 that aren’t available in Python 2.x. For instance, Python 3.5 makes asynchronous programming less thorny by making the async and await keywords part of the language’s syntax. Python 3.2 brought a major upgrade to the Global Interpreter Lock that significantly improves how Python handles multiple threads.

If you’re worried about speed regressions between versions of Python, the language’s core developers recently restarted a site used to track changes in performance across releases.

As Python has matured, so have dynamic and interpreted languages in general. You can expect improvements in compiler technology and interpreter optimizations to bring greater speed to Python in the years ahead.

That said, a faster platform takes you only so far. The performance of any application will always depend more on the person writing it than on the system executing it. Fortunately for Pythonistas, the rich Python ecosystem gives us many options to make our code run faster. After all, a Python app doesn’t have to be the fastest, as long as it’s fast enough.