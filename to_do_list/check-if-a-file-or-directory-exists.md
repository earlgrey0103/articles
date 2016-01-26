# Python：检查某个文件或文件夹是否存在


There are quite a few ways to solve a problem in programming, and this holds true especially in Python. Many times you'll find that multiple built-in or standard modules serve essentially the same purpose, but with slightly varying functionality. Checking if a file or directory exists using Python is definitely one of those cases.

Here are a few ways to check for existing files/directories and their nuances. Throughout these examples we'll assume our current working directory has these files and directories in it:

drwxr-xr-x  3 scott  staff  102 Jan 12 10:01 dir  
-rw-r--r--  1 scott  staff    5 Jan 12 09:56 file.txt
lrwxr-xr-x  1 scott  staff    8 Jan 12 09:56 link.txt -> file.txt  
lrwxr-xr-x  1 scott  staff    3 Jan 12 10:00 sym -> dir  
Notice that we have one directory (dir), one file (file.txt), one file symlink (link.txt), and one directory symlink (sym).

Checking if a File Exists
This is arguably the easiest way to check if both a file exists and if it is a file.

import os  
os.path.isfile('./file.txt')    # True  
os.path.isfile('./link.txt')    # True  
os.path.isfile('./fake.txt')    # False  
os.path.isfile('./dir')    # False  
os.path.isfile('./sym')    # False  
os.path.isfile('./foo')    # False  
Note that os.path.isfile does follow symlinks, so we get True when checking link.txt.

isfile is actually just a helper method that internally uses os.stat and stat.S_ISREG(mode) underneath, which we'll touch on later.

Checking if a Directory Exists
Like the isfile method, os.path.isdir is the easiest way to check if a directory exists, or if the path given is a directory.

import os  
os.path.isdir('./file.txt')    # False  
os.path.isdir('./link.txt')    # False  
os.path.isdir('./fake.txt')    # False  
os.path.isdir('./dir')    # True  
os.path.isdir('./sym')    # True  
os.path.isdir('./foo')    # False  
Again, just like isfile, os.path.isdir does follow symlinks. It is also just a simple wrapper around os.stat and stat.S_ISDIR(mode), so you're not getting much more than convenience from it.

Checking if Either Exist
Another way to check if a path exists (as long as you don't care if the path points to a file or directory) is to use os.path.exists.

import os  
os.path.exists('./file.txt')    # True  
os.path.exists('./link.txt')    # True  
os.path.exists('./fake.txt')    # False  
os.path.exists('./dir')    # True  
os.path.exists('./sym')    # True  
os.path.exists('./foo')    # False  
As you can see, it doesn't care if the path points to a file, directory, or symlink, so it's almost like you're using isfile(path) or isdir(path). But actually, internally it is just trying to call os.stat(path), and if an error is thrown then it returns False.

Advanced
Throughout the article I've been mentioning how all of the above methods utilize the os.stat method, so I figured it would be useful to take a look at it. This is a lower-level method that will provide you with detailed information about files, directories, sockets, buffers, and more.

Like all the other methods we'v already covered, os.stat follows symlinks, so if you want to get the stat info on a link, try using os.lstat() instead.

Since every operating system is different, the data provided by os.stat varies greatly. Here is just some of the data that each OS has in common:

st_mode: protection bits
st_uid: owner's user id
st_gid: owner's group id
st_size: size of file in bytes
st_atime: time of last access
st_mtime: time of last modification
st_ctime: time of last metadata change on Unix, or time of creation on Windows
You can then use this data with the stat module to get interesting information, like whether a path points to a socket (stat.S_ISSOCK(mode)), or if a file is actually a named pipe (stat.S_ISFIFO(mode)).

If you need some more advanced functionality, then this is where you should go. But for 90% of the time you're dealing with directories and files, the os or os.path modules should have you covered.

Although, one valid use-case might be when you're doing multiple tests on the same file and want to avoid the overhead of the stat system call for each test. So if you have quite a few tests to do then this will help you do it more efficiently.