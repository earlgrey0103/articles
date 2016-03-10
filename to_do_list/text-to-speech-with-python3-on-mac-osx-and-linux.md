OSX

Synthesising speech is a simple matter for OSX users because the operating system comes with the say  command. We can use subprocess  to call it.

import subprocess

def say(text):
    subprocess.call('say ' + text, shell=True)

say('Hello, world!')

Linux

On Linux, there are a few different options. I like to use the espeak  Python bindings when I can. You can install it on Ubuntu using apt-get .

apt-get install python-espeak

Then use it like so:


from espeak import espeak
espeak.synth('Hello, world!')

espeak  supports multiple languages, so if you are not dealing with English text, you need to pass in the language code. Unfortunately, it looks like the Python bindings don’t support that yet, but we can still use subprocess  like we did on linux.

import subprocess

def say_with_espeak(text, lang="en"):
    subprocess.call("espeak -v {0} {1}".format(lang, text), shell=True)

The list of available languages can be found on the espeak website here.

http://espeak.sourceforge.net/languages.html

https://pythonspot.com/speech-engines-with-python-tutorial/